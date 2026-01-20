from __future__ import annotations

import asyncio
import shutil
import uuid
from pathlib import Path
from types import SimpleNamespace
from datetime import datetime

from fasthtml.common import (
    APIRouter,
    Div,
    Response,
    StreamingResponse,
    RedirectResponse,
    FileResponse,
    to_xml,
)
from pydantic_ai import Agent, BinaryContent
from pydantic_ai.messages import (
    ModelMessage,
    ModelRequest,
    ModelResponse,
    UserPromptPart,
    ThinkingPart,
    TextPart,
    ToolCallPart,
    PartStartEvent,
    FunctionToolCallEvent,
    FunctionToolResultEvent,
)

from ui.app import (
    ChatPage,
    UserMessage,
    StreamContainer,
    ChatFormDisabled,
    ChatFormEnabled,
    ProgressIndicator,
    ErrorBlock,
    ThinkingBlock,
    ToolCallBlock,
    TextBlock,
    ChatDropdown,
)
from varro.agent.assistant import agent, sql_query, jupyter_notebook
from varro.agent.memory import SessionStore
from varro.db import crud
from varro.db.models.chat import Chat, Message
from varro.db.models.user import User

ar = APIRouter()


def get_user(auth) -> User | None:
    if not auth:
        return None
    return crud.user.get(auth)


def sort_messages(chat: Chat) -> None:
    if not chat.messages:
        return
    chat.messages = sorted(
        chat.messages,
        key=lambda m: (m.created_at or datetime.min, m.id or 0),
    )


@ar("/chat", methods=["GET"])
def chat_page(sess, auth):
    user = get_user(auth)
    if not user:
        return Response(status_code=403)

    chat_id = sess.get("chat_id")
    chat = crud.chat.get(chat_id, add_msgs=True)
    if chat and chat.user_id != user.id:
        sess["chat_id"] = None
        chat = None
    if chat:
        sort_messages(chat)

    return ChatPage(chat)


@ar("/chat/send", methods=["POST"])
def chat_send(sess, auth, message: str):
    user = get_user(auth)
    if not user:
        return Response(status_code=403)

    chat_id = sess.get("chat_id")
    chat = crud.chat.get(chat_id) if chat_id else None
    if not chat or chat.user_id != user.id:
        chat = crud.chat.create(Chat(user_id=user.id, title=message[:30]))
        chat_id = chat.id
        sess["chat_id"] = chat_id

    crud.message.create(
        Message(chat_id=chat_id, role="user", content={"text": message})
    )
    crud.chat.update(Chat(id=chat_id, updated_at=datetime.utcnow()))

    return Div(
        UserMessage(message),
        StreamContainer(chat_id),
        ChatFormDisabled(),
        id="message-area",
    )


@ar("/chat/stream/{chat_id}")
async def chat_stream(sess, auth, chat_id: int):
    user = get_user(auth)
    if not user:
        return Response(status_code=403)

    chat = crud.chat.get(chat_id, add_msgs=True)
    if not chat or chat.user_id != user.id:
        return Response(status_code=403)

    sort_messages(chat)

    return StreamingResponse(
        agent_html_stream(chat, user),
        media_type="text/event-stream",
    )


@ar("/chat/stop/{chat_id}")
def chat_stop(sess, auth, chat_id: int):
    user = get_user(auth)
    if not user:
        return Response(status_code=403)

    return Div(
        Div(id="stream-container"),
        ChatFormEnabled(),
    )


@ar("/chat/new")
def chat_new(sess):
    sess["chat_id"] = None
    return RedirectResponse("/chat", status_code=303)


@ar("/chat/switch/{chat_id}")
def chat_switch(sess, auth, chat_id: int):
    user = get_user(auth)
    if not user:
        return Response(status_code=403)

    chat = crud.chat.get(chat_id)
    if chat and chat.user_id == user.id:
        sess["chat_id"] = chat_id
    return RedirectResponse("/chat", status_code=303)


@ar("/chat/delete/{chat_id}")
def chat_delete(sess, auth, chat_id: int):
    user = get_user(auth)
    if not user:
        return Response(status_code=403)

    chat = crud.chat.get(chat_id)
    if chat and chat.user_id == user.id:
        upload_dir = Path(f"{user.id}/chat_data/{chat_id}")
        if upload_dir.exists():
            shutil.rmtree(upload_dir)
        crud.chat.delete(chat)
        if sess.get("chat_id") == chat_id:
            sess["chat_id"] = None
    return RedirectResponse("/chat", status_code=303)


@ar("/chat/history")
def chat_history(auth):
    user = get_user(auth)
    if not user:
        return Response(status_code=403)

    chats = crud.chat.get_recent_by_user(user.id, limit=10)
    return ChatDropdown(chats)


@ar("/uploads/{path:path}")
def serve_upload(path: str, auth):
    user = get_user(auth)
    if not user:
        return Response(status_code=403)

    if not path.startswith(f"{user.id}/"):
        return Response(status_code=403)

    filepath = Path(path)
    if not filepath.exists():
        return Response(status_code=404)
    return FileResponse(filepath)


async def restore_session_store(chat: Chat, deps: SessionStore):
    ctx = SimpleNamespace(deps=deps)
    for msg in chat.messages:
        if msg.role != "assistant":
            continue
        for node in msg.content.get("nodes", []):
            for part in node.get("parts", []):
                if part.get("type") != "tool_call":
                    continue

                tool = part.get("tool")
                args = part.get("args", {})

                if tool == "sql_query":
                    sql_query(ctx, args.get("query", ""), args.get("df_name"))
                elif tool == "jupyter_notebook":
                    await jupyter_notebook(
                        ctx, args.get("code", ""), args.get("show", [])
                    )


def build_message_history(chat: Chat) -> list[ModelMessage]:
    history: list[ModelMessage] = []
    messages = chat.messages[:-1] if chat.messages else []

    for msg in messages:
        if msg.role == "user":
            history.append(
                ModelRequest(parts=[UserPromptPart(content=msg.content.get("text", ""))])
            )
        else:
            for node in msg.content.get("nodes", []):
                parts = []
                for part in node.get("parts", []):
                    if part.get("type") == "thinking":
                        parts.append(ThinkingPart(content=part.get("content", "")))
                    elif part.get("type") == "text":
                        parts.append(TextPart(content=part.get("content", "")))
                    elif part.get("type") == "tool_call":
                        parts.append(
                            ToolCallPart(
                                tool_name=part.get("tool", ""),
                                args=part.get("args", {}),
                            )
                        )
                if parts:
                    history.append(ModelResponse(parts=parts))
    return history


async def agent_html_stream(chat: Chat, user: User):
    deps = SessionStore(user=user)

    if chat.messages and len(chat.messages) > 1:
        yield sse_html("progress", ProgressIndicator("Restoring session..."))
        try:
            await restore_session_store(chat, deps)
        except Exception as e:
            yield sse_html("content", ErrorBlock(f"Failed to restore session: {e}"))
            yield sse_done(chat.id, error=True)
            return

    message_history = build_message_history(chat)
    user_msg = chat.messages[-1].content.get("text", "") if chat.messages else ""

    assistant_nodes = []
    current_node_parts = []

    try:
        async with agent.iter(
            user_msg, deps=deps, message_history=message_history
        ) as run:
            async for node in run:
                if Agent.is_model_request_node(node):
                    yield sse_html("progress", ProgressIndicator("Thinking..."))
                    async with node.stream(run.ctx) as request_stream:
                        async for event in request_stream:
                            if isinstance(event, PartStartEvent) and isinstance(
                                event.part, ThinkingPart
                            ):
                                yield sse_html(
                                    "progress", ProgressIndicator("Reasoning...")
                                )

                elif Agent.is_call_tools_node(node):
                    if current_node_parts:
                        assistant_nodes.append({"parts": current_node_parts})
                        current_node_parts = []

                    for part in node.model_response.parts:
                        if isinstance(part, ThinkingPart):
                            current_node_parts.append(
                                {"type": "thinking", "content": part.content}
                            )
                            yield sse_html("content", ThinkingBlock(part.content))

                    async with node.stream(run.ctx) as handle_stream:
                        current_tool = None
                        async for event in handle_stream:
                            if isinstance(event, FunctionToolCallEvent):
                                tool_name = event.part.tool_name
                                yield sse_html(
                                    "progress", ProgressIndicator(get_tool_status(tool_name))
                                )
                                current_tool = {
                                    "tool": tool_name,
                                    "args": event.part.args,
                                    "tool_call_id": event.part.tool_call_id,
                                }

                            elif isinstance(event, FunctionToolResultEvent):
                                if not current_tool:
                                    continue
                                if event.tool_call_id != current_tool["tool_call_id"]:
                                    continue

                                result_content = event.result.content
                                attachments = []

                                if isinstance(result_content, list):
                                    for item in result_content:
                                        if isinstance(item, BinaryContent):
                                            path = save_binary_content(
                                                user.id, chat.id, item
                                            )
                                            attachments.append(
                                                {
                                                    "path": path,
                                                    "media_type": item.media_type,
                                                }
                                            )

                                tool_data = {
                                    "type": "tool_call",
                                    "tool": current_tool["tool"],
                                    "args": current_tool["args"],
                                    "result": str(result_content)
                                    if not attachments
                                    else "",
                                    "attachments": attachments,
                                }
                                current_node_parts.append(tool_data)

                                yield sse_html(
                                    "content",
                                    ToolCallBlock(
                                        current_tool["tool"],
                                        current_tool["args"],
                                        tool_data["result"],
                                        attachments,
                                    ),
                                )
                                current_tool = None

                elif Agent.is_end_node(node):
                    if current_node_parts:
                        assistant_nodes.append({"parts": current_node_parts})
                        current_node_parts = []

                    final_text = run.result.output if run.result else ""
                    assistant_nodes.append(
                        {"parts": [{"type": "text", "content": final_text}]}
                    )

                    yield sse_html("content", TextBlock(final_text))

        crud.message.create(
            Message(chat_id=chat.id, role="assistant", content={"nodes": assistant_nodes})
        )

        yield sse_done(chat.id)

    except asyncio.CancelledError:
        pass

    except Exception as e:
        yield sse_html("content", ErrorBlock(str(e)))
        yield sse_done(chat.id, error=True)


def sse_html(event: str, component) -> str:
    html = to_xml(component)
    html_escaped = html.replace("\n", "&#10;")
    return f"event: {event}\ndata: {html_escaped}\n\n"


def sse_done(chat_id: int, error: bool = False) -> str:
    final_container = Div(id="stream-container")
    form = ChatFormEnabled()
    html = to_xml(Div(final_container, form))
    html_escaped = html.replace("\n", "&#10;")
    return f"event: done\ndata: {html_escaped}\n\n"


def save_binary_content(user_id: int, chat_id: int, content: BinaryContent) -> str:
    upload_dir = Path(f"{user_id}/chat_data/{chat_id}")
    upload_dir.mkdir(parents=True, exist_ok=True)
    ext = content.media_type.split("/")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    filepath = upload_dir / filename
    filepath.write_bytes(content.data)
    return f"{user_id}/chat_data/{chat_id}/{filename}"


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
