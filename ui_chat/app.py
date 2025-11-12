import chainlit as cl
from varro.agent.memory import SessionStore
from varro.chat.message import assistant_msg
from varro.db import crud


# ────────────────────────────  Chat lifecycle  ───────────────────── #
@cl.on_chat_start
async def start():
    email = cl.user_session.get("user").identifier
    user = crud.user.get_with_plans(email=email)

    cl.user_session.set("message_history", [])
    cl.user_session.set("session_store", SessionStore(user=user))


@cl.on_message
async def assistant_handler(msg: cl.Message):
    await assistant_msg(msg.content)


@cl.on_chat_end
async def on_chat_end():
    # Gracefully stop the kernel if it exists
    store: SessionStore = cl.user_session.get("session_store")
    if store and getattr(store, "jupyter", None):
        try:
            store.jupyter.stop()

        except Exception:
            pass


if __name__ == "__main__":
    from chainlit.cli import run_chainlit
    import os

    os.environ["CHAINLIT_PORT"] = "8026"

    run_chainlit(__file__)
