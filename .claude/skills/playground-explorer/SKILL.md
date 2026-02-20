---
name: playground-explorer
description: >
  Interactive trajectory exploration for the Varro playground. Use this skill to
  probe agent behavior live, inspect observations/actions as they unfold, and
  produce actionable improvements to tools, prompts, docs, and UI-as-agent-tools.
---

# Playground Explorer

## Mission

Explore how the AI agent behaves on a subject through iterative questioning,
inspect trajectory artifacts as they are produced, and propose environment
improvements that make better trajectories easier.

The playground is the environment in the observation-action loop where tools and
UI are the agent interface:

```
observe → decide → act → observe ...
```

## Primary execution path (CLI-first)

Use the playground CLI as the default path for all probes:

```bash
uv run python -m varro.playground.cli
```

Optional:

```bash
uv run python -m varro.playground.cli --user-id 1 --chat-id 62 --current-url /dashboard/boligpriser-sammenligning
```

Use commands during exploration:

- `:status`
- `:url <path>`
- `:trajectory [turn_idx]`
- `:snapshot [url]`

Avoid non-CLI trajectory generation unless blocked.

## Workflow

1. Start or resume a CLI session.
2. Define a subject and exploration goal.
3. Ask one probe question at a time, like a human investigator.
4. After each turn, inspect:
   - final response,
   - trajectory artifacts (`turn.md`, `tool_calls/`, `images/`),
   - URL/snapshot artifacts when relevant.
5. Record what changed in behavior and why.
6. Continue targeted follow-up probes until root causes are clear.
7. Write or update `findings.md`.

## Exploration rubric

Do not start from "was the answer correct?" Start from trajectory mechanics:

- What observation did the agent receive?
- Why did that observation lead to this action?
- What missing or ambiguous signal created extra steps or uncertainty?
- What is the smallest change in tool output, prompt, docs, or UI that would improve the next decision?

Correctness matters when it reveals environment gaps.

## Scope boundaries

In scope:

- Tool output shape and clarity
- Tool instructions and prompt clarity
- Documentation discoverability and task-fit guidance
- URL/state ergonomics
- Snapshot usability
- Dashboard as communication surface for agent and user

Out of scope:

- Broad model capability judgments without environment evidence

## Output contract

Always write (or update):

`data/trajectory/{user_id}/{chat_id}/findings.md`

Each finding must include:

- `Hypothesis`
- `Probe` (question + optional URL context)
- `Observed Trajectory Evidence` (turn/step/tool refs)
- `Interpretation`
- `Proposed Change`
- `Expected Trajectory Delta`
- `Validation Probe`

Template:

```markdown
# Findings: Chat {chat_id}

## Exploration Goal
{What subject/behavior was explored and why}

## Findings

### {short title}
**Hypothesis**: {what you expected}
**Probe**: {question asked, optional URL}
**Observed Trajectory Evidence**: {turn/step/tool references}
**Interpretation**: {why behavior emerged}
**Proposed Change**: {specific system change}
**Expected Trajectory Delta**: {steps removed / decision clarified}
**Validation Probe**: {next question to verify change}

## Prioritized Actions
1. {highest impact, lowest effort first}
2. {next}
```

## Stopping criteria

Stop when one of the following is true:

- Root causes are clear and supported by trajectory evidence.
- Additional probes are not changing conclusions.
- You have at least one high-impact, testable proposed change with a validation probe.

## Relationship to other skill

Use `$analyse-trajectory` for retrospective audit of completed chats.
Use `$playground-explorer` for interactive probing and improvement discovery.
