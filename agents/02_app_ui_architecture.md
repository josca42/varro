# App + UI Architecture

## App bootstrap (`app/main.py`)

- Creates FastHTML app via `daisy_app(exts="ws", before=beforeware, live=True)`.
- `beforeware` sets:
  - `sess["user_id"]` (demo fallback user id 1),
  - `req.state.chats = crud.chat.for_user(user_id)`.
- Mounts:
  - dashboard routes via `mount_dashboard_routes(...)`,
  - chat routes via `app.routes.chat`,
  - command palette search route via `app.routes.commands`.
  - dashboard routes are user-scoped (`DATA_DIR/user/{id}/dashboard`).
- Starts/stops idle websocket session cleanup on startup/shutdown.

## Shell layout (`ui/app/layout.py`)

`AppShell(chat, content)` renders a split layout:

- left: chat panel (`#chat-root`) with websocket extension,
- center: resize handle (Alpine pointer drag),
- right: navbar + URL-driven content panel (`#content-panel`).

Content panel behavior:

- `hx_history_elt="true"` for history snapshots,
- `hx_boost="true"` so normal links become HTMX swaps,
- `hx_target="#content-panel"` and `hx_swap="innerHTML"`.

## Main routes

- `/` -> dashboard overview content (full shell or fragment for HTMX)
- `/dashboard/{name}` -> dashboard (owned by `varro/dashboard/routes.py`)
- `/settings` -> placeholder settings page

## Chat routes (`app/routes/chat.py`)

- `/ws` websocket endpoint for chat messages.
- `/chat/new`, `/chat/switch/{id}` return OOB chat panel swaps.
- `/chat/history` returns dropdown list content.
- `/chat/delete/{id}` deletes DB rows and turn files.
- `/chat/heartbeat`, `/chat/close` maintain/close sid sessions.

## Command palette (`app/routes/commands.py` + `ui/app/command_palette.py`)

- Server side:
  - discovers dashboards from configured dashboard folder,
  - returns grouped filtered menu items for `/commands/search`.
- Client side:
  - `Cmd/Ctrl + K` open/close,
  - keyboard navigation,
  - HTMX navigation to target panels,
  - pushes history when swap is not `"none"`.

## UI library shape

- `ui/core.py`: app headers (daisy/tailwind/plotly/alpine), class helpers.
- `ui/daisy.py`: low-level class wrappers.
- `ui/components/`: opinionated component API.
- `ui/app/`: app-level compositions (layout, chat, navbar, auth UI).
- Theme tokens: `ui/theme.css` (`warmink`, `warmink-dark`).

## Auth modules

- Auth routes and UI exist (`app/routes/auth.py`, `ui/app/auth.py`).
- In current `app/main.py`, auth routes are not mounted.

## Markdown-first editing pattern (2026-02-09)

- Prefer file-backed pages for user-facing content:
  - welcome page source at `DATA_DIR/user/{user_id}/welcome.md`,
  - dashboard source at `DATA_DIR/user/{user_id}/dashboard/{slug}/dashboard.md`.
- Keep HTMX navigation URL-first:
  - `/dashboard/{slug}` for rendered dashboard,
  - `/dashboard/{slug}/code` for source editing,
  - `/` (or `/welcome`) for rendered welcome page,
  - `/welcome/code` for editing welcome markdown.
- Follow HTMX click-to-edit flow:
  - view fragment with `hx-get` to load editor fragment,
  - editor form with `hx-put` to save and swap back rendered fragment,
  - optional autosave with `hx-trigger="keyup changed delay:1000ms"` and `hx-sync="closest form:replace"` to avoid save races.

### Implemented in app (2026-02-09)

- `/` now renders markdown from `DATA_DIR/user/{id}/welcome.md` (auto-created if missing).
- `{{dashboard_list}}` placeholder in `welcome.md` is replaced at render time with markdown links to available dashboards.
- `/welcome/code` provides textarea editor with `PUT` save and file-hash conflict guard.
- Welcome code editor UI is minimal: raw textarea + `Save` + `View welcome page`.
- Navbar tabs now perform URL-based HTMX navigation:
  - `Code` routes to `/welcome/code` or `/dashboard/{slug}/code` based on current URL.
- Dashboard code mode includes file tabs (`dashboard.md`, `outputs.py`, `queries/*.sql`) and edits the selected file in a textarea.
