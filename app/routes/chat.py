from __future__ import annotations

import asyncio
from uuid import uuid4

from fasthtml.common import APIRouter, Div, EventStream, RedirectResponse, Response

from ui.app.chat import (
    ChatDropdown,
    ChatFormEnabled,
    ChatFormRunning,
    ChatPanel,
    ChatProgressEnd,
    ChatProgressStart,
    ChatRunStream,
    ErrorBlock,
)
from varro.chat.run_manager import run_manager
from varro.chat.runtime_state import runtime_state_fp
from varro.chat.shell_pool import shell_pool, shell_snapshot_fp
from varro.config import DATA_DIR
from varro.db import crud
from varro.db.models import Chat

ar = APIRouter()


def _chat_artifact_paths(chat, user_id: int):
    turn_paths = [DATA_DIR / turn.obj_fp for turn in chat.turns]
    cache_paths = [path.with_suffix(".cache.json") for path in turn_paths]
    state_path = runtime_state_fp(user_id, chat.id)
    snapshot_path = shell_snapshot_fp(user_id, chat.id)
    return turn_paths, cache_paths, state_path, snapshot_path


def _delete_chat_with_artifacts(chats, chat, user_id: int) -> None:
    turn_paths, cache_paths, state_path, snapshot_path = _chat_artifact_paths(chat, user_id)
    chats.delete(chat)
    for path in turn_paths:
        path.unlink(missing_ok=True)
    for path in cache_paths:
        path.unlink(missing_ok=True)
    state_path.unlink(missing_ok=True)
    snapshot_path.unlink(missing_ok=True)


def _stream_block(block):
    attrs = getattr(block, "attrs", None)
    if isinstance(attrs, dict) and "hx-swap-oob" in attrs:
        return block
    return Div(block, hx_swap_oob="beforebegin:#chat-progress")


async def _publish_blocks(run_id: str, *blocks) -> None:
    for block in blocks:
        if block is None:
            continue
        await run_manager.publish(run_id, _stream_block(block))


async def _execute_run(
    *,
    run_id: str,
    user_id: int,
    chat_id: int,
    msg: str,
    current_url: str | None,
) -> None:
    from varro.chat.agent_run import run_agent

    chats = crud.chat.for_user(user_id)
    request_url = (current_url or "").strip()

    try:
        async with shell_pool.lease(user_id=user_id, chat_id=chat_id) as shell:
            async for block in run_agent(
                msg,
                user_id=user_id,
                chats=chats,
                shell=shell,
                chat_id=chat_id,
                current_url=request_url,
            ):
                await run_manager.publish(run_id, _stream_block(block))

        await _publish_blocks(
            run_id,
            ChatProgressEnd(),
            ChatFormEnabled(chat_id),
        )
    except asyncio.CancelledError:
        await _publish_blocks(
            run_id,
            ChatProgressEnd(),
            ChatFormEnabled(chat_id),
        )
    except Exception as exc:
        await shell_pool.invalidate(user_id, chat_id)
        await _publish_blocks(
            run_id,
            ErrorBlock(str(exc)),
            ChatProgressEnd(),
            ChatFormEnabled(chat_id),
        )
    finally:
        await run_manager.close(run_id)


@ar.post("/chat/runs")
async def chat_run_start(
    msg: str,
    sess,
    req,
    chat_id: int | None = None,
    current_url: str | None = None,
):
    msg = (msg or "").strip()
    if not msg:
        return Response(status_code=400)

    user_id = sess.get("user_id")
    if user_id is None:
        return Response(status_code=403)

    chats = req.state.chats
    if chat_id is None:
        chat = chats.create(Chat())
        chat_id = chat.id
    elif not chats.get(chat_id):
        return Response(status_code=404)

    run_id = uuid4().hex
    run = await run_manager.create_run(
        run_id=run_id,
        user_id=user_id,
        chat_id=chat_id,
    )
    if run is None:
        return Response(status_code=409)

    sess["chat_id"] = chat_id
    task = asyncio.create_task(
        _execute_run(
            run_id=run_id,
            user_id=user_id,
            chat_id=chat_id,
            msg=msg,
            current_url=current_url,
        )
    )
    await run_manager.attach_task(run_id, task)

    return (
        ChatFormRunning(chat_id, run_id),
        ChatProgressStart(),
        ChatRunStream(run_id, hx_swap_oob="outerHTML:#chat-run-stream"),
    )


@ar.get("/chat/runs/{run_id}/stream")
async def chat_run_stream(run_id: str, sess):
    user_id = sess.get("user_id")
    if user_id is None:
        return Response(status_code=404)

    stream = await run_manager.stream_for_user(run_id=run_id, user_id=user_id)
    if stream is None:
        return Response(status_code=404)

    return EventStream(stream)


@ar.post("/chat/runs/{run_id}/cancel")
async def chat_run_cancel(run_id: str, sess):
    user_id = sess.get("user_id")
    if user_id is None:
        return Response(status_code=404)

    run = await run_manager.get_for_user(run_id, user_id)
    if run is None:
        return Response(status_code=404)

    sess["chat_id"] = run.chat_id
    await run_manager.cancel(run_id)
    return Response(status_code=204)

@ar.get("/chat")
def chat_page():
    return RedirectResponse("/", status_code=303)


@ar.get("/chat/new")
def chat_new(req, sess):
    sess.pop("chat_id", None)
    return ChatPanel(None, shell=None, hx_swap_oob="outerHTML:#chat-panel")


@ar.get("/chat/switch/{chat_id}")
def chat_switch(chat_id: int, req, sess):
    chat = req.state.chats.get(chat_id, with_turns=True)
    if not chat:
        return Response(status_code=404)
    sess["chat_id"] = chat_id
    return ChatPanel(chat, shell=None, hx_swap_oob="outerHTML:#chat-panel")


@ar.get("/chat/history")
def chat_history(req):
    return ChatDropdown(req.state.chats.get_recent(limit=10))


@ar.delete("/chat/delete/{chat_id}")
async def chat_delete(chat_id: int, req, sess):
    chat = req.state.chats.get(chat_id, with_turns=True)
    if not chat:
        return Response(status_code=404)

    user_id = sess.get("user_id") or chat.user_id
    _delete_chat_with_artifacts(req.state.chats, chat, user_id)
    await shell_pool.remove_chat(user_id, chat_id)

    if sess.get("chat_id") == chat_id:
        sess.pop("chat_id", None)

    return Response(status_code=200)
