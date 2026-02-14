---
name: chat-review
description: Generate and inspect chat review reports. Use when a user wants to review a chat conversation, inspect what happened in a chat, see tool calls/results, or create a readable summary of a chat session. Triggers on requests like "review chat 61", "what happened in this chat", "show me the chat history".
---

# Chat Review

## Generate a review

```bash
python -c "from varro.chat.review import review_chat; print(review_chat(user_id=USER_ID, chat_id=CHAT_ID))"
```

Idempotent — only new turns are processed on repeat calls.

## Output location

`mnt/chat_reviews/{user_id}/{chat_id}/`

```
chat.md              # overview with per-turn summaries
0/
  turn.md            # full turn detail
  summary.md         # 3-line summary used to build chat.md
  tool_calls/        # SQL queries, Jupyter code, large results
  images/            # extracted user/tool images
1/
  ...
```

## Inspect

1. Read `chat.md` for the overview
2. Read `{turn_idx}/turn.md` for full detail on a specific turn
3. Read files in `tool_calls/` and `images/` for artifacts

## Delete a review

```python
import shutil
from varro.config import REVIEWS_DIR
shutil.rmtree(REVIEWS_DIR / str(user_id) / str(chat_id))
```
