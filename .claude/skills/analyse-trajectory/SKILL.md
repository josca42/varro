---
name: analyse-trajectory
description: >
  Review and evaluate agent conversations to find improvements for tooling,
  instructions, and documentation. The goal is NOT to judge answer correctness
  but to identify what system changes would help the agent take better trajectories.
  Use when asked to: review a chat, evaluate agent performance, find tooling
  improvements, analyze a conversation, inspect what happened in a chat, or when
  given a chat ID to review.
---

# Analyse Trajectory

## Generate trajectory files

```bash
uv run python -c "from varro.playground.trajectory import generate_chat_trajectory; print(generate_chat_trajectory(user_id=USER_ID, chat_id=CHAT_ID))"
```

Idempotent: turns regenerate only when `turn.md` is missing or `.trajectory_version` is outdated.

## Trajectory file structure

Output at `data/trajectory/{user_id}/{chat_id}/`:

```
chat.md                    # one-line summary per turn: user input, tools, final excerpt
system_instructions.md     # full system prompt given to the agent
tool_instructions.md       # all tools with descriptions and parameter schemas
{turn_idx}/
  turn.md                  # trajectory: User → Steps (Thinking/Actions/Observations) → Final response → Usage
  tool_calls/              # extracted .sql, .py, large .txt results
  images/                  # extracted plots and images
```

## Review process

1. Read `chat.md` for the overview
2. Read `system_instructions.md` and `tool_instructions.md` once to understand what the agent was given
3. For each turn, read `turn.md` and inspect extracted artifacts in `tool_calls/`
4. Evaluate each turn against the framework below
5. Write findings to `data/trajectory/{user_id}/{chat_id}/findings.md`

## Evaluation framework

Focus on what **system builders can change** (instructions, tools, documentation), not on what the model should have known.

### Instructions quality

Does the system prompt give the agent precise enough guidance?

- Agent guessing at workflow steps that instructions could have specified
- Agent ignoring instructions that exist (too buried or unclear)
- Missing guidance for a common question pattern
- Ambiguity that caused the agent to pick a suboptimal path

### Tool adequacy

Do tools return clear, actionable output that makes the next decision obvious?

- Tool output missing information the agent needed next (row count, available levels, column names)
- Agent calling the same tool repeatedly to get information one call could have returned
- Agent working around a tool limitation using Bash/SQL when a dedicated tool or a small tool change would be cleaner
- Tool descriptions that are misleading or incomplete
- Fuzzy matching returning unhelpful results

### Trajectory efficiency

Did the agent take unnecessary steps because of instruction or tool gaps?

- Steps that only exist because prior tool output was incomplete
- Exploratory steps that instructions could have eliminated
- Repeated queries that differ only in filter values the agent was searching for
- Trial-and-error discovery of something documentation could have stated

### Relevance

Is the user question within scope for the state statistician?

- Questions the agent shouldn't need to handle (general chat, non-data questions)
- Questions that are borderline — note whether the agent should redirect or attempt

## Output format

Write findings to `data/trajectory/{user_id}/{chat_id}/findings.md`:

```markdown
# Review: Chat {chat_id}

## Summary
{1-3 sentences: what the user asked, overall assessment of how the system supported the agent}

## Findings

### {short title}
**Dimension**: {Instructions | Tool | Trajectory | Documentation}
**Turn**: {turn_idx}, Step {step_idx}
**Observation**: {What happened — reference actual tool calls and results}
**Suggestion**: {Concrete change to instructions, tool output, or documentation}
**Impact**: {Steps saved, or what class of questions this helps}

...

## Verdict
{The single most impactful improvement from this review}
```

**Guidelines:**
- Be concrete. Reference actual step numbers, tool calls, and results.
- Suggest specific changes. "Add row count to Sql tool output" not "improve tool output."
- Estimate impact. "Would save 2-3 steps for geographical queries" is useful.
- One finding per root cause. Group repeated issues across turns.
- Skip clean turns — only note what can be improved.

## Agent environment (reference)

The reviewed agent (Rigsstatistikeren) operates in a sandboxed filesystem:

```
/subjects/{root}/{mid}/{leaf}.md   — subject overviews listing available tables
/fact/{root}/{mid}/{leaf}/{id}.md  — per-table docs: columns, joins, value ranges
/dim/                              — dimension table docs
/dashboard/                        — saved dashboard definitions
/skills/                           — guides for complex tasks (e.g., dashboard creation)
```

Tools: `ColumnValues`, `Sql`, `Jupyter`, `Read`, `Write`, `Edit`, `Bash`, `UpdateUrl`, `Snapshot`, `WebSearch`

Typical efficient trajectory for data analysis:
1. Identify subject area → `Bash ls`
2. Read subject overview → `Read`
3. Read table docs → `Read`
4. Check column values → `ColumnValues`
5. Query data → `Sql` with `df_name`
6. Visualize → `Jupyter` with `show`
7. Explain → final response
