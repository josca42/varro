# Deployment

## Stack

- **Caddy** — reverse proxy, TLS, compression, sticky sessions
- **systemd template units** — `varro@{001..010}.service`, one uvicorn worker per unit
- **uvicorn** — ASGI server, one per worker on ports 8001–8010
- **Postgres** — 4 cores, 16GB memory allocation

## Files

All deployment config lives in `deploy/`:

| File | Purpose |
|------|---------|
| `varro@.service` | systemd template unit — instance `001` → port `8001`, etc. |
| `Caddyfile` | Cookie-sticky reverse proxy, gzip/zstd, HSTS, health checks |
| `manage-workers.sh` | Scale, restart, deploy, logs |
| `setup.sh` | One-time initial install |

## Initial Setup

```bash
sudo cp deploy/varro@.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo cp deploy/Caddyfile /etc/caddy/Caddyfile
sudo caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
sudo systemctl reload caddy

for i in $(seq 1 10); do
  id=$(printf "%03d" "$i")
  sudo systemctl enable "varro@${id}.service"
  sudo systemctl start "varro@${id}.service"
done
```

## Common Operations

```bash
# Status
systemctl list-units 'varro@*' --no-pager

# Rolling restart (all workers)
./deploy/manage-workers.sh restart

# Restart single worker
./deploy/manage-workers.sh restart 3

# Scale to N workers (updates Caddy too)
./deploy/manage-workers.sh scale 10

# Deploy (git pull + deps + rolling restart)
./deploy/manage-workers.sh deploy

# Logs for worker 1
./deploy/manage-workers.sh logs 1
# Or directly:
journalctl -u varro@001.service -f
```

## Architecture Notes

- **10 workers** on 16 cores / 64GB — leaves 6 cores for Postgres and OS
- Workers are **stateful**: `run_manager` (SSE streams) and `shell_pool` (IPython shells) are in-process
- **Sticky sessions** via Caddy `cookie` policy are mandatory — a user's SSE stream and shell must hit the same worker
- Dashboard requests are stateless — any worker can serve them
- Each IPython shell is a sandboxed bwrap subprocess (~80-120MB baseline, 2GB RLIMIT_AS cap)
- `VARRO_LIVE=0` disables FastHTML live reload in production

## Health Check

`GET /health` returns `200 "ok"`. Caddy checks every 10s and removes unhealthy workers from the pool.

## Env Var

- `VARRO_LIVE=0` — set in the systemd unit, disables live reload
- `VARRO_LIVE=1` (default) — used in development with `uv run python app/main.py`
