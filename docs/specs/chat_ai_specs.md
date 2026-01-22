Below is a concrete, implementation-oriented design + spec you can iterate on, aligned with your project structure (UI library in `ui/`, app routes in `app/`, core logic in `varro/`) and the “one active ChatSession per user” constraint.

---

## 1) Product & system goals

### Functional goals

1. **Single-user chat** (not multi-user broadcast): user sends prompts; assistant responds.
2. **Websocket-driven UI updates**: server streams HTML fragments; client applies them.
3. **Sessionful compute**: each active chat has a `ChatSession` with:

   * message history for `pydantic-ai`,
   * a stateful IPython shell namespace,
   * ability to restore shell namespace from stored history.
4. **Persistence**: store chat turns to disk (Postgres/SQLModel/CRUD).
5. **Append-only rendering** for normal operation:

   * every new turn appends new DOM blocks,
   * exception: user edits an earlier message → truncate subsequent turns both in UI and DB, then continue append-only from the edit point.

### Non-goals (initially)

* Multi-tab multi-session per user.
* Horizontal scaling across multiple worker processes without sticky sessions.
* Perfect token-by-token streaming (you can add later).

---

## 2) Key design choices

### A. Treat the websocket as the “render pipe”

Instead of sending JSON events that the client re-renders, the server sends **fully-formed HTML fragments** representing “what just happened” in the agent run (nodes / tool calls / thinking / assistant text).

This aligns with:

* HTMX’s websocket extension style,
* FastHTML’s strengths (server-rendered hypermedia),
* your existing `ui/app/chat.py` blocks (ThinkingBlock, ToolCallBlock, TextBlock).

FastHTML websocket patterns and HTMX ws extension usage are consistent with this approach. 

### B. Each user has *at most one* active in-memory ChatSession

Maintain a global in-memory registry:

* key: `user.id`
* value: `{chat_id, ChatSession, send_fn, connection_id, lock, active_run_task, ...}`

If the same user opens a second websocket:

* choose a deterministic policy (“newest wins” is simplest): close old connection/session and replace.

### C. DB stores **turns**, not “messages”

You already called this out: one `Message` row = a “message turn” (user + assistant). This is the correct primitive for:

* truncation after editing,
* restore of chat history and shell state,
* replay semantics.

### D. Node-based streaming first, event streaming later

PydanticAI offers multiple streaming approaches. For your “HTML per node” requirement, `agent.iter()` is the best match: it yields graph nodes (UserPromptNode, ModelRequestNode, CallToolsNode, End). 

Later you can upgrade to per-token/per-delta streaming by calling `node.stream(run.ctx)` (still within `iter`) if desired. 

---

## 3) Data model spec (DB)

### Tables

#### `chat`

* `id` (pk)
* `user_id` (fk)
* `title` (nullable)
* `created_at`
* `updated_at`

(You already have this.)

#### `message` (but semantically “turn”)

Add/confirm these fields:

* `id` (pk)
* `chat_id` (fk)
* `turn_index` (int, monotonic per chat) **recommended**
* `content` (JSONB) – raw, versioned “turn payload”
* `created_at`

> Why `turn_index`?
> It makes truncation and DOM IDs far easier. If you don’t want a column, you can derive ordering from `created_at`, but truncation becomes less deterministic when timestamps collide.

### `content` JSON schema (versioned)

Store a *single* JSON object representing the entire turn:

```json
{
  "v": 1,
  "user": {
    "text": "…",
    "ts": "2026-01-22T12:34:56Z"
  },
  "assistant": {
    "pydantic_messages": [ /* ModelMessage JSON list */ ],
    "attachments": {
      "tool_call_id_1": [
        {"path": "uploads/...", "media_type": "image/png"}
      ]
    },
    "final_text": "optional cached final string"
  },
  "meta": {
    "model": "claude-sonnet-4-5",
    "usage": { "input_tokens": 123, "output_tokens": 456 }
  }
}
```

Notes:

* `assistant.pydantic_messages` should be the serialized list from `RunResult.new_messages_json()` or equivalent, so you can restore conversation context exactly as PydanticAI expects. 
* `attachments` mirrors what your UI already expects (`attachments.get(part.tool_call_id, [])`).
* Store `v` for forward-compatible migrations.

### CRUD operations needed (minimum)

In `varro/db/crud/chat.py` (or a new `crud/turn.py`), add:

* `create_chat(user_id) -> Chat`
* `append_turn(chat_id, user_text, assistant_payload) -> MessageTurn`
* `update_turn_user_text(turn_id, new_text)`
* `truncate_turns_after(chat_id, turn_index)` (delete where `turn_index > X`)
* `list_turns(chat_id)` (ordered)

---

## 4) In-memory session manager spec

### `ChatSessionManager` (new module)

Create `varro/chat/live_sessions.py`:

Core responsibilities:

* Create/replace sessions on connect
* Route inbound websocket “actions” to the correct session
* Ensure one active session per user
* Serialize concurrent runs (per-session lock)
* Cleanup on disconnect

Suggested structure:

```py
@dataclass
class LiveChatSession:
    user_id: int
    chat_id: int
    sess: ChatSession
    send: Callable[[str], Awaitable[None]]
    lock: asyncio.Lock
    active_task: asyncio.Task | None
    connected_at: datetime
    last_seen_at: datetime
```

Manager:

* `sessions_by_user: dict[int, LiveChatSession]`

### Connection policy

On websocket connect:

1. Resolve `user` and `chat_id` (see Section 6).
2. If `user_id` exists in registry:

   * close old websocket (if possible) and `sess.end()`
   * remove from dict
3. Create `ChatSession(user, chats, chat_id)`
4. `await chat_session.start()`:

   * load history from DB
   * restore shell namespace
5. Store in dict.

On disconnect:

* `sess.end()`
* remove from dict

### Concurrency and cancellation

* One run at a time per session (`lock`).
* Optional `Stop` action:

  * cancel `active_task`
  * send an error/info block and re-enable input.

---

## 5) ChatSession lifecycle spec

You already have `ChatSession.start()` and `_restore_shell_namespace()` conceptually. The lifecycle spec should be explicit:

### `start()`

* Load turns from DB.
* Construct:

  * `chat_session.turns` (your own list of turn metadata)
  * `chat_session.msgs` (flattened list of `ModelMessage` for PydanticAI history)
* If any previous tool calls existed that mutated shell state:

  * replay them in order to reconstruct namespace.
  * (Your existing `_restore_shell_namespace` does this by scanning tool-call parts.)

### `run_turn(user_text)`

* Append user_text to the run (via agent call)
* Stream node HTML blocks to the client
* At end:

  * persist turn payload (including pydantic messages + attachments)
  * update `chat_session.msgs` and cached shell state
  * update `chat.updated_at`

### `edit_turn(turn_index, new_user_text)`

Define the required invariants:

1. All turns after `turn_index` are deleted (DB + memory + DOM).
2. The edited turn’s user text is updated.
3. The session state (shell + `msgs`) is rebuilt to match the truncated history.

Pragmatic implementation approach (robust, easiest):

* truncate DB turns after `turn_index`
* reset shell (`sess.end()` / recreate shell)
* re-instantiate `ChatSession` and `start()` to replay tool calls from remaining history
* then run agent starting from the edited prompt (see Section 7 UX decision)

This is computationally heavier, but correct and simple. You can optimize later.

---

## 6) Routes & integration boundaries

You’re already using Beforeware to attach `user` and scoped `CrudChat` to the request. Keep that for HTTP routes (chat list, create, delete, switch). For websockets, you need an equivalent way to resolve user + chat.

### HTTP routes (APIRouter)

Keep these HTTP endpoints:

* `GET /chat` (page) – renders current chat
* `POST /chat/new` – creates chat, sets `sess["chat_id"]`, returns new page fragment
* `GET /chat/history` – returns dropdown menu of chats
* `POST /chat/delete?id=...` – deletes chat

Follow your “simple verbs” / FastHTML idioms (query params, function-based routes). 

### Websocket route

One websocket endpoint, e.g.:

* `WS /chat/ws?chat_id=...`

FastHTML supports websocket routes via `@app.ws`, and session data can be shared between HTTP and websocket handlers, which is ideal for auth integration (cookie-backed session). 

#### User resolution in websocket

Preferred order:

1. `ws.scope["session"]` has `user_id` (set by your existing auth layer).
2. Otherwise: reject.

Then load `user = crud.user.get(user_id)` and scoped `chats = crud.chat.for_user(user_id)`, then validate `chat_id` belongs to user.

---

## 7) Websocket message protocol (client → server)

Even if your connection is “one way” conceptually, the client still has to send messages. Define explicit `action`s.

HTMX ws sends form fields; FastHTML can parse parameters directly into handler args or accept `data` dict. 

### Actions

1. **Send message**

   * fields: `action="send"`, `chat_id`, `msg`
2. **Edit message**

   * fields: `action="edit"`, `chat_id`, `turn_index`, `msg`
3. **Stop**

   * fields: `action="stop"`, `chat_id`

### UX decision for edit

Pick one of these and codify it:

**Option A (recommended)**: “Save & regenerate from here”

* When user edits a turn and submits, the server truncates subsequent turns and immediately runs the assistant again from the edited message.
* This matches how most “editable history” chat UIs work.

**Option B**: “Save only”

* Only truncates future turns; user must explicitly hit “Send” to continue.

Option A is more intuitive and keeps your spec simpler.

---

## 8) Server → client HTML streaming spec

### DOM structure (stable IDs)

Define stable containers so the server can target swaps precisely:

* `#chat-turns` (container for all turns)
* `#turn-{turn_index}` (wrapper per turn)
* `#assistant-{turn_index}` (assistant stream area for that turn)
* `#progress` or `#progress-{turn_index}` (status indicator)

### Append-only normal operation

For a new user message:

1. Server immediately sends:

   * appended `TurnShell(turn_index)` containing:

     * User bubble
     * empty assistant stream container
     * progress indicator
2. Server then streams assistant node blocks, appended to `#assistant-{turn_index}`.
3. Server finally sends:

   * progress cleared/updated
   * input re-enabled
   * input cleared

### Edit exception: truncate after edited message

When editing `turn_index = k`:

* Server instructs client to remove all `#turn-{i}` where `i > k`
* Server then streams regenerated content (Option A) as new assistant blocks in `#assistant-{k}` (or create a fresh assistant subcontainer).

**Mechanism to remove DOM nodes:**
HTMX does not have a built-in “remove everything after selector X” primitive. Two practical approaches:

1. **OOB `innerHTML` reset of `#chat-turns`**

   * Server re-renders the truncated chat history and swaps `#chat-turns` entirely.
   * Pros: simplest, deterministic.
   * Cons: not “append-only”, but allowed under your edit caveat.

2. **A small Alpine/JS helper**

   * Server sends a `<script>` OOB that runs `truncateTurnsAfter(k)`.
   * Pros: preserves the “append-only except deletions” spirit more literally.
   * Cons: slightly more JS surface area.

Given your “iterable spec” goal, start with (1) and only optimize if you feel it.

---

## 9) Mapping PydanticAI graph nodes to UI blocks

Your requirement: “each html returned is a pydantic-ai node in an agent stream.”

Use `agent.iter()` and produce **one outer block per node** that may contain multiple sub-blocks.

PydanticAI’s `iter()` yields nodes like ModelRequestNode / CallToolsNode / End. 

### Node → UI mapping

* **UserPromptNode**

  * usually no UI (you already rendered the user bubble)
* **ModelRequestNode**

  * update progress: “Thinking…”
* **CallToolsNode**

  * append:

    * ThinkingBlock(s) (if present)
    * ToolCallBlock(s) + results + attachments
    * TextBlock(s) (assistant output parts)
* **End**

  * progress cleared
  * input enabled
  * persist to DB

### Optional future upgrade: event streaming within a node

Within ModelRequestNode, you can do:

* `async with node.stream(run.ctx) as stream: ...`

This supports finer-grained streaming (text deltas, tool call deltas, etc.). 
Only do this after your “node blocks” MVP is solid.

---

## 10) Attachment pipeline spec (BinaryContent → /uploads)

Your tools already can return `BinaryContent` via `ToolReturn` (e.g., plotly PNG, matplotlib PNG). Your UI expects `/uploads/{path}`.

Define:

* Upload root directory (e.g., `varro/config.py: UPLOADS_DIR`)
* A stable serving route `GET /uploads/{file}` using FastHTML static route or Starlette FileResponse.

Processing rules:

* On tool result:

  * split text vs binary items
  * persist binary items to disk
  * add metadata into `assistant.attachments[tool_call_id]`
* Persist attachment metadata in the turn JSONB content so history renders correctly on reload.

---

## 11) UI/UX spec (MVP)

### Layout

* Header: chat title + chat dropdown + “New chat”
* Body: scrollable list of turns (`#chat-turns`)
* Footer: input bar (textarea + send)

### Behaviors

* Auto-scroll to bottom on new blocks.
* Disable input while a run is active (optional but recommended).
* Show progress indicator states:

  * Thinking
  * Running tools
  * Done / cleared
* Errors:

  * show ErrorBlock inline in assistant stream area
  * re-enable input

### Editing (v1)

* Each user bubble has an “Edit” action.
* Edit UI:

  * toggle into textarea inline,
  * “Save & regenerate from here”
  * “Cancel”
* On save:

  * truncate subsequent turns
  * regenerate from edited turn (Option A)