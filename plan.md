# Full SSE Chat Migration with Chat-Scoped Shell Pool

## Summary
Migrate chat transport from WebSocket to HTTP + SSE while decoupling shell lifecycle from transport state.  
This removes the current same-`sid` reconnect cancellation failure mode, keeps run streaming robust with reconnect catch-up, and enforces memory control with 10-minute idle shell eviction plus dill snapshot restore and replay fallback.

This is a good architecture for your current workload (server-streamed assistant output with occasional client actions), but it is not universally “better” than WebSockets. It is better here because it removes fragile connection/session coupling and keeps the chat runtime easier to reason about.

## Scope
1. Replace `/ws` chat transport with `POST start run` + `GET SSE stream` + `POST cancel`.
2. Remove transport-scoped `UserSession` ownership of shell state.
3. Introduce chat-scoped shell manager keyed by `(user_id, chat_id)` with TTL eviction and snapshot restore.
4. Keep existing chat rendering components and persisted turn format.
5. Remove WebSocket-only lifecycle routes and cleanup logic.
6. Update docs and agent notes after implementation.

## Out of Scope
1. Persisting active runs across server restart.
2. Cross-browser-tab synchronization beyond per-chat run lock.
3. Redesigning assistant tool UI semantics.

## Public API / Interface Changes

### HTTP endpoints
1. `POST /chat/runs`
Request fields: `msg`, `chat_id` (optional), `current_url` (optional).  
Response: `202` with OOB HTML for `ChatFormRunning` + `ChatProgressStart` and header trigger `chatRunStarted` containing `{ run_id, chat_id }`.  
Behavior: Enforces one active run per `(user_id, chat_id)`. Creates new chat when `chat_id` is missing.

2. `GET /chat/runs/{run_id}/stream?since=<event_id>`
Response: `text/event-stream`.  
Behavior: Replays buffered events with `event_id > since`, then tails live events until terminal state.

3. `POST /chat/runs/{run_id}/cancel`
Response: `204`.  
Behavior: Cancels active run task, publishes rollback/final UI events, and restores previous chat context when cancelling first turn of a newly-created chat.

4. `GET /chat/runs/{run_id}/status`
Response: JSON `{ state, chat_id, terminal }`.  
Behavior: Used by client reconnect fallback when stream errors persist.

### Removed endpoints
1. `/ws` in `/Users/josca/dev/varro/app/routes/chat.py`.
2. `/chat/heartbeat` and `/chat/close` (no longer needed after removing transport session tracking).

### UI contract changes
1. Chat form in `/Users/josca/dev/varro/ui/app/chat.py` changes from `ws_send=True` to `hx_post="/chat/runs"` with `hx_swap="none"`.
2. Stop button posts to `/chat/runs/{run_id}/cancel`.
3. `sid` hidden input and sessionStorage `sid` generation are removed.
4. `ChatClientScript` becomes an SSE run-stream manager and remains idempotent (single global init guard).

### Runtime type/interface changes
1. Replace transport session manager in `/Users/josca/dev/varro/varro/chat/session.py` with:
`RunManager` and `ShellPool` modules.
2. Update `AssistantRunDeps` in `/Users/josca/dev/varro/varro/agent/assistant.py`:
add `touch_shell: Callable[[], None]`.
3. Refactor `/Users/josca/dev/varro/varro/chat/agent_run.py`:
remove dependency on `UserSession`; accept explicit `user_id`, `CrudChat`, `shell`, `chat_id`.

## Server Architecture

### RunManager
1. New module `/Users/josca/dev/varro/varro/chat/run_manager.py`.
2. `RunRecord` fields:
`run_id`, `user_id`, `chat_id`, `previous_chat_id`, `created_chat`, `state`, `task`, `events`, `next_event_id`, `subscriber_queues`, `created_at`, `finished_at`.
3. Lock policy: one active run per `(user_id, chat_id)`.
4. Event buffer policy:
store full event log for active run for guaranteed catch-up.
5. Safety cap:
if serialized event log exceeds `16MB`, mark run as `resync_required`; reconnect falls back to status polling + final persisted chat render.
6. Retention policy:
completed/cancelled/failed run records kept for `5 minutes`, then GC.

### SSE event model
1. Event `dom` payload:
`{ event_id, ops: [ { kind, selector, position?, html } ] }`.
2. Event `status` payload:
`{ event_id, state: running|completed|cancelled|failed|resync_required }`.
3. Event `ping` payload:
`{ event_id }` every `15s` to keep connection alive.
4. Catch-up:
server replays `dom`/`status` events where `event_id > since`, then streams tail.

### DOM op mapping
1. Parse `hx-swap-oob` when present.
2. `beforebegin:#chat-progress` maps to insert op before `#chat-progress`.
3. `outerHTML:#id` maps to replace op for selector `#id`.
4. Missing `hx-swap-oob` maps to insert-before-progress op.
5. `outerHTML` without selector maps to replace using element `id`; fallback insert-before-progress when selector is missing.

## Shell Architecture

### ShellPool
1. New module `/Users/josca/dev/varro/varro/chat/shell_pool.py`.
2. Key: `(user_id, chat_id)`.
3. Entry fields:
`shell`, `last_used`, `in_use_count`, `lock`, `snapshot_meta`.
4. TTL: `10 minutes` idle, checked every `60s`.
5. Eviction:
only when `in_use_count == 0`.
6. On eviction:
snapshot namespace with dill, then reset shell and close history session.
7. Restore order:
load dill snapshot first, then replay missing turns from `/Users/josca/dev/varro/varro/chat/shell_replay.py` if snapshot missing/invalid/stale.

### Snapshot format
1. Path: `/Users/josca/dev/varro/<DATA_DIR>/chats/{user_id}/{chat_id}/shell.pkl`.
2. Meta path: `/Users/josca/dev/varro/<DATA_DIR>/chats/{user_id}/{chat_id}/shell.meta.json`.
3. Metadata fields:
`schema_version`, `saved_at`, `turn_count`, `python_version`.
4. Snapshot content:
dict of user variables excluding baseline startup namespace keys and private keys.
5. Size guard:
if snapshot exceeds `512MB`, skip snapshot and rely on replay.

### Tool touches
1. In `Sql` and `Jupyter` tools in `/Users/josca/dev/varro/varro/agent/assistant.py`, call `ctx.deps.touch_shell()` after successful execution.
2. Run lifecycle also touches shell on acquire/release.

## Client Architecture

### ChatClientScript responsibilities
1. Ensure single initialization guard (`window.__varroChatClientInitialized`).
2. Listen for `chatRunStarted` and open EventSource for that `run_id`.
3. Track per-run `last_event_id`.
4. Apply `dom` ops deterministically.
5. On SSE error, reconnect with backoff using `since=last_event_id`.
6. If reconnect cannot recover and status is `resync_required`, poll `/chat/runs/{run_id}/status` until terminal, then refresh chat panel from persisted chat route.

### Run lifecycle in browser
1. Submit form via HTMX `POST /chat/runs`.
2. Receive OOB running/progress UI and `chatRunStarted`.
3. Stream blocks via SSE and apply ops.
4. On `status=completed`, close stream and ensure `ChatProgressEnd` + `ChatFormEnabled` are applied.
5. On `status=cancelled`, apply rollback ops sent by server and close stream.

## Execution Flow

1. `POST /chat/runs` validates chat ownership and run lock.
2. Creates run record and async task `_execute_run`.
3. `_execute_run` acquires shell from `ShellPool`.
4. Runs `/Users/josca/dev/varro/varro/chat/agent_run.py` and converts yielded blocks to `dom` ops.
5. Publishes stream events through `RunManager`.
6. Persists turn on success exactly as today.
7. Handles `CancelledError` using existing rollback semantics from `/Users/josca/dev/varro/app/routes/chat.py`.
8. Publishes terminal status and releases shell.

## Migration Plan

1. Add new modules:
`/Users/josca/dev/varro/varro/chat/run_manager.py`, `/Users/josca/dev/varro/varro/chat/shell_pool.py`, `/Users/josca/dev/varro/varro/chat/stream_ops.py`.
2. Refactor `/Users/josca/dev/varro/varro/chat/agent_run.py` to accept explicit shell/chat context.
3. Refactor `/Users/josca/dev/varro/app/routes/chat.py` to implement start/stream/cancel/status endpoints and remove `/ws`.
4. Update `/Users/josca/dev/varro/ui/app/chat.py` form and client script for SSE flow.
5. Update `/Users/josca/dev/varro/app/main.py` to remove `exts="ws"` and replace startup/shutdown hooks for `RunManager`/`ShellPool`.
6. Add dependency `dill` to `/Users/josca/dev/varro/pyproject.toml`.
7. Remove obsolete websocket/session tests and add new run/sse/shell tests.
8. Update `/Users/josca/dev/varro/docs/varro/chat_app.md`.
9. Update `/Users/josca/dev/varro/agents/index.md` and add/update a note in `/Users/josca/dev/varro/agents/` describing the new SSE + shell-pool architecture.

## Test Cases and Scenarios

1. Start run in existing chat:
returns `chatRunStarted`, streams blocks, persists turn, restores idle form.
2. Start run without `chat_id`:
creates chat, first turn persisted, `sess["chat_id"]` set.
3. One-run-per-chat lock:
second submit in same chat returns busy; other chats can run concurrently.
4. UpdateUrl during run:
no cancellation, stream continues, turn remains visible.
5. SSE reconnect catch-up:
disconnect mid-run, reconnect with `since`, missed events replayed, live tail continues.
6. SSE disconnect until completion:
no reconnect while running, run completes, persisted turn appears after refresh/switch.
7. Cancel existing-chat run:
task cancelled, progress/form reset, chat remains.
8. Cancel new-chat first run:
created chat deleted, artifacts removed, previous chat restored.
9. Shell idle eviction:
after 10m idle shell is snapshotted and reset.
10. Shell restore from dill:
next run loads snapshot and skips full replay.
11. Shell restore fallback:
corrupted/missing snapshot falls back to replay with no user-visible error.
12. Cross-user access:
stream/cancel/status for foreign run_id returns not found/forbidden.
13. Client script idempotency:
reprocessed scripts do not create duplicate listeners or duplicate streams.
14. Startup/shutdown:
cleanup tasks start and stop cleanly, no pending task leaks.

## Assumptions and Defaults

1. Run lock scope is per `(user_id, chat_id)`.
2. Reconnect policy is replay buffered chunks then tail.
3. If stream drops and never reconnects, run still completes and persists turn.
4. Active runs are not recoverable across server restart.
5. Shell eviction TTL is 10 minutes, cleanup interval is 60 seconds.
6. Snapshot strategy is dill first, replay fallback.
7. Snapshot files are trusted internal server artifacts; no external upload path is introduced.
8. Backward compatibility with websocket transport is intentionally not preserved.