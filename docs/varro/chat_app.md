# Chat App Architecture

A WebSocket-based chat runtime embedded in the unified app shell. Built with FastHTML, HTMX, and Pydantic-AI.

## Overview

```
WebSocket Connection
        |
        v
+-------------------+
|  SessionManager   |  In-memory transport sessions (tab scoped)
|  sessions.get()   |
|  sessions.create()|
+--------+----------+
         |
         v
+-------------------+
|   UserSession     |  Shell + websocket identity only
|   - shell         |
|   - shell_chat_id |
+--------+----------+
         |
         v
+-------------------+
|   run_agent()     |  Rebuilds message history from disk each run,
|                   |  streams incremental blocks for the new turn
+--------+----------+
         |
         v
+-------------------+
|   Persistence     |  Chat/Turn rows + turn msgpack files + runtime.json
+-------------------+
```

## Key Files

| File | Purpose |
|------|---------|
| `app/main.py` | Unified app entrypoint + beforeware |
| `app/routes/chat.py` | WebSocket handlers, OOB chat routes |
| `ui/app/layout.py` | AppShell layout (chat panel lives here) |
| `ui/app/chat.py` | ChatPanel + chat UI components |
| `varro/chat/session.py` | `UserSession`, `SessionManager` |
| `varro/chat/agent_run.py` | Agent iteration, node->HTML conversion, turn persistence |
| `varro/chat/turn_store.py` | Turn file pathing + msgpack/zstd save/load |
| `varro/chat/render_cache.py` | Cache HTML for `<fig />` / `<df />` placeholders |
| `varro/chat/shell_replay.py` | Replay `Sql`/`Jupyter` tool calls when switching chats |
| `varro/chat/runtime_state.py` | Per-chat runtime state (`bash_cwd`) |
| `varro/db/models/chat.py` | Chat, Turn SQLModel definitions |
| `varro/db/crud/chat.py` | CrudChat, CrudTurn |
| `varro/dashboard/parser.py` | Shared markdown parser for chat/dashboard tags |

## Data Model

```
Chat (1) ------< Turn (N)
  |                |
  |                +- user_text: str
  |                +- obj_fp: str (path to msgpack file)
  |                +- idx: int (turn index)
  |
  +- user_id, title, created_at, updated_at
```

Turn files:
- `data/chats/{user_id}/{chat_id}/{idx}.mpk` (pydantic-ai `ModelMessage` list, msgpack+zstd)
- `data/chats/{user_id}/{chat_id}/{idx}.cache.json` (rendered fig/df HTML cache)
- `data/chats/{user_id}/{chat_id}/runtime.json` (`{"bash_cwd": "/..."}`)

## WebSocket Flow

1. Connect (`on_conn`): creates `UserSession` for `{user_id, sid}`.
2. Message (`on_message`):
   - creates chat if needed,
   - disables chat form and starts progress animation,
   - calls `run_agent(...)`.
3. `run_agent(...)`:
   - loads full history from Turn files,
   - computes `turn_idx` from persisted turns,
   - ensures shell for target chat (replay on chat switch),
   - streams only blocks from the new run,
   - saves new turn + render cache + DB row.
4. Disconnect (`on_disconn`): cleanup session shell + websocket.

## Session Lifecycle

```python
session = sessions.create(user_id, sid, chats, send, ws)
await session.ensure_shell_for_chat(chat_id, message_history)
session.cleanup()
```

`UserSession` intentionally does not track chat history, `turn_idx`, URL state, or bash cwd.

## History Rendering Behavior

- `/chat/switch/{chat_id}` returns full `ChatPanel(...)` with all persisted turns.
- WebSocket `on_message` appends streamed blocks for the active turn only.

## URL Model

- Client writes `current_url` hidden input from `window.location.pathname + window.location.search`.
- Hidden values are refreshed on initial load, HTMX swaps, popstate, and immediately before submit.
- Server treats `current_url` as request-scoped input only.
- Assistant tools access URL via `ctx.deps.request_current_url()`.

## Bash Runtime State

- `Bash` tool loads cwd from `runtime.json` at start of each call.
- `Bash` tool saves cwd back to `runtime.json` after command execution.
- This is chat-scoped and allows server restart continuity.
- Concurrent bash tool calls use last-writer-wins behavior.

## Agent->HTML Mapping

Each completed pydantic-ai node maps to a UI block:

| Node Type | UI Component | Renders |
|-----------|--------------|---------|
| `UserPromptNode` | `UserPromptBlock` | User message bubble |
| `ModelRequestNode` | `ReasoningBlock` (OOB update) | Tool return results merged into reasoning |
| `CallToolsNode` | `ReasoningBlock` + `CallToolsBlock` (final) | Thinking, text, tool calls |
| `EndNode` | (optional) `ReasoningBlock` | Flushes pending reasoning |

## Progress Indicator

- A small Game of Life logo is always last in `#chat-messages`.
- On message start, `ChatProgressStart()` swaps it to animated (`data-run=1`).
- On completion, `ChatProgressEnd()` swaps it to static (`data-run=0`).
- `window.__golRefresh()` runs after swaps.

## Markdown Rendering

- Chat markdown is parsed server-side via `parse_dashboard_md()` and rendered with `mistletoe`.
- Supported placeholders:
  - `<fig name="figure_id" />` -> Plotly figure from shell namespace or cache.
  - `<df name="df_id" />` -> DataFrame table from shell namespace or cache.
