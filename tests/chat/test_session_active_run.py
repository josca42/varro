from __future__ import annotations

import asyncio
import contextlib
from types import SimpleNamespace

import varro.chat.session as session_mod


class _DummyHistoryManager:
    def __init__(self):
        self.ended = False

    def end_session(self):
        self.ended = True


class _DummyShell:
    def __init__(self):
        self.history_manager = _DummyHistoryManager()
        self.reset_calls: list[bool] = []
        self.run_cells: list[str] = []

    def run_cell(self, code):
        self.run_cells.append(code)

    def reset(self, new_session):
        self.reset_calls.append(new_session)


def _make_session(monkeypatch):
    shell = _DummyShell()
    monkeypatch.setattr(session_mod, "get_shell", lambda: shell)
    monkeypatch.setattr(session_mod, "JUPYTER_INITIAL_IMPORTS", "")

    async def send(_):
        return None

    session = session_mod.UserSession(
        user_id=1,
        sid="sid-1",
        chats=SimpleNamespace(),
        send=send,
        ws=SimpleNamespace(),
    )
    return session, shell


def test_start_run_registers_active_run(monkeypatch):
    session, _ = _make_session(monkeypatch)

    started = session.start_run(
        run_id="run-1",
        chat_id=7,
        previous_chat_id=4,
        created_chat=True,
    )

    assert started is True
    assert session.active_run is not None
    assert session.active_run.run_id == "run-1"
    assert session.active_run.chat_id == 7
    assert session.active_run.previous_chat_id == 4
    assert session.active_run.created_chat is True


def test_start_run_rejects_when_active_run_exists(monkeypatch):
    session, _ = _make_session(monkeypatch)

    assert session.start_run(
        run_id="run-1",
        chat_id=9,
        previous_chat_id=None,
        created_chat=False,
    )

    started = session.start_run(
        run_id="run-2",
        chat_id=10,
        previous_chat_id=9,
        created_chat=False,
    )

    assert started is False
    assert session.active_run is not None
    assert session.active_run.run_id == "run-1"


def test_cancel_active_run_respects_run_id(monkeypatch):
    async def scenario():
        session, _ = _make_session(monkeypatch)
        assert session.start_run(
            run_id="run-1",
            chat_id=9,
            previous_chat_id=None,
            created_chat=False,
        )

        async def pending():
            await asyncio.sleep(60)

        task = asyncio.create_task(pending())
        session.attach_run_task("run-1", task)

        assert session.cancel_active_run("run-other") is False
        assert task.cancelled() is False

        assert session.cancel_active_run("run-1") is True
        with contextlib.suppress(asyncio.CancelledError):
            await task
        assert task.cancelled() is True

    asyncio.run(scenario())


def test_cleanup_cancels_active_run_and_clears_state(monkeypatch):
    async def scenario():
        session, shell = _make_session(monkeypatch)
        assert session.start_run(
            run_id="run-1",
            chat_id=9,
            previous_chat_id=None,
            created_chat=False,
        )

        async def pending():
            await asyncio.sleep(60)

        task = asyncio.create_task(pending())
        session.attach_run_task("run-1", task)
        session.shell_chat_id = 9

        session.cleanup()
        with contextlib.suppress(asyncio.CancelledError):
            await task

        assert session.active_run is None
        assert shell.reset_calls == [False]
        assert shell.history_manager.ended is True
        assert session.shell_chat_id is None

    asyncio.run(scenario())
