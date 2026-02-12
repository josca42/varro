from __future__ import annotations

import asyncio

from varro.chat.run_manager import RunManager


def test_run_manager_enforces_one_active_run_per_chat():
    async def scenario():
        manager = RunManager()
        first = await manager.create_run(run_id="run-1", user_id=1, chat_id=9)
        assert first is not None

        blocked = await manager.create_run(run_id="run-2", user_id=1, chat_id=9)
        assert blocked is None

        await manager.close("run-1")
        second = await manager.create_run(run_id="run-3", user_id=1, chat_id=9)
        assert second is not None

    asyncio.run(scenario())


def test_stream_emits_messages_and_done_event():
    async def scenario():
        manager = RunManager()
        run = await manager.create_run(run_id="run-1", user_id=1, chat_id=3)
        assert run is not None

        stream = await manager.stream_for_user(run_id="run-1", user_id=1)
        assert stream is not None

        await manager.publish("run-1", "<div>a</div>")
        await manager.close("run-1")

        payloads = []
        async for event in stream:
            payloads.append(event)

        assert any("event: message" in event for event in payloads)
        assert any("<div>a</div>" in event for event in payloads)
        assert any("event: done" in event for event in payloads)

    asyncio.run(scenario())


def test_cancel_returns_false_when_no_task_attached():
    async def scenario():
        manager = RunManager()
        run = await manager.create_run(run_id="run-1", user_id=1, chat_id=7)
        assert run is not None

        cancelled = await manager.cancel("run-1")

        assert cancelled is False

    asyncio.run(scenario())
