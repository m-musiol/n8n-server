# 📂 Automatische Dokumentenanalyse mit `docwatcher`

Dieses Setup automatisiert die Erkennung, Textextraktion und Indexierung von PDFs mit Hilfe von OCR und ChromaDB. Die Dokumente werden bei Eingang in einem Verzeichnis analysiert und indexiert, um später durchsuchbar zu sein.

## ✍þ Funktionen

* ✨ Automatische Erkennung neuer PDF-Dateien
* 🔍 Text direkt oder via OCR (Tesseract)
* 💾 Speicherung der Inhalte in einer lokalen ChromaDB-Instanz
* 📁 Automatisches Verschieben nach erfolgreicher Verarbeitung

## 📂 Verzeichnisstruktur

```bash
/home/mm/docwatch/
├── inbox       # Eingang für neue PDFs
├── processed   # Erfolgreich verarbeitete PDFs
└── deleted    # Optionale Ablage für aussortierte Dateien
```

## 🧱 Benötigte Pakete

```bash
sudo apt install tesseract-ocr
pip install watchdog pymupdf pytesseract pdf2image chromadb
```

## 🚀 Start der Komponenten

### 1. ChromaDB manuell starten

```bash
source ~/chromaenv/bin/activate
~/start-chroma.sh
```

Dabei wird ChromaDB gestartet **und automatisch `docwatcher.service` aktiviert**, sobald der Port erreichbar ist.

### 2. Manuelle Ausführung (Testweise)

```bash
python3 /home/mm/chromaenv/docwatcher.py
```

## ⚖ Indexierung in ChromaDB

* Indexiert werden PDF-Texte in der Collection `documents`
* Bei leerem PDF-Inhalt erfolgt ein OCR-Fallback
* Jede Datei wird eindeutig über ihren Dateinamen identifiziert

## ⚙ Systemdienst (optional)

`docwatcher.service` kann auch dauerhaft über systemd betrieben werden.

### Beispiel: `/etc/systemd/system/docwatcher.service`

```ini
[Unit]
Description=DocWatcher - Automatische PDF-Überwachung
After=network.target

[Service]
Type=simple
ExecStart=/home/mm/chromaenv/bin/python3 /home/mm/chromaenv/docwatcher.py
Restart=always
User=mm
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

## 🔎 Beispielausgabe

```bash
[+] Neue Datei erkannt: inbox/scan_001.pdf
[1] Versuche Text direkt zu extrahieren …
[2] Kein Text gefunden. Starte OCR-Erkennung …
🧠 Text per OCR erkannt
📂 In ChromaDB gespeichert: scan_001.pdf
📁 Verschoben nach: processed/scan_001.pdf
```

## 📃 Weitere Hinweise

* OCR-Erkennung kann je nach PDF-Größe einige Sekunden dauern
* Gespeicherte Inhalte sind anschließend über ChromaDB API durchsuchbar
* Die automatische Ablage vermeidet doppelte Indexierungen
