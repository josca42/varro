# Varro

This project aims to create building blocks that make it straightforward to let an AI reason about data from denmarks statistics. A project overview is given in this [video](https://www.youtube.com/watch?v=RnVnrH4BBsI)

## Code

For a quick code walkthrough see this video

#### /data
1. All public tables from denmarks statistics along with table descriptions and subject hierachies are downloaded to disk. /data/statbank_to_disk/*
2. Claude code then analyses the different fact tables and creates links between columns in fact tables and dimension tables from https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer.  /data/fact_col_to_dim_table
3. All fact tables and dimension tables are processed and copied into a postgres database. /data/disk_to_db

#### /context
1. Dimension table README.md's are created from the documentation page on dst.dk and the values in the table. /context/dim_table.py
2. For fact tables the table info exposed by the dst api is to create a fact table README.md. /context/*.py
3. The subject hierarcy along with fact table info is used to create subject README.md /context/*.py

#### /agent
A basic AI agent is created using pydantic-ai. The tables subject hierarchy is provided in compact form in the system prompt. And the agent then has access to a subject_overview and table_docs tool for reading subject README's and table README's. For searching unique values in a table then the agent can use view_column_values.

For accessing data the agent has access to a sql_query tool that executes sql_queries against the postgres database and then the resulting table data can be saved as a pandas dataframe

For more in depth analysis the agent has access to a stateful jupyter notebook that it can use to run code and create plots.

#### /chat
The agent can be accessed through a standard chat interface using chainlit. For nicer tool calling ui and display of inline plots and dataframes then some custom message processing has been added in /chat/message.py .
The chat-ui is specified in ui_chat/app.py

## Roadmap

- Create chatgpt plugin
- Metabase integration and new UI
- Better context
- Better agent

## Why

### More agency and less bureaucracy

> AI is a solution to the increasing complexity of the modern world causing the rise of bureaucracy and information overload. - Rohit Krishnan

Todays large organisations are riddled with stringent rules and bureaucracy thet helps make processes more scalable. Ideally everyone would like a simpler system, where an agent made informed decisions on a case by case basis. That is how things used to be. Fewer rules and more agency. AI gives us the possibility of creating a scalable version of what we used to have. A personal connection inside organisations that helps us make the right decisions. 

This project is a "soft API" to denmark statistics that allows for more human ways of interacting with data about Denmark. Giving you the agency to explore the truth about subjects you care about. Whether that be immmigration, your municipality's finances or ..?

### Informing the narrative upstream

...
