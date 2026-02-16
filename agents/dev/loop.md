# Dev Loop

A repeating cycle — **Test → Review → Implement** — where all three roles are Claude agents. Each cycle produces artifacts in a numbered folder under `agents/dev/cycles/`.

## The Cycle

### 1. Test

The tester agent walks through the app using questions from [test_plan.md](test_plan.md). For each question it:

- Opens a new chat (or continues an existing one)
- Asks the question and observes the agent's response
- Takes screenshots of the UI using `url_to_png()` from `varro/agent/playwright_render.py`
- Notes issues: wrong answers, broken UI, slow responses, confusing output

**Produces:** `test.md` with per-question observations and screenshots in `assets/`.

### 2. Review

The reviewer agent analyzes the chats from the test phase. It:

- Generates chat reviews using `review_chat(user_id, chat_id)` from `varro/chat/review.py`
- Reads through the tester's `test.md` observations
- Inspects tool call trajectories for inefficiencies or errors
- Identifies patterns across multiple chats

**Produces:** `review.md` with trajectory analysis and improvement suggestions.

### 3. Implement

The implementer agent works through the task list. It:

- Reads `review.md` for context on each issue
- Implements fixes, one task at a time
- Checks off completed tasks in `tasks.md`

**Produces:** code changes + updated `tasks.md`.

## Folder Convention

```
agents/dev/cycles/
  01/
    test.md        # tester output
    review.md      # reviewer output
    tasks.md       # task list for implementer
    assets/        # screenshots
  02/
    ...
```

## Kicking Off Each Phase

### Test phase
```
Run questions from test_plan.md against the app at http://0.0.0.0:5001/.
Record observations in agents/dev/cycles/{N}/test.md.
Save screenshots to agents/dev/cycles/{N}/assets/.
```

### Review phase
```
Generate chat reviews for the chats tested in cycle {N}.
Read agents/dev/cycles/{N}/test.md.
Write analysis to agents/dev/cycles/{N}/review.md.
Produce agents/dev/cycles/{N}/tasks.md.
```

### Implement phase
```
Read agents/dev/cycles/{N}/review.md and tasks.md.
Work through tasks, checking them off as completed.
```

## Agent Prompts

TODO: fill in specific system prompts for each agent role.
