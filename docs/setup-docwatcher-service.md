# 🛠️ systemd-Dienst: DocWatcher

Dieses Dokument beschreibt, wie der `docwatcher`-Dienst eingerichtet ist, um automatisch eingehende PDF-Dateien zu überwachen, zu verarbeiten und in ChromaDB zu speichern.

---

## 📂 Verzeichnisstruktur

```bash
/home/mm/n8n-server/
├── scripts/
│   └── docwatcher.py         # Hauptskript zur PDF-Verarbeitung
├── docs/
│   └── setup-docwatcher-service.md  # ← Diese Datei
```

---

## ⚙️ systemd-Konfiguration

Pfad zur Dienstdefinition:

```bash
/etc/systemd/system/docwatcher.service
```

### Inhalt:

```ini
[Unit]
Description=DocWatcher - Automatische PDF-Überwachung
After=network.target

[Service]
Type=simple
Environment=VIRTUAL_ENV=/home/mm/chromaenv
Environment=PATH=/home/mm/chromaenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin
WorkingDirectory=/home/mm/chromaenv

ExecStartPre=/bin/bash -c '
  for i in {1..30}; do
    echo "⏳ Warte auf ChromaDB (127.0.0.1:8001) – Versuch $i …";
    nc -z 127.0.0.1 8001 && exit 0;
    sleep 2;
  done;
  echo "❌ ChromaDB nicht erreichbar, Abbruch.";
  exit 1'

ExecStart=/home/mm/chromaenv/bin/python3 /home/mm/n8n-server/scripts/docwatcher.py
Restart=always
User=mm
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

---

## ▶️ Dienst aktivieren & starten

```bash
sudo systemctl daemon-reload
sudo systemctl enable docwatcher.service
sudo systemctl start docwatcher.service
```

---

## ✅ Status prüfen

```bash
systemctl status docwatcher.service
```

Bei erfolgreicher Ausführung werden neue PDFs automatisch verarbeitet und in ChromaDB gespeichert.

