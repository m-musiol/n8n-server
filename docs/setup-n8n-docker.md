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

Passe in `docker-compose.yml` den Benutzer:

```yaml
user: "1000:1000"
```

→ Damit wird sichergestellt, dass n8n Schreibrechte im Verzeichnis `/opt/n8n` hat.

Optional: Passe `.env` für eigene Umgebungsvariablen an (z. B. für DuckDNS, n8n-User etc.).

### 3. Volume vorbereiten

```bash
sudo mkdir -p /opt/n8n
sudo chown 1000:1000 /opt/n8n
```

### 4. Container starten

```bash
docker compose -f docker-compose.yml -f docker-compose.caddy.yml up -d
```

### 5. Registrierung durchführen

Öffne `http://localhost:5678` im Browser und registriere einen neuen Benutzer.

Anschließend sollten die Dateien `database.sqlite` und `config` im Volume `/opt/n8n` erscheinen:

```bash
ls -lh /opt/n8n
```

→ Jetzt ist das Setup dauerhaft funktionsfähig und benutzerverwaltet.

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
* Die n8n-Daten werden persistent gespeichert im Verzeichnis `/opt/n8n`, das im Container unter `/home/node/.n8n` eingebunden ist.
* Für ein Backup kannst du z. B. folgendes nutzen:

```bash
cp /opt/n8n/database.sqlite ~/n8n-backup.sqlite
```
