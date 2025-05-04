# Caddy mit DuckDNS und HTTPS

Diese Anleitung beschreibt die Einrichtung von Caddy als Reverse-Proxy mit automatischem HTTPS-Zertifikat über DuckDNS auf einem Raspberry Pi 5.

⚠️ **Hinweis:** Diese Dokumentation ist öffentlich. Stelle sicher, dass keine vertraulichen Informationen preisgegeben werden. Passe die Werte z. B. für Domains und Passwörter entsprechend an.

---

## Voraussetzungen

* Caddy ist per Docker installiert
* Eine DuckDNS-Domain ist aktiv (z. B. `m8m.duckdns.org`)
* Portweiterleitung (TCP 80 und 443) vom Router an die lokale IP des Raspberry Pi
* Zugriff auf das bestehende Docker-Netzwerk, in dem z. B. `n8n` läuft

---

## 1. Caddy Docker-Setup

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

## 2. Caddyfile mit Reverse Proxy und Basic Auth

**Datei:** `docker/Caddyfile`

```caddyfile
m8m.duckdns.org {
    reverse_proxy n8n:5678
    basic_auth {
        admin <BCRYPT_HASH>
    }
}
```

**Hinweis:**

* Ersetze `m8m.duckdns.org` durch deine eigene Subdomain.
* Ersetze `<BCRYPT_HASH>` durch einen sicheren Passwort-Hash.
* Erstelle den Passwort-Hash mit:

```bash
docker run --rm -it caddy caddy hash-password
```

---

## 3. Netzwerk vorbereiten (falls nicht vorhanden)

```bash
docker network create n8n-network
```

---

## 4. Caddy starten

```bash
cd ~/n8n-server/docker
docker compose -f docker-compose.caddy.yml up -d
```

---

## 5. Zugriff testen

Im Browser aufrufen:

```
https://<deine-subdomain>.duckdns.org
```

Du solltest nun zur Eingabe von Benutzername (`admin`) und Passwort aufgefordert werden.

---

## Fertig

Caddy läuft nun als Reverse Proxy mit automatischer HTTPS-Konfiguration über Let's Encrypt und schützt den Zugriff mit Basic Auth.
