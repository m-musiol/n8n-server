# n8n mit Docker starten

Diese Anleitung beschreibt, wie du n8n per Docker auf einem Raspberry Pi 5 lokal betreibst. Sie ist optimiert für das Setup in diesem Repository.

---

## 🧱 Voraussetzungen

* Raspberry Pi 5 mit Raspberry Pi OS
* Docker & Docker Compose installiert
* n8n-Ordnerstruktur laut README eingerichtet

---

## 🔧 Schritt-für-Schritt-Anleitung

### 1. Repository klonen

```bash
cd ~
git clone https://github.com/m-musiol/n8n-server.git
cd n8n-server/docker
```

### 2. Konfiguration anpassen

Erstelle die Konfigurationsdatei:

```bash
cp docker-compose.caddy.yml docker-compose.yml
```

Optional: Passe `.env` für eigene Umgebungsvariablen an (z. B. für DuckDNS, n8n-User etc.).

### 3. Container starten

```bash
docker compose up -d
```

### 4. Zugriff auf n8n

* **Lokal ohne HTTPS:** `http://localhost:5678`
* **Über HTTPS mit Domain:** `https://deine-subdomain.duckdns.org` (wenn eingerichtet)

---

## 🛠 Nützliche Kommandos

Logs anzeigen:

```bash
docker compose logs -f
```

Container stoppen:

```bash
docker compose down
```

---

## 📌 Hinweise

* Wenn du HTTPS verwenden willst, richte [Caddy mit DuckDNS](./setup-caddy-https.md) ein.
* Die n8n-Daten werden persistent gespeichert im Verzeichnis `~/.n8n` (wird im Volume gemountet).

---