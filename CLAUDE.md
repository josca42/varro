# Code style
When writing code then only include essential comments. Otherwise leave comments out.

Prefer simple and concise code. Do not implement a lot of try/except instead let code fail.

# Work dir
Use the following folder as working directory: agents

- Put scripts you make in agents/scripts
- General notes or updates to notes in agents/notes
- Task specific notes in agents/tasks. In general create a new folder in agents/tasks and put your notes related to the task there.


# Skills
When doing task you have the following skills at your disposal:

- Subjects: For exploring tables from denmarks statistics through a subjects hierarchy and for accessing metadata about the tables
- Tables: For previewing tables and seeing their schema and the first n rows.
- Sql: For executing sql queries against a postgres database. Currently all tables are on disk as parquet files but should be moved to postgres db.

# Answer style
If you make a markdown file with detailed notes about a question or create relevant python code files. Then you can always reference these in a final answer by providing the file paths.