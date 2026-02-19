# Playground Exploration

Snapshot date: 2026-02-17.

## Core framing

- Treat Varro as a playground environment for the agent loop:
  - `observe -> decide -> act -> observe`
- The app is the agent's environment surface:
  - data tools (`Sql`, `Jupyter`, `ColumnValues`, `Read`, `Bash`, etc.)
  - UI/URL tools (`UpdateUrl`, `Snapshot`, dashboard routes)

## Skill split (important)

- `analyse-trajectory` is retrospective:
  - post-hoc audit of completed chat
  - summarize root causes and improvements
- `playground-explorer` is interactive:
  - CLI-first probing with follow-up questions
  - inspect trajectory artifacts as they are produced
  - produce experiment-driven findings

## CLI-first exploration workflow

Use:

```bash
uv run python -m varro.playground.cli
```

Key commands:

- `:status`
- `:url <path>`
- `:trajectory [turn_idx]`
- `:snapshot [url]`

Default behavior:

- new chat by default, optional resume via `--chat-id`
- each plain input line is a new user turn
- review artifacts regenerate after each ask
- output paths are printed for quick inspection

## Artifact model

- source turns: `mnt/chat/{user_id}/{chat_id}/{idx}.mpk`
- derived trajectories: `mnt/trajectory/{user_id}/{chat_id}/`
- exploration output stays in existing trajectory tree:
  - `mnt/trajectory/{user_id}/{chat_id}/findings.md`

## Findings format for exploration

Each finding should include:

- `Hypothesis`
- `Probe`
- `Observed Trajectory Evidence`
- `Interpretation`
- `Proposed Change`
- `Expected Trajectory Delta`
- `Validation Probe`

This keeps improvements tied to observed trajectory mechanics, not generic model critique.

## Runtime contracts learned

- `UpdateUrl` tool returns parseable payload:
  - `UPDATE_URL {json}`
- `Snapshot` tool returns parseable payload with both URL and folder:
  - `SNAPSHOT_RESULT {"url":"...","folder":"..."}`
- Snapshot still requires app availability (`http://127.0.0.1:5001`) for full dashboard rendering.

## Common trajectory friction

- Inline categorical totals are not always `TOT` (e.g. `fact.folk1a.alder` uses `IALT`); missing value docs can lead to empty queries and extra tool calls.
- `Sql` observations do not currently surface row counts; empty results are easy to miss until a Jupyter print.

## Relevant files

- `varro/playground/cli.py`
- `varro/playground/trajectory.py`
- `.agents/skills/playground-explorer/SKILL.md`
- `.agents/skills/analyse-trajectory/SKILL.md`
- `tests/playground/test_cli.py`
- `tests/agent/test_snapshot.py`
