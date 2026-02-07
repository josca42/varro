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
- writes sid to websocket url and hidden inputs,
- sends heartbeat (`/chat/heartbeat`) while active/visible,
- sends close beacon on unload (`/chat/close`).

## Session model (`UserSession`)

State fields:

- `chat_id`, `msgs`, `turn_idx`,
- stateful IPython shell (`TerminalInteractiveShell`),
- `cached_prompts`,
- persisted bash working directory (`bash_cwd`).

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

## Agent prompt (`varro/prompts/agent/rigsstatistiker.j2`)

Structured as:

1. **Role** — Rigsstatistikeren identity + current date.
2. **Environment** — Sandboxed filesystem layout (`/subjects/`, `/fact/`, `/dim/`, `/dashboards/`, `/skills/`).
3. **Database schema** — dim/fact schema, join pattern.
4. **Tools** — Documents all 7 registered tools by their exact names.
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
