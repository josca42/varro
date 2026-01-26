from __future__ import annotations

from fasthtml.common import (
    APIRouter,
    Div,
    Response,
    RedirectResponse,
)

from ui.app.chat import (
    ChatPage,
    ChatFormDisabled,
    ChatFormEnabled,
    ChatDropdown,
)
from varro.chat.session import sessions
from varro.chat.agent_run import run_agent
from varro.db.crud.chat import CrudChat
from varro.db.models import Chat, User
from varro.db import crud

ar = APIRouter()


async def on_conn(ws, send, sess, user: User, chats: CrudChat):
    """Called when websocket connects."""
    session = sessions.create(user, chats, send)

    chat_id = sess.get("chat_id")
    if chat_id:
        await session.start_chat(chat_id)


def on_disconn(ws, sess):
    """Called when websocket disconnects."""
    sessions.remove(sess["user_id"])


@ar.ws("/ws", conn=on_conn, disconn=on_disconn)
async def on_message(msg: str, chat_id: int | None, edit_idx: int | None, sess):
    """
    Handle incoming chat messages.

    Args:
        msg: The user's message text
        chat_id: The chat ID (may be None for new chat)
        edit_idx: If provided, delete turns from this index before processing
    """
    session = sessions.get(sess["user_id"])
    if not session:
        return

    if chat_id is None:
        chat = session.chats.create(Chat(user_id=sess["user_id"]))
        chat_id = chat.id
        sess["chat_id"] = chat_id

    if edit_idx is not None:
        session.delete_from_idx(edit_idx)

    if session.chat_id != chat_id:
        await session.start_chat(chat_id)

    await session.send(ChatFormDisabled())

    async for html in run_agent(msg, session):
        await session.send(
            Div(html, hx_swap_oob="beforeend:#chat-messages")
        )

    await session.send(ChatFormEnabled())


@ar.get("/chat")
def chat_page(sess, chats: CrudChat):
    """Render the main chat page."""
    chat_id = sess.get("chat_id")
    chat = chats.get(chat_id, with_turns=True) if chat_id else None
    return ChatPage(chat)


@ar.get("/chat/new")
def chat_new(sess):
    """Start a new chat."""
    sess.pop("chat_id", None)
    return RedirectResponse("/chat", status_code=303)


@ar.get("/chat/switch/{chat_id}")
async def chat_switch(chat_id: int, sess, chats: CrudChat):
    """Switch to a different chat."""
    chat = chats.get(chat_id)
    if not chat:
        return Response(status_code=404)

    sess["chat_id"] = chat_id

    if session := sessions.get(sess["user_id"]):
        await session.start_chat(chat_id)

    return RedirectResponse("/chat", status_code=303)


@ar.get("/chat/history")
def chat_history(chats: CrudChat):
    """Get recent chat history for dropdown."""
    return ChatDropdown(chats.get_recent(limit=10))


@ar.delete("/chat/delete/{chat_id}")
def chat_delete(chat_id: int, sess, chats: CrudChat):
    """Delete a chat."""
    chat = chats.get(chat_id)
    if not chat:
        return Response(status_code=404)

    chats.delete(chat)

    if sess.get("chat_id") == chat_id:
        sess.pop("chat_id", None)

    return Response(status_code=200)
