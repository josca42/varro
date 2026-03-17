---
name: ask-statistician
description: >
  Ask the Varro AI statistician questions about Danish statistics and data.
  Use when you need to query Denmark's statistical data, create dashboards,
  or publish dashboards. Supports multi-turn conversations with --chat-id.
---

# Ask Statistician

Send questions to the AI statistician and get text answers back.

## Ask a question

```bash
uv run python .claude/skills/ask-statistician/scripts/ask.py "What is the population of Denmark?"
```

Resume a conversation (multi-turn):

```bash
uv run python .claude/skills/ask-statistician/scripts/ask.py --chat-id 42 "Break that down by region"
```

Output format (one line per field, parseable):

```
chat_id: 42
current_url: /dashboard/befolkning
response: The population of Denmark is approximately 5.9 million...
```

Save the `chat_id` from the first call to reuse in follow-ups. The `current_url` tracks what dashboard the statistician navigated to.

## Create a dashboard

Ask the statistician to create a dashboard. Be directive about structure:

```bash
uv run python .claude/skills/ask-statistician/scripts/ask.py "Create a dashboard showing housing prices by region since 2010"
```

The statistician will create the dashboard files and navigate to it. The `current_url` in the output tells you the dashboard path.

## Publish a dashboard

After the statistician creates a dashboard, publish it to get a public URL:

```bash
uv run python .claude/skills/ask-statistician/scripts/publish.py --slug boligpriser
```

Output:

```
url: https://varro.dk/public/1/boligpriser
```

## Options

Both scripts accept `--user-id N` (default: 1).

`ask.py` also accepts:
- `--chat-id N` — resume an existing chat (omit to create new)
- `--current-url /path` — set the initial dashboard URL context

## Shell state

Each `ask.py` invocation starts a fresh Jupyter shell. The statistician re-queries data as needed. Message history persists across turns via `--chat-id`, so the agent has full conversational context.

## Timeouts

Agent runs can take 30-120 seconds for complex queries. Use a generous timeout (e.g. 300000ms) when calling the scripts.
