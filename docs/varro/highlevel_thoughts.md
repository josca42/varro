# Running notes

This document is a living summary of the spoken design walkthrough for a Python web app built with **FastHTML + HTMX**, backed by **Postgres** (via **SQLModel / SQLAlchemy**) and **pydantic-ai** agents.

## Core design philosophy

### File over app

* Prefer **files as the primary unit of composition** over a tightly-coupled “application object” mindset.
* Motivation: make the system **easy for an AI agent to generate and navigate**, especially for dashboards and content-driven features.

### HTML as application state

* Prefer an **HTML-native** server-rendered approach.
* Treat **HTML as the application state** returned from routes.
* Avoid “JSON API + SPA client state” as the default.
* Motivation: keep **control and state on the server**, reduce client-side complexity, and make agent-driven navigation/inspection straightforward.

## App purpose and domain

* Build an AI **“statistician”** that can work with **Statistics Denmark (StatBank/DST)** data.
* Data access:

  * All tables are materialized/ingested into **Postgres**.
  * Accessed via **SQLModel / SQLAlchemy** from Python.
* Documentation access:

  * Table documentation is stored as **markdown files**.
  * Organized in a **subject hierarchy** (browseable taxonomy).

## Agent workflow goal

1. User asks a question.
2. The statistician/analyst agent:

   * locates relevant fact/dim tables via **subject-hierarchy docs** (markdown on disk)
   * queries **Postgres** using **SQL**
   * uses **Python** for transformations and visualizations
3. As the analysis stabilizes, the agent **packages it as a dashboard** so it can be revisited, iterated, and expanded across future chat sessions.

## Computation model

* **SQL** is the primary data access language (Postgres).
* **Python** runs in a **stateful Jupyter notebook** to:

  * keep analysis state between steps
  * perform non-trivial transformations
  * generate figures/visualizations

## Dashboard lifecycle and spec

* A dashboard is created by writing a **dashboard markdown file** and dumping companion artifacts as defined in `dashboard_spec`, typically:

  * `dashboard.md` (markdown + custom tags)
  * `queries/{query_name}.sql` (named SQL queries referenced from the markdown)
  * `figures.py` (plugin figure functions/modules when needed)
* The server converts the dashboard markdown to **HTML** and serves it.
* Key property: the markdown format is **token-efficient** and easy for both **humans and AI agents** to read and edit.

## Documentation and table organization

* Table access + documentation is central to correctness:

  * `dim.*` holds **dimension tables**
  * `fact.*` holds **fact tables**
  * fact tables are organized into a **subject hierarchy**; docs mirror this hierarchy as markdown files

## Filesystem as the durable state store

* The agent primarily uses **filesystem-native commands** to:

  * find and read documentation
  * update documentation when user preferences/interpretations emerge
  * create/edit dashboards by editing markdown + companion files
* Docs and dashboards act as evolving “memory”:

  * user preferences can be written back into table docs
  * dashboards capture good analysis patterns for reuse

## Dashboard/content model

### Markdown-first dashboards

* Dashboards are authored as **markdown**.
* A **custom markdown syntax** (custom tags / directives) is used to turn markdown into **server-rendered HTML dashboards**.

## URL as the primary state carrier

* The **URL encodes application state** (selected dashboard, settings page, dashboard filters, etc.).
* URLs are designed to be:

  * **human-readable**
  * **conventional / predictable**
  * **easy to mutate** (especially by an AI agent)
* Motivation: an agent can **navigate the entire app by constructing/updating URLs**, rather than relying on hidden client-side state.

## Intended outcome

* An architecture that is:

  * **server-centric** (minimal client logic)
  * **agent-friendly** (easy to generate, introspect, and operate)
  * **content-driven** (dashboards as files/markdown)
  * **URL-driven** (state is explicit and shareable)
