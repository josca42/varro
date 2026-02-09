# Chat + Agent Runtime

## Websocket chat flow

Primary runtime lives in:

- `app/routes/chat.py`
- `varro/chat/session.py`
- `varro/chat/agent_run.py`

Flow:

1. Browser connects to `/ws?sid=...`.
2. `SessionManager.create(...)` allocates a `UserSession`.
3. Incoming message:
  - create chat if needed,
  - optionally delete turns from `edit_idx`,
  - disable chat form + start progress animation,
  - run agent and stream blocks,
  - save turn, stop progress animation, re-enable form.

## Browser session identity

`ui/app/chat.py::ChatClientScript()`:

- creates per-tab sid in `sessionStorage`,
- writes sid to websocket url and hidden inputs (`sid`, `current_url`),
- sends heartbeat (`/chat/heartbeat`) while active/visible,
- sends close beacon on unload (`/chat/close`).

## Session model (`UserSession`)

State fields:

- `chat_id`, `msgs`, `turn_idx`,
- stateful IPython shell (`TerminalInteractiveShell`),
- `cached_prompts`,
- persisted bash working directory (`bash_cwd`).
- current URL state (`current_url`) for assistant navigation.

Turn persistence:

- messages serialized as msgpack + zstd:
  - `data/chats/{user_id}/{chat_id}/{idx}.mpk`
- cache file for rendered placeholders:
  - `{idx}.cache.json` (`fig:name` / `df:name` -> HTML).

## Agent orchestration (`varro/chat/agent_run.py`)

- uses `agent.iter(...)` from pydantic-ai.
- maps completed nodes to UI blocks:
  - user prompt bubbles,
  - reasoning block (thinking/text/tool calls + tool returns),
  - final answer block(s).
- first user turn triggers async title generation with a small agent model.

## Agent configuration (`varro/agent/assistant.py`)

- model: `claude-sonnet-4-5`
- thinking enabled with token budget
- builtin web search tool with Copenhagen locale metadata
- custom tools exposed in code:
  - `ColumnValues`
  - `Sql`
  - `Jupyter`
  - `Read` / `Write` / `Edit`
  - `Bash`
  - `UpdateUrl`

## Agent prompt (`varro/prompts/agent/rigsstatistiker.j2`)

Structured as:

1. **Role** — Rigsstatistikeren identity + current date.
2. **Environment** — Sandboxed filesystem layout (`/subjects/`, `/fact/`, `/dim/`, `/dashboards/`, `/skills/`).
3. **Database schema** — dim/fact schema, join pattern.
4. **Tools** — Documents all registered tools by their exact names.
5. **Workflow** — Step-by-step: identify subject → read docs → check values → query → analyze.
6. **Output format** — `<df />` and `<fig />` embedding tags.
7. **Dashboards** — Brief pointer to `/skills/dashboard_creation.md`.
8. **Subject hierarchy** — Compact (roots + mids only) injected via `{{ SUBJECT_HIERARCHY }}`. Agent discovers leaves on-demand via `Bash("ls /subjects/{root}/{mid}/")`.

The agent accesses table docs and subject overviews via `Read` and `Bash` on the filesystem.

## Tool runtime helpers

- `varro/agent/ipython_shell.py`: patched shell `run_cell`, timeout support.
- `varro/agent/utils.py`: dataframe/figure rendering helpers.
- `varro/agent/playwright_render.py`: persistent headless browser for plotly png snapshots.
- `varro/agent/bash.py`: sandboxed command execution with allowlist and per-user working root.

## URL-state navigation flow

- `UpdateUrl(path?, params?, replace?)` builds app-relative URLs and stores the latest URL in session state.
- Tool output uses the marker format `UPDATE_URL {json_payload}`.
- `ui/app/tool.py` detects `UpdateUrl` results and emits a script call to `window.__varroApplyUpdateUrl(callId, payload)`.
- `ui/app/layout.py::UrlStateScript()` applies navigation via HTMX (`#content-panel`) and updates browser history (`pushState`/`replaceState`).

## Chat UI rendering

`ui/app/chat.py` handles:

- message list + form + dropdown,
- model-part rendering (`ThinkingPart`, `TextPart`, `ToolCallPart`),
- markdown rendering with dashboard parser support,
- inline placeholders:
  - `<fig name="..."/>`
  - `<df name="..."/>`

## Important runtime notes

- History replay attempts to re-run prior tool calls to rebuild shell state.
- Chat edit flow removes turns >= `edit_idx` from DB and disk.
- Progress indicator uses Game of Life canvas and OOB swaps.
- Chat form hidden fields (`sid`, `current_url`) are initially set by `ChatClientScript`, and each turn replaces `#chat-form` via websocket OOB swaps (`ChatFormDisabled`/`ChatFormEnabled`).
- `ChatClientScript` now re-applies hidden values on both `htmx:afterSwap` and `htmx:oobAfterSwap`, preventing follow-up messages from dropping `sid` and being ignored by `on_message`.
- `Read` tool uses fail-on-read behavior for non-images: it tries UTF-8 text reads for files regardless of extension (e.g. `.py`, `.sql`, `.html`) and returns an error from the read/decode attempt for binary files (e.g. `.parquet`), instead of extension allowlisting.
