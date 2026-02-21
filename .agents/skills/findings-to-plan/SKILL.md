---
name: findings-to-plan
description: >
  Convert trajectory findings into a concrete implementation plan. Use when
  given a findings.md (from $analyse-trajectory or $playground-explorer) and
  asked to create an implementation plan, map findings to code changes, or
  turn trajectory analysis into actionable improvements.
---

# Findings to Plan

Convert findings into an `implementation_plan.md` with targeted, surgical code changes that build on existing implementations.

## Input

Read `data/trajectory/{user_id}/{chat_id}/findings.md`. Two formats exist:

- **analyse-trajectory**: Dimension / Turn / Observation / Suggestion / Impact
- **playground-explorer**: Hypothesis / Probe / Observed Trajectory Evidence / Proposed Change / Expected Trajectory Delta

Extract from each finding: title, trajectory references (turn/step/tool_call files), proposed change, impact.

## Workflow

### 1. Verify trajectory evidence

For each finding, read the referenced artifacts:
- `data/trajectory/{user_id}/{chat_id}/{turn_idx}/turn.md`
- `data/trajectory/{user_id}/{chat_id}/{turn_idx}/tool_calls/*.sql|*.py|*.txt`

Confirm the finding's observation matches what actually happened. Drop or flag findings with weak evidence.

### 2. Trace to existing code

Use the code ownership map to find the relevant source files. **Read the existing code** to understand current behavior before proposing changes. Look for:
- Existing functions that already do something close
- Patterns used elsewhere in the same module
- Related logic that would need to stay consistent

### 3. Design targeted fixes

For each finding, propose the smallest change that fixes the observed problem. Prefer:
- Adding a parameter to an existing function over creating a new one
- Extending existing output over adding a new tool
- A one-line prompt addition over a new workflow section

### 4. Write the plan

Output to `data/trajectory/{user_id}/{chat_id}/implementation_plan.md`.

Each change should include: what file to edit, what the current code does, what to change and why, how to verify the fix.

Prioritize by impact/effort — smallest high-impact changes first.

Include a Risks / Unknowns section for anything uncertain.

## Code ownership map

| Area | Files |
|---|---|
| Agent prompt | `varro/prompts/agent/rigsstatistiker.j2` |
| Tool behavior and prompts (Sql, ColumnValues, Jupyter, Read/Write/Edit, Bash) | `varro/agent/assistant.py` |
| Tool behavior (Bash sandbox) | `varro/agent/bash.py` |
| Tool behavior (Read/Write/Edit) | `varro/agent/filesystem.py` |
| Tool behavior (Snapshot) | `varro/agent/snapshot.py` |
| IPython shell | `varro/agent/ipython_shell.py` |
| Agent workspace | `varro/agent/workspace.py` |
| Fact table context docs | `varro/context/fact_table.py` |
| Dimension table context docs | `varro/context/dim_table.py` |
| Subject hierarchy docs | `varro/context/subjects.py` |
| Context utilities (fuzzy match) | `varro/context/utils.py` |
| Data ingestion | `varro/data/statbank_to_disk/`, `varro/data/disk_to_db/` |
| Dimension linking | `varro/data/fact_col_to_dim_table/` |
| Dashboard framework | `varro/dashboard/` |
| Chat runtime | `varro/chat/` |
| Trajectory generation | `varro/playground/trajectory.py` |
| Playground CLI | `varro/playground/cli.py` |
| UI components | `ui/components/`, `ui/app/` |
| App routes | `app/routes/` |
| Tests | `tests/` mirrors `varro/` structure |
| Config / paths | `varro/config.py` |

## Relationship to other skills

- `$playground-explorer` — interactive probing, produces findings
- `$analyse-trajectory` — retrospective audit, produces findings
- `$findings-to-plan` — reads findings, traces to code, writes implementation plan