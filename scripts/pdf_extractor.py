import sys
import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from pathlib import Path

def extract_text_with_fitz(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        print(f"[!] Fehler beim Lesen mit fitz: {e}")
        return ""

def extract_text_with_ocr(pdf_path):
    try:
        images = convert_from_path(pdf_path)
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"[!] Fehler bei OCR: {e}")
        return ""

def main(pdf_path):
    print(f"📄 Eingabe-PDF: {pdf_path}")
    if not Path(pdf_path).is_file():
        print("[!] Datei existiert nicht.")
        return

    print("[1] Versuche Text direkt zu extrahieren …")
    text = extract_text_with_fitz(pdf_path)

    if text:
        print("✅ Text direkt extrahiert:")
    else:
        print("[2] Kein Text gefunden. Starte OCR-Erkennung …")
        text = extract_text_with_ocr(pdf_path)
        if text:
            print("🧠 Text per OCR erkannt:")
        else:
            print("❌ Konnte keinen Text extrahieren.")

    print("-" * 40)
    print(text[:200] + "…" if text else "Kein Text gefunden.")
    print("-" * 40)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("⚠️ Nutzung: python3 pdf_extractor.py <pfad_zur_pdf>")
    else:
        main(sys.argv[1])
