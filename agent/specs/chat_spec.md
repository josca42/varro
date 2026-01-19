# Chat UI Specification

## Overview

Real-time chat interface for the Rigsstatistikeren AI agent. Uses SSE with HTMX to stream server-rendered HTML fragments. Follows HTMX philosophy: server manages state, renders HTML, minimal client-side JS.

## Architecture

```
┌─────────────┐     POST /chat/send   ┌─────────────┐
│   Browser   │ ──────────────────────→│  FastHTML   │
│    (HTMX)   │                        │   Server    │
│             │ ←── HTML + SSE connect │             │
│             │                        │             │
│             │ ←── SSE HTML fragments │             │
└─────────────┘                        └──────┬──────┘
                                              │
                                              │ agent.iter()
                                              ▼
                                       ┌─────────────┐
                                       │ pydantic-ai │
                                       │    Agent    │
                                       └─────────────┘
```

---

## Data Models

### Chat

```python
class Chat(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    title: str | None = None  # First 30 chars of first user message
    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )
    updated_at: datetime | None = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    )
    messages: list["Message"] = Relationship(
        back_populates="chat",
        sa_relationship_kwargs={"cascade": "all, delete"},
    )
```

### Message

```python
class Message(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    chat_id: int = Field(foreign_key="chat.id", index=True)
    role: str  # 'user' | 'assistant'
    content: dict = Field(sa_column=Column(JSONB))
    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )
    chat: Chat | None = Relationship(back_populates="messages")
```

### Message Content Structure

**User message:**
```json
{
  "text": "Hvad er arbejdsløsheden i Danmark?"
}
```

**Assistant message:**
```json
{
  "nodes": [
    {
      "parts": [
        {"type": "thinking", "content": "I need to find unemployment data..."},
        {"type": "tool_call", "tool": "sql_query", "args": {"query": "SELECT ...", "df_name": "df_result"}, "result": "Stored as df_result\n| col1 | col2 |..."}
      ]
    },
    {
      "parts": [
        {"type": "thinking", "content": "Now I'll visualize this data..."},
        {"type": "tool_call", "tool": "jupyter_notebook", "args": {"code": "fig = px.bar(...)"}, "result": "", "attachments": [{"path": "1/chat_data/5/abc123.png", "media_type": "image/png"}]}
      ]
    },
    {
      "parts": [
        {"type": "text", "content": "Arbejdsløsheden i Danmark er 4.2% pr. januar 2025..."}
      ]
    }
  ]
}
```

---

## Binary File Storage

**Directory structure:**
```
/{user_id}/chat_data/{chat_id}/{uuid}.png
```

**Lifecycle:**
- Created when tool produces `BinaryContent`
- Referenced via `attachments` array in tool_call part
- Deleted when chat is deleted (entire `/{user_id}/chat_data/{chat_id}/` folder)

---

## Session Management

### Cookie Session

```python
sess['chat_id']  # Current active chat ID or None
```

### SessionStore Lifecycle

`SessionStore` contains:
- `shell`: IPython InteractiveShell (namespace with DataFrames)
- `shell_imports`: bool
- `memory`: Memory instance
- `cached_prompts`: dict

**On sending message in existing chat:**
- Replay all tool calls from chat history to restore `SessionStore`
- Then execute new message with restored state

### Replay Logic

```python
async def restore_session_store(chat: Chat, deps: SessionStore):
    """Replay tool calls to restore SessionStore state."""
    for msg in chat.messages:
        if msg.role != 'assistant':
            continue

        for node in msg.content.get('nodes', []):
            for part in node.get('parts', []):
                if part['type'] != 'tool_call':
                    continue

                tool = part['tool']
                args = part['args']

                if tool == 'sql_query':
                    sql_query(deps, args['query'], args.get('df_name'))
                elif tool == 'jupyter_notebook':
                    jupyter_notebook(deps, args['code'], args.get('show', []))
```

---

## HTMX SSE Flow

### 1. User Submits Message

Form posts to `/chat/send`. Server:
1. Creates chat if needed
2. Saves user message
3. Returns HTML fragment with user message + SSE streaming container

```html
<!-- Returned by POST /chat/send -->
<div id="msg-42" class="flex justify-end mb-4">
  <div class="bg-base-200 px-4 py-3 rounded-box max-w-[85%]">User message</div>
</div>

<div id="stream-container"
     hx-ext="sse"
     sse-connect="/chat/stream/{chat_id}"
     hx-swap="beforeend">

  <div id="progress-indicator" class="flex items-center mb-4">
    <span class="loading loading-dots loading-sm"></span>
    <span id="progress-text" class="ml-2 text-sm text-base-content/50">Thinking...</span>
  </div>

  <div id="streaming-content" sse-swap="content:beforeend"></div>
</div>

<!-- Re-enable input form via OOB swap -->
<form id="chat-form" hx-swap-oob="true" ...>
  <!-- Form with disabled state during streaming -->
</form>
```

### 2. SSE Stream Sends HTML Fragments

Each event sends pre-rendered HTML:

```
event: content
data: <div class="thinking-block">...</div>

event: progress
data: <div id="progress-indicator" hx-swap-oob="true">Running SQL query...</div>

event: content
data: <div class="tool-call-block">...</div>

event: content
data: <div class="text-block prose">Final answer...</div>

event: done
data: <div id="stream-container" hx-swap-oob="outerHTML"><!-- Final content without sse-connect --></div>
```

### 3. Stream Completion

The `done` event replaces `stream-container` with static content (no `sse-connect`), which closes the SSE connection.

### 4. Cancellation

Stop button uses `hx-get="/chat/stop"` which:
1. Returns HTML that replaces `stream-container` (closing SSE)
2. Re-enables input form
3. Partial assistant message is NOT saved

---

## Backend Implementation

### Endpoints

```python
@rt("/chat")
def chat_page(sess, user: User):
    """Main chat page."""
    chat = crud.chat.get(sess.get("chat_id"), add_msgs=True)
    if chat and chat.user_id != user.id:
        sess["chat_id"] = None
        chat = None
    return ChatPage(chat)


@rt("/chat/send", methods=["POST"])
async def chat_send(sess, user: User, message: str):
    """Handle message submission, return HTML with SSE connect."""
    chat_id = sess.get('chat_id')

    # Create new chat if needed
    if not chat_id:
        chat = crud.chat.create(Chat(
            user_id=user.id,
            title=message[:30]
        ))
        chat_id = chat.id
        sess['chat_id'] = chat_id

    # Save user message
    user_msg = crud.message.create(Message(
        chat_id=chat_id,
        role='user',
        content={'text': message}
    ))

    # Return user message + streaming container
    return Div(
        UserMessage(message),
        StreamContainer(chat_id),
        ChatFormDisabled(),  # OOB swap to disable form
        id="message-area"
    )


@rt("/chat/stream/{chat_id}")
async def chat_stream(sess, user: User, chat_id: int):
    """SSE endpoint that streams HTML fragments."""
    chat = crud.chat.get(chat_id, add_msgs=True)
    if not chat or chat.user_id != user.id:
        return Response(status_code=403)

    return StreamingResponse(
        agent_html_stream(chat, user),
        media_type="text/event-stream"
    )


@rt("/chat/stop/{chat_id}")
def chat_stop(sess, user: User, chat_id: int):
    """Stop generation - returns HTML that closes SSE."""
    # Just return empty final container (closes SSE) + enabled form
    return Div(
        Div(id="stream-container"),  # Empty, no sse-connect
        ChatFormEnabled(),  # OOB swap to re-enable form
    )


@rt("/chat/new")
def chat_new(sess):
    """Start a new chat."""
    sess['chat_id'] = None
    return RedirectResponse("/chat")


@rt("/chat/switch/{chat_id}")
def chat_switch(sess, user: User, chat_id: int):
    """Switch to an existing chat."""
    chat = crud.chat.get(chat_id)
    if chat and chat.user_id == user.id:
        sess['chat_id'] = chat_id
    return RedirectResponse("/chat")


@rt("/chat/delete/{chat_id}")
def chat_delete(sess, user: User, chat_id: int):
    """Delete a chat."""
    chat = crud.chat.get(chat_id)
    if chat and chat.user_id == user.id:
        upload_dir = Path(f"{user.id}/chat_data/{chat_id}")
        if upload_dir.exists():
            shutil.rmtree(upload_dir)
        crud.chat.delete(chat)
        if sess.get('chat_id') == chat_id:
            sess['chat_id'] = None
    return RedirectResponse("/chat")


@rt("/chat/history")
def chat_history(user: User):
    """Get recent chats for dropdown."""
    chats = crud.chat.get_recent_by_user(user.id, limit=10)
    return ChatDropdown(chats)
```

### SSE HTML Stream Generator

```python
async def agent_html_stream(chat: Chat, user: User):
    """Yield SSE events with HTML fragments."""
    deps = SessionStore(user=user)

    # Restore SessionStore if continuing chat
    if len(chat.messages) > 1:
        yield sse_html("progress", ProgressIndicator("Restoring session..."))
        try:
            await restore_session_store(chat, deps)
        except Exception as e:
            yield sse_html("content", ErrorBlock(f"Failed to restore session: {e}"))
            yield sse_done(chat.id, error=True)
            return

    message_history = build_message_history(chat)
    user_msg = chat.messages[-1].content['text']

    assistant_nodes = []
    current_node_parts = []

    try:
        async with agent.iter(user_msg, deps=deps, message_history=message_history) as run:
            async for node in run:
                if Agent.is_model_request_node(node):
                    yield sse_html("progress", ProgressIndicator("Thinking..."))

                    async with node.stream(run.ctx) as request_stream:
                        async for event in request_stream:
                            if isinstance(event, PartStartEvent):
                                if 'Thinking' in type(event.part).__name__:
                                    yield sse_html("progress", ProgressIndicator("Reasoning..."))

                elif Agent.is_call_tools_node(node):
                    if current_node_parts:
                        assistant_nodes.append({"parts": current_node_parts})
                        current_node_parts = []

                    # Process thinking parts
                    for part in node.model_response.parts:
                        if 'Thinking' in type(part).__name__:
                            current_node_parts.append({
                                "type": "thinking",
                                "content": part.content
                            })
                            yield sse_html("content", ThinkingBlock(part.content))

                    # Execute tools
                    async with node.stream(run.ctx) as handle_stream:
                        current_tool = None

                        async for event in handle_stream:
                            if isinstance(event, FunctionToolCallEvent):
                                tool_name = event.part.tool_name
                                yield sse_html("progress", ProgressIndicator(get_tool_status(tool_name)))
                                current_tool = {
                                    "tool": tool_name,
                                    "args": event.part.args,
                                    "tool_call_id": event.part.tool_call_id
                                }

                            elif isinstance(event, FunctionToolResultEvent):
                                if current_tool and event.tool_call_id == current_tool["tool_call_id"]:
                                    result_content = event.result.content
                                    attachments = []

                                    if isinstance(result_content, list):
                                        for item in result_content:
                                            if isinstance(item, BinaryContent):
                                                path = save_binary_content(user.id, chat.id, item)
                                                attachments.append({
                                                    "path": path,
                                                    "media_type": item.media_type
                                                })

                                    tool_data = {
                                        "type": "tool_call",
                                        "tool": current_tool["tool"],
                                        "args": current_tool["args"],
                                        "result": str(result_content) if not attachments else "",
                                        "attachments": attachments
                                    }
                                    current_node_parts.append(tool_data)

                                    yield sse_html("content", ToolCallBlock(
                                        current_tool["tool"],
                                        current_tool["args"],
                                        tool_data["result"],
                                        attachments
                                    ))
                                    current_tool = None

                elif Agent.is_end_node(node):
                    if current_node_parts:
                        assistant_nodes.append({"parts": current_node_parts})
                        current_node_parts = []

                    final_text = run.result.output
                    assistant_nodes.append({
                        "parts": [{"type": "text", "content": final_text}]
                    })

                    yield sse_html("content", TextBlock(final_text))

        # Save assistant message
        crud.message.create(Message(
            chat_id=chat.id,
            role='assistant',
            content={"nodes": assistant_nodes}
        ))

        yield sse_done(chat.id)

    except asyncio.CancelledError:
        pass  # Client disconnected

    except Exception as e:
        yield sse_html("content", ErrorBlock(str(e)))
        yield sse_done(chat.id, error=True)


def sse_html(event: str, component) -> str:
    """Format component as SSE event with HTML data."""
    html = to_xml(component)
    # SSE data can't have newlines, encode them
    html_escaped = html.replace('\n', '&#10;')
    return f"event: {event}\ndata: {html_escaped}\n\n"


def sse_done(chat_id: int, error: bool = False) -> str:
    """Send done event that replaces stream container and re-enables form."""
    final_container = Div(id="stream-container")  # Empty, closes SSE
    form = ChatFormEnabled()
    html = to_xml(Div(final_container, form))
    html_escaped = html.replace('\n', '&#10;')
    return f"event: done\ndata: {html_escaped}\n\n"


def get_tool_status(tool_name: str) -> str:
    return {
        "sql_query": "Running SQL query...",
        "jupyter_notebook": "Executing Python code...",
        "subject_overview": "Looking up documentation...",
        "table_docs": "Looking up table docs...",
        "view_column_values": "Checking column values...",
        "web_search": "Searching the web...",
        "memory": "Accessing memory...",
    }.get(tool_name, f"Running {tool_name}...")
```

### SSE Helpers

```python
def save_binary_content(user_id: int, chat_id: int, content: BinaryContent) -> str:
    upload_dir = Path(f"{user_id}/chat_data/{chat_id}")
    upload_dir.mkdir(parents=True, exist_ok=True)
    ext = content.media_type.split("/")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    filepath = upload_dir / filename
    filepath.write_bytes(content.data)
    return f"{user_id}/chat_data/{chat_id}/{filename}"


def build_message_history(chat: Chat) -> list[ModelMessage]:
    history = []
    for msg in chat.messages[:-1]:
        if msg.role == 'user':
            history.append(ModelRequest(parts=[
                UserPromptPart(content=msg.content['text'])
            ]))
        else:
            for node in msg.content.get('nodes', []):
                parts = []
                for part in node.get('parts', []):
                    if part['type'] == 'thinking':
                        parts.append(ThinkingPart(content=part['content']))
                    elif part['type'] == 'text':
                        parts.append(TextPart(content=part['content']))
                    elif part['type'] == 'tool_call':
                        parts.append(ToolCallPart(tool_name=part['tool'], args=part['args']))
                if parts:
                    history.append(ModelResponse(parts=parts))
    return history
```

---

## Frontend Components

### Page Structure

```python
def ChatPage(chat: Chat | None):
    messages = chat.messages if chat else []
    return Main(
        ChatHeader(chat),
        ChatMessages(messages),
        ChatForm(disabled=False),
        cls="flex flex-col h-screen"
    )
```

### Chat Messages Container

```python
def ChatMessages(messages: list[Message]):
    return Div(
        *[MessageComponent(m) for m in messages],
        Div(id="stream-container"),  # SSE content goes here
        id="chat-messages",
        cls="flex-1 overflow-y-auto px-4 py-6"
    )


def MessageComponent(message: Message):
    if message.role == 'user':
        return UserMessage(message.content['text'])
    else:
        return AssistantMessage(message.content)
```

### Stream Container (returned by /chat/send)

```python
def StreamContainer(chat_id: int):
    return Div(
        ProgressIndicator("Thinking..."),
        Div(id="streaming-content", sse_swap="content:beforeend"),
        Button(
            "Stop",
            hx_get=f"/chat/stop/{chat_id}",
            hx_target="#stream-container",
            hx_swap="outerHTML",
            cls="btn btn-error btn-sm mt-2"
        ),
        id="stream-container",
        hx_ext="sse",
        sse_connect=f"/chat/stream/{chat_id}",
        sse_swap="done:outerHTML"
    )


def ProgressIndicator(status: str):
    return Div(
        Span(cls="loading loading-dots loading-sm"),
        Span(status, cls="ml-2 text-sm text-base-content/50"),
        id="progress-indicator",
        hx_swap_oob="true",
        cls="flex items-center mb-4"
    )
```

### Chat Form

```python
def ChatForm(disabled: bool = False):
    return Form(
        Div(
            Textarea(
                id="message-input",
                name="message",
                placeholder="Ask about Danish statistics...",
                rows="1",
                disabled=disabled,
                cls="textarea textarea-bordered w-full resize-none",
            ),
            Button(
                "Send",
                type="submit",
                disabled=disabled,
                cls="btn btn-primary btn-sm"
            ),
            cls="flex gap-2 items-end"
        ),
        hx_post="/chat/send",
        hx_target="#stream-container",
        hx_swap="outerHTML",
        id="chat-form",
        cls="px-4 py-3 border-t"
    )


def ChatFormDisabled():
    """OOB swap to disable form during streaming."""
    return ChatForm(disabled=True).__ft__()  # with hx_swap_oob="true"


def ChatFormEnabled():
    """OOB swap to re-enable form after streaming."""
    return Div(
        ChatForm(disabled=False),
        hx_swap_oob="outerHTML:#chat-form"
    )
```

### Message Components

```python
def UserMessage(content: str):
    return Div(
        Div(content, cls="bg-base-200 px-4 py-3 rounded-box max-w-[85%]"),
        cls="flex justify-end mb-4"
    )


def AssistantMessage(content: dict):
    parts = []
    for node in content.get('nodes', []):
        for part in node.get('parts', []):
            if part['type'] == 'thinking':
                parts.append(ThinkingBlock(part['content']))
            elif part['type'] == 'tool_call':
                parts.append(ToolCallBlock(
                    part['tool'], part['args'],
                    part['result'], part.get('attachments', [])
                ))
            elif part['type'] == 'text':
                parts.append(TextBlock(part['content']))
    return Div(*parts, cls="mb-6")
```

### Thinking Block (Collapsible)

```python
def ThinkingBlock(content: str):
    return Div(
        Div(
            Span("▶", cls="text-xs transition-transform duration-200 mr-2",
                 **{":class": "{'rotate-90': open}"}),
            "Thinking...",
            cls="cursor-pointer text-sm text-base-content/50 flex items-center",
            **{"@click": "open = !open"}
        ),
        Div(
            content,
            cls="pl-4 border-l-2 border-base-300 mt-2 text-sm text-base-content/60 whitespace-pre-wrap",
            x_show="open",
            x_collapse=True
        ),
        x_data="{open: false}",
        cls="mb-2"
    )
```

### Tool Call Block (Collapsible)

```python
def ToolCallBlock(tool: str, args: dict, result: str, attachments: list):
    return Div(
        Div(
            Span("▶", cls="text-xs transition-transform duration-200 mr-2",
                 **{":class": "{'rotate-90': open}"}),
            f"Called {tool}",
            cls="cursor-pointer text-sm text-base-content/50 flex items-center",
            **{"@click": "open = !open"}
        ),
        Div(
            ToolArgsDisplay(tool, args),
            ToolResultDisplay(result, attachments),
            cls="pl-4 border-l-2 border-base-300 mt-2",
            x_show="open",
            x_collapse=True
        ),
        x_data="{open: false}",
        cls="mb-2"
    )


def ToolArgsDisplay(tool: str, args: dict):
    if tool == 'sql_query':
        return Div(
            Pre(Code(args.get('query', ''), cls="language-sql"),
                cls="text-xs bg-base-200 p-2 rounded overflow-x-auto"),
            Span(f"→ {args.get('df_name')}", cls="text-xs text-base-content/50")
                if args.get('df_name') else None
        )
    elif tool == 'jupyter_notebook':
        return Pre(Code(args.get('code', ''), cls="language-python"),
                   cls="text-xs bg-base-200 p-2 rounded overflow-x-auto")
    else:
        return Pre(json.dumps(args, indent=2, ensure_ascii=False),
                   cls="text-xs bg-base-200 p-2 rounded overflow-x-auto")


def ToolResultDisplay(result: str, attachments: list):
    parts = []
    if result:
        if '|' in result and '\n' in result:
            parts.append(MarkdownTable(result))
        else:
            parts.append(Pre(result, cls="text-xs overflow-x-auto mt-2"))
    for att in attachments:
        parts.append(Img(src=f"/uploads/{att['path']}", cls="max-w-full rounded mt-2"))
    return Div(*parts) if parts else None


def TextBlock(content: str):
    return Div(
        NotStr(render_markdown(content)),
        cls="prose prose-sm max-w-none mb-6"
    )


def ErrorBlock(message: str):
    return Div(
        f"Error: {message}",
        cls="text-error text-sm mb-4"
    )
```

### Header with Dropdown

```python
def ChatHeader(chat: Chat | None):
    return Header(
        Div(
            H1("Rigsstatistikeren", cls="text-xl font-semibold"),
            ChatDropdownTrigger(chat),
            cls="flex items-center gap-4"
        ),
        Button("New Chat", hx_get="/chat/new", cls="btn btn-primary btn-sm"),
        cls="flex justify-between items-center px-4 py-3 border-b"
    )


def ChatDropdownTrigger(chat: Chat | None):
    title = chat.title if chat else "New chat"
    return Div(
        Button(title, Span("▼", cls="ml-2 text-xs"), cls="btn btn-ghost btn-sm",
               **{"@click": "open = !open"}),
        Div(id="chat-dropdown", hx_get="/chat/history", hx_trigger="click from:previous",
            cls="absolute mt-2 w-64 bg-base-100 shadow-lg rounded-box z-50",
            x_show="open", **{"@click.outside": "open = false"}),
        x_data="{open: false}",
        cls="relative"
    )


def ChatDropdown(chats: list[Chat]):
    return Ul(*[ChatDropdownItem(c) for c in chats], cls="menu p-2")


def ChatDropdownItem(chat: Chat):
    return Li(Div(
        A(Span(chat.title or "Untitled", cls="truncate"),
          Span(chat.created_at.strftime("%Y-%m-%d"), cls="text-xs text-base-content/50"),
          hx_get=f"/chat/switch/{chat.id}", cls="flex flex-col"),
        Button("×", hx_delete=f"/chat/delete/{chat.id}", hx_confirm="Delete?",
               cls="btn btn-ghost btn-xs"),
        cls="flex justify-between items-center"
    ))
```

---

## Cancellation Handling

**Mechanism:** Stop button triggers `hx-get` that replaces the SSE container.

1. User clicks "Stop" button
2. `hx-get="/chat/stop/{chat_id}"` fires
3. Server returns HTML without `sse-connect` attribute
4. HTMX replaces `#stream-container`, closing the SSE connection
5. Form is re-enabled via OOB swap
6. Partial assistant message is NOT saved (generator catches `CancelledError`)

**Benefits:**
- No client-side JS needed
- Server controls all state
- Natural HTMX pattern

---

## CRUD Operations

```python
class CrudChat(CrudBase[Chat]):
    def get(self, chat_id: int | None, add_msgs: bool = False) -> Chat | None:
        if chat_id is None:
            return None
        with Session(self.engine) as session:
            query = select(Chat).where(Chat.id == chat_id)
            if add_msgs:
                query = query.options(selectinload(Chat.messages))
            return session.exec(query).first()

    def get_recent_by_user(self, user_id: int, limit: int = 10) -> list[Chat]:
        with Session(self.engine) as session:
            return session.exec(
                select(Chat)
                .where(Chat.user_id == user_id)
                .order_by(Chat.updated_at.desc())
                .limit(limit)
            ).all()


class CrudMessage(CrudBase[Message]):
    pass
```

---

## Static Files

```python
@rt("/uploads/{path:path}")
def serve_upload(path: str, user: User):
    if not path.startswith(f"{user.id}/"):
        return Response(status_code=403)
    filepath = Path(path)
    if not filepath.exists():
        return Response(status_code=404)
    return FileResponse(filepath)
```

---

## Summary

| Aspect | Decision |
|--------|----------|
| Architecture | Server renders HTML, SSE streams HTML fragments |
| Client JS | Minimal (Alpine.js for collapsibles only) |
| Data storage | Postgres JSONB + filesystem for binary |
| SSE events | `content` (append HTML), `progress` (OOB update), `done` (close stream) |
| Cancellation | Stop button replaces SSE container via hx-get |
| Form state | Server controls via OOB swaps |
| History | Dropdown with recent 10 chats |
