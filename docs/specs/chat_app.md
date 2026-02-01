# Chat App Architecture

A WebSocket-based chat application using FastHTML, HTMX, and Pydantic-AI.

## Overview

```
WebSocket Connection
        │
        ▼
┌───────────────────┐
│  SessionManager   │  In-memory sessions (one per user)
│  sessions.get()   │
│  sessions.create()│
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│   UserSession     │  Shell, message history, turn management
│   - shell         │
│   - msgs          │
│   - turn_idx      │
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│   run_agent()     │  Iterates pydantic-ai nodes, yields HTML
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│   Persistence     │  Chat/Turn models, msgpack+zstd files
└───────────────────┘
```

## Key Files

| File | Purpose |
|------|---------|
| `app/main_chat.py` | App entry, beforeware setup |
| `app/routes/chat.py` | WebSocket handlers, HTTP routes |
| `varro/chat/session.py` | UserSession, SessionManager |
| `varro/chat/agent_run.py` | Agent iteration, node→HTML conversion |
| `varro/db/models/chat.py` | Chat, Turn SQLModel definitions |
| `varro/db/crud/chat.py` | CrudChat, CrudTurn |
| `ui/app/chat.py` | UI components for rendering |
| `varro/dashboard/parser.py` | Shared markdown parser for chat/dashboard tags |

## Data Model

```
Chat (1) ──────< Turn (N)
  │                │
  │                ├─ user_text: str
  │                ├─ obj_fp: str (path to msgpack file)
  │                └─ idx: int (turn index)
  │
  └─ user_id, title, created_at, updated_at
```

**Turn storage**: Each turn saves pydantic-ai `ModelMessage` objects as msgpack+zstd at `data/chats/{user_id}/{chat_id}/{idx}.mpk`

## WebSocket Flow

1. **Connect** (`on_conn`): Creates `UserSession`, restores chat if `chat_id` in session
2. **Message** (`on_message`):
   - Creates chat if needed
   - Handles edit via `edit_idx` (deletes subsequent turns)
   - Disables input, shows progress animation
   - Runs agent, streams HTML blocks
   - Stops animation and re-enables input
3. **Disconnect** (`on_disconn`): Cleans up session and shell

## Session Lifecycle

```python
session = sessions.create(user, chats, send)  # On connect
await session.start_chat(chat_id)              # Load/restore chat
session.save_turn(new_msgs, user_text)         # After agent completes
session.delete_from_idx(idx)                   # On message edit
session.cleanup()                              # On disconnect
```

## Agent→HTML Mapping

Each pydantic-ai node maps to a UI component:

| Node Type | UI Component | Renders |
|-----------|--------------|---------|
| `UserPromptNode` | `UserPromptBlock` | User message bubble |
| `ModelRequestNode` | `ReasoningBlock` (OOB update) | Tool return results merged into reasoning |
| `CallToolsNode` | `ReasoningBlock` + `CallToolsBlock` (final) | Thinking, text, tool calls |
| `EndNode` | (optional) `ReasoningBlock` | Flushes any pending reasoning |

### Reasoning / Tool Calls UI

- Tool calls that belong to the reasoning process are grouped into a single **Reasoning** box.
- The reasoning box contains interleaved **Thinking**, **Text**, and **ToolCall** steps.
- Tool return outputs are merged into the matching tool call by `tool_call_id`.
- The reasoning box updates in-place via `hx-swap-oob="outerHTML:#reasoning-{turn}"`.
- The final answer is rendered separately (finish_reason = "stop").

### Progress Indicator

- A small Game of Life logo sits **last** in `#chat-messages`.
- On message start, `ChatProgressStart()` swaps the logo to animated (`data-run=1`).
- On completion, `ChatProgressEnd()` swaps it to the final static form (`data-run=0`).
- After any HTMX swap, `window.__golRefresh()` re-initializes the canvas.

## Markdown Rendering

- Chat markdown is parsed server-side using `parse_dashboard_md()` and then rendered with `mistletoe`.
- Self-closing tags are supported in text blocks:
  - `<fig name="figure_id" />` → Plotly figure from `session.shell.user_ns`
  - `<df name="df_id" />` → DataFrame table from `session.shell.user_ns`
- Everything else is normal markdown and rendered inside a `.prose` container.

## Key Patterns

**One node = one WebSocket send**: Agent nodes are awaited to completion before rendering (not streaming partial events).

**OOB swaps**:
- Reasoning updates use `outerHTML:#reasoning-{turn}` to keep one box.
- The progress logo uses `outerHTML:#chat-progress`.
- Non-OOB blocks are inserted **before** `#chat-progress` to keep the logo last.

**Form state**: `ChatFormDisabled()`/`ChatFormEnabled()` toggle input during processing.

## Edit Message Flow

1. Frontend sends `{msg, chat_id, edit_idx}`
2. `session.delete_from_idx(edit_idx)` removes turns ≥ idx from DB and disk
3. Reloads remaining messages into `session.msgs`
4. Normal message flow continues from that point
