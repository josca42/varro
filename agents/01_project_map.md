# Project Map

Snapshot date: 2026-02-07.

## Goal

Build an AI state statistician for Denmark that can:

- understand DST table metadata and subject hierarchy,
- query and analyze data in Postgres,
- present results in chat and persistent dashboards.

## Main parts

- `ui/`: shared FastHTML + DaisyUI component library.
- `app/`: web app shell, routes, SSE chat run wiring.
- `varro/`: domain/runtime library:
  - `agent/`: pydantic-ai agent and tool implementations.
  - `chat/`: run manager, shell pool, and turn persistence/runtime.
  - `dashboard/`: markdown dashboard framework.
  - `context/`: docs generation and lookup helpers.
  - `data/`: ingestion and DB loading scripts.
  - `db/`: SQLModel models + CRUD.
  - `prompts/`: Jinja prompts for agent and data-cleaning tasks.

## Runtime stack

- Python 3.12
- FastHTML + HTMX + Alpine.js
- DaisyUI + Tailwind browser runtime
- SQLModel / SQLAlchemy
- Postgres
- pandas + plotly + matplotlib
- pydantic-ai (Anthropic model backend)

## Entry points

- Unified app shell: `app/main.py`
- Chat-only entrypoint: `app/main_chat.py`
- Demo user dashboard content: `mnt/user/1/dashboard/sales/`

## Key docs read

- `docs/varro/app_structure.md`
- `docs/varro/chat_app.md`
- `docs/varro/dashboard_spec.md`
- `docs/varro/highlevel_thoughts.md`

## Testing footprint

- Dashboard tests in `tests/dashboard/`:
  - parser/loader
  - executor
  - routes

## Fast orientation commands

- Run app: `uv run python app/main.py`
- Run dashboard tests: `uv run pytest tests/dashboard`
- Inspect dashboard example: `example_dashboard_folder/sales/`
