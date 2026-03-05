#!/usr/bin/env bash
set -euo pipefail

# Initial setup for Varro production deployment.
# Run once: sudo bash deploy/setup.sh
#
# After setup, use: ./deploy/manage-workers.sh scale 4

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WORKERS=${1:-4}

echo "=== Installing systemd template unit ==="
cp "${SCRIPT_DIR}/varro@.service" /etc/systemd/system/varro@.service
systemctl daemon-reload

echo "=== Installing Caddyfile ==="
cp "${SCRIPT_DIR}/Caddyfile" /etc/caddy/Caddyfile
caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
systemctl reload caddy

echo "=== Starting ${WORKERS} workers ==="
for i in $(seq 1 "$WORKERS"); do
    id=$(printf "%03d" "$i")
    systemctl enable "varro@${id}.service"
    systemctl start "varro@${id}.service"
    echo "  Started worker ${id} (port 800${i})"
done

echo ""
echo "=== Setup complete ==="
echo "Workers: ${WORKERS}"
echo "Manage with: ./deploy/manage-workers.sh {scale|status|restart|deploy|logs}"
echo ""
systemctl list-units 'varro@*' --no-pager
