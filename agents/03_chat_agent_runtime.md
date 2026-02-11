# Chat + Agent Runtime

## Websocket chat flow

Primary runtime:

- `app/routes/chat.py`
- `varro/chat/session.py`
- `varro/chat/agent_run.py`

Flow:

1. Browser connects to `/ws?sid=...`.
2. `SessionManager.create(...)` allocates a `UserSession`.
3. Incoming message:
  - create chat if needed,
  - switch send button into stop mode + start progress animation,
  - run agent in a cancellable task and stream blocks,
  - on completion: persist the new turn, stop progress, restore send mode,
  - on cancel: rollback to the pre-turn chat state and discard streamed partial output.
4. `/chat/cancel` cancels the active run for `{user_id, sid, run_id}`.

## Browser session identity

`ui/app/chat.py::ChatClientScript()`:

- creates per-tab sid in `sessionStorage`,
- writes sid to websocket URL and hidden inputs (`sid`, `current_url`),
- refreshes hidden values on initial load, HTMX swaps, popstate, and form submit,
- chat composer keyboard behavior is Enter-to-send, Shift+Enter for newline, with whitespace-only submits blocked and IME-safe Enter handling,
- sends heartbeat (`/chat/heartbeat`) while active/visible,
- sends close beacon on unload (`/chat/close`).

## Session model (`UserSession`)

`UserSession` is transport + shell identity only:

- `user_id`, `sid`, `send`, `ws`, `chats`
- stateful IPython shell (`TerminalInteractiveShell`)
- `shell_chat_id` to track which chat shell state currently represents
- `active_run` to track cancellable in-flight turn execution (`run_id`, chat ids, task)

No per-session chat history state is stored (`msgs`, `turn_idx`, `current_url`, `bash_cwd`, `cached_prompts` removed).

## Turn/runtime persistence

Turn files:

- `data/chats/{user_id}/{chat_id}/{idx}.mpk` (msgpack+zstd `ModelMessage` list)
- `data/chats/{user_id}/{chat_id}/{idx}.cache.json` (fig/df cached HTML)

Chat runtime state:

- `data/chats/{user_id}/{chat_id}/runtime.json`
- schema: `{"bash_cwd": "/..."}`

Helpers:

- `varro/chat/turn_store.py`
- `varro/chat/render_cache.py`
- `varro/chat/runtime_state.py`
- `varro/chat/shell_replay.py`

## Agent orchestration (`varro/chat/agent_run.py`)

`run_agent(...)` now does stateless history reconstruction per request:

1. Load turns from DB (`chat_id`, `with_turns=True`).
2. Load full message history from turn files.
3. Compute `turn_idx = len(turns)`.
4. Ensure shell for this chat (`ensure_shell_for_chat`):
  - reset shell on chat switch,
  - replay prior `Sql(df_name=...)` and `Jupyter(...)` tool calls.
5. Run `agent.iter(...)` with request-scoped deps.
6. Persist new turn messages + render cache + DB turn row.
7. Trigger async title generation when `turn_idx == 0`.

## Session manager liveness

`SessionManager` stores entries as:

- `{session: UserSession, last_seen: datetime}`

`touch`, `evict_idle`, `find_by_ws`, `get`, `create`, and `remove` use entry metadata; `last_seen` is no longer on `UserSession`.

`UserSession` run lifecycle methods:

- `start_run(...)` reserves the active turn slot.
- `attach_run_task(...)` links the asyncio task to that run id.
- `cancel_active_run(run_id)` cancels in-flight work (idempotent/stale-safe).
- `clear_run(run_id)` clears tracking after completion/cancel.

## Assistant deps and tool runtime

`varro/agent/assistant.py` uses:

- `AssistantRunDeps(user_id, chat_id, shell, request_current_url)`

Tool changes:

- `Bash` loads/saves cwd via `runtime.json` per chat.
- `Snapshot(url?)` uses explicit `url` or `request_current_url()`.
- `UpdateUrl(path?, params?, replace?)` builds payload from explicit `path` or `request_current_url()`.
- Prompt generation uses module-level cache for static expensive prompt parts (`SUBJECT_HIERARCHY`).

## URL-state navigation flow

- Frontend captures current content URL into hidden `current_url` at send time.
- `on_message` passes `current_url` into `run_agent(...)`.
- Assistant reads URL via `ctx.deps.request_current_url()` during that run only.
- No URL state is persisted on `UserSession`.

## Chat load vs streaming behavior

- `/chat/switch/{chat_id}` returns full `ChatPanel(...)` from persisted turns.
- WebSocket message path streams only new blocks for the active run.
- Cancel path (`/chat/cancel`) triggers rollback by re-sending a full OOB `ChatPanel(...)`.
- Edit-message flow is removed.

## Important runtime notes

- Disk IO is now the source of truth for history on every message run.
- Shell continuity is preserved only through replay + in-memory shell per active chat session.
- Chat deletion removes turn files, render cache files, and `runtime.json`.
- Full-history vs incremental rendering is route-driven, not inferred:
  - `/chat/switch/{chat_id}` returns full `ChatPanel(...)`.
  - WebSocket `on_message` streams only new blocks for the active run.
- Cancel rollback semantics:
  - existing chat run: keep chat id, discard in-flight UI via full panel re-render.
  - newly created chat run: delete created chat + turn/cache/runtime artifacts and restore previous chat selection.
- `request_current_url()` is a request-snapshot of browser URL captured client-side at send time; server tools cannot execute browser JavaScript mid-tool-call.
- Concurrent `Bash` tool calls for the same chat are accepted with last-writer-wins semantics for persisted `bash_cwd`.

## Workspace docs symlinks + read-only paths

- `ensure_user_workspace` now seeds `/subjects`, `/fact`, and `/dim` as symlinks to `docs_template` instead of copying those trees.
- `/skills` and `/dashboard` are still copied into each user workspace and remain writable.
- Filesystem tools enforce docs read-only behavior:
  - `Read` supports readonly symlink traversal for docs paths.
  - `Write` and `Edit` return `Error: file_path is read-only` for `/subjects`, `/fact`, and `/dim`.
- Bash enforces docs read-only behavior:
  - read/list commands still work (`ls`, `find`, `grep`, etc.),
  - mutating commands and output redirections targeting readonly docs paths are blocked with `Error: path is read-only`.
