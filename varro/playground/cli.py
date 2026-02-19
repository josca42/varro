from __future__ import annotations

import argparse
import asyncio
import json
from dataclasses import dataclass
from pathlib import Path

from varro.agent.snapshot import snapshot_dashboard_url
from varro.chat.agent_run import run_agent
from varro.chat.shell_pool import shell_pool
from varro.chat.trace import extract_trace
from varro.chat.turn_store import load_turn_messages
from varro.config import DATA_DIR, TRAJECTORIES_DIR
from varro.db import crud
from varro.db.models.chat import Chat
from varro.playground.trajectory import generate_chat_trajectory


@dataclass
class PlaygroundSession:
    user_id: int
    chat_id: int
    current_url: str
    trajectory_dir: Path


def parse_update_url_payload(text: str) -> dict[str, object] | None:
    if not text.startswith("UPDATE_URL "):
        return None
    raw_json = text.removeprefix("UPDATE_URL ").strip()
    if not raw_json:
        return None
    try:
        payload = json.loads(raw_json)
    except json.JSONDecodeError:
        return None
    if not isinstance(payload, dict):
        return None
    url = payload.get("url")
    if not isinstance(url, str) or not url.startswith("/"):
        return None
    return payload


def _collect_turn_outcome(msgs, current_url: str) -> tuple[str, str]:
    trace = extract_trace(msgs)
    final_parts = [
        event.text
        for event in trace.events
        if event.kind == "assistant_text" and event.is_final and event.text
    ]
    next_url = current_url
    for event in trace.events:
        if event.kind != "tool_return" or event.tool_name != "UpdateUrl" or not event.text:
            continue
        payload = parse_update_url_payload(event.text.strip())
        if payload:
            next_url = str(payload["url"])
    final_response = "\n".join(final_parts).strip() or "_None_"
    return final_response, next_url


def _turn_artifact_path(user_id: int, chat_id: int, turn_idx: int) -> Path:
    return DATA_DIR / "chat" / str(user_id) / str(chat_id) / f"{turn_idx}.mpk"


def _print_help() -> None:
    print("Commands:")
    print(":help                 Show this help")
    print(":status               Show session status")
    print(":url <path>           Set current URL (must start with /)")
    print(":trajectory [turn_idx]    Refresh trajectory and print artifact path")
    print(":snapshot [url]       Snapshot dashboard URL")
    print(":quit | :exit         Exit")
    print("")
    print("Any non-command input is sent as a user question.")


def _print_status(session: PlaygroundSession) -> None:
    chat = crud.chat.for_user(session.user_id).get(session.chat_id, with_turns=True)
    turns = len(chat.turns) if chat else 0
    print(f"user_id: {session.user_id}")
    print(f"chat_id: {session.chat_id}")
    print(f"turns: {turns}")
    print(f"current_url: {session.current_url}")
    print(f"trajectory_dir: {session.trajectory_dir}")
    print(f"chat_turn_dir: {DATA_DIR / 'chats' / str(session.user_id) / str(session.chat_id)}")


def _normalize_url(value: str) -> str | None:
    candidate = value.strip()
    if not candidate.startswith("/"):
        return None
    return candidate


async def _ask(session: PlaygroundSession, message: str) -> None:
    chats = crud.chat.for_user(session.user_id)
    try:
        async with shell_pool.lease(user_id=session.user_id, chat_id=session.chat_id) as shell:
            async for _ in run_agent(
                message,
                user_id=session.user_id,
                chats=chats,
                shell=shell,
                chat_id=session.chat_id,
                current_url=session.current_url,
            ):
                pass
    except Exception:
        await shell_pool.invalidate(session.user_id, session.chat_id)
        raise

    chat = chats.get(session.chat_id, with_turns=True)
    if not chat or not chat.turns:
        raise ValueError("No turn was persisted.")
    turn = chat.turns[-1]
    msgs = load_turn_messages(DATA_DIR / turn.obj_fp)
    final_response, next_url = _collect_turn_outcome(msgs, session.current_url)
    session.current_url = next_url
    session.trajectory_dir = generate_chat_trajectory(session.user_id, session.chat_id)

    print("")
    print("Final response:")
    print(final_response)
    print("")
    print(f"trajectory_dir: {session.trajectory_dir}")
    print(f"chat_trajectory: {session.trajectory_dir / 'chat.md'}")
    print(f"turn_trajectory: {session.trajectory_dir / str(turn.idx) / 'turn.md'}")
    print(f"turn_file: {_turn_artifact_path(session.user_id, session.chat_id, turn.idx)}")
    print(f"current_url: {session.current_url}")


async def _snapshot(session: PlaygroundSession, raw_url: str | None) -> None:
    target = (raw_url or session.current_url).strip()
    if not target:
        print("Error: no URL provided.")
        return
    if not target.startswith("/"):
        print("Error: URL must start with '/'.")
        return
    try:
        result = await snapshot_dashboard_url(session.user_id, target)
    except Exception as exc:
        print(f"Snapshot error: {exc}")
        return
    print(f"snapshot_url: {result.url}")
    print(f"snapshot_folder: {result.folder}")


def _refresh_trajectory_path(session: PlaygroundSession, raw_turn_idx: str | None) -> None:
    session.trajectory_dir = generate_chat_trajectory(session.user_id, session.chat_id)
    if raw_turn_idx is None:
        print(f"chat_trajectory: {session.trajectory_dir / 'chat.md'}")
        return
    try:
        turn_idx = int(raw_turn_idx)
    except ValueError:
        print("Error: turn_idx must be an integer.")
        return
    print(f"turn_trajectory: {session.trajectory_dir / str(turn_idx) / 'turn.md'}")


def _create_or_resume_chat(user_id: int, chat_id: int | None) -> int:
    chats = crud.chat.for_user(user_id)
    if chat_id is not None:
        chat = chats.get(chat_id)
        if not chat:
            raise ValueError(f"Chat {chat_id} not found for user {user_id}")
        return chat_id
    chat = chats.create(Chat())
    if chat.id is None:
        raise ValueError("Failed to create chat")
    return chat.id


async def _run(args) -> int:
    chat_id = _create_or_resume_chat(args.user_id, args.chat_id)
    session = PlaygroundSession(
        user_id=args.user_id,
        chat_id=chat_id,
        current_url=args.current_url,
        trajectory_dir=TRAJECTORIES_DIR / str(args.user_id) / str(chat_id),
    )

    print("Interactive playground started.")
    _print_status(session)
    print("")
    _print_help()

    while True:
        try:
            line = input("playground> ")
        except EOFError:
            print("")
            return 0
        except KeyboardInterrupt:
            print("")
            return 0

        text = line.strip()
        if not text:
            continue

        if text in {":quit", ":exit"}:
            return 0
        if text == ":help":
            _print_help()
            continue
        if text == ":status":
            _print_status(session)
            continue
        if text.startswith(":url"):
            raw_url = text[4:].strip()
            new_url = _normalize_url(raw_url)
            if not new_url:
                print("Error: URL must start with '/'.")
                continue
            session.current_url = new_url
            print(f"current_url: {session.current_url}")
            continue
        if text.startswith(":trajectory"):
            raw_turn = text[12:].strip() or None
            _refresh_trajectory_path(session, raw_turn)
            continue
        if text.startswith(":snapshot"):
            raw_url = text[9:].strip() or None
            await _snapshot(session, raw_url)
            continue

        try:
            await _ask(session, text)
        except Exception as exc:
            print(f"Run error: {exc}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--user-id", type=int, default=1)
    parser.add_argument("--chat-id", type=int)
    parser.add_argument("--current-url", default="/")
    args = parser.parse_args()
    current_url = _normalize_url(args.current_url)
    if not current_url:
        parser.error("--current-url must start with '/'")
    args.current_url = current_url
    return asyncio.run(_run(args))


if __name__ == "__main__":
    raise SystemExit(main())
