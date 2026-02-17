---
name: chat-review
description: >
  Retrospective audit of completed agent chats to identify concrete improvements
  to instructions, tools, and documentation. This is post-hoc analysis, not an
  interactive exploration loop.
---

# Chat Review

## When to use this skill

Use `$chat-review` when you already have a completed chat (or set of chats) and
you want a concise audit of what happened and what should be improved.

Use `$playground-explorer` instead when you want to iteratively ask new
questions, inspect trajectories as they unfold, and probe hypotheses in the
playground.

## Generate review files

```bash
uv run python -c "from varro.playground.review import review_chat; print(review_chat(user_id=USER_ID, chat_id=CHAT_ID))"
```

Idempotent: turns regenerate only when `turn.md` is missing or `.review_version` is outdated.

## Review file structure

Output at `mnt/chat_reviews/{user_id}/{chat_id}/`:

```
chat.md                    # one-line summary per turn: user input, tools, final excerpt
system_instructions.md     # full system prompt given to the agent
tool_instructions.md       # all tools with descriptions and parameter schemas
{turn_idx}/
  turn.md                  # trajectory: User → Steps (Thinking/Actions/Observations) → Final response → Usage
  tool_calls/              # extracted .sql, .py, large .txt results
  images/                  # extracted plots and images
```

## Review process (retrospective)

1. Read `chat.md` for the overview
2. Read `system_instructions.md` and `tool_instructions.md` once
3. For each turn, read `turn.md` and inspect extracted artifacts in `tool_calls/`
4. Evaluate root causes and propose concrete system changes
5. Write findings to `mnt/chat_reviews/{user_id}/{chat_id}/findings.md`

## Evaluation framework

Focus on what system builders can change (instructions, tool output, docs), not
what the model "should have known."

### Instructions quality

- Missing workflow guidance for common question patterns
- Ambiguous wording that led to suboptimal trajectories
- Guidance that exists but is hard to follow in practice

### Tool adequacy

- Output missing key next-step signals (row count, levels, column names)
- Repeated tool calls to collect information that should be returned once
- Tool descriptions that are misleading, incomplete, or hard to operationalize

### Trajectory efficiency

- Detours caused by unclear observations
- Repeated near-identical queries during discovery
- Trial-and-error that clearer docs or tool output could remove

## Output format

Write findings to `mnt/chat_reviews/{user_id}/{chat_id}/findings.md`:

```markdown
# Review: Chat {chat_id}

## Summary
{1-3 sentences: request + overall system support quality}

## Findings

### {short title}
**Dimension**: {Instructions | Tool | Trajectory | Documentation}
**Turn**: {turn_idx}, Step {step_idx}
**Observation**: {What happened with references}
**Suggestion**: {Specific system change}
**Impact**: {Expected effect on trajectory quality}

## Verdict
{Single most impactful improvement}
```

Note: exploratory sessions produced with `$playground-explorer` may provide
richer evidence trails; this retrospective format should summarize those into
clear, actionable changes.

## Playground definition

In Varro, the playground is the environment in the observation-action loop where
tools and UI are the agent interface:

```
observe → decide → act → observe ...
```
