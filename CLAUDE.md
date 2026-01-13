This project aims to create the danish AI state statistician. An expert AI analyst that help users understand data about denmark.

## The project consists of 3 parts:

**ui**: A ui library in the ui/ folder. The ui library is structured to follow the code style and organisation of shadcn-ui, where larger app components are in ui/app and more specific components are in ui/components. Custom css is in ui/theme.css.

stack: fasthtml, daisy-ui, alpine.js, HTMX

**app**: The web app in the app/ folder. The app should use ui components from the ui library and if a new component is needed in the app then that component is added to the ui library and then imported into the app code. 

stack: fasthtml, HTMX

**varo**: The library varro implements the main functionality. 
- /agent: An AI agent is implemented using pydantic-ai and given acces to various tools
- /chat: Placeholder folder for ui functionality related to having a chat between the AI agent and the user.
- /context: Table metadata from denmark statistics is used to create a README.md for the different tables and groups of tables.
- /dashboard: Implementing a custom markdown to html parser that allows creating dashboards from some sql queries, python code for tables and plotly plots and a dashboard markdown file. queries, plot and table code and the dashboard.md is used to create an interactive dashboard using fashtml and htmx.
- /data: Code for downloading tables and metadata from denmarks statistics to disk and then adding the data to a local postgres db.
- /db: database connection strings and table models and crud methods implemented using SQLModel.

stack: pandas, pydantic-ai, SQLModel, SQLAlchemy, plotly, fasthtml, HTMX, mistletoe, postgres

## Docs

I have gathered a set of useful docs

fasthtml: agent/docs/fasthtml.txt, agent/docs/fasthtml_best_practices.md
daisy-ui: agent/docs/daisy-ui.txt
alpine.js: agent/docs/alpine_js/*
url-design: agent/docs/url_design.txt
