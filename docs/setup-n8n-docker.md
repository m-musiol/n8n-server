# n8n Docker Setup

Diese Anleitung beschreibt die Einrichtung von n8n auf einem Raspberry Pi 5 mit Docker, inklusive Reverse-Proxy mit Caddy und automatischer HTTPS-Konfiguration via DuckDNS.

⚠️ **Hinweis:** Diese Dokumentation ist öffentlich. Stelle sicher, dass keine vertraulichen Informationen preisgegeben werden. Passe deine Eingaben an den entsprechenden Stellen an.

---

## Voraussetzungen

- Raspberry Pi 5 mit aktuellem Raspberry Pi OS
- Docker & Docker Compose sind installiert
- DuckDNS-Domain ist eingerichtet (z. B. `m8m.duckdns.org`)
- GitHub-Zugriff (für Repository-Klon)
- Freigabe der Ports 80 & 443 am Router auf die lokale IP des Raspberry Pi

---

## Projektstruktur

```
n8n-server/
├── docker/           # Docker-Konfigurationen für n8n und Caddy
│   ├── docker-compose.yml
│   ├── docker-compose.caddy.yml
│   └── Caddyfile
├── docs/             # Dokumentation
│   └── setup-n8n-docker.md
└── workflows/        # Eigene n8n-Workflows als .json
```

---

## 1. n8n per Docker installieren

**Datei:** `docker/docker-compose.yml`

```yaml
services:
  n8n:
    image: n8nio/n8n:latest
    restart: always
    ports:
      - "5678:5678"
    volumes:
      - n8n_data:/home/node/.n8n
    networks:
      - n8n-network

volumes:
  n8n_data:

networks:
  n8n-network:
    external: true
```

---

## 2. Caddy als Reverse Proxy mit HTTPS

**Datei:** `docker/docker-compose.caddy.yml`

```yaml
services:
  caddy:
    image: caddy:latest
    container_name: caddy
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile
      - caddy_data:/data
      - caddy_config:/config
    networks:
      - n8n-network

volumes:
  caddy_data:
  caddy_config:

networks:
  n8n-network:
    external: true
```

---

## 3. Zugangsschutz mit Passwort

**Datei:** `docker/Caddyfile`

```text
m8m.duckdns.org {
    reverse_proxy n8n:5678
    basic_auth {
        admin <BCRYPT_HASH>
    }
}
```

**Hash generieren:**

```bash
docker run --rm -it caddy caddy hash-password
```

---

## 4. Netzwerk vorbereiten

Nur einmal erforderlich:

```bash
docker network create n8n-network
```

---

## 5. Container starten

```bash
cd /home/mm/n8n-server/docker
docker compose -f docker-compose.yml up -d
docker compose -f docker-compose.caddy.yml up -d
```

---

## 6. n8n per HTTPS erreichbar machen

Öffne im Browser:

```
https://<deine-subdomain>.duckdns.org
```

Beispiel:  
[https://m8m.duckdns.org/](https://m8m.duckdns.org/)

> Du wirst nach Benutzername und Passwort gefragt (`admin` + dein gewähltes Passwort aus Schritt 3).

---

## ✅ Fertig!

n8n ist nun unter deiner DuckDNS-Adresse mit HTTPS und Passwortschutz erreichbar.
