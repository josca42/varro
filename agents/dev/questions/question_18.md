# Question 18: Dashboard om turisme (when one already exists)

Use question 18 from `agents/dev/test_plan.md` as a starter for exploring the varro agent using the playground-explorer skill in `.claude/skills/playground-explorer/SKILL.md`. For how to interpret the trajectory see `.claude/skills/analyse-trajectory/SKILL.md`.

**Prerequisite**: Run this after question 13 has been completed and a tourism dashboard exists at `/dashboard/`.

## Opening question

> Lav et dashboard om turisme

## Behavior

Behave like a curious but non-expert user, not a tester. Start with the question as written — don't add specifics the original doesn't have. Then respond naturally to what the agent shows you:

- If it asks clarifying questions, answer them but don't over-specify. Let the agent guide you toward interesting angles.
- If it shows data or charts, react to what's interesting and ask follow-ups. ("Hvad med forskellen mellem X og Y?", "Kan du vise det over tid?")
- If it offers to create a dashboard, say yes. If it builds up a good analysis without offering, ask for one after 3-4 turns.
- Once a dashboard exists, ask to navigate to it, try a filter, and request at least one change.

Aim for 3-6 turns total. Don't rush to the dashboard.

## Additional focus for this question

Pay special attention to whether the agent checks `/dashboard/index.md` and surfaces the existing tourism dashboard before creating a new one.

## Findings

After the conversation, write `findings.md` evaluating these dimensions:

1. **Collaboration quality** — Did the agent clarify scope before diving in, or did it jump to building? Did it show intermediate results and let you steer? Did it check for existing dashboards?
2. **Exploration → dashboard transition** — Was the move to dashboard natural (offered after substantive exploration) or premature?
3. **Dashboard execution** — Did it reuse queries from the exploration? Did validation and snapshot pass? Is the result coherent?
4. **Standard trajectory quality** — Tool efficiency, unnecessary steps, instruction gaps (per the normal evaluation framework).
