# App + UI Architecture

## App bootstrap (`app/main.py`)

- Creates FastHTML app via `daisy_app(before=beforeware, live=True)`.
- `beforeware` now follows the auth-first pattern:
  - `auth = req.scope["auth"] = sess.get("auth")`
  - unauthenticated internal requests redirect to `/login` (303)
  - authenticated requests set `sess["user_id"] = auth`
  - chat state is initialized with `req.state.chats = crud.chat.for_user(auth)`
- Auth skip list combines:
  - static patterns,
  - `AUTH_SKIP` from `app/routes/auth.py`,
  - exact public root path `/`.
- Mounted routes:
  - dashboards via `mount_dashboard_routes(...)`,
  - chat routes (`app/routes/chat.py`),
  - command routes (`app/routes/commands.py`),
  - content routes (`app/routes/content.py`),
  - auth routes (`app/routes/auth.py`).
- Starts/stops `RunManager` and `ShellPool` cleanup tasks on startup/shutdown.

## Public vs authenticated routes

- Public frontpage:
  - `GET /` renders `ui/app/frontpage.py`.
  - Signed-in users hitting `/` are redirected to `/app` (303).
- Authenticated intro flow:
  - `GET /app` renders welcome markdown inside `AppShell`.
  - `GET /app/code` renders intro markdown editor inside `AppShell`.
  - `PUT /app/code` saves editor content with hash guard for optimistic conflict handling.
- Internal routes requiring auth include:
  - `/app`, `/app/code`, `/settings`, `/chat*`, `/dashboard*`, `/commands/search`.
- Legacy `/welcome/code` is no longer routed.

## Shell layout (`ui/app/layout.py`)

`AppShell(chat, content)` renders a split layout:

- left chat panel (`#chat-root`) with chat client script,
- center resize handle (Alpine pointer drag),
- right navbar + URL-driven content panel (`#content-panel`).

Content panel behavior:

- `hx_history_elt="true"` for history snapshots,
- `hx_boost="true"` so normal links become HTMX swaps,
- `hx_target="#content-panel"` and `hx_swap="innerHTML"`.

## Navigation updates

- Navbar tab fallbacks (`ui/app/navbar.py`):
  - dashboard fallback -> `/app`
  - code fallback -> `/app/code`
  - overview -> `/app`
- Command palette Home command now targets `/app`.
- `GET /chat` redirect target is `/app`.

## Markdown-first editing

- Welcome source remains file-backed at `DATA_DIR/user/{user_id}/welcome.md`.
- `{{dashboard_list}}` is replaced at render time with dashboard links.
- Intro page and editor use URL-first HTMX routing at:
  - `/app` for rendered content,
  - `/app/code` for editing + save.

## UI library shape

- `ui/core.py`: app headers (daisy/tailwind/plotly/alpine), class helpers.
- `ui/daisy.py`: low-level class wrappers.
- `ui/components/`: opinionated component API.
- `ui/app/`: app-level compositions (layout, chat, navbar, auth UI, frontpage).
- Theme tokens: `ui/theme.css` (`warmink`, `warmink-dark`).
