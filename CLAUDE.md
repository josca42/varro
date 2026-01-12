## Backend

Chainlit chat UI + Pydantic-AI agent for Danish Statistics data analysis.

## Commands

```bash
chainlit run ui_chat/app.py --port 8026   # Start chat UI
python scripts/setup_auth.py --email x --password y  # Create user
alembic upgrade head   # Run migrations
uv sync               # Install dependencies
```

## Architecture

```
ui_chat/
  app.py              # Chainlit lifecycle (on_chat_start, on_message, on_chat_end)
  public/dashboard.js # Detects <!--DASHBOARD_PORT:xxx--> and posts to parent iframe

varro/
  agent/
    assistant.py      # Pydantic-AI agent (Claude Sonnet 4.5 + extended thinking)
    memory.py         # SessionStore (user state, IPython shell, Evidence manager)
    ipython_shell.py  # IPython wrapper with timeout

  chat/
    message.py        # MessageStreamHandler (streaming to Chainlit UI)

  context/
    tools.py          # subject_overview, table_docs tools

  db/
    models/user.py    # User model
    crud/             # CRUD operations

  evidence/
    manager.py        # EvidenceManager (dashboard lifecycle, dev server)

  prompts/
    agent/rigsstatistiker.j2  # System prompt
```

## Agent Tools

| Tool | Purpose |
|------|---------|
| `memory` | File-based persistent storage (also Evidence pages) |
| `subject_overview` | Get tables in a subject |
| `table_docs` | Get table schema/docs |
| `view_column_values` | Inspect column values with fuzzy match |
| `sql_query` | Execute SQL, optionally store result |
| `jupyter_notebook` | Stateful Python environment |
| `create_dashboard` | Start Evidence dashboard server |

## Evidence Dashboard Flow

1. AI calls `create_dashboard(name)` → starts Evidence dev server on dynamic port
2. Port sent via `<!--DASHBOARD_PORT:xxx-->` marker → custom JS posts to parent
3. AI uses `memory` tool to write `/memories/d/dashboard/pages/index.md`
4. Evidence HMR updates dashboard automatically
5. On chat end, `SessionStore.cleanup()` stops Evidence server

## Database

- **neocortex**: `fact.*` and `dim.*` schemas (statistics data)
- **chainlit**: Session/message storage

## Config

- `.env`: `DATA_DIR`, `DBUSER`, `DBPASS`
- `~/docs/`: `column_values/`, `subjects/`, `tables/`
