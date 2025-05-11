# n8n-server

Automatisierte Workflows mit [n8n](https://n8n.io) und lokaler KI-Unterstützung auf einem Raspberry Pi 5. Dieses Repository enthält:

* ein Docker-Setup für n8n
* HTTPS per Caddy + DuckDNS
* lokale KI per Ollama (TinyLlama, Gemma)
* automatische Dokumentenanalyse mit ChromaDB & Tesseract OCR

---

## 🤖 Ziel

Eine lokal betriebene n8n-Instanz mit einfacher Konfiguration, erweiterbar durch lokale Sprachmodelle (LLMs) und eine dokumentenbasierte Vektordatenbank.

---

## 🚀 Schnellstart

```bash
cd docker
cp docker-compose.caddy.yml docker-compose.yml
# Optional: .env mit deinen Zugangsdaten ergänzen

# Starten
docker compose up -d
```

Zugriff auf n8n:

* **ohne HTTPS:** [http://localhost:5678](http://localhost:5678)
* **mit HTTPS:** [https://deine-subdomain.duckdns.org](https://deine-subdomain.duckdns.org) (falls eingerichtet)

---

## 📚 Dokumentation

| Thema                               | Pfad                                                             |
| ----------------------------------- | ---------------------------------------------------------------- |
| n8n mit Docker starten              | [docs/setup-n8n-docker.md](docs/setup-n8n-docker.md)             |
| Caddy mit HTTPS via DuckDNS         | [docs/setup-caddy-https.md](docs/setup-caddy-https.md)           |
| Lokale LLMs mit Ollama              | [docs/setup-ollama-local.md](docs/setup-ollama-local.md)         |
| Installierte LLMs (Übersicht)       | [docs/installed-models.md](docs/installed-models.md)             |
| Dokumentenanalyse mit ChromaDB      | [docs/setup-docwatcher-chromadb.md](docs/setup-docwatcher-chromadb.md) |
| Abfrage lokaler Dokumente mit LLMs  | [docs/query-documents-chromadb.md](docs/query-documents-chromadb.md) |
| DocWatcher systemd-Dienst           | [docs/setup-docwatcher-service.md](docs/setup-docwatcher-service.md) |

---

## 📁 Struktur

```bash
n8n-server/
├── docker/                        # Docker-Setups für n8n, Caddy, Ollama
├── docs/                          # Setup-Anleitungen
│   ├── installed-models.md
│   ├── query-documents-chromadb.md
│   ├── setup-caddy-https.md
│   ├── setup-docwatcher-chromadb.md
│   ├── setup-docwatcher-service.md
│   ├── setup-n8n-docker.md
│   └── setup-ollama-local.md
├── scripts/                       # Python-Skripte (z. B. docwatcher, Tests)
│   ├── docwatcher.py
│   ├── list_collections.py
│   ├── main.py
│   ├── pdf_extractor.py
│   └── query_test.py
├── docwatch/                      # Dokumenten-Ein-/Ausgangsordner für PDF-Überwachung
├── workflows/                     # Beispielhafte n8n-Flows (optional)
└── README.md                      # Diese Datei
```
