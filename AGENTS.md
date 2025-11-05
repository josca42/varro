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
The goal of this repo is move data from denmarks statistics in a local postgres database. The table is downloaded to disk. The data is organised as fact tables and dimension tables.
The current task is now to insert the tables into the postgres database and do it such that the database has a simple schema that is easy to query. Part of the process is to create documentation and helper tools that makes it easy for an experienced data analyst, who has never seen the data before to explore the data and create the relevant sql queries for performing an analysis.

# Assistants
You have access to a research assistant that can analyze the data for you. The assistant analyzes the data using the tools in the skills folder .claude/skills .

You have access to the research assistant through the bash terminal

```bash
claude -p "Give me an overview of the dimension tables"
```

You can also ask for assistance from a highly skilled researcher on difficult design decisions. This is done by compiling a markdown file containing a detailed overview of what should be researched along with links to relevant files (links should be made using the relative file paths). Then the user will submit research request to the expert researcer.The researcher only has access to the markdown file and the files linked in the markdon file.