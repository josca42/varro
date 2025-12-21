# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

VARRO is a Danish Statistics AI analyst platform providing AI-powered access to Denmark's Statistics statbank (Danmarks Statistik). It combines a Chainlit web chat interface with a Pydantic-AI agent backend for querying, visualizing, and analyzing Danish statistical data.

## Commands

### Running the Application
```bash
# Start the chat UI (runs on port 8026)
chainlit run ui_chat/app.py --port 8026

# Create a new user
python scripts/setup_auth.py --email user@example.com --password secret
```

### Database Migrations
```bash
# Run migrations
alembic upgrade head

# Create new migration
alembic revision --autogenerate -m "description"
```

### Package Management
```bash
# Install dependencies (uses uv)
uv sync
```

## Architecture

### Core Components

**Agent Layer** (`varro/agent/`)
- `assistant.py`: Main Pydantic-AI agent using Claude Sonnet 4.5 with extended thinking (3000 token budget). Implements tools: `subject_overview`, `table_docs`, `view_column_values`, `sql_query`, `jupyter_notebook`, and web search.
- `memory.py`: `SessionStore` dataclass holding per-user state (DataFrames, figures, Jupyter kernel, cached prompts).
- `jupyter_kernel.py`: Stateful Jupyter kernel management with Parquet-based DataFrame transfer.

**Chat/UI Layer** (`ui_chat/`)
- `app.py`: Chainlit lifecycle hooks (`on_chat_start`, `on_message`, `on_chat_end`) and password auth callback.
- Configuration in `.chainlit/config.toml`.

**Message Streaming** (`varro/chat/message.py`)
- `MessageStreamHandler`: Finite-state machine transforming Pydantic-AI streaming nodes into Chainlit UI elements (thinking steps, tool calls, response messages).
- `PlaceholderParser`: Parses `<df>name</df>` and `<fig>name</fig>` placeholders to embed DataFrames and Plotly figures inline.

**Database Layer** (`varro/db/`)
- PostgreSQL connections to `neocortex` (fact/dim data) and `chainlit` (session storage).
- SQLModel-based User model with CRUD operations and bcrypt authentication.

**Data Context** (`varro/context/`)
- `tools.py`: Subject hierarchy navigation and table documentation retrieval.
- `subjects.py`: NetworkX graph of subject hierarchy from `subjects_graph_da.gml`.
- `fact_table.py`, `dim_table.py`: Metadata extraction for fact and dimension tables.

**Prompts** (`varro/prompts/`)
- Jinja2 templates, primarily `agent/rigsstatistiker.j2` defining the "Rigsstatistikeren" role.

### Database Schema

Two PostgreSQL databases:
- **neocortex**: `fact` schema (~2,000 tables with `indhold`, `tid`, dimension cols) and `dim` schema (~40 hierarchical dimension tables with `kode`, `niveau`, `titel`).
- **chainlit**: Session and message storage.

### Data Flow
```
User Message → Chainlit UI → Agent (Pydantic-AI) → Tools
    → SessionStore [DataFrames, Figures, Jupyter]
    → MessageStreamHandler → Chainlit UI
```

### Key Configuration

Environment variables (`.env`):
- `DATA_DIR`: Path to raw data files
- `DBUSER`, `DBPASS`: PostgreSQL credentials

Docs directory (`~/docs/`):
- `column_values/`: Parquet files with unique column values for fuzzy matching
- `subjects/`: Subject hierarchy README.md files
- `tables/`: Table documentation markdown files

## Code Style

- Only include essential comments
- Prefer simple and concise code
- Let code fail naturally (minimal try/except)

## Agent Folder

When creating scripts or notes:
- `agents/scripts/`: Custom scripts
- `agents/notes/`: General notes
- `agents/tasks/`: Task-specific notes (create subfolder per task)

## Skills

Available skills for data exploration:
- **Subjects**: Explore tables through the subjects hierarchy
- **Tables**: Preview tables with schema and sample rows
- **Sql**: Execute SQL queries against the PostgreSQL database

## Answer Style

Reference created markdown notes or Python scripts by providing file paths in final answers.

