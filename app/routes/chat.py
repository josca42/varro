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
    ErrorBlock,
)
from varro.chat.session import sessions
from varro.chat.agent_run import run_agent
from varro.db.crud.chat import CrudChat
from varro.db.models import Chat
from varro.db import crud

ar = APIRouter()


async def on_conn(ws, send, sess, req):
    """Called when websocket connects."""
    user_id = sess.get("user_id")
    chats = crud.chat.for_user(user_id)
    session = sessions.create(user_id, chats, send)

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
    s = sessions.get(sess["user_id"])
    if not s:
        return

    if chat_id is None:
        chat = s.chats.create(Chat())
        chat_id = chat.id
        sess["chat_id"] = chat_id

    if edit_idx is not None:
        s.delete_from_idx(edit_idx)

    if s.chat_id != chat_id:
        await s.start_chat(chat_id)

    await s.send(ChatFormDisabled())
    try:
        async for html in run_agent(msg, s):
            await s.send(Div(html, hx_swap_oob="beforeend:#chat-messages"))
    except Exception:
        await s.send(
            Div(
                ErrorBlock("Something went wrong. Please try again."),
                hx_swap_oob="beforeend:#chat-messages",
            )
        )
    finally:
        await s.send(ChatFormEnabled())


@ar.get("/chat")
def chat_page(req, sess):
    """Render the main chat page."""
    chat_id = sess.get("chat_id")
    chat = req.state.chats.get(chat_id, with_turns=True) if chat_id else None
    return ChatPage(chat)


@ar.get("/chat/new")
def chat_new(sess):
    """Start a new chat."""
    sess.pop("chat_id", None)
    return RedirectResponse("/chat", status_code=303)


@ar.get("/chat/switch/{chat_id}")
async def chat_switch(chat_id: int, req, sess):
    """Switch to a different chat."""
    chat = req.state.chats.get(chat_id)
    if not chat:
        return Response(status_code=404)

    sess["chat_id"] = chat_id

    if session := sessions.get(sess["user_id"]):
        await session.start_chat(chat_id)

    return RedirectResponse("/chat", status_code=303)


@ar.get("/chat/history")
def chat_history(req):
    """Get recent chat history for dropdown."""
    return ChatDropdown(req.state.chats.get_recent(limit=10))


@ar.delete("/chat/delete/{chat_id}")
def chat_delete(chat_id: int, req, sess):
    """Delete a chat."""
    chat = req.state.chats.get(chat_id)
    if not chat:
        return Response(status_code=404)

    req.state.chats.delete(chat)

    if sess.get("chat_id") == chat_id:
        sess.pop("chat_id", None)

    return Response(status_code=200)
