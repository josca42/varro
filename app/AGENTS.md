# Web Application

The unified FastHTML web app that renders the split-panel shell and mounts chat + dashboards.

## Structure

```
app/
├── main.py          # App entrypoint, beforeware, unified shell routes
└── routes/
    ├── chat.py      # WebSocket + OOB chat routes
    ├── auth.py      # Authentication routes (optional)
    └── index.py     # Auth landing routes (optional)
```

## Key Patterns

### Unified Shell
- `AppShell` renders the split layout (chat left, content right).
- Content routes are dual-mode:
  - Normal request → full AppShell.
  - HTMX request → content fragment only.
- The content panel uses `hx-history-elt` so back/forward only swaps the right panel.

### Chat Isolation
- Chat state is session + WebSocket only.
- `/chat/new` and `/chat/switch/{id}` return OOB swaps targeting `#chat-panel`.
- The URL never determines chat state.

### Dashboard Mount
- Dashboards are mounted via `mount_dashboard_routes` in `app/main.py`.
- `/dash/{name}` renders dashboard content; URL params drive filters.

## Usage

Always import UI components from the `ui` library. If a new component is needed, add it to `ui/components/` first (or `ui/app/` for app-specific compositions).
