# Sticky Session Deployment: FastHTML + Caddy + systemd

Deploying a stateful FastHTML/ASGI application across multiple workers with session affinity, using systemd template units and Caddy's cookie-based load balancing. Designed for a Hetzner server (Ubuntu) with 24 cores / 100GB RAM, supporting up to 30+ workers.

---

## Architecture Overview

```
                          ┌─────────────────┐
                          │     Caddy        │
         Internet ──────▶ │  (HTTPS + LB)   │
                          │  cookie-sticky   │
                          └────────┬─────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                     │
        ┌─────┴─────┐      ┌─────┴─────┐        ┌─────┴─────┐
        │ uvicorn    │      │ uvicorn    │   ...  │ uvicorn    │
        │ :8001      │      │ :8002      │        │ :8030      │
        │ + IPython  │      │ + IPython  │        │ + IPython  │
        └────────────┘      └────────────┘        └────────────┘
```

Each uvicorn process is independent, listens on its own port, and owns its own IPython kernel. Caddy sets a cookie on the user's first request and routes all subsequent requests to the same backend.

---

## 1. Application Setup

### Port Configuration

The app must read its port from an environment variable so each worker instance binds to a unique port. In your FastHTML entrypoint (e.g. `main.py`):

```python
import os

port = int(os.environ.get("PORT", 8001))

# If using FastHTML's serve():
serve(host="127.0.0.1", port=port)

# Or if you launch via uvicorn CLI, handle it there instead
# and don't call serve() at all.
```

If you launch via the uvicorn CLI (recommended for production), you don't need this — the port is passed as a CLI flag.

### Project Structure

```
/home/titan/myapp/
├── .venv/
├── main.py
├── requirements.txt
└── ...
```

---

## 2. systemd Template Unit

systemd template units use `@` in the filename. The part after `@` when starting the service becomes `%i` inside the unit file.

### Create the Template

```bash
sudo nano /etc/systemd/system/myapp@.service
```

```ini
[Unit]
Description=MyApp worker %i (port 8%i)
After=network.target

[Service]
User=titan
Group=titan
WorkingDirectory=/home/titan/myapp
Environment="PATH=/home/titan/myapp/.venv/bin"
Environment="PYTHONUNBUFFERED=1"

# Port is derived from the instance number: instance 001 → port 8001, etc.
ExecStart=/home/titan/myapp/.venv/bin/uvicorn main:app \
    --host 127.0.0.1 \
    --port 8%i \
    --log-level info

# Process management
Restart=always
RestartSec=3
StartLimitIntervalSec=60
StartLimitBurst=5

# Resource limits (optional but recommended)
LimitNOFILE=65536
MemoryMax=3G

# Security hardening
PrivateTmp=true
NoNewPrivileges=true
ProtectSystem=strict
ReadWritePaths=/home/titan/myapp

[Install]
WantedBy=multi-user.target
```

### Instance Numbering Scheme

Use zero-padded three-digit instance IDs so the port math works cleanly:

| Instance ID | Port  |
|-------------|-------|
| `001`       | 8001  |
| `002`       | 8002  |
| `010`       | 8010  |
| `030`       | 8030  |

This supports ports 8001–8099 (up to 99 workers) without any scheme changes.

**Important:** The `%i` substitution in the `ExecStart` line means instance `001` → `--port 8001`. This works because systemd does simple string substitution: `8%i` becomes `8001`.

### Enable and Start Workers

To spin up 4 workers:

```bash
sudo systemctl daemon-reload

# Enable (auto-start on boot) and start
for i in $(seq -w 1 4); do
    id=$(printf "%03d" $i)
    sudo systemctl enable myapp@${id}.service
    sudo systemctl start myapp@${id}.service
done
```

To spin up 30 workers:

```bash
for i in $(seq -w 1 30); do
    id=$(printf "%03d" $i)
    sudo systemctl enable myapp@${id}.service
    sudo systemctl start myapp@${id}.service
done
```

### Check Status

```bash
# All workers at once
systemctl list-units 'myapp@*' --no-pager

# Specific worker
sudo systemctl status myapp@003.service

# Logs for a specific worker
journalctl -u myapp@003.service -f
```

---

## 3. Caddy Configuration

### Caddyfile

The Caddyfile needs to list all backend upstreams. For a dynamic number of workers, use a Caddy snippet or generate the block.

#### Static config (if worker count is stable)

```
myapp.vindra.dk {
    reverse_proxy localhost:8001 localhost:8002 localhost:8003 localhost:8004 {
        lb_policy cookie myapp_sticky
    }
}
```

#### Dynamic config for many workers

Rather than hand-typing 30 upstreams, generate the Caddyfile block with a script (see Section 5). The result looks like:

```
myapp.vindra.dk {
    reverse_proxy localhost:8001 localhost:8002 localhost:8003 localhost:8004 \
                  localhost:8005 localhost:8006 localhost:8007 localhost:8008 \
                  localhost:8009 localhost:8010 localhost:8011 localhost:8012 \
                  localhost:8013 localhost:8014 localhost:8015 localhost:8016 \
                  localhost:8017 localhost:8018 localhost:8019 localhost:8020 \
                  localhost:8021 localhost:8022 localhost:8023 localhost:8024 \
                  localhost:8025 localhost:8026 localhost:8027 localhost:8028 \
                  localhost:8029 localhost:8030 {
        lb_policy cookie myapp_sticky

        # Health checks: remove unresponsive workers from rotation
        health_uri /health
        health_interval 10s
        health_timeout 3s
        health_status 200
    }
}
```

### How Cookie-Based Sticky Sessions Work

1. User sends first request → Caddy picks a backend (round-robin among healthy upstreams).
2. Caddy sets a cookie (`myapp_sticky`) containing an identifier for that backend.
3. On subsequent requests, the browser sends the cookie back → Caddy routes to the same backend.
4. If that backend goes down, Caddy picks a new one and updates the cookie.

**Important:** This means if a worker restarts, users pinned to it will be reassigned to a new worker. Their IPython state in the old worker is lost. See Section 6 for mitigation.

### Health Check Endpoint

Add a `/health` route to your app so Caddy can detect down workers:

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

### Reload Caddy

```bash
sudo systemctl reload caddy
```

---

## 4. Management Script

Create a helper script to manage workers and keep the Caddyfile in sync.

```bash
sudo nano /home/titan/myapp/manage-workers.sh
chmod +x /home/titan/myapp/manage-workers.sh
```

```bash
#!/usr/bin/env bash
set -euo pipefail

APP_NAME="myapp"
CADDY_FILE="/etc/caddy/Caddyfile"
DOMAIN="myapp.vindra.dk"
BASE_PORT=8000
HEALTH_URI="/health"

usage() {
    echo "Usage: $0 {scale|status|restart|logs} [args]"
    echo ""
    echo "  scale N        - Scale to N workers (enables/disables as needed)"
    echo "  status         - Show status of all workers"
    echo "  restart [N]    - Restart worker N, or all workers if N omitted"
    echo "  logs N         - Tail logs for worker N"
    echo ""
    exit 1
}

get_active_workers() {
    systemctl list-units "${APP_NAME}@*" --no-pager --no-legend 2>/dev/null | \
        grep -oP "${APP_NAME}@\K[0-9]+" | sort -n
}

scale() {
    local target=$1
    echo "Scaling ${APP_NAME} to ${target} workers..."

    # Start/enable workers up to target
    for i in $(seq 1 "$target"); do
        id=$(printf "%03d" "$i")
        sudo systemctl enable "${APP_NAME}@${id}.service" 2>/dev/null
        sudo systemctl start "${APP_NAME}@${id}.service" 2>/dev/null
        echo "  ✓ Worker ${id} (port $((BASE_PORT + i)))"
    done

    # Stop/disable workers above target
    for i in $(seq $((target + 1)) 99); do
        id=$(printf "%03d" "$i")
        if systemctl is-enabled "${APP_NAME}@${id}.service" &>/dev/null; then
            sudo systemctl stop "${APP_NAME}@${id}.service"
            sudo systemctl disable "${APP_NAME}@${id}.service"
            echo "  ✗ Worker ${id} stopped"
        fi
    done

    # Regenerate Caddy upstream list
    update_caddy "$target"

    echo "Done. ${target} workers running."
}

update_caddy() {
    local count=$1
    local upstreams=""

    for i in $(seq 1 "$count"); do
        upstreams+="localhost:$((BASE_PORT + i)) "
    done

    # Generate the reverse_proxy block
    local block="${DOMAIN} {
    reverse_proxy ${upstreams}{
        lb_policy cookie ${APP_NAME}_sticky
        health_uri ${HEALTH_URI}
        health_interval 10s
        health_timeout 3s
        health_status 200
    }
}"

    echo "Updating Caddy config..."

    # Write to a temp file and validate before replacing
    local tmpfile
    tmpfile=$(mktemp)

    # Preserve other site blocks: remove old block for this domain, append new one
    # This assumes each domain block is self-contained in the Caddyfile
    python3 -c "
import re, sys

with open('${CADDY_FILE}', 'r') as f:
    content = f.read()

# Remove existing block for this domain (greedy within braces, handles nested)
pattern = r'${DOMAIN}\s*\{[^}]*(?:\{[^}]*\}[^}]*)*\}\s*'
content = re.sub(pattern, '', content).strip()

with open('${tmpfile}', 'w') as f:
    if content:
        f.write(content + '\n\n')
    f.write('''${block}
''')
"

    sudo cp "$tmpfile" "$CADDY_FILE"
    rm "$tmpfile"

    sudo caddy validate --config "$CADDY_FILE" --adapter caddyfile && \
        sudo systemctl reload caddy && \
        echo "  Caddy reloaded." || \
        echo "  ⚠ Caddy config invalid! Check ${CADDY_FILE}"
}

status() {
    echo "=== ${APP_NAME} workers ==="
    systemctl list-units "${APP_NAME}@*" --no-pager
}

restart_workers() {
    if [ -n "${1:-}" ]; then
        local id
        id=$(printf "%03d" "$1")
        echo "Restarting worker ${id}..."
        sudo systemctl restart "${APP_NAME}@${id}.service"
    else
        echo "Restarting all workers..."
        for unit in $(systemctl list-units "${APP_NAME}@*" --no-pager --no-legend | awk '{print $1}'); do
            sudo systemctl restart "$unit"
        done
    fi
}

show_logs() {
    local id
    id=$(printf "%03d" "$1")
    journalctl -u "${APP_NAME}@${id}.service" -f
}

case "${1:-}" in
    scale)   scale "${2:?'Specify number of workers'}" ;;
    status)  status ;;
    restart) restart_workers "${2:-}" ;;
    logs)    show_logs "${2:?'Specify worker number'}" ;;
    *)       usage ;;
esac
```

### Usage

```bash
# Scale to 8 workers (starts workers, updates Caddy, reloads)
./manage-workers.sh scale 8

# Scale down to 4 (stops excess workers, updates Caddy)
./manage-workers.sh scale 4

# Check status of all workers
./manage-workers.sh status

# Restart a specific worker
./manage-workers.sh restart 3

# Restart all workers
./manage-workers.sh restart

# Tail logs for worker 5
./manage-workers.sh logs 5
```

---

## 5. Resource Planning

### Memory Budget

With 100GB RAM and each uvicorn + IPython worker using roughly 200–500MB (depending on loaded data):

| Workers | Estimated Memory | RAM Headroom |
|---------|-----------------|--------------|
| 4       | 1–2 GB          | ~98 GB free  |
| 10      | 2–5 GB          | ~95 GB free  |
| 30      | 6–15 GB         | ~85 GB free  |

The `MemoryMax=3G` in the systemd unit caps any single worker from consuming more than 3GB (adjust as needed for your workload).

### CPU Budget

Each worker runs one async event loop on one core. With 24 cores:

- 4–8 workers: plenty of headroom for background tasks, other services
- 12–16 workers: moderate load, still comfortable
- 24+ workers: leaves little room for OS, Caddy, databases, other services

**Start with 4–8 workers and scale up based on observed load.** IPython-backed workers likely have bursty CPU usage, so overprovisioning workers relative to cores is fine since they won't all peak simultaneously.

---

## 6. Handling Worker Restarts and State Loss

The main risk with sticky sessions: if a worker restarts (crash, deploy, OOM kill), users pinned to it lose their IPython state. Mitigations:

### Graceful Deploys

When deploying new code, restart workers one at a time with a delay:

```bash
for i in $(seq 1 30); do
    id=$(printf "%03d" $i)
    sudo systemctl restart myapp@${id}.service
    sleep 5  # let Caddy health check detect it's back
done
```

### Client-Side Resilience

Have the frontend detect when its session state is gone (e.g. the IPython kernel returns an error or a "new session" indicator) and prompt the user to reinitialize, rather than silently failing.

### Longer-Term: External State Store

If state loss becomes a real problem, consider persisting IPython kernel state (variables, history) to Redis or disk, and restoring on reconnection. This is the "Option B" architecture — more work, but fully resilient.

---

## 7. Quick Reference

```bash
# Start everything from scratch with 8 workers
sudo systemctl daemon-reload
./manage-workers.sh scale 8

# Deploy new code
cd /home/titan/myapp && git pull
source .venv/bin/activate && pip install -r requirements.txt
./manage-workers.sh restart

# Monitor
./manage-workers.sh status
htop
journalctl -u 'myapp@*' -f

# Scale up under load
./manage-workers.sh scale 16

# Scale back down
./manage-workers.sh scale 4
```