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
  - disable chat form + start progress animation,
  - run agent and stream blocks,
  - persist the new turn,
  - stop progress animation + re-enable form.

## Browser session identity

`ui/app/chat.py::ChatClientScript()`:

- creates per-tab sid in `sessionStorage`,
- writes sid to websocket URL and hidden inputs (`sid`, `current_url`),
- refreshes hidden values on initial load, HTMX swaps, popstate, and form submit,
- sends heartbeat (`/chat/heartbeat`) while active/visible,
- sends close beacon on unload (`/chat/close`).

## Session model (`UserSession`)

`UserSession` is transport + shell identity only:

- `user_id`, `sid`, `send`, `ws`, `chats`
- stateful IPython shell (`TerminalInteractiveShell`)
- `shell_chat_id` to track which chat shell state currently represents

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
- Edit-message flow is removed.

## Important runtime notes

- Disk IO is now the source of truth for history on every message run.
- Shell continuity is preserved only through replay + in-memory shell per active chat session.
- Chat deletion removes turn files, render cache files, and `runtime.json`.
- Full-history vs incremental rendering is route-driven, not inferred:
  - `/chat/switch/{chat_id}` returns full `ChatPanel(...)`.
  - WebSocket `on_message` streams only new blocks for the active run.
- `request_current_url()` is a request-snapshot of browser URL captured client-side at send time; server tools cannot execute browser JavaScript mid-tool-call.
- Concurrent `Bash` tool calls for the same chat are accepted with last-writer-wins semantics for persisted `bash_cwd`.
