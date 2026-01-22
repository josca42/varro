Below is a design that stays aligned with your constraints (HTMX-native HTML over the wire; SSE only for streaming HTML; lifecycle handled cleanly; clear separation between `ChatSession`, `streaming.py`, and `app/routes/chat.py`) while keeping the implementation close to what you already have.

I’ll describe the target architecture first, then walk through the concrete flow (GET page → POST send → SSE stream → persist → cleanup), then show a practical `ChatSession` API + code skeleton, and finally show what `streaming.py` and `app/routes/chat.py` become.

---

## 1) What you already have that’s strong

You already have three important “primitives” that are worth preserving:

1. **DB persistence model**: `Chat` + `Message` rows; `Message.content` stores:

   * user: `{ "text": ... }`
   * assistant: `{ "pydantic_messages": [...], "attachments": {...} }`

2. **Replay-based state restoration**: re-running past `sql_query`/`jupyter_notebook` tool calls to rebuild the IPython namespace is a pragmatic stateless-server approach.

3. **UI rendering based on stored Pydantic AI messages**: `ui/app/chat.py::AssistantMessage()` already knows how to render `ThinkingPart`, tool calls, results, and `TextPart` using the same blocks your stream uses.

So the main goal is not to change those primitives—just to reorganize responsibilities so:

* lifecycle & persistence move into `ChatSession`
* streaming becomes “node → HTML blocks”
* routes become thin orchestrators

---

## 2) Target separation of concerns

### A. `varro/chat/session.py` – “Chat lifecycle + state manager”

A `ChatSession` instance exists per request (POST send, SSE stream, etc.), but it encapsulates:

* Chat identity and ownership validation
* Loading & sorting DB messages
* Building `message_history` for the agent (Pydantic AI `ModelMessage` list)
* Creating and owning **agent deps** (`SessionStore` today)
* Restoring the IPython shell namespace by replaying tool calls
* Persisting the *assistant run output* back to DB (including attachments)
* Cleanup (`shell.reset(...)`, `end_session()`)

This keeps the “chat lifecycle” logic out of `streaming.py` and out of `routes/chat.py`.

### B. `varro/chat/streaming.py` – “Render completed nodes”

`streaming.py` becomes:

* **No DB reads**
* **No restoration logic**
* Minimal exception handling (primarily to render an error block + done)
* A generator that:

  * updates progress (“Thinking…”, “Running tools…”)
  * renders blocks for each *completed node*
  * executes tools (quietly) and then renders the tool call blocks with results
  * calls `session.save_assistant_run(...)` once at the end

This aligns with using `agent.iter()` (node-level control) and avoids event-level complexity. 

### C. `app/routes/chat.py` – “HTTP orchestration”

Routes do only:

* auth/user lookup (assumed elsewhere in your prompt, but your structure remains)
* create `ChatSession`
* call `ensure_chat()` / `add_user_message()` in POST
* call `await session.start()` in SSE stream route
* return HTMX fragments (same components)

Also, you can optionally align routes to FastHTML idioms (query params over path params; `.to()` URL generation).  

---

## 3) Step-by-step flow (how it behaves at runtime)

### Step 1: GET `/chat`

* Route loads current chat_id from session, fetches chat + messages.
* Renders `ChatPage(chat)` as today.
* No agent deps, no restoration.

### Step 2: POST `/chat/send`

* Create `ChatSession(user, chat_id=sess.get("chat_id"))`
* `session.ensure_chat(title=message[:30])`
* `session.add_user_message(message)`
* Update `sess["chat_id"]`
* Return HTMX partial that:

  * appends `UserMessage(message)`
  * swaps in `StreamContainer(chat_id)` (which opens SSE)
  * disables form

### Step 3: SSE GET `/chat/stream?...`

* Create `ChatSession(user, chat_id)`
* `await session.start()`:

  * load chat + DB messages
  * build Pydantic `message_history`
  * create deps (`SessionStore`) and restore shell namespace by replay
* Then `StreamingResponse(agent_html_stream(session))`

### Step 4: `agent_html_stream(session)` renders nodes

For each node yielded by `agent.iter(...)`:

* `ModelRequestNode`: yield “Thinking…” progress
* `CallToolsNode`:

  * render all `ThinkingPart` blocks in that node
  * if there are tool calls:

    * yield “Running tools…” progress
    * execute tools by consuming `node.stream(run.ctx)`
    * collect tool results keyed by `tool_call_id`
    * save `BinaryContent` to disk, add to `attachments_map`
    * render one `ToolCallBlock` per tool call
  * render any `TextPart` blocks in that node
* `End`: don’t duplicate text (it was already rendered from the response parts)

### Step 5: Persist the run atomically

When the run ends successfully:

* `new_msgs = run.result.new_messages()`
* `session.save_assistant_run(new_msgs, attachments_map)`
* yield `done` SSE event to replace stream container and re-enable form

### Step 6: Cleanup always

In a `finally:`:

* `session.end()` → resets shell and closes history

### Stop / cancel behavior

* “Stop” button swaps out the SSE container (no `sse_connect` anymore), so the browser closes the EventSource.
* Starlette cancels the streaming generator, you get `asyncio.CancelledError`.
* In `CancelledError`, you just exit, but `finally` runs and cleans up.
* No assistant message is persisted (avoids partial/invalid history).

This achieves “graceful lifecycle” without extra JS: browser closing, navigation, and “New Chat” all naturally close the SSE connection as well.

---

## 4) `ChatSession` design and concrete API

### Design principles

* **Two-phase use**:

  * For POST `/chat/send`, you only need *ensure chat + store user message*. No restore required.
  * For SSE stream, you need *load + restore + provide message_history and deps*.
* Keep the existing agent deps (`SessionStore`) unless you explicitly want to merge them. The cleanest refactor is: `ChatSession` **owns** a `SessionStore` instance and passes it as `deps=` to the agent.

### Suggested file: `varro/chat/session.py`

```py
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime
from types import SimpleNamespace
from typing import Any

from pydantic_ai import ModelMessagesTypeAdapter
from pydantic_ai.messages import ModelMessage, ModelResponse, BaseToolCallPart
from pydantic_core import to_jsonable_python

from varro.db import crud
from varro.db.models.chat import Chat, Message
from varro.db.models.user import User
from varro.agent.assistant import SessionStore, sql_query, jupyter_notebook


def _sort_db_messages(chat: Chat) -> None:
    if not chat.messages:
        return
    chat.messages = sorted(
        chat.messages,
        key=lambda m: (m.created_at or datetime.min, m.id or 0),
    )


@dataclass
class ChatSession:
    user: User
    chat_id: int | None = None

    chat: Chat | None = None
    db_messages: list[Message] = field(default_factory=list)

    message_history: list[ModelMessage] = field(default_factory=list)
    deps: SessionStore = field(init=False)

    def __post_init__(self):
        self.deps = SessionStore(user=self.user)

    def ensure_chat(self, title: str) -> Chat:
        if self.chat_id:
            chat = crud.chat.get(self.chat_id)
            if chat and chat.user_id == self.user.id:
                self.chat = chat

        if not self.chat:
            self.chat = crud.chat.create(Chat(user_id=self.user.id, title=title[:30]))
            self.chat_id = self.chat.id

        return self.chat

    def add_user_message(self, text: str) -> Message:
        if not self.chat_id:
            raise ValueError("chat_id is not set")
        msg = crud.message.create(Message(chat_id=self.chat_id, role="user", content={"text": text}))
        crud.chat.update(Chat(id=self.chat_id, updated_at=datetime.utcnow()))
        return msg

    async def start(self) -> Chat:
        if not self.chat_id:
            raise ValueError("chat_id is not set")

        chat = crud.chat.get(self.chat_id, with_msgs=True)
        if not chat or chat.user_id != self.user.id:
            raise PermissionError("Chat not found or not owned by user")

        _sort_db_messages(chat)
        self.chat = chat
        self.db_messages = chat.messages or []
        self.message_history = self._build_message_history()
        await self._restore_shell_namespace()
        return chat

    def last_user_text(self) -> str:
        for msg in reversed(self.db_messages):
            if msg.role == "user":
                return msg.content.get("text", "")
        return ""

    def save_assistant_run(self, new_messages: list[ModelMessage], attachments: dict[str, Any]) -> Message:
        if not self.chat_id:
            raise ValueError("chat_id is not set")

        stored = to_jsonable_python(new_messages)
        msg = crud.message.create(
            Message(
                chat_id=self.chat_id,
                role="assistant",
                content={
                    "pydantic_messages": stored,
                    "attachments": attachments,
                },
            )
        )
        crud.chat.update(Chat(id=self.chat_id, updated_at=datetime.utcnow()))
        self.message_history.extend(new_messages)
        return msg

    def end(self) -> None:
        self.deps.cleanup()

    def _build_message_history(self) -> list[ModelMessage]:
        history: list[ModelMessage] = []
        for msg in self.db_messages:
            stored = msg.content.get("pydantic_messages")
            if stored:
                history.extend(ModelMessagesTypeAdapter.validate_python(stored))
        return history

    async def _restore_shell_namespace(self) -> None:
        if not self.message_history:
            return

        ctx = SimpleNamespace(deps=self.deps)

        for msg in self.message_history:
            if not isinstance(msg, ModelResponse):
                continue

            for part in msg.parts:
                if not isinstance(part, BaseToolCallPart):
                    continue

                args = part.args or {}
                if isinstance(args, str):
                    args = json.loads(args)

                if part.tool_name == "sql_query":
                    df_name = args.get("df_name")
                    if df_name:
                        sql_query(ctx, args.get("query", ""), df_name)

                elif part.tool_name == "jupyter_notebook":
                    await jupyter_notebook(ctx, args.get("code", ""), show=[])
```

Notes on this specific shape:

* It preserves your current “assistant message row stores `pydantic_messages`” approach, so **no UI changes are required**.
* Shell restoration only replays `sql_query` if `df_name` is present (because otherwise it’s not in the namespace anyway).
* Restoration replays *all* `jupyter_notebook` calls, but disables rendering (`show=[]`) to avoid re-creating attachment files.

---

## 5) `streaming.py` simplified to “node → blocks”

Now `varro/chat/streaming.py` can be much smaller and deterministic: it does not “restore session”, it assumes `ChatSession.start()` already did that.

Key tactics:

* Render `ThinkingPart` blocks immediately when you see them in `CallToolsNode`.
* If there are tool calls, execute them, collect results, render tool blocks.
* Render `TextPart` blocks from the node (don’t wait for `End`).

This approach is exactly what `agent.iter()` is designed for: you iterate graph nodes and optionally stream tool execution/events when handling a node. 

---

## 6) Routes become thin orchestration

### Minimal changes in `app/routes/chat.py`

* POST `/chat/send` uses `ChatSession` for chat creation and user message persistence.
* SSE route creates session, calls `await start()`, then streams.

Also: you can keep your existing paths. If you want to adopt FastHTML’s “query param over path param” preference, you can, but it’s optional.  

---

## 7) Lifecycle edge cases to explicitly decide

These are the few “policy decisions” you should pick deliberately:

1. **Do you persist partial assistant output when stopped?**
   I recommend **no**: don’t write assistant messages to DB unless the run completes successfully. This keeps history consistent and makes restore deterministic.

2. **Do you want to record “cancelled” / “failed” events?**
   Optional, but if you do, store a lightweight assistant row like:

   * `{ "error": "...", "kind": "cancelled" }`
     Then `AssistantMessage()` can render a small `ErrorBlock` in history. Right now you only show errors in-stream.

3. **Concurrency control (multiple tabs / multiple runs)**
   If you expect concurrent streams for the same chat/user, you should add:

   * a per-chat `asyncio.Lock`, or
   * an in-memory registry of running streams keyed by `(user_id, chat_id)` to prevent overlapping runs.

   With the current IPython approach, concurrency is the bigger risk than DB consistency.

---

## 8) Practical refactor plan (low-risk sequence)

1. Add `varro/chat/session.py` with `ChatSession`.
2. Update `app/routes/chat.py`:

   * replace inline “create chat / add msg” with `ChatSession.ensure_chat()` + `add_user_message()`
   * in SSE route, instantiate session + `await session.start()`
3. Simplify `varro/chat/streaming.py`:

   * remove `restore_session_store` and `build_message_history` (they live in session)
   * render nodes (not events)
   * persist via `session.save_assistant_run(...)`
   * ensure `finally: session.end()`
4. Keep UI unchanged. The stored `pydantic_messages` format remains identical.

---

If you want, I can also propose a small optional improvement to the “Stop” behavior so the form is always re-enabled even if the SSE connection drops unexpectedly (network blip): that typically involves one small HTMX hook or a server-side heartbeat/done-on-exit convention, but it’s not required if you’re satisfied with the current Stop button semantics.