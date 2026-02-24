# Playground Exploration

Snapshot date: 2026-02-21.

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
- `findings-to-plan` is implementation planning:
  - consumes completed `findings.md`
  - verifies trajectory and code evidence for each finding
  - produces `implementation_plan.md` with concrete file-level actions

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

- source turns: `data/chat/{user_id}/{chat_id}/{idx}.mpk`
- derived trajectories: `data/trajectory/{user_id}/{chat_id}/`
- exploration output stays in existing trajectory tree:
  - `data/trajectory/{user_id}/{chat_id}/findings.md`
  - `data/trajectory/{user_id}/{chat_id}/implementation_plan.md`

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

- Inline categorical totals are not always `TOT` (e.g. `fact.folk1a.alder` uses `IALT`), so docs must expose sentinel codes clearly.
- Prompt guidance already tells the agent to check `ColumnValues` for filters; prompt tweaks are lower priority than improving tool/context signals.

## Chat-15 pattern (2026-02-24)

- Hierarchy depth metadata (`levels [1,2,3]`) is insufficient without observed top-level coverage per fact table.
- Fact doc join guidance should reflect actual join expression/casts when fact and dim key types differ.
- `ColumnValues` on dim tables needs optional fact-table scoping (`for_table`) to avoid conflating taxonomy universe with table coverage.
- Subject readmes should surface table coverage mismatches early to reduce expensive pivot/debug loops.

## Chat-15 fixes landed (2026-02-24)

- `varro/context/fact_table.py` now emits dtype-aware join expressions in fact docs and includes level-1 coverage lists for dim-linked columns.
- `varro/context/subjects.py` now emits a `<coverage notes>` block when leaf-subject coverage differs across tables or is uniformly a subset of the full dimension level-1 set.
- `varro/agent/assistant.py` `ColumnValues` now supports `for_table` for dim-table calls and filters dimension values to the fact-table subset.
- `varro/prompts/agent/rigsstatistiker.j2` now documents `for_table` usage explicitly for shared dimensions.
- Regression tests added:
  - `tests/agent/test_assistant_column_values_tool.py`
  - `tests/context/test_subjects.py`
  - expanded `tests/context/test_fact_table.py`

## Chat-66 fixes landed (2026-02-23)

- `Sql` now returns `row_count: <n>` and warns explicitly on `row_count: 0` with a `ColumnValues` hint (`varro/agent/assistant.py`).
- Fact-doc generation no longer skips `alder` in value mappings (`SKIP_VALUE_MAP_COLUMNS` now only skips `tid` in `varro/context/fact_table.py`).
- Regenerated `context/fact/borgere/befolkning/befolkningstal/folk1a.md` now includes `alder` values with `IALT=Alder i alt`.
- `get_dim_tables()` now uses `dst_read_engine` (not undefined `engine`) in `varro/agent/utils.py`.
- Regression tests added:
  - `tests/agent/test_assistant_sql_tool.py`
  - `tests/context/test_fact_table.py`

## Three-skill pipeline

```
$playground-explorer / $analyse-trajectory  →  findings.md  →  $findings-to-plan  →  implementation_plan.md  →  code changes
```

- `$playground-explorer` — interactive probing, produces findings with validation probes
- `$analyse-trajectory` — retrospective audit, produces findings with concrete suggestions
- `$findings-to-plan` — reads findings, maps evidence to code ownership, and outputs a PR-ready implementation plan

## Relevant files

- `varro/playground/cli.py`
- `varro/playground/trajectory.py`
- `.claude/skills/playground-explorer/SKILL.md`
- `.claude/skills/analyse-trajectory/SKILL.md`
- `.claude/skills/findings-to-plan/SKILL.md`
- `tests/playground/test_cli.py`
- `tests/agent/test_snapshot.py`
