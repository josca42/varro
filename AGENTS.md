# Code style
When writing code then only include essential comments. Otherwise leave comments out.

Prefer simple and concise code. Do not implement a lot of try/except instead let code fail.

# Work dir
Use the following folder as working directory: agents

- Put scripts you make in agents/scripts
- General notes or updates to notes in agents/notes
- Task specific notes in agents/tasks. In general create a new folder in agents/tasks and put your notes related to the task there.

When doing a task check if there are relevant notes in agents/notes

# Goal
The goal of this repo is to create a better version denmark statistics "statistikbank" that can be used by AI analyst and human analysts alike. 
All the data from denmark statistics is currently downloaded to disk. The data is organised as fact tables and dimension tables.

# Assistants
You have access to a research assistant that can analyze the data for you. The assistant analyzes the data using the tools in the skills folder .claude/skills .

You have access to the research assistant through the bash terminal

```bash
claude -p "Give me an overview of the dimension tables"
```

# Context
Denmark’s StatBank export lives on disk as ~2000 fact tables (Parquet) plus ~40 dimension tables; they form a classic star schema that we ingest into Postgres under the fact and dim schemas using the scripts in varro/data/disk_to_db/. Every fact table is normalized during loading (lower-case ASCII column names, parsed tid, etc.), while each dimension exposes kode, niveau, titel, and related metadata for decoding categorical codes.