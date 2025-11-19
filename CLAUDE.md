# Code style
When writing code then only include essential comments. Otherwise leave comments out.

Prefer simple and concise code. Do not implement a lot of try/except instead let code fail.

# Agent folder

If you want to create python scripts or notes use the following structure:

- Put scripts you make in agents/scripts
- General notes or updates to notes in agents/notes
- Task specific notes in agents/tasks. In general create a new folder in agents/tasks and put your notes related to the task there.


# Skills
When doing task you have the following skills at your disposal:

- Subjects: For exploring tables from denmarks statistics through a subjects hierarchy
- Tables: For previewing tables and seeing their schema and the first n rows.
- Sql: For executing sql queries against a postgres database with the fact and dim tables.

# Answer style
If you make a markdown file with detailed notes about a question or create relevant python code files. Then you can always reference these in a final answer by providing the file paths.

# Context
Denmark’s StatBank export lives on disk as ~2000 fact tables (Parquet) plus ~40 dimension tables; they form a classic star schema that we ingest into Postgres under the fact and dim schemas using the scripts in varro/data/disk_to_db/. Every fact table is normalized during loading (lower-case ASCII column names, parsed tid, etc.), while each dimension exposes kode, niveau, titel, and related metadata for decoding categorical codes.

Navigation starts with the subject hierarchy: an acyclic tree where internal nodes are subject headers and leaves list the fact tables belonging to that branch. Use the subjects skill (python .claude/skills/subjects/scripts/subjects.py "Borgere/Befolkning" --depth 2) to browse or locate tables, and note that each listed table includes its short description pulled from the metadata bundle.

Per-table inspection happens through the tables skill. view previews a fact table as stored on disk or in DB-ready form (same transformation used by the loaders), while info prints the official StatBank metadata (description, unit, and the text labels for each dimension). All values in the raw facts are coded; the metadata clarifies the code ↔ label mapping, and full hierarchies reside in the dimension tables mentioned above.

Once you know the table IDs and dimensions you need, switch to the sql skill. It wraps psql with the project DSN so you can \dt fact.*, inspect column comments (which describe dimension links), and run analyses that join fact.<table> to dim.<dimension> on kode. Comments on fact columns summarize any dimension link that was detected during loading, so you can quickly see whether a join target exists.

These three skills—subjects (find tables), tables (preview and metadata), sql (query fact/dim schemas)—form the primary toolkit for any AI analyst or developer joining the project.