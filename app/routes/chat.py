from __future__ import annotations

from pathlib import Path
from urllib.parse import parse_qs

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
    ChatMessages,
)
from varro.chat.session import sessions
from varro.chat.agent_run import run_agent
from varro.db.models import Chat
from varro.db import crud

ar = APIRouter()


async def on_conn(ws, send, sess, req):
    """Called when websocket connects."""
    user_id = sess.get("user_id")
    sid = None
    if req is not None and getattr(req, "query_params", None) is not None:
        sid = req.query_params.get("sid")
    if not sid and getattr(ws, "query_params", None) is not None:
        sid = ws.query_params.get("sid")
    if not sid:
        qs = ws.scope.get("query_string", b"").decode()
        sid = parse_qs(qs).get("sid", [None])[0]
    if not sid:
        await ws.close()
        return
    chats = crud.chat.for_user(user_id)
    session = await sessions.create(user_id, sid, chats, send, ws)
    session.touch()

    chat_id = sess.get("chat_id")
    if chat_id:
        await session.start_chat(chat_id)


def on_disconn(ws, sess):
    """Called when websocket disconnects."""
    if session := sessions.find_by_ws(sess["user_id"], ws):
        sessions.remove(sess["user_id"], session.sid)


@ar.ws("/ws", conn=on_conn, disconn=on_disconn)
async def on_message(
    msg: str,
    sess,
    chat_id: int | None = None,
    edit_idx: int | None = None,
    sid: str | None = None,
):
    """
    Handle incoming chat messages.

    Args:
        msg: The user's message text
        chat_id: The chat ID (may be None for new chat)
        edit_idx: If provided, delete turns from this index before processing
    """
    if not sid:
        return
    s = sessions.get(sess["user_id"], sid)
    if not s:
        return
    s.touch()

    if chat_id is None:
        chat = s.chats.create(Chat())
        chat_id = chat.id
        sess["chat_id"] = chat_id

    if s.chat_id != chat_id:
        await s.start_chat(chat_id)

    if edit_idx is not None:
        s.delete_from_idx(edit_idx)
        chat = s.chats.get(s.chat_id, with_turns=True)
        if chat:
            await s.send(
                ChatMessages(
                    chat.turns, shell=s.shell, hx_swap_oob="outerHTML:#chat-messages"
                )
            )

    await s.send(ChatFormDisabled(chat_id))

    async for block in run_agent(msg, s):
        await s.send(Div(block, hx_swap_oob="beforeend:#chat-messages"))

    await s.send(ChatFormEnabled(chat_id))


@ar.get("/chat")
def chat_page(req, sess):
    """Render the main chat page."""
    chat_id = sess.get("chat_id")
    chat = req.state.chats.get(chat_id, with_turns=True) if chat_id else None
    return ChatPage(chat, shell=None)


@ar.post("/chat/heartbeat")
def chat_heartbeat(sid: str, sess):
    sessions.touch(sess.get("user_id"), sid)
    return Response(status_code=204)


@ar.post("/chat/close")
async def chat_close(sid: str, sess):
    await sessions.close_and_remove(sess.get("user_id"), sid)
    return Response(status_code=204)


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
    return RedirectResponse("/chat", status_code=303)


@ar.get("/chat/history")
def chat_history(req):
    """Get recent chat history for dropdown."""
    return ChatDropdown(req.state.chats.get_recent(limit=10))


@ar.delete("/chat/delete/{chat_id}")
def chat_delete(chat_id: int, req, sess):
    """Delete a chat."""
    chat = req.state.chats.get(chat_id, with_turns=True)
    if not chat:
        return Response(status_code=404)

    turn_paths = [Path(turn.obj_fp) for turn in chat.turns]

    req.state.chats.delete(chat)

    if sess.get("chat_id") == chat_id:
        sess.pop("chat_id", None)

    for path in turn_paths:
        if path.exists():
            path.unlink()

    return Response(status_code=200)
