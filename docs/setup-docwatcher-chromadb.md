# DocWatcher: PDF-Analyse mit ChromaDB

Diese Anleitung beschreibt, wie PDF-Dokumente automatisch verarbeitet, analysiert und in einer lokalen ChromaDB gespeichert werden. Das Setup ist für Raspberry Pi 5 mit laufender n8n-Instanz optimiert.

---

## 🔧 Voraussetzungen

* n8n läuft stabil (siehe [setup-n8n-docker.md](./setup-n8n-docker.md))
* ChromaDB wird lokal per `~/start-chroma.sh` gestartet
* Python-Umgebung mit `pymupdf`, `pytesseract`, `Pillow`, `sentence-transformers`, `chromadb` installiert
* OCR ist optional via `tesseract-ocr` verfügbar

---

## 🔍 Funktion

1. Neue PDFs werden in `/home/mm/docwatch/inbox/` abgelegt.
2. Das Skript `store_doc.py` überprüft:

   * ob es eine Text- oder Bild-PDF ist
   * extrahiert ggf. Text via OCR
   * speichert das Ergebnis in ChromaDB
   * verschiebt die Datei nach `/home/mm/docwatch/processed/`
3. Bei Löschung einer Datei in `processed` wird auch der Eintrag in ChromaDB entfernt (optional).

---

## 🌐 Datenbank

* Speicherort: standardgemäß `./chroma`
* Zugriff via HTTP unter `http://localhost:8001`
* Muss vor jedem `store_doc.py`-Lauf laufen

---

## 🔄 Beispielaufruf

```bash
source ~/chromaenv/bin/activate
~/start-chroma.sh
python3 /home/mm/n8n-server/scripts/store_doc.py /home/mm/docwatch/inbox/deindokument.pdf
```

---

## ⚖️ Integration in n8n

* Nutze einen **Webhook**-Trigger in n8n
* Übergebe Pfade als JSON an ein Shell-Skript oder einen Exec-Node
* Beispiel:

```json
{
  "file": "/home/mm/docwatch/inbox/test1.pdf"
}
```

* oder per Shell:

```bash
curl -X POST http://localhost:5678/webhook/trigger-docwatch -H "Content-Type: application/json" -d '{"file": "/home/mm/docwatch/inbox/test1.pdf"}'
```

---

## 🚫 Fehlerbehebung

* Wenn ChromaDB nicht erreichbar ist: Stelle sicher, dass `start-chroma.sh` aktiv ist.
* Bei `ModuleNotFoundError`: Aktiviere `chromaenv` und installiere fehlende Pakete
* Wenn PDF nicht verarbeitet wird: Überprüfe, ob sie Text enthält (z. B. via `pdftotext`)

---

## 📅 ToDo / Erweiterungen

* Automatische Löschung in ChromaDB bei Dateilöschung aus `processed`
* Erweiterung für Metadaten (z. B. Importdatum, Erkennungsmethode)
* Anbindung an Frage-Antwort-System (Query-Interface in n8n)
