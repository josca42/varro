from __future__ import annotations

import asyncio
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import AsyncIterator

from fasthtml.common import to_xml


@dataclass(slots=True)
class RunRecord:
    run_id: str
    user_id: int
    chat_id: int
    task: asyncio.Task | None
    queue: asyncio.Queue[str | None]


class RunManager:
    def __init__(
        self,
        *,
        retention: timedelta = timedelta(minutes=5),
        gc_interval: int = 30,
    ):
        self._retention = retention
        self._gc_interval = gc_interval

        self._runs: dict[str, RunRecord] = {}
        self._active_by_chat: dict[tuple[int, int], str] = {}
        self._finished_at: dict[str, datetime] = {}

        self._lock = asyncio.Lock()
        self._cleanup_task: asyncio.Task | None = None

    async def create_run(self, *, run_id: str, user_id: int, chat_id: int) -> RunRecord | None:
        async with self._lock:
            key = (user_id, chat_id)
            active_run_id = self._active_by_chat.get(key)
            if active_run_id:
                active = self._runs.get(active_run_id)
                if active and (active.task is None or not active.task.done()):
                    return None
                self._active_by_chat.pop(key, None)

            run = RunRecord(
                run_id=run_id,
                user_id=user_id,
                chat_id=chat_id,
                task=None,
                queue=asyncio.Queue(),
            )
            self._runs[run_id] = run
            self._active_by_chat[key] = run_id
            return run

    async def attach_task(self, run_id: str, task: asyncio.Task) -> None:
        async with self._lock:
            run = self._runs.get(run_id)
            if run is None:
                task.cancel()
                return
            run.task = task

    async def get_for_user(self, run_id: str, user_id: int) -> RunRecord | None:
        async with self._lock:
            run = self._runs.get(run_id)
            if run is None or run.user_id != user_id:
                return None
            return run

    async def publish(self, run_id: str, block) -> None:
        async with self._lock:
            run = self._runs.get(run_id)
            if run is None:
                return

        html = block if isinstance(block, str) else to_xml(block)
        run.queue.put_nowait(html)

    async def cancel(self, run_id: str) -> bool:
        async with self._lock:
            run = self._runs.get(run_id)
            if run is None or run.task is None or run.task.done():
                return False
            run.task.cancel()
            return True

    async def close(self, run_id: str) -> None:
        async with self._lock:
            run = self._runs.get(run_id)
            if run is None:
                return
            self._active_by_chat.pop((run.user_id, run.chat_id), None)
            self._finished_at[run_id] = _utc_now()

        run.queue.put_nowait(None)

    async def stream_for_user(self, *, run_id: str, user_id: int) -> AsyncIterator[str] | None:
        async with self._lock:
            run = self._runs.get(run_id)
            if run is None or run.user_id != user_id:
                return None
            queue = run.queue

        async def _stream() -> AsyncIterator[str]:
            while True:
                item = await queue.get()
                if item is None:
                    yield _sse("done", "")
                    return
                yield _sse("message", item)

        return _stream()

    async def evict_finished(self, retention: timedelta | None = None) -> None:
        ttl = self._retention if retention is None else retention
        cutoff = _utc_now() - ttl

        async with self._lock:
            expired = [
                run_id
                for run_id, finished_at in self._finished_at.items()
                if finished_at < cutoff
            ]
            for run_id in expired:
                self._finished_at.pop(run_id, None)
                self._runs.pop(run_id, None)

    def start_cleanup_task(
        self,
        *,
        retention: timedelta | None = None,
        interval: int | None = None,
    ) -> None:
        if self._cleanup_task and not self._cleanup_task.done():
            return

        ttl = self._retention if retention is None else retention
        delay = self._gc_interval if interval is None else interval

        async def _loop() -> None:
            while True:
                await asyncio.sleep(delay)
                await self.evict_finished(ttl)

        self._cleanup_task = asyncio.create_task(_loop())

    def stop_cleanup_task(self) -> None:
        if self._cleanup_task and not self._cleanup_task.done():
            self._cleanup_task.cancel()


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _sse(event: str, data: str) -> str:
    lines = data.splitlines() or [""]
    payload = "".join(f"data: {line}\n" for line in lines)
    return f"event: {event}\n{payload}\n"


run_manager = RunManager()
