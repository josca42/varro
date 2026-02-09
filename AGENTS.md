This project aims to create the danish AI state statistician. An expert AI analyst that help users understand data about denmark.

# Agent notes

Use the `agents/` folder for project notes and learnings.
The notes index is [index.md](agents/index.md).

If you have learned something during a conversation then update the notes in the `agents/` folder, so you can use these learnings in a future work session.
If new features are implemented or existing features changed then also update notes accordingly.

If you have deleted a feature then remove corresponding notes to keep notes up to date.

Not everything needs to be written down. Use your judgement

# Code style
When writing code then only include essential comments. Otherwise leave comments out.

Prefer simple and concise code. Do not implement a lot of try/except instead let code fail.

Convention over configuration.

Do not keep backwards compability unless specifically requested. Always assume that backward compability is not important. What's important is simple and concise code.

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
