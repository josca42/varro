This project aims to create the danish AI state statistician. An expert AI analyst that help users understand data about denmark.

# Agent notes

Use the `agents/` folder for project notes and learnings.
The notes index is [index.md](agents/index.md).

If you have learned something during a conversation then update the notes in the `agents/` folder, so you can use these learnings in a future work session.
If new features are implemented or existing features changed then also update notes accordingly.

If you have deleted a feature then remove corresponding notes to keep notes up to date.

Not everything needs to be written down. Use your judgement

# Code style

Elegant minimalism. Every line should earn its place.

**No commentary.** Only include essential comments. If the code needs a comment to be understood, consider rewriting the code. Don't add docstrings, type annotations, or comments to code you didn't change.

**Let it fail.** No defensive try/except. Let exceptions propagate with clear tracebacks. Only catch exceptions at system boundaries where you need to convert them (e.g. `ModelRetry` for the AI agent, cleanup in async lifecycle).

**Convention over configuration.** Use the patterns already in the codebase. Module-level constants for config, `snake_case` for functions and variables, `PascalCase` for classes, direct absolute imports. Don't introduce new patterns when existing ones work.

**No backwards compatibility.** Unless specifically requested, don't preserve old interfaces. No renamed `_vars`, no re-exports, no shims. Delete what's unused.

**Functions over classes.** Use plain functions for logic, dataclasses/Pydantic models for data. Only use classes when there's genuine state to manage (CRUD, database models). A factory function is almost always better than inheritance.

**Small functions, flat modules.** Keep functions under ~50 lines. Keep directory nesting to 2–3 levels. If a module grows past ~400 lines, split it. Group related functions as sibling modules in a package, not as methods on a class.

# Design principles

**State as values.** Each interaction produces immutable values on disk. A chat turn is serialized to `{idx}.mpk` and never modified. A dashboard snapshot freezes outputs as PNG, parquet, and JSON files. The current state is the ordered collection of these values — not a mutable place that gets updated.

**Explicit transitions.** The AI agent is the transition function: `(prior_turns, user_message) → new_turn_value`. Tool calls within a turn are the steps of the transition. Keep this boundary clean — the agent reads values, calls tools, produces a new value.

**Filesystem reflects the app.** Dashboards are markdown + SQL + Python files. Chat turns are ordered files in a directory. Trajectories are derived markdown in a parallel tree. If you can understand the app by reading files on disk, then an AI agent can too — and crucially, an AI trajectory analysis agent can evaluate how well the system performed.

**Don't complect.** Keep independent concerns separate:
- Source vs derived: `chat/` (immutable .mpk) vs `trajectory/` (regenerable .md)
- Identity vs state: a chat ID is an identity; its state is the sequence of turn values
- Layout vs data vs transforms: `dashboard.md` vs `queries/` vs `outputs.py`

**Built for trajectory analysis.** The trajectory system (`varro/playground/trajectory.py`) generates readable markdown and extracted tool calls from binary turn data. The primary consumer is an AI trajectory analysis agent that evaluates system performance — inspecting real user conversations, investigating bugs, and identifying where the statistician agent struggled or could be helped by better tool outputs. Optimizing for AI reviewability means: text over binary, extracted code over inline blobs, clear structure over compact encoding.

When adding new features, ask: can the result be represented as an immutable value on disk? Can an AI analysis agent inspect it by reading files? Is the transition function explicit? If yes, the feature will compose well with the rest of the system.

More details are in `docs/Design thoughts.md`

# The project consists of 3 parts:

**ui**: A ui library in the ui/ folder. The ui library is structured to follow the code style and organisation of shadcn-ui, where larger app components are in ui/app and more specific components are in ui/components. Custom css is in ui/theme.css.

stack: fasthtml, daisy-ui, alpine.js, HTMX

**app**: The web app in the app/ folder. The app should use ui components from the ui library and if a new component is needed in the app then that component is added to the ui library and then imported into the app code. 

stack: fasthtml, HTMX

**varro**: The library varro implements the main functionality.
- /agent: An AI agent is implemented using pydantic-ai and given access to various tools
- /context: Table metadata from denmark statistics is used to create a README.md for the different tables and groups of tables.
- /dashboard: Implementing a custom markdown to html parser that allows creating dashboards from some sql queries, python code for tables and plotly plots and a dashboard markdown file. queries, plot and table code and the dashboard.md is used to create an interactive dashboard using fasthtml and htmx.
- /data: Code for downloading tables and metadata from denmarks statistics to disk and then adding the data to a local postgres db.
- /db: database connection strings and table models and crud methods implemented using SQLModel.
- /prompts: Jinja2 templates for system prompts used by the AI agent and data cleaning processes.
- /config.py: Central configuration for data directories and paths.

stack: pandas, pydantic-ai, SQLModel, SQLAlchemy, plotly, fasthtml, HTMX, mistletoe, postgres

# Inspecting app

You can run the app by doing

```bash
uv run python app/main.py
```

The app will then be running at http://0.0.0.0:5001/

In general use uv run python to run python scripts and code
