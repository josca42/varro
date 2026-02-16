---
name: chat-review
description: Generate and inspect chat review reports. Use when a user wants to review a chat conversation, inspect what happened in a chat, see tool calls/results, or create a readable summary of a chat session. Triggers on requests like "review chat 61", "what happened in this chat", "show me the chat history".
---

# Chat Review

## Generate a review

```bash
uv run python -c "from varro.chat.review import review_chat; print(review_chat(user_id=USER_ID, chat_id=CHAT_ID))"
```

Idempotent:
- Turn files are regenerated only when `turn.md` is missing or `.review_version` is outdated.
- `chat.md` is rebuilt from `.mpk` turns each run.

## Output location

`mnt/chat_reviews/{user_id}/{chat_id}/`

```
chat.md              # overview with user/tools/final excerpt + details link
0/
  turn.md            # full turn detail
  .review_version    # renderer format version
  tool_calls/        # SQL queries, Jupyter code, large results
  images/            # extracted user/tool images
1/
  ...
```

`turn.md` structure:
- `User`
- `Trajectory` with `Step N` sections
- Step fields: `Thinking`, `Actions`, `Observations`
- `Final response`
- `Usage`

Observation notes:
- Multiline outputs are plain markdown text.
- No `→` markers are used.

## Inspect

1. Read `chat.md` for the overview across turns.
2. Read `{turn_idx}/turn.md` for full trajectory detail on a turn.
3. Read files in `tool_calls/` and `images/` for extracted artifacts.
