# 🔎 Durchsuchen der indexierten Dokumente mit ChromaDB

Dieses Dokument beschreibt, wie du gespeicherte Dokumenteninhalte in ChromaDB abfragen kannst. Ziel ist es, Textinhalte, die zuvor per `docwatcher` automatisch extrahiert und gespeichert wurden, lokal und ohne Cloud-Dienste zu durchsuchen.

---

## 📦 Voraussetzungen

* Die Datei wurde erfolgreich mit `docwatcher.py` verarbeitet
* ChromaDB wurde gestartet
* Die Python-Umgebung ist aktiv:

  ```bash
  source ~/chromaenv/bin/activate
  ```

---

## 🧪 Beispielskript zur Abfrage (`query_test.py`)

```python
import chromadb
client = chromadb.HttpClient(host="127.0.0.1", port=8001)
collection = client.get_collection("documents")

results = collection.query(
    query_texts=["Conversion Booster mit KI"],
    n_results=2
)

for doc, score in zip(results["documents"], results["distances"]):
    print("\n📄 Dokument:", doc)
    print("📏 Ähnlichkeit:", score)
```

---

## 📚 Hinweise zur Abfrage

* Die Texte werden semantisch durchsucht (Vektorvergleich)
* Die Ausgabe enthält den passenden Dokumenttext und eine Distanzmetrik
* Je niedriger der Wert unter "📏 Ähnlichkeit", desto besser die Übereinstimmung

---

## 🛠 Tipps zur Nutzung

* Stelle sicher, dass ChromaDB **bereits läuft**, bevor du das Skript startest
* Suchbegriffe können auch längere Fragen oder Stichworte sein
* Passe `n_results` an, um mehr oder weniger Treffer zu erhalten

---

## 🧼 Fehlerbehandlung

Falls du folgende Fehlermeldung siehst:

```
chromadb.errors.NotFoundError: Collection [documents] does not exist
```

Dann wurde noch kein Dokument gespeichert oder `docwatcher.py` lief nicht erfolgreich.

---

## 🧪 Erweiterungsidee

Für interaktive Nutzung in n8n kann dieses Skript auch in einem **n8n-Code-Node** (Python) verwendet oder über einen lokalen HTTP-Endpunkt aufgerufen werden.
