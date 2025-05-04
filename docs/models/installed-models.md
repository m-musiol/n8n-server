# Installierte lokale Sprachmodelle

Dieses Dokument gibt einen Überblick über die auf dem Raspberry Pi 5 installierten LLMs (Large Language Models), die lokal via [Ollama](https://ollama.com) betrieben werden. Es werden sowohl die installierten Modelle als auch die Gründe für deren Auswahl genannt. Darüber hinaus werden Alternativen aufgezeigt.

⚠️ **Hinweis:** Dieses Repository ist öffentlich. Stelle sicher, dass keine vertraulichen Informationen preisgegeben werden.

---

## Voraussetzungen

* Docker ist installiert und funktionsfähig
* Ollama läuft im Container auf Port `11434`
* Genügend Speicherplatz für Modelle (je nach Modell mehrere GB)

---

## Installierte Modelle

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

---

## Alternative Modelle (nicht installiert)

| Modell     | Größe    | Beschreibung                               | Bemerkung                     |
| ---------- | -------- | ------------------------------------------ | ----------------------------- |
| llama2:7b  | \~4 GB   | Gute Sprachqualität, von Meta              | Zu groß für Pi ohne SWAP      |
| mistral:7b | \~4 GB   | Sehr gutes, schnelles Modell               | Nur mit 8+ GB RAM praktikabel |
| phi:2      | \~1,5 GB | Kompakt, gute Ergebnisse im Benchmark      | Englisch fokussiert           |
| orca-mini  | \~1,4 GB | Microsoft-Modell, gutes Instruction-Tuning | Kompatibel mit Ollama         |

---

## Empfehlung zur Auswahl

* **Für Produktivbetrieb auf Raspberry Pi 5:**

  * `gemma:2b` ist ein robuster Kompromiss zwischen Performance und Qualität.

* **Für Experimente und Geschwindigkeit:**

  * `tinyllama` ist eine hervorragende Wahl für schnelle Tests.

---

## Ausblick

Zukünftig könnten auch quantisierte Modelle im `ggml`- oder `gguf`-Format eingesetzt werden, um den RAM-Bedarf weiter zu reduzieren. Diese werden aktuell nicht über Ollama angeboten, könnten aber über `llama.cpp` eingebunden werden.
