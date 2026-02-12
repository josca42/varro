# Chat SSE Migration Implementation Notes

Date: 2026-02-12

## 1. Context and intent

This document captures the implementation details for migrating chat transport from WebSocket (`/ws`) to HTTP + Server-Sent Events (SSE), while decoupling shell lifecycle from transport/session lifecycle.

Primary goals:

- Replace websocket-bound run lifecycle with explicit run resources.
- Preserve existing chat rendering behavior and turn persistence.
- Keep cancellation semantics (including rollback of newly-created first chats).
- Improve reconnect robustness with server-side replay buffer and client catch-up.
- Move shell lifecycle to chat scope (`user_id`, `chat_id`) with idle eviction and snapshot restore.

## 2. Transport architecture (HTTP + SSE)

### 2.1 New endpoints

Implemented in `app/routes/chat.py`:

- `POST /chat/runs`
  - Starts a new run.
  - Creates chat if `chat_id` missing.
  - Enforces one active run per `(user_id, chat_id)` via `RunManager`.
  - Returns 202 with OOB HTML:
    - `ChatFormRunning`
    - `ChatProgressStart`
  - Sends `HX-Trigger` with event payload:
    - `chatRunStarted: { run_id, chat_id }`

- `GET /chat/runs/{run_id}/stream?since=<event_id>`
  - Returns `text/event-stream` via `EventStream(...)`.
  - Replays buffered events newer than `since` then tails live events.

- `POST /chat/runs/{run_id}/cancel`
  - Cancels active run task if run is still `running`.
  - Returns 204.
  - No-op for terminal runs.

- `GET /chat/runs/{run_id}/status`
  - Returns JSON `{ state, chat_id, terminal }`.
  - Used by client reconnect/resync fallback.

### 2.2 Removed websocket/session routes

Removed from runtime behavior:

- `/ws`
- `/chat/heartbeat`
- `/chat/close`
- `/chat/cancel` (old `sid`-based cancel)

## 3. Run orchestration (`RunManager`)

Implemented in `varro/chat/run_manager.py`.

### 3.1 Core responsibilities

- Own in-memory run records.
- Enforce one active run per `(user_id, chat_id)`.
- Buffer events for replay on reconnect.
- Manage status transitions.
- Provide SSE stream iterators scoped by user ownership.
- Garbage-collect terminal run records.

### 3.2 Record model

`RunRecord` fields include:

- Identity: `run_id`, `user_id`, `chat_id`
- Rollback context: `previous_chat_id`, `created_chat`
- Lifecycle: `state`, `task`, `created_at`, `finished_at`, `result_chat_id`
- Eventing: `events`, `next_event_id`, `subscriber_queues`
- Replay safety: `resync_required`, `truncated_before_event_id`, `buffered_bytes`

### 3.3 Event model

SSE events emitted:

- `dom`: `{ event_id, ops: [...] }`
- `status`: `{ event_id, state }`
- `ping`: `{ event_id }` keepalive while idle

Run state values:

- `running`, `completed`, `cancelled`, `failed`
- plus stream/status compatibility state `resync_required`

### 3.4 Buffer cap and resync

- Event buffer is capped (`16MB` configured in manager ctor).
- On cap overflow:
  - record marked `resync_required`
  - buffered replay log is truncated
  - client receives/observes `resync_required`
- Client then polls `/status` until terminal and refreshes panel from persisted state.

### 3.5 Retention

- Terminal runs retained for 5 minutes (startup-configured in `app/main.py`).
- Periodic GC removes expired run records.

## 4. Shell lifecycle (`ShellPool`)

Implemented in `varro/chat/shell_pool.py`.

### 4.1 Why

Previously, shell state lived inside websocket-tab sessions (`sid` scope). That coupled shell continuity to transport lifetimes and reconnect behavior.

Now shell state is scoped to chat identity and leased per run:

- Key: `(user_id, chat_id)`
- Stable across transport reconnects

### 4.2 Lease model

- `lease(user_id, chat_id, chats)` is an async context manager.
- Increments `in_use_count` on acquire.
- Ensures shell is loaded (snapshot restore + replay fallback) once.
- Decrements `in_use_count` on release.

### 4.3 Idle eviction and cleanup

- Idle TTL: 10 minutes
- Cleanup interval: 60s
- Evict only when `in_use_count == 0`

On eviction:

1. Snapshot shell namespace to disk.
2. Dispose shell/reset history session.
3. Remove entry from in-memory pool.

### 4.4 Snapshot format and paths

Paths:

- `data/chats/{user_id}/{chat_id}/shell.pkl`
- `data/chats/{user_id}/{chat_id}/shell.meta.json`

Meta fields:

- `schema_version`
- `saved_at`
- `turn_count`
- `python_version`

Behavior:

- Snapshot excludes baseline startup keys and private (`_`) keys.
- Max snapshot size: 512MB.
- If too large or invalid -> snapshot skipped/fallback to replay.

### 4.5 Replay fallback

If snapshot is missing/invalid/stale:

- Reset shell and replay persisted tool calls via `restore_shell_namespace(...)`.
- Replay source is persisted turn messages (`turn_store`).

### 4.6 Chat deletion integration

`chat_delete` now removes shell artifacts and evicts live pooled shell entry via `ShellPool.remove_chat(...)`.

## 5. Agent runtime refactor

Updated in `varro/chat/agent_run.py`.

### 5.1 Signature decoupling

`run_agent(...)` no longer receives `UserSession`. It now takes explicit runtime context:

- `user_id`
- `chats`
- `shell`
- `chat_id`
- `current_url`
- `touch_shell`

This removes transport/session coupling from agent execution.

### 5.2 Persistence behavior retained

Existing behavior preserved:

- Load full message history from persisted turn files.
- Stream blocks as nodes complete.
- Save new turn message pack and render cache.
- Insert `Turn` row and update `Chat.updated_at`.
- Async first-turn title generation still runs.

## 6. Assistant deps/tool updates

Updated in `varro/agent/assistant.py`.

### 6.1 Deps

`AssistantRunDeps` gained:

- `touch_shell: Callable[[], None]`

### 6.2 Tool touch points

On successful execution:

- `Sql` calls `ctx.deps.touch_shell()`
- `Jupyter` calls `ctx.deps.touch_shell()`

This keeps shell activity timestamps accurate for eviction policy.

## 7. DOM operation stream mapping

Implemented in `varro/chat/stream_ops.py`.

### 7.1 Mapping rules

- Parse `hx-swap-oob` and translate to deterministic ops:
  - `outerHTML:#id` -> `replace` op
  - `beforebegin:#chat-progress` -> `insert` op
- Missing OOB swap defaults to insert-before-progress.
- HTML is normalized by removing `hx-swap-oob` attributes before sending to client.

### 7.2 Why ops instead of raw HTML stream

Using op payloads keeps client application deterministic and supports replay/catch-up without relying on extension-specific swap behavior.

## 8. Route-level run execution flow

Main run coroutine in `app/routes/chat.py` (`_execute_run(...)`):

1. Lease shell from `ShellPool`.
2. Run agent and convert each block to DOM ops.
3. Publish ops through `RunManager`.
4. On success:
   - sync turn count to shell pool
   - publish progress end + enabled form
   - set run status `completed`
5. On `CancelledError`:
   - execute rollback logic
   - set status `cancelled`
6. On exception:
   - invalidate shell entry
   - publish error block + progress end + enabled form
   - set status `failed`

## 9. Cancel rollback semantics (preserved)

In `app/routes/chat.py`:

- Existing chat run cancel:
  - keep current chat
  - publish `ChatProgressEnd` + `ChatFormEnabled(chat_id)`

- New chat first-turn cancel (`created_chat=True`):
  - delete created chat and artifacts
  - restore previous chat id (or clear selection)
  - publish full `ChatPanel(...)` rollback OOB
  - publish `ChatProgressEnd` + `ChatFormEnabled(restored_chat_id)`

## 10. Frontend migration (`ui/app/chat.py`)

### 10.1 Form changes

`ChatForm` changes:

- submit path changed from websocket send to:
  - `hx_post="/chat/runs"`
  - `hx_swap="none"`
- removed hidden `sid`
- stop button now posts run-specific endpoint:
  - `/chat/runs/{run_id}/cancel`

### 10.2 Client script responsibilities

`ChatClientScript()` now:

- has single-init global guard: `window.__varroChatClientInitialized`
- listens for `chatRunStarted` (HTMX trigger event)
- opens `EventSource` for run stream
- tracks `lastEventId`
- applies `dom` ops (`insert`/`replace`) deterministically
- executes inserted `<script>` nodes and re-processes HTMX on inserted fragments
- reconnects with exponential backoff and `since=lastEventId`
- on persistent stream issues:
  - checks `/status`
  - if `resync_required`, polls status until terminal
  - refreshes chat panel from persisted route (`/chat/switch/{id}` or `/chat/new`)

### 10.3 URL propagation retained

`current_url` hidden input is still maintained on swap/popstate/submit so tools depending on request URL continue to work.

## 11. App bootstrap changes (`app/main.py`)

- Removed websocket extension load (`exts="ws"`).
- Startup hooks now start:
  - `run_manager` cleanup loop
  - `shell_pool` cleanup loop
- Shutdown hooks stop both loops.

## 12. Removed legacy module

Deleted `varro/chat/session.py` and all code paths relying on:

- `SessionManager`
- `UserSession`
- `sid`-scoped shell/run ownership

## 13. Dependencies

Added dependency:

- `dill>=0.4.0`

Updated:

- `pyproject.toml`
- `uv.lock`

`ShellPool` currently attempts `dill` first and falls back to `pickle` if import is unavailable.

## 14. Tests

### 14.1 Removed obsolete tests

- `tests/chat/test_session_active_run.py` deleted (websocket session model obsolete).

### 14.2 Added tests

- `tests/chat/test_run_manager.py`
  - run lock behavior
  - replay semantics with `since`
  - `resync_required` status behavior

- `tests/chat/test_shell_pool.py`
  - replay-once behavior for loaded chats
  - snapshot roundtrip on eviction

### 14.3 Updated tests

- `tests/chat/test_chat_cancel_flow.py`
  - stream op mapping checks
  - form endpoint contract checks
  - cancel semantics for created chat rollback
  - missing run and terminal-run cancel behavior

### 14.4 Verification status

- `uv run pytest tests/chat -q` passed (26 tests).
- Full suite currently has one unrelated failure in dashboard parser tests due missing fixture path:
  - `tests/dashboard/test_parser_loader.py::test_parse_example_dashboard_builds_expected_structure`
  - missing `example_dashboard_folder/sales/dashboard.md` in current workspace state.

## 15. Docs and agent notes updated

Updated to reflect SSE + shell-pool architecture:

- `docs/varro/chat_app.md`
- `docs/varro/app_structure.md`
- `agents/03_chat_agent_runtime.md`
- `agents/02_app_ui_architecture.md`
- `agents/01_project_map.md`
- `agents/index.md`
- `app/AGENTS.md`
- `app/CLAUDE.md`

## 16. Known caveats / follow-up ideas

- Run state is in-memory only (not recoverable across process restart).
- Cross-tab synchronization is intentionally limited; lock scope is per `(user_id, chat_id)` run start.
- Resync fallback currently refreshes from persisted routes when replay buffer is no longer sufficient.
- Snapshot serialization safety/trust model is internal-only; no external upload path is exposed.

## 17. File-level implementation index

Core runtime:

- `app/routes/chat.py`
- `varro/chat/run_manager.py`
- `varro/chat/shell_pool.py`
- `varro/chat/stream_ops.py`
- `varro/chat/agent_run.py`
- `varro/agent/assistant.py`

UI/bootstrap:

- `ui/app/chat.py`
- `ui/app/layout.py`
- `app/main.py`

Tests:

- `tests/chat/test_run_manager.py`
- `tests/chat/test_shell_pool.py`
- `tests/chat/test_chat_cancel_flow.py`

Removed:

- `varro/chat/session.py`
- `tests/chat/test_session_active_run.py`
