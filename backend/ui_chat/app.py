import chainlit as cl
from varro.agent.memory import SessionStore
from varro.chat.message import assistant_msg
from varro.db import crud, models
from chainlit.data.sql_alchemy import SQLAlchemyDataLayer
from varro.db.db import CHAINLIT_DSN
from varro.chat.postgres_storage_client import PostgresStorageClient


# ────────────────────────────  Chat lifecycle  ───────────────────── #
@cl.on_chat_start
async def start():
    cl_user = cl.user_session.get("user")
    db_user = crud.user.get_by_email(cl_user.identifier)
    if not db_user:
        db_user = crud.user.create(
            models.User(email=cl_user.identifier, name=cl_user.identifier)
        )
    cl.user_session.set("message_history", [])
    cl.user_session.set("session_store", SessionStore(user=db_user))


@cl.password_auth_callback
def auth_callback(username: str, password: str):
    db_user = crud.user.authenticate(username, password)
    if db_user:
        return cl.User(identifier=db_user.email, metadata={"db_user_id": db_user.id})
    return None


@cl.data_layer
def get_data_layer():
    return SQLAlchemyDataLayer(
        conninfo=CHAINLIT_DSN, storage_provider=PostgresStorageClient()
    )


@cl.on_message
async def assistant_handler(msg: cl.Message):
    await assistant_msg(msg.content)


@cl.on_chat_end
async def on_chat_end():
    # Gracefully stop resources
    store = cl.user_session.get("session_store")
    store.cleanup()


if __name__ == "__main__":
    from chainlit.cli import run_chainlit
    import os

    os.environ["CHAINLIT_PORT"] = "8026"

    run_chainlit(__file__)
