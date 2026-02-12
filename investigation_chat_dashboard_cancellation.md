# Investigation: Chat Disappears After Dashboard Creation

## Problem observed

When the agent creates a dashboard from chat and updates the URL to show it in the content area, the in-progress chat turn disappears.

## What was tested

### Hypothesis: "No final assistant text causes the turn to disappear"

This is unlikely to be the cause.

- The user message bubble is rendered from persisted `turn.user_text`, independent of assistant final text.
- Tool/reasoning blocks render even for tool-heavy turns.
- Local checks of saved turns that include `UpdateUrl` showed final `ModelResponse(finish_reason=\"stop\")` text exists.
- Simulating a turn render without final assistant text still rendered user + tool blocks.

## Most likely root cause

The run is being cancelled during URL navigation, not dropped because of missing final text.

Likely chain:

1. Agent emits `UpdateUrl`.
2. Client applies URL change immediately (`__varroApplyUpdateUrl` -> `__varroNavigate` -> HTMX request).
3. Chat websocket setup script can be re-processed/re-run in that lifecycle.
4. A second websocket connects with the same `{user_id, sid}`.
5. `SessionManager.create(...)` currently closes/cleans the old session for same sid.
6. Cleanup cancels the active run task.
7. Cancel rollback re-renders chat panel from previous persisted state, so the in-progress streamed turn disappears.

## Why this matches behavior

- You confirmed the chat is cancelled exactly when dashboard URL update occurs.
- Server code explicitly rolls back UI on cancelled runs.
- Session manager currently treats same-sid reconnect as replacement that cleans up the existing session.

## Fix direction

To keep chat independent of URL updates while staying in the app shell:

1. Preserve session/run on same-sid reconnect:
   - Change same-sid websocket handling to rebind transport (`ws`, `send`) without calling cleanup/cancel on the existing `UserSession`.
2. Make chat bootstrap idempotent:
   - Ensure `ChatClientScript` websocket init/listeners run once and are not duplicated by subsequent swaps/script reprocessing.
3. Keep `UpdateUrl` immediate:
   - Continue immediate content navigation so the agent can guide analysis interactively.
4. Optional hardening:
   - Force fragment responses for client-driven content-panel navigation with an explicit partial-request header.

## Expected outcome after fix

- Agent can navigate dashboards and filter URLs during a run.
- Chat run does not get cancelled by URL updates.
- Streamed turn remains visible and completes normally.
