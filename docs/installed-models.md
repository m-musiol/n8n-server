# 📚 Installierte Modelle (Ollama)

Dieses Dokument listet die speziell für diesen Anwendungszweck installierten KI-Modelle im Docker-Ollama-Setup auf. Die Modelle wurden manuell per API gezogen und stehen über den Ollama-Server unter `http://localhost:11434` zur Verfügung.

## 📦 Aktuell installierte Modelle

### 1. `gemma:2b`

* **Modellgröße:** ca. 1,7 GB
* **Typ:** Decoder-only, Chat-optimiert
* **Sprache:** Multilingual (inkl. Deutsch)
* **Vorteile:**

  * Gute Balance aus Geschwindigkeit und Sprachqualität
  * Lauffähig auf Raspberry Pi 5 (8 GB RAM empfohlen)
  * Lizenz von Google erlaubt Forschung und private Nutzung
* **Einsatz:** Allgemeine Texteingabe, einfache Dialogsysteme

**Beispielbefehl zur Installation:**

```bash
docker exec -it ollama ollama run gemma:2b
```

### 2. `tinyllama`

* **Modellgröße:** ca. 640 MB
* **Typ:** Kleinstes lauffähiges LLM mit brauchbarer Sprachleistung
* **Sprache:** Englisch (eingeschränkt auch andere Sprachen)
* **Vorteile:**

  * Extrem leichtgewichtig
  * Ideal für ressourcenarme Systeme wie den Pi 5
  * Schnellere Antwortzeiten
* **Einschränkungen:**

  * Begrenzte Kontextlänge
  * Sprachqualität niedriger als bei größeren Modellen
* **Einsatz:** Tests, einfache Promptbeispiele, Skriptgenerierung

**Beispielbefehl zur Installation:**

```bash
docker exec -it ollama ollama run tinyllama
```

## 📁 Speicherort

Die Modelle liegen standardmäßig im Docker-Volume `ollama`, das beim Starten des Containers automatisch angelegt wird:

```bash
volumes:
  - ollama:/root/.ollama
```

## 🔁 Modellpflege

### Aktualisieren eines Modells

```bash
curl http://localhost:11434/api/pull -d '{"name": "tinyllama"}'
```

### Modell entfernen (wenn möglich)

> Derzeit ist das Entfernen nicht direkt dokumentiert. Container-Reset entfernt auch Modelle.

## 📄 Referenzen

* [Ollama Model Registry](https://ollama.com/library)
* [API Referenz](https://ollama.com/docs/api)
