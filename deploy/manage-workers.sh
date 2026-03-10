#!/usr/bin/env bash
set -euo pipefail

APP_NAME="varro"
CADDY_FILE="/etc/caddy/Caddyfile"
DOMAIN="varro.dk"
BASE_PORT=8000

usage() {
    echo "Usage: $0 {scale|status|restart|deploy|logs} [args]"
    echo ""
    echo "  scale N        - Scale to N workers (enables/disables as needed, updates Caddy)"
    echo "  status         - Show status of all workers"
    echo "  restart [N]    - Restart worker N, or rolling-restart all if N omitted"
    echo "  deploy         - Pull code, install deps, rolling-restart all workers"
    echo "  logs N         - Tail logs for worker N"
    echo ""
    exit 1
}

scale() {
    local target=$1
    echo "Scaling ${APP_NAME} to ${target} workers..."

    for i in $(seq 1 "$target"); do
        id=$(printf "%03d" "$i")
        sudo systemctl enable "${APP_NAME}@${id}.service" 2>/dev/null
        sudo systemctl start "${APP_NAME}@${id}.service" 2>/dev/null || true
        echo "  + Worker ${id} (port $((BASE_PORT + i)))"
    done

    for i in $(seq $((target + 1)) 99); do
        id=$(printf "%03d" "$i")
        if systemctl is-enabled "${APP_NAME}@${id}.service" &>/dev/null; then
            sudo systemctl stop "${APP_NAME}@${id}.service"
            sudo systemctl disable "${APP_NAME}@${id}.service"
            echo "  - Worker ${id} stopped"
        fi
    done

    update_caddy "$target"
    echo "Done. ${target} workers running."
}

update_caddy() {
    local count=$1
    local upstreams=""

    for i in $(seq 1 "$count"); do
        upstreams+="localhost:$((BASE_PORT + i)) "
    done

    local tmpfile
    tmpfile=$(mktemp)

    cat > "$tmpfile" <<CADDYEOF
${DOMAIN} {
    encode zstd gzip
    header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload"

    handle /static/* {
        root * /home/prod/varro
        file_server
        header Cache-Control "public, max-age=2592000"
    }

    reverse_proxy ${upstreams}{
        lb_policy cookie ${APP_NAME}_sticky

        health_uri /health
        health_interval 10s
        health_timeout 3s
        health_status 200
    }
}
CADDYEOF

    echo "Updating Caddy config..."
    sudo cp "$tmpfile" "$CADDY_FILE"
    rm "$tmpfile"

    if sudo caddy validate --config "$CADDY_FILE" --adapter caddyfile; then
        sudo systemctl reload caddy
        echo "  Caddy reloaded."
    else
        echo "  WARNING: Caddy config invalid! Check ${CADDY_FILE}"
    fi
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
        echo "Rolling restart of all workers..."
        for unit in $(systemctl list-units "${APP_NAME}@*" --no-pager --no-legend | awk '{print $1}'); do
            echo "  Restarting ${unit}..."
            sudo systemctl restart "$unit"
            sleep 5
        done
        echo "Done."
    fi
}

deploy() {
    echo "Deploying..."
    cd /home/prod/varro
    git pull
    /home/prod/varro/.venv/bin/pip install -r requirements.txt --quiet
    sudo systemctl daemon-reload
    restart_workers
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
    deploy)  deploy ;;
    logs)    show_logs "${2:?'Specify worker number'}" ;;
    *)       usage ;;
esac
