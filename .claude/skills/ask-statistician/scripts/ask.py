from __future__ import annotations

import argparse
import asyncio
from uuid import uuid4

from varro.chat.agent_run import run_agent
from varro.chat.shell_pool import shell_pool
from varro.chat.turn_store import load_turn_messages
from varro.config import DATA_DIR
from varro.db import crud
from varro.playground.cli import _create_or_resume_chat, _collect_turn_outcome


async def _run(user_id: int, chat_id: int | None, message: str, current_url: str):
    chat_id = _create_or_resume_chat(user_id, chat_id)
    chats = crud.chat.for_user(user_id)

    try:
        async with shell_pool.lease(user_id=user_id, chat_id=chat_id) as shell:
            async for _ in run_agent(
                message,
                user_id=user_id,
                chats=chats,
                shell=shell,
                chat_id=chat_id,
                run_id=f"ask-{uuid4().hex}",
                current_url=current_url,
            ):
                pass
    except Exception:
        await shell_pool.invalidate(user_id, chat_id)
        raise

    chat = chats.get(chat_id, with_turns=True)
    if not chat or not chat.turns:
        raise ValueError("No turn was persisted.")

    turn = chat.turns[-1]
    msgs = load_turn_messages(DATA_DIR / turn.obj_fp)
    response, next_url = _collect_turn_outcome(msgs, current_url)

    print(f"chat_id: {chat_id}")
    print(f"current_url: {next_url}")
    print(f"response: {response}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("message")
    parser.add_argument("--user-id", type=int, default=1)
    parser.add_argument("--chat-id", type=int, default=None)
    parser.add_argument("--current-url", default="/")
    args = parser.parse_args()
    asyncio.run(_run(args.user_id, args.chat_id, args.message, args.current_url))


if __name__ == "__main__":
    main()
