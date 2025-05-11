import os
import time
import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import chromadb
from chromadb.config import Settings

# ChromaDB-Client initialisieren
client = chromadb.HttpClient(host="127.0.0.1", port=8001)
collection = client.get_or_create_collection(name="pdf_texts")

INBOX_DIR = os.path.expanduser("~/docwatch/inbox")
PROCESSED_DIR = os.path.expanduser("~/docwatch/processed")

def extract_text(pdf_path):
    print(f"📄 Eingabe-PDF: {pdf_path}")
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    if text.strip():
        print("[1] Text direkt extrahiert.")
        return text.strip()

    print("[2] Kein Text gefunden. Starte OCR-Erkennung …")
    images = convert_from_path(pdf_path)
    ocr_text = ""
    for img in images:
        ocr_text += pytesseract.image_to_string(img)

    print("🧠 Text per OCR erkannt:")
    print("----------------------------------------")
    print(ocr_text.strip()[:500])  # nur Vorschau
    print("----------------------------------------")
    return ocr_text.strip()

def store_in_chromadb(file_path, content):
    file_name = os.path.basename(file_path)
    document_id = file_name.replace(" ", "_")
    collection.add(
        documents=[content],
        metadatas=[{
            "file": file_name,
            "imported_at": datetime.utcnow().isoformat()
        }],
        ids=[document_id]
    )
    print(f"💾 In ChromaDB gespeichert: {document_id}")

class PDFHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith(".pdf"):
            return
        time.sleep(2)  # kurzes Delay, falls Datei noch kopiert wird
        print(f"[+] Neue Datei erkannt: {event.src_path}")
        try:
            text = extract_text(event.src_path)
            store_in_chromadb(event.src_path, text)
            filename = os.path.basename(event.src_path)
            os.rename(event.src_path, os.path.join(PROCESSED_DIR, filename))
            print(f"📁 Verschoben nach: {PROCESSED_DIR}/{filename}")
        except Exception as e:
            print(f"[!] Fehler bei der Verarbeitung: {e}")

if __name__ == "__main__":
    print(f"👀 Beobachte Ordner: {INBOX_DIR}")
    event_handler = PDFHandler()
    observer = Observer()
    observer.schedule(event_handler, INBOX_DIR, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
