# 🔐 Caddy mit HTTPS für n8n

Dieses Setup ermöglicht eine abgesicherte Verbindung per HTTPS mit automatischer Zertifikatsverwaltung über [Caddy](https://caddyserver.com/).

## 📁 Voraussetzungen

* Domain mit A-Eintrag auf die IP-Adresse deines Raspberry Pi
* Ports 80 und 443 sind offen und auf deinen Pi weitergeleitet (Port-Forwarding)
* Docker & Docker Compose sind installiert

## 📦 Verwendete Dateien

* `docker-compose.caddy.yml`: Definiert den Caddy-Container
* `Caddyfile`: Konfiguriert das Routing inkl. HTTPS für n8n

## ⚙ Verzeichnisstruktur

```bash
n8n-server/
├── docker-compose.yml                # Hauptkomposition
├── docker-compose.caddy.yml         # Optionaler Caddy-Container
├── Caddyfile                        # Konfiguration für Caddy
└── docs/
    ├── setup-n8n-docker.md
    └── setup-caddy-https.md         # ← diese Datei
```

## 🧰 Caddy Setup Schritt-für-Schritt

### 1. Konfigurationsdateien erstellen

#### `Caddyfile`

```Caddyfile
n8n.example.com {
  reverse_proxy n8n:5678
}
```

> Ersetze `n8n.example.com` durch deine eigene Domain.

### 2. Caddy starten (zusätzlich zu deinem Haupt-Docker-Setup)

```bash
docker compose -f docker-compose.caddy.yml up -d
```

Caddy holt automatisch ein TLS-Zertifikat von Let's Encrypt und leitet den Verkehr auf Port 443 an den internen n8n-Container weiter.

## ✅ Test

1. Rufe deine Domain im Browser auf (`https://n8n.example.com`)
2. Das n8n-Interface sollte über HTTPS erreichbar sein

Wenn es nicht funktioniert, prüfe:

* Ist die Domain korrekt konfiguriert?
* Sind Ports 80 und 443 weitergeleitet?
* Ist der Caddy-Container erfolgreich gestartet?

## 📄 Referenzen

* [Caddy Dokumentation](https://caddyserver.com/docs/)
* [n8n Dokumentation](https://docs.n8n.io/)
