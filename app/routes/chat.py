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
    ChatPanel,
    ChatFormDisabled,
    ChatFormEnabled,
    ChatDropdown,
    ChatMessages,
    ChatProgressStart,
    ChatProgressEnd,
)
from varro.chat.session import sessions
from varro.chat.agent_run import run_agent
from varro.db.models import Chat
from varro.db import crud

ar = APIRouter()


async def on_conn(ws, send, sess, req):
    """Called when websocket connects."""
    user_id = sess.get("user_id")

    # Extract sid from query params (try multiple sources)
    sid = (
        getattr(req, "query_params", {}).get("sid")
        or getattr(ws, "query_params", {}).get("sid")
        or parse_qs(ws.scope.get("query_string", b"").decode()).get("sid", [None])[0]
    )
    if not sid:
        await ws.close()
        return

    chats = crud.chat.for_user(user_id)
    session = await sessions.create(user_id, sid, chats, send, ws)
    session.touch()

    if chat_id := sess.get("chat_id"):
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
    await s.send(ChatProgressStart())

    async for block in run_agent(msg, s):
        attrs = getattr(block, "attrs", None)
        if isinstance(attrs, dict) and "hx-swap-oob" in attrs:
            await s.send(block)
        else:
            await s.send(Div(block, hx_swap_oob="beforebegin:#chat-progress"))

    await s.send(ChatProgressEnd())
    await s.send(ChatFormEnabled(chat_id))


@ar.get("/chat")
def chat_page():
    return RedirectResponse("/", status_code=303)


@ar.post("/chat/heartbeat")
def chat_heartbeat(sid: str, sess):
    sessions.touch(sess.get("user_id"), sid)
    return Response(status_code=204)


@ar.post("/chat/close")
async def chat_close(sid: str, sess):
    await sessions.close_and_remove(sess.get("user_id"), sid)
    return Response(status_code=204)


@ar.get("/chat/new")
def chat_new(req, sess):
    """Start a new chat."""
    sess.pop("chat_id", None)
    return ChatPanel(None, shell=None, hx_swap_oob="outerHTML:#chat-panel")


@ar.get("/chat/switch/{chat_id}")
def chat_switch(chat_id: int, req, sess):
    """Switch to a different chat."""
    chat = req.state.chats.get(chat_id, with_turns=True)
    if not chat:
        return Response(status_code=404)
    sess["chat_id"] = chat_id
    return ChatPanel(chat, shell=None, hx_swap_oob="outerHTML:#chat-panel")


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
