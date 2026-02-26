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
- `ColumnValues(..., for_table=...)` now has an interim fallback for empty/missing `dimension_links` metadata: infer fact column from name similarity first, then kode overlap against fact column-value parquets.
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

## Chat-16 pattern (2026-02-24)

- `fuzzy_match` in `context/utils.py` used `df.iloc[index]` but rapidfuzz returns pandas label indices, not positional. Crashes when `for_table` filters produce non-contiguous DataFrame index.
- CLI playground loses kernel state between invocations because `ShellPool._release()` doesn't save snapshots (only `evict_idle` does).
- `folk1a` population queries are a recurring trap: 5 dimensions (omrade, køn, alder, civilstand, tid) require all to be filtered to totals (`kon='TOT'`, `alder='IALT'`, `civilstand='TOT'`), otherwise SUM inflates by cross-product factor.

## Chat-16 fixes landed (2026-02-24)

- `varro/context/utils.py` `fuzzy_match`: `df.iloc[index]` → `df.loc[index, id_col]`. Fixes crash on filtered dimension DataFrames.
- Regression test added: `tests/agent/test_assistant_column_values_tool.py::test_column_values_fuzzy_match_with_for_table_filtered_index`

## Three-skill pipeline

```
$playground-explorer / $analyse-trajectory  →  findings.md  →  $findings-to-plan  →  implementation_plan.md  →  code changes
```

- `$playground-explorer` — interactive probing, produces findings with validation probes
- `$analyse-trajectory` — retrospective audit, produces findings with concrete suggestions
- `$findings-to-plan` — reads findings, maps evidence to code ownership, and outputs a PR-ready implementation plan

## Chat-24/25 pattern (2026-02-26)

Test: Dashboard creation (test plan #11 "befolkningsudvikling med filtre for region og tidsperiode") + navigation/iteration (#14, #15, #16).

Key findings:
- **Turn persistence on error**: When `agent.iter()` raises (Snapshot ModelRetry exceeded), the turn is not persisted. All ~20 tool calls in that turn are lost. Dashboard files exist on disk but trajectory cannot be generated.
- **SQL bugs only surface at Snapshot**: Agent tests queries via `Sql` tool with hardcoded values. Dashboard executor uses typed `bindparams`. SQL errors (missing GROUP BY) only appear when Snapshot executes the full dashboard.
- **datetime.date vs Timestamp**: The dashboard executor returns `datetime.date` from Postgres date columns. Agent writes `.dt.year` (pandas accessor) which only works on Timestamps. The types are the same from `Sql` tool but the agent never tests the output functions, only the raw queries.
- **Snapshot error cascade**: `max_retries=1` means 2 failures kill the run. The error includes raw SQL but not the query file name, making self-repair difficult.
- **Navigation/iteration works well**: Agent correctly discovers filters from dashboard.md and uses UpdateUrl with params. When asked to "show less data", agent wisely uses existing date filter rather than editing code.

Proposed fixes (priority order):
1. Persist turns on error (`agent_run.py`)
2. Auto-convert `datetime.date` → Timestamp in `executor.py`
3. Include query file name in Snapshot errors
4. Add dashboard output validation step
5. Increase Snapshot max_retries to 2-3

Findings file: `data/trajectory/1/25/findings.md`

## Chat-26 validation probe (2026-02-26)

Starter probe: test plan #11 ("Lav et dashboard over befolkningsudviklingen i Danmark med filtre for region og tidsperiode") after adding auto-validation + explicit `ValidateDashboard`.

Observed behavior:
- Auto-validation runs on `Write`/`Edit` inside `/dashboard/{slug}/`.
- Incremental creation is non-blocking with `Validation pending: Missing ...` until required files exist.
- First full validation failure was correctly blocking and aggregated query + output errors (real SQL `GroupingError`), enabling immediate repair.
- Post-fix edits returned `Validation passed ...` and `VALIDATION_RESULT` payloads with query row counts and output kind map.
- Snapshot remained separate from validation. Same-turn `UpdateUrl` then bare `Snapshot()` still failed once (`url must match /dashboard/{slug}`), while `Snapshot(url="...")` succeeded.

Current assessment:
- Validation behavior is working as designed for authoring loop quality.
- Remaining UX improvement is optional: better same-turn URL handoff between `UpdateUrl` and implicit `Snapshot()`.

Findings file: `data/trajectory/1/26/findings.md`

## Chat-28 pattern (2026-02-26)

Test plan #11 again, confirming Chat-24/25/26 patterns. Initial creation run crashed before turn data was saved.

New observations:
- **Write auto-validation also crashes runs**: Same cascade as Snapshot but triggered by `run_dashboard_validation_after_write` raising `ModelRetry`. Agent wrote 9 dashboard files successfully, then the 10th batch (fixes) triggered validation → `ModelRetry` → exceeded max_retries=1. Entire run lost.
- **Postgres alias in HAVING**: Agent wrote `HAVING aldersgruppe IS NOT NULL` using a column alias from a CASE expression. Valid in MySQL, invalid in Postgres. Fixed with CTE wrapper. This is a recurring SQL knowledge gap that could be addressed in docs/prompts.
- **No final text response after fix**: Turn 0 (fix + ValidateDashboard + Edit + UpdateUrl) produced `Final: _None_`. Agent's thinking contained the explanation but no text was emitted. May be related to thinking budget (3000 tokens) or the agent treating UpdateUrl as a sufficient response.
- **Iteration flow is excellent**: Turn 1 (navigation): 1 tool call. Turn 2 (snapshot): 3 steps, data-rich response. Turn 3 (edit): 6 steps with auto-validation catching a type error, immediate fix, and proactive follow-up suggestion.

Priority 1 action: Make `run_dashboard_validation_after_write` return errors as strings instead of raising `ModelRetry`. This prevents Write cascade crashes while keeping the feedback loop (agent sees errors in tool result and can fix them next step).

Findings file: `data/trajectory/1/28/findings.md`

## Relevant files

- `varro/playground/cli.py`
- `varro/playground/trajectory.py`
- `.claude/skills/playground-explorer/SKILL.md`
- `.claude/skills/analyse-trajectory/SKILL.md`
- `.claude/skills/findings-to-plan/SKILL.md`
- `tests/playground/test_cli.py`
- `tests/agent/test_snapshot.py`
