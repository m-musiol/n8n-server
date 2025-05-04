# Lokale Installation von LLMs mit Ollama auf dem Raspberry Pi 5

Diese Anleitung beschreibt die Einrichtung von Ollama zur lokalen Ausführung von Sprachmodellen (LLMs) wie **Gemma 2B** und **TinyLlama** auf einem Raspberry Pi 5.

> ⚠️ **Hinweis:** Diese Dokumentation ist öffentlich. Stelle sicher, dass keine vertraulichen Informationen preisgegeben werden. Passe deine Eingaben entsprechend an.

---

## Voraussetzungen

- Raspberry Pi 5 mit aktuellem Raspberry Pi OS (64-Bit)
- Docker ist installiert und funktionsfähig
- Ca. 5–6 GB freier Arbeitsspeicher empfohlen (ZRAM oder Auslagerung ggf. aktivieren)
- Internetverbindung für den Modell-Download
- Optional: DuckDNS-Setup für API-Zugriff aus dem Netzwerk

---

## Projektstruktur (Auszug)

```plaintext
n8n-server/
├── docker/
├── docs/
│   └── setup-ollama-local.md
└── workflows/
```

---

## Schritte zur Einrichtung

### 1. Docker-Container starten

```bash
docker pull ollama/ollama

docker run -d \
  -v ollama:/root/.ollama \
  -p 11434:11434 \
  --name ollama \
  ollama/ollama
```

Nach dem Start ist der Ollama-Endpunkt unter `http://localhost:11434` erreichbar.

---

### 2. Gemma 2B-Modell laden

```bash
docker exec -it ollama ollama run gemma:2b
```

Der Download kann einige Minuten dauern. Nach erfolgreichem Laden erscheint eine Eingabeaufforderung.

---

### 3. TinyLlama-Modell laden

```bash
docker exec -it ollama ollama run tinyllama
```

Auch dieses Modell wird beim ersten Aufruf heruntergeladen und danach lokal ausgeführt.

---

### 4. Zugriff über die API testen

Beispielaufruf via `curl`:

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "gemma:2b",
  "prompt": "Was ist der Sinn des Lebens?",
  "stream": false
}'
```

Die Antwort erfolgt im JSON-Format und enthält den vom Modell generierten Text.

---

### 5. Automatischer Start bei Systemstart (optional)

```bash
docker update --restart always ollama
```

---

## Nächstes Ziel

Die lokal laufenden LLMs sollen später über n8n-Workflows angesteuert werden. Weitere Beispiele und Workflows folgen im Projektordner `workflows/`.

---

## Weitere Informationen

- [Ollama Dokumentation](https://ollama.com)
- [Ollama API-Dokumentation](https://ollama.com/library)
