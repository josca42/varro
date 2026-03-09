---
name: dashboard-builder
description: >
  Collaborate with the AI statistician to create a polished data dashboard.
  Use when given a topic brief, research question, or set of DST table references
  and asked to produce a dashboard. Drives the full loop: data exploration →
  dashboard creation → validation → visual inspection → iteration. Invoke with
  a startup prompt describing the subject, key data angles, and desired
  dashboard concept.
---

# Dashboard Builder

## Mission

Drive an iterative conversation with the AI statistician (via the playground
CLI) to produce a publication-quality dashboard on a given topic. Act as an
editorial director: set the analytical direction, evaluate outputs, and push
for improvements until the dashboard communicates its story clearly.

## Execution flow

### 1. Prepare the brief

The user supplies a startup prompt. Extract from it:

- **Subject** — the topic or question the dashboard should answer
- **Data angles** — specific DST tables, indicators, or metrics to explore
- **Dashboard concept** — desired charts, comparisons, or narrative structure

If any of these are unclear, ask before starting.

### 2. Start a CLI session

```bash
uv run python -m varro.playground.cli --user-id 1
```

Or resume an existing chat:

```bash
uv run python -m varro.playground.cli --user-id 1 --chat-id <id>
```

Use interactive mode (not piped) so shell state persists across turns.

### 3. Explore the data (1–3 turns)

Send exploration prompts to the statistician. Guide it to:

- Discover which tables have the relevant data
- Run initial SQL queries to understand what's available
- Identify the right dimensions, time ranges, and breakdowns

Keep exploration focused. The goal is to gather enough understanding to plan
a good dashboard — not to exhaustively analyze every angle.

### 4. Commission the dashboard (1 turn)

Send a clear dashboard request that includes:

- Dashboard name (slug)
- Which queries and outputs to create
- Layout structure (metrics row, tabs, grid)
- Filter dimensions (region, time period, etc.)
- Narrative framing — brief markdown text between charts

Be specific about the story the dashboard should tell. The statistician builds
better dashboards when given a clear editorial direction.

### 5. Validate and inspect

After the statistician creates the dashboard:

1. Check the CLI output for any errors during creation.
2. Use `:trajectory` to inspect what the agent did if needed.
3. Read the created dashboard files directly to verify structure:
   - `queries/*.sql` — check SQL correctness
   - `outputs.py` — check output functions
   - `dashboard.md` — check layout and narrative

### 6. Iterate (1–3 turns)

Based on inspection, send follow-up messages to fix or improve:

- SQL errors or empty results
- Missing or misleading chart labels
- Better filter defaults
- Additional tabs or metrics
- Narrative text that contextualizes the data

### 7. Final validation

Once satisfied:

1. Ask the statistician to run `ValidateDashboard` and `Snapshot`
2. Read the snapshot PNG to visually verify the dashboard
3. Read `metrics.json` to verify metric values make sense

### 8. Record results

After the dashboard is complete, note:

- The chat ID used (for trajectory reference)
- The dashboard slug and URL
- Any data caveats or limitations discovered
- Key editorial decisions made during iteration

## Conversation strategy

**Be directive, not vague.** Instead of "make a dashboard about housing," say
"Create a dashboard at /dashboard/boligmarked that shows property price indices
by region since 2010, with a filter-select for region and filter-date for
period. Include metrics for latest price index and year-over-year change.
Use tabs to separate price trends from sales volume."

**One major change per turn.** Don't ask for five fixes at once. The
statistician handles focused requests better than sprawling ones.

**Read before asking for changes.** Always read the current dashboard files
before requesting modifications. Reference specific lines or output names.

**Use the snapshot as ground truth.** The PNG shows what users will actually
see. If it looks wrong, that's what matters — not whether the code seems right.

## Shell state reminder

Interactive CLI mode preserves dataframes across turns. The statistician can
reference exploration results when building the dashboard. If you restart the
CLI process, previous dataframes are lost — the agent will need to re-query.

## Stopping criteria

Stop when:

- Dashboard validates without errors
- Snapshot PNG shows a clear, well-structured layout
- Metrics and charts tell a coherent story
- Narrative text contextualizes the data for a general audience
