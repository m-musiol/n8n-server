# Dokumentenanfragen aus ChromaDB beantworten

Diese Anleitung beschreibt, wie du in n8n gezielt Informationen aus der lokalen ChromaDB abrufst – etwa auf Fragen wie: *„Welche Dokumente enthalten Informationen zur Mehrwertsteuer?“*

Das Ziel ist eine funktionierende Kombination aus ChromaDB + n8n + LLM (lokal oder remote), die strukturierte Antworten mit Belegen liefert.

---

## 🔧 Voraussetzungen

* ChromaDB läuft lokal (siehe `~/start-chroma.sh`)
* `query_documents.py` oder entsprechendes Skript ist vorhanden und funktional
* Python-Umgebung (`chromaenv`) ist aktiv und installiert alle benötigten Pakete (inkl. sentence-transformers)
* `store_doc.py` wurde bereits verwendet, um Dokumente zu indexieren

---

## 📥 Beispiel-Workflow

1. Ein Benutzer gibt in n8n eine Frage ein (z. B. über einen UI-Formular-Node)
2. Die Frage wird an ein Shell-Skript übergeben:

```bash
python3 /home/mm/n8n-server/scripts/query_documents.py "Welche Dokumente enthalten Informationen zur Mehrwertsteuer?"
```

3. Das Skript durchsucht ChromaDB und liefert:

   * Dateinamen
   * Textauszüge (Matches)
   * Ähnlichkeitswerte
   * ggf. Begründungen

4. n8n zeigt die Antwort als strukturierte Nachricht an (z. B. E-Mail, UI, Messenger, etc.)

---

## 🧠 Antwortformat

Die Antwort des Python-Skripts sollte wie folgt formatiert sein:

```json
{
  "matches": [
    {
      "file": "rechnung_2023.pdf",
      "excerpt": "... enthaltene Mehrwertsteuer betrug ...",
      "score": 0.83
    },
    ...
  ]
}
```

n8n kann die Antwort anschließend visualisieren oder weiterverarbeiten.

---

## ⚠️ Hinweise zur Qualität

* Die Genauigkeit hängt stark vom verwendeten Transformer-Modell ab (z. B. `all-MiniLM-L6-v2`)
* Verwende immer denselben Encoder wie beim Speichern (`store_doc.py`)
* Kontextfenster sind begrenzt – formuliere präzise Fragen

---

## 🔄 Beispielaufruf (manuell)

```bash
source ~/chromaenv/bin/activate
~/start-chroma.sh
python3 /home/mm/n8n-server/scripts/query_documents.py "Welche Dokumente nennen Unternehmen außerhalb der EU?"
```

---

## ✅ Tipps für Integration in n8n

* Verwende `Execute Command` oder `HTTP Request` an lokales API
* Lasse Benutzerfragen per UI-Formular eingeben
* Analysiere das JSON-Ergebnis mit `Edit Fields` oder `IF Node`
* Nutze `Markdown`-Format für klare Antworten

---

## 📌 Optional: Lokales LLM einbinden

* Lasse n8n eine finale Antwort per LLM erzeugen
* Prompt-Vorlage:

```text
Die folgenden Dokumentenausschnitte wurden als relevant zur Frage erkannt:

1. {{excerpt1}}
2. {{excerpt2}}

Formuliere eine präzise Antwort basierend auf diesen Auszügen.
```

* Übergib das als Prompt an Ollama/TinyLlama oder externes LLM

---

## 🧪 Testfrage (Beispiel)

```json
{
  "question": "Welche PDFs enthalten Informationen zu Steuerbefreiung bei Ausfuhren?"
}
```

Antwort:

```json
{
  "matches": [
    {
      "file": "steuer_ausfuhr_2024.pdf",
      "excerpt": "... bei Ausfuhren in Drittstaaten steuerfrei ...",
      "score": 0.91
    }
  ]
}
```

---

## 📁 Dateien

* `query_documents.py`: ChromaDB-Abfrage via Command Line
* `store_doc.py`: PDF-Import & Vektorisierung
* `start-chroma.sh`: Startet ChromaDB mit Health-Check
