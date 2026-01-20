from __future__ import annotations

import asyncio
import json
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
from pydantic_ai import ModelMessagesTypeAdapter
from pydantic_ai.messages import (
    ModelMessage,
    ModelResponse,
    BaseToolCallPart,
    ThinkingPart,
    PartStartEvent,
    FunctionToolCallEvent,
    FunctionToolResultEvent,
)
from pydantic_core import to_jsonable_python

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
    history = build_message_history(chat)
    for msg in history:
        if not isinstance(msg, ModelResponse):
            continue
        for part in msg.parts:
            if not isinstance(part, BaseToolCallPart):
                continue

            tool = part.tool_name
            if tool not in {"sql_query", "jupyter_notebook"}:
                continue

            args = part.args or {}
            if isinstance(args, str):
                args = json.loads(args)

            if tool == "sql_query":
                sql_query(ctx, args.get("query", ""), args.get("df_name"))
            elif tool == "jupyter_notebook":
                await jupyter_notebook(
                    ctx, args.get("code", ""), args.get("show", [])
                )


def build_message_history(chat: Chat) -> list[ModelMessage]:
    history: list[ModelMessage] = []
    for msg in chat.messages or []:
        stored = msg.content.get("pydantic_messages")
        if stored:
            history.extend(ModelMessagesTypeAdapter.validate_python(stored))
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

    attachments_map = {}

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
                    for part in node.model_response.parts:
                        if isinstance(part, ThinkingPart):
                            yield sse_html("content", ThinkingBlock(part.content))

                    async with node.stream(run.ctx) as handle_stream:
                        current_tool = None
                        async for event in handle_stream:
                            if isinstance(event, FunctionToolCallEvent):
                                tool_name = event.part.tool_name
                                args = event.part.args or {}
                                if isinstance(args, str):
                                    args = json.loads(args)
                                yield sse_html(
                                    "progress", ProgressIndicator(get_tool_status(tool_name))
                                )
                                current_tool = {
                                    "tool": tool_name,
                                    "args": args,
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

                                if attachments:
                                    attachments_map[current_tool["tool_call_id"]] = (
                                        attachments
                                    )

                                result_text = ""
                                if isinstance(result_content, list):
                                    result_text = "\n".join(
                                        str(item)
                                        for item in result_content
                                        if not isinstance(item, BinaryContent)
                                    )
                                elif result_content is not None:
                                    result_text = str(result_content)

                                yield sse_html(
                                    "content",
                                    ToolCallBlock(
                                        current_tool["tool"],
                                        current_tool["args"],
                                        result_text,
                                        attachments,
                                    ),
                                )
                                current_tool = None

                elif Agent.is_end_node(node):
                    final_text = run.result.output if run.result else ""

                    yield sse_html("content", TextBlock(final_text))

        stored_messages = []
        if run.result:
            stored_messages = to_jsonable_python(run.result.new_messages())

        crud.message.create(
            Message(
                chat_id=chat.id,
                role="assistant",
                content={
                    "pydantic_messages": stored_messages,
                    "attachments": attachments_map,
                },
            )
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
