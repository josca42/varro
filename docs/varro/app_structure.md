# Varro App Structure

## Overview

The app is a unified FastHTML + HTMX application with a split-panel layout:
- **Left panel:** Chat (session + WebSocket, independent of URL)
- **Right panel:** URL-driven content (dashboards, overview, settings)

The URL is the source of truth for the content panel. Chat state is never derived from the URL.

## High-Level Layout

```
app/
  main.py                # App entrypoint + unified shell routes
  routes/
    chat.py              # WebSocket + OOB chat operations

ui/
  app/
    layout.py            # AppShell, ContentNavbar, Welcome/Overview/Settings
    chat.py              # ChatPanel + chat UI components
  components/            # Reusable UI primitives

varro/
  dashboard/             # Markdown dashboard framework
  chat/                  # Session + agent runtime
  db/                    # SQLModel models + CRUD
```

## Entry Point (app/main.py)

`app/main.py` is the single entrypoint:
- Creates the FastHTML app with `daisy_app(exts="ws", before=beforeware)`
- Injects `user_id` and `req.state.chats` via beforeware
- Mounts dashboard routes (`mount_dashboard_routes`)
- Mounts chat routes (`app.routes.chat`)
- Starts/stops chat session cleanup on startup/shutdown

Routes:
- `/` → Welcome content
- `/dash/{name}` → Dashboard content (dual-mode)
- `/dash/overview` → Overview placeholder
- `/settings` → Settings placeholder

## Unified Shell (ui/app/layout.py)

`AppShell` renders:
- Top navbar (Lovable-style mock)
- Split panel:
  - **Chat panel:** `ChatPanel` + `ChatClientScript`
  - **Resize handle:** Alpine-driven drag handle
  - **Content panel:** `#content-panel`

Key HTMX behavior:
- `#content-panel` uses `hx-history-elt="true"` so history restores only the content panel
- `hx-boost="true"` on the content panel allows standard links to use HTMX swaps
- Content fragments include their own `ContentNavbar` header

## Chat System

Chat is embedded in the left panel and does not own a page route.

Routes in `app/routes/chat.py`:
- `/ws` → WebSocket for chat streaming
- `/chat/new` → OOB swap for `#chat-panel` (new chat)
- `/chat/switch/{id}` → OOB swap for `#chat-panel` (switch chat)
- `/chat/history` → Dropdown list (HTMX)
- `/chat/delete/{id}` → Deletes chat
- `/chat` → Redirects to `/`

Client wiring:
- `ChatClientScript` sets a per-tab `sid` in `sessionStorage`
- Script attaches `ws-connect="/ws?sid=..."` to `#chat-root`
- Hidden form input `sid` is synced for WebSocket messages

## Dashboard System

Dashboards are loaded from `example_dashboard_folder/` in this repo. Each dashboard folder contains:
- `queries/` (SQL files)
- `outputs.py` (@output functions)
- `dashboard.md` (layout)

Dashboard route behavior (`varro/dashboard/routes.py`):
- `/dash/{name}` renders **full AppShell** for normal requests
- `/dash/{name}` returns **content fragment** for HTMX requests
- Filters update URL via `HX-Replace-Url` and trigger `filtersChanged`
- Placeholders re-load with `hx-trigger="load, filtersChanged from:body"`

## URL State

The URL is the state for the content panel:
- `/dash/{name}?region=east&period_from=2025-01-01`
- Filter changes update the URL without creating history entries
- Chat is independent and never changes via URL

## Key Files

- `app/main.py` — app entrypoint, unified routing
- `ui/app/layout.py` — AppShell + ContentNavbar
- `ui/app/chat.py` — ChatPanel + chat UI + client script
- `app/routes/chat.py` — WebSocket + OOB chat routes
- `varro/dashboard/routes.py` — dashboard routes + dual-mode responses
- `varro/dashboard/components.py` — dashboard rendering + HTMX placeholders
