import shutil
from datetime import datetime
from pathlib import Path
from fasthtml.common import (
    APIRouter,
    Div,
    Response,
    StreamingResponse,
    RedirectResponse,
    FileResponse,
)
from varro.chat.session import ChatSession
from varro.chat.streaming import agent_html_stream
from ui.app import (
    ChatPage,
    UserMessage,
    StreamContainer,
    ChatFormDisabled,
    ChatFormEnabled,
    ChatDropdown,
)
from varro.db import crud
from varro.db.models.chat import Chat
from varro.db.models.user import User

ar = APIRouter()


def get_user(auth) -> User | None:
    if not auth:
        return None
    return crud.user.get(auth)


@ar("/chat", methods=["GET"])
def chat_page(sess, auth):
    user = get_user(auth)
    if not user:
        return Response(status_code=403)

    chat_id = sess.get("chat_id")
    chat = crud.chat.get(chat_id, with_msgs=True)
    if chat and chat.user_id != user.id:
        sess["chat_id"] = None
        chat = None
    return ChatPage(chat)


@ar("/chat/send", methods=["POST"])
def chat_send(sess, auth, message: str):
    user = get_user(auth)
    if not user:
        return Response(status_code=403)

    session = ChatSession(user, sess.get("chat_id"))
    session.ensure_chat(title=message)
    session.add_user_message(message)
    sess["chat_id"] = session.chat_id

    return Div(
        UserMessage(message),
        StreamContainer(session.chat_id),
        ChatFormDisabled(),
        id="message-area",
    )


@ar("/chat/stream/{chat_id}")
async def chat_stream(sess, auth, chat_id: int):
    user = get_user(auth)
    if not user:
        return Response(status_code=403)

    session = ChatSession(user, chat_id)
    chat = await session.start()
    if not chat:
        return Response(status_code=403)

    return StreamingResponse(
        agent_html_stream(session),
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
