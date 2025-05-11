# 🧠 Ollama lokal mit Docker nutzen

Dieses Setup beschreibt, wie du [Ollama](https://ollama.com/) lokal auf deinem Raspberry Pi (oder einem anderen Linux-System) im Docker-Container betreibst und per API ansteuerst.

## 📁 Voraussetzungen

* Docker & Docker Compose
* ca. 4–8 GB RAM empfohlen (je nach Modell)
* optional: Reverse Proxy (z. B. Caddy)

## 🧰 Schritt-für-Schritt

### 1. `docker-compose.ollama.yml` erstellen

```yaml
disversion: '3.8'
services:
  ollama:
    image: ollama/ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama:/root/.ollama
    restart: unless-stopped
volumes:
  ollama:
```

> Port 11434 ist der Standardport der Ollama-API.

### 2. Container starten

```bash
docker compose -f docker-compose.ollama.yml up -d
```

### 3. Modell herunterladen

Beispiel für TinyLlama:

```bash
curl http://localhost:11434/api/pull -d '{"name": "tinyllama"}'
```

Alternativ via UI (nur verfügbar, wenn aktiviert).

## 🧪 Testen

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Was ist der Sinn des Lebens?"
}'
```

## 📁 Beispielverzeichnis

```bash
n8n-server/
├── docker-compose.yml
├── docker-compose.ollama.yml         # ← optionaler Container für Ollama
└── docs/
    └── setup-ollama-local.md         # ← diese Datei
```

## 📄 Weiterführend

* [Ollama Docs](https://ollama.com/library)
* [API Referenz](https://ollama.com/docs/api)
