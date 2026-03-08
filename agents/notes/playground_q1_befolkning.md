# Playground Q1: Befolkning (Chat 70)

Date: 2026-03-06.

Findings at: `data/trajectory/1/70/findings.md`

## Key issues discovered

1. **Snapshot auth failure** — Playwright browser has no session cookies, gets redirected to login. Every Snapshot call times out waiting for `[data-slot='dashboard-shell']`. Fix: use public route `/public/{owner_id}/{name}` or inject auth cookies.

2. **Snapshot ModelRetry too broad** — `except Exception: raise ModelRetry(...)` in `assistant.py:426` causes pydantic-ai to retry and then crash the entire turn when retries are exhausted. Infrastructure failures should return error strings, not ModelRetry.

3. **Leftover files from failed turns** — Write tool calls persist even when the turn fails. Agent gets confused by stale files from previous attempts.

## What worked well

- Exploration trajectory (turns 0-2) was excellent: 3-4 tool calls per turn, clean data → chart → insight flow.
- Agent self-corrected Plotly category-as-date issue in pyramid chart over 3 iterations.
- Dashboard structure (queries, outputs.py, dashboard.md) was well-formed with tabs, metrics, and filters.
- Agent offered natural follow-up directions without over-clarifying.
