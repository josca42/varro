# Chat App Architecture

HTTP + SSE chat runtime embedded in the unified app shell. Built with FastHTML, HTMX, and Pydantic-AI.

## Overview

```
POST /chat/runs
        |
        v
+-------------------+
|    RunManager     |  One active run per (user_id, chat_id)
| run records + SSE |
+--------+----------+
         |
         v
+-------------------+
|    ShellPool      |  Chat-scoped shell lease
| snapshot + replay |
+--------+----------+
         |
         v
+-------------------+
|    run_agent()    |  Rebuilds message history from disk each run,
|                   |  streams incremental blocks for the new turn
+--------+----------+
         |
         v
+-------------------+
|   Persistence     |  Chat/Turn rows + turn msgpack files + runtime.json
+-------------------+
```

## Key Files

| File | Purpose |
|------|---------|
| `app/main.py` | Unified app entrypoint + beforeware + startup/shutdown cleanup hooks |
| `app/routes/chat.py` | Run start/stream/cancel/status endpoints and OOB chat routes |
| `ui/app/layout.py` | App shell layout (chat panel on the left) |
| `ui/app/chat.py` | ChatPanel + form + SSE client script |
| `varro/chat/run_manager.py` | Run lock, event buffering/replay, run status, retention GC |
| `varro/chat/shell_pool.py` | Chat-scoped shell lease, idle eviction, snapshot/replay restore |
| `varro/chat/stream_ops.py` | FT block -> deterministic DOM ops (`insert`/`replace`) |
| `varro/chat/agent_run.py` | Agent iteration, node->HTML conversion, turn persistence |
| `varro/chat/turn_store.py` | Turn file pathing + msgpack/zstd save/load |
| `varro/chat/render_cache.py` | Cache HTML for `<fig />` / `<df />` placeholders |
| `varro/chat/shell_replay.py` | Replay `Sql`/`Jupyter` tool calls from persisted history |
| `varro/chat/runtime_state.py` | Per-chat runtime state (`bash_cwd`) |

## Transport Flow

1. `POST /chat/runs`:
   - validates chat ownership,
   - creates chat on first turn when `chat_id` is missing,
   - reserves run lock for `(user_id, chat_id)`,
   - returns OOB `ChatFormRunning` + `ChatProgressStart` and `HX-Trigger: chatRunStarted`.
2. Browser opens `EventSource` to `GET /chat/runs/{run_id}/stream?since=...`.
3. Server replays buffered events, then tails live `dom`/`status` events.
4. `POST /chat/runs/{run_id}/cancel` cancels the run task.
5. `GET /chat/runs/{run_id}/status` supports reconnect/poll fallback.

## RunManager Model

- Run record fields include:
  - `run_id`, `user_id`, `chat_id`, `previous_chat_id`, `created_chat`
  - `state`, `task`, `events`, `next_event_id`
  - `resync_required`, `result_chat_id`, `created_at`, `finished_at`
- Enforces one active run per `(user_id, chat_id)`.
- Event log is buffered for replay (16MB cap).
- On overflow:
  - marks `resync_required`,
  - stops buffering catch-up events,
  - stream consumers fall back to status polling + panel refresh.
- Terminal runs are retained for 5 minutes, then garbage-collected.

## SSE Event Types

- `dom`:
  - payload `{event_id, ops:[...]}` where ops are:
    - `{"kind":"insert","selector":"#...","position":"beforebegin|afterbegin|beforeend|afterend","html":"..."}`
    - `{"kind":"replace","selector":"#...","html":"..."}`
- `status`:
  - payload `{event_id, state}`
  - states: `running | completed | cancelled | failed | resync_required`
- `ping`:
  - payload `{event_id}`
  - keep-alive every 15 seconds while idle.

## ShellPool Model

- Key: `(user_id, chat_id)`.
- Entry fields:
  - `shell`, `baseline_keys`, `loaded`, `turn_count`, `last_used`, `in_use_count`.
- Lease model:
  - run acquires shell at start and releases in `finally`.
  - tools call `touch_shell()` to extend idle timer.
- Restore order:
  1. try snapshot (`shell.pkl` + `shell.meta.json`),
  2. replay missing turns,
  3. fallback to full replay if snapshot is invalid.
- Idle eviction:
  - 10-minute TTL, checked every 60 seconds,
  - only evicts when `in_use_count == 0`,
  - writes snapshot (max 512MB), then resets/disposes shell.

Snapshot paths:
- `data/chat/{user_id}/{chat_id}/shell.pkl`
- `data/chat/{user_id}/{chat_id}/shell.meta.json`

## Cancel Semantics

- Existing chat run:
  - cancel emits `ChatProgressEnd` + `ChatFormEnabled(chat_id)`.
- First run in newly-created chat:
  - delete created chat and artifacts,
  - restore prior chat (or empty new chat panel if none),
  - emit panel rollback + form/progress reset.

## Browser Runtime

`ChatClientScript`:

- idempotent global initialization guard (`window.__varroChatClientInitialized`),
- listens for `chatRunStarted` trigger and opens EventSource per run,
- tracks `lastEventId`,
- applies streamed DOM ops deterministically and processes inserted HTMX/script content,
- reconnects with backoff using `since=lastEventId`,
- when `resync_required`, polls run status until terminal and refreshes chat panel from persisted routes.

## Turn/runtime persistence

Turn files:
- `data/chat/{user_id}/{chat_id}/{idx}.mpk` (`ModelMessage` list, msgpack+zstd)
- `data/chat/{user_id}/{chat_id}/{idx}.cache.json` (fig/df cached HTML)

Runtime state:
- `data/chat/{user_id}/{chat_id}/runtime.json`
- schema: `{"bash_cwd": "/..."}`
