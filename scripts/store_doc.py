import sys
import os
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import chromadb

CHROMA_HOST = "127.0.0.1"
CHROMA_PORT = 8001
COLLECTION_NAME = "pdf_texts"

def extract_text(pdf_path):
    """Extrahiert Text aus PDF, nutzt OCR als Fallback."""
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        text = page.get_text().strip()
        if not text:
            pix = page.get_pixmap(dpi=300)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text = pytesseract.image_to_string(img)
        full_text += text + "\n"

    return full_text.strip()

def store_in_chromadb(text, source_file):
    """Speichert Textdokument in ChromaDB, Embedding wird dort erzeugt."""
    client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    doc_id = os.path.basename(source_file)

    collection.add(
        documents=[text],
        metadatas=[{"filename": doc_id}],
        ids=[doc_id]
    )

    print(f"✅ Gespeichert: {doc_id}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Bitte gib einen PDF-Pfad an.")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print("❌ Datei existiert nicht.")
        sys.exit(1)

    extracted = extract_text(input_path)
    store_in_chromadb(extracted, input_path)
