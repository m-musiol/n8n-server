# n8n-server

Self-hosted [n8n](https://n8n.io/) automation server running on Docker, reverse-proxied via Caddy with automatic HTTPS using DuckDNS.

## 🔧 Projektstruktur

n8n-server/ ├── docker/ # Docker-Setup inkl. Caddy und n8n │ ├── Caddyfile │ ├── docker-compose.yml │ └── docker-compose.caddy.yml ├── docs/ # Dokumentation zur Installation und Erweiterung └── workflows/ # Eigene n8n-Workflows als JSON-Export

## 🚀 Setup (getestet auf Raspberry Pi 5)

### Voraussetzungen

- [Docker & Docker Compose](https://docs.docker.com/engine/install/)
- [DuckDNS Domain](https://www.duckdns.org/)
- Portweiterleitung (TCP 80 & 443) auf die lokale IP des Pi
- GitHub SSH-Zugriff eingerichtet (optional)

### Installation

1. Klone das Repository via SSH:
    ```bash
    git clone git@github.com:m-musiol/n8n-server.git
    cd n8n-server/docker
    ```

2. Starte den n8n-Container (lokal):
    ```bash
    docker-compose up -d
    ```

3. Starte den Caddy-Reverse-Proxy mit HTTPS via DuckDNS:
    ```bash
    docker-compose -f docker-compose.caddy.yml up -d
    ```

4. Rufe deine Instanz im Browser auf:  
   **https://dein-subdomain.duckdns.org**

   Zugang geschützt mit Basic Auth (`admin` + Passwort deiner Wahl).

## 🧠 Ziel

Dieses Projekt dient als Basis für eigene Automatisierungen und Experimente mit n8n.  
In Zukunft sollen auch lokale LLMs eingebunden werden. Dokumentationen dazu folgen im Ordner `docs/`.

## 📂 Workflows

Eigene Workflows werden in der Struktur `workflows/` als `.json` hinterlegt und nach und nach ergänzt.