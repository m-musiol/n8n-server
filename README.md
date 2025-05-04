# n8n-Server Setup

Dieses Repository enthält eine vollständige Selfhosting-Anleitung für folgende Komponenten:

- 🧩 [n8n mit Docker installieren](docs/setup-n8n-docker.md)  
- 🧠 [Lokale Sprachmodelle mit Ollama betreiben](docs/setup-ollama-local.md)  
- 🌐 [Caddy mit DuckDNS und HTTPS einrichten](docs/setup-caddy-https.md)

---

## Struktur

| Ordner         | Inhalt                                                              |
|----------------|---------------------------------------------------------------------|
| `docker/`       | Docker-Compose-Dateien und Konfigs für n8n, Caddy, Ollama          |
| `docs/`         | Schritt-für-Schritt-Anleitungen (Markdown)                         |
| `docs/models/`  | Zusatzinfos zu verwendeten Modellen                                |
| `workflows/`    | Exportierte n8n-Workflows als JSON-Dateien                         |

---

Alle Anleitungen sind so geschrieben, dass keine vertraulichen Informationen preisgegeben werden.  
⚠️ Die Eingaben müssen daher an den entsprechenden Stellen angepasst werden (z. B. DuckDNS-Subdomain, Passwörter, Tokens etc.).