# Chat + Agent Runtime

## SSE chat flow

Primary runtime:

- `app/routes/chat.py`
- `varro/chat/run_manager.py`
- `varro/chat/shell_pool.py`
- `varro/chat/agent_run.py`

Flow:

1. Browser submits `POST /chat/runs`.
2. Server validates/creates chat, reserves one active run per `(user_id, chat_id)`, and returns OOB fragments:
   - `ChatFormRunning`
   - `ChatProgressStart`
   - `ChatRunStream(run_id)`
3. HTMX SSE extension opens `GET /chat/runs/{run_id}/stream` from `#chat-run-stream`.
4. `_execute_run` leases shell from `ShellPool`, runs `run_agent(...)`, and streams HTML blocks incrementally.
5. Server emits `ChatProgressEnd` + `ChatFormEnabled` and then closes the stream with SSE `done` event.
6. `POST /chat/runs/{run_id}/cancel` cancels the task; chat remains (no rollback/delete edge-case handling).

## Run manager model

`RunRecord` is intentionally minimal:

- `run_id`
- `user_id`
- `chat_id`
- `task`
- `queue`

Behavior:

- one active run per `(user_id, chat_id)`
- queue carries pre-rendered HTML fragments
- stream emits only SSE events:
  - `message` with HTML fragment
  - `done` to close the connection
- terminal records are retained briefly and garbage-collected.

## Stream payload model

- No DOM-op translation layer.
- Blocks are streamed as HTML.
- Non-OOB blocks are wrapped with `hx-swap-oob="beforebegin:#chat-progress"`.
- OOB blocks (`ChatFormEnabled`, `ChatProgressEnd`, errors, etc.) are streamed as-is.

## Shell pool model

`ShellPool` is chat-scoped and simple:

- key: `(user_id, chat_id)`
- lease lifecycle: `lease(...)` and release
- idle eviction: 10 minutes (startup interval 60s)
- snapshot path:
  - `data/chats/{user_id}/{chat_id}/shell.pkl`

Snapshot behavior:

- on close/eviction, dump shell namespace with `dill` to `shell.pkl`
- when creating a missing in-memory shell, load `shell.pkl` if present
- `ping(user_id, chat_id)` also hydrates from disk when entry is missing

## Turn/runtime persistence

Turn files:

- `data/chats/{user_id}/{chat_id}/{idx}.mpk` (msgpack+zstd)
- `data/chats/{user_id}/{chat_id}/{idx}.cache.json` (fig/df render cache)

Runtime state:

- `data/chats/{user_id}/{chat_id}/runtime.json`
- schema: `{"bash_cwd": "/..."}`

## Agent orchestration (`varro/chat/agent_run.py`)

`run_agent(...)` keeps incremental reasoning/tool-call streaming:

- loads message history from persisted turn files
- emits blocks per completed pydantic-ai node
- persists new turn + render cache + DB `Turn`
- updates `Chat.updated_at`
- creates first-turn title asynchronously

## Client behavior

`ui/app/chat.py`:

- `#chat-run-stream` is the SSE connection node.
- `ChatClientScript()` is intentionally minimal:
  - keep `current_url` hidden input synchronized
  - refresh interactive widgets after swaps
- no custom EventSource reconnect/status/resync logic.

## SSE design learnings (from scratch)

- Keep run transport state as small as possible. `run_id + task + queue` is enough for start/stream/cancel; additional run state should only be added when a concrete need appears.
- Prefer streaming server-rendered HTML fragments over a custom DOM-op protocol when using HTMX OOB swaps. It removes client-side diff/apply code and keeps behavior easy to reason about.
- Use a queue boundary between producer (`_execute_run`) and consumer (SSE endpoint). This decouples agent speed from network speed and keeps cancellation straightforward.
- Normalize stream output in one place (`_stream_block`): plain blocks are wrapped with `beforebegin:#chat-progress`, OOB blocks pass through. A single rule avoids many UI edge cases.
- Keep an always-present SSE mount node (`#chat-run-stream`) in the panel so run-start can replace it OOB with a live stream connection.
- Lazy-import heavy runtime dependencies in request execution paths (e.g. `run_agent` inside `_execute_run`) to avoid import-time DB coupling in route modules and tests.
- Separate concerns strictly:
  - run manager owns run lifecycle and queues
  - shell pool owns shell lifecycle and persistence
  - routes own HTTP contract and chat CRUD wiring
