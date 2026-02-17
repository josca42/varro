
# From soft ware you have come to soft ware you shall become
#### Example used to illustrate each of the statements: Varro.dk
I am creating a dashboard app, where an AI agent create dashboards to answer question about Denmark. The agent does this by finding relevant tables from statistics Denmark, creating sql queries to extract relevant data from these tables, plotting it using python and then exposing the analysis as a dashboard.
#### File over app
AI agents are good at reading files and navigating filesystems using bash commands. So if the app mostly reads/writes/edits files then it can be easily navigated and extended by an AI agent.

In practice this means that UI elements are represented as files that are human readable and in my case by choosing to send html instead of json from the server to the browser.
In many cases it can be easier to read a markdown file than an html file so I use markdown files for most things and then use a standard markdown to html converter. Having this approach allows me to add some custom markdown syntax such that I can represent for instance dashboards as markdown files.

**Example**:
I have implemented my dashboard application by letting a dashboard be represented by a set of query_name.sql files, an outputs.py file specifying figures and tables created from those queries and then a markdown file specifying the layout and various titles and comments.

An example folder structure could look like this

```
dashboards/
├── sales/
│   ├── queries/         # Folder with SQL queries (one file per query)
│   │   ├── regions.sql
│   │   ├── monthly_revenue.sql
│   │   └── top_products.sql
│   ├── outputs.py       # @output functions returning figures, tables, metrics
│   ├── dashboard.md     # Layout and component references
│   └── notes.md         # If the AI agent wants to include notes for future
						 # reference it can do so in a notes.md file
```

The markdown file uses `:::` fence syntax to indicate UI containers and <object_type /> to indicate python objects that should be displayed. So a dashboard could look like this

```
# Danish Population Dashboard

::: filters
<filter-select name="region" label="Region" options="query:regions" default="all" />
<filter-date name="period" label="Period" default="all" />
:::

::: grid cols=2
<metric name="total_population" />
<metric name="quarters_shown" />
:::

::: tabs
::: tab name="Trend"
<fig name="population_trend_chart" />
:::
::: tab name="Age Groups"
<fig name="age_chart" />
:::
:::

The dashboard shows that ...
```

The above syntax is easy to use for the AI agent because it maps to wellknown syntax already used in other [custom markdown parsers](https://docusaurus.io/).

So the above markdown can be converted to html and the figures/tables/metrics can be served by using simple conventions for endpoints. In my case I do the following:

| Endpoint                                       | Purpose                                                                      |
| ---------------------------------------------- | ---------------------------------------------------------------------------- |
| `GET /dashboard/{name}`                        | Dashboard shell (filters + placeholders); returns fragment for HTMX requests |
| `GET /dashboard/{name}/_/filters`              | Filter sync (updates URL, triggers reload)                                   |
| `GET /dashboard/{name}/_/figure/{output_name}` | Render Plotly figure                                                         |
| `GET /dashboard/{name}/_/table/{output_name}`  | Render DataFrame table                                                       |
| `GET /dashboard/{name}/_/metric/{output_name}` | Render metric card                                                           |

In this way dashboards are represented as files that are easily read by humans and therefore by AI agents. Hence, new dashboards can easily be created by the AI agent using components it knows well such as sql, python and markdown.

#### Url as state and path
By letting the state of the app be determined by the url and [making the url readable](https://alfy.blog/2025/10/31/your-url-is-your-state.html) then the AI agent can navigate - and infer state of - the application by updating/reading the url. Since the AI agent will have likely read billions of urls during training on internet data then navigating the app using the url will be second nature.
To keep the file over app approach consistent I let the folder structure and url structure mirror each other (to the extent it makes sense).

**Example**:
In my dashboard application then if I go to the sales dashboard the relative url is /dashboard/sales and if filter on regions so I only have regions from "North" then the url is /dashboard/sales?region=North.
This url structure is then reflected in the folder structure on disk in the following way. The sales dashboard folder is /dashboard/sales . But more importantly I have given then AI agent the ability to take a snapshot of dashboards. The snapshot is taken by providing an url and in the case snapshot(url=/dashboard/sales?region=North) then the following folder structure would be produced

```
/dashboards/sales/
└── snapshots/
    └── region=North/                  # If no filters then folder name is _
        ├── dashboard.png
        ├── 2026-02-10.date            # Snapshot timestamp. File is empty
        ├── figures/
        │   ├── revenue_chart.png      # Plotly figures as png files
        │   └── trend_line.png
        ├── tables/
        │   └── sales_summary.parquet  # Tables as parquet files
        └── metrics.json               # Metric cards are dumped as json
```

Notice that the folder name of the snapshot are the filter values used in the url. In this way the AI agent can easily navigate the app using the url and "view" the app using the url. 

####  Chat as trajectory
Each chat interaction is an agent trajectory. The goal is to complete the user request and the agents trajectory is the observe -> decide -> act -> observe -> decide -> act ... loop the agent is running using the tools at its disposal.



**Example**:
Each chat

#### Organic composition
**Verbs**
Read/Write/Edit
**Infrastructure**
Sql, Jupyter, UpdateUrl, Snapshot, Bash


**Words that create words that create words**
A key aspect of the "file over app" philosophy is that the filesystem is the state of the system. Hence, how the program behaves evolves as the files change. In my dashboard app this is enabled in 3 ways. 

- **Dashboards as memory**: A dashboard represents an analysis that the user has iterated on. As such it encapsulates various decisions about what a good analysis is. What tables were used, what plots were created and how were the pieces put together. By having the dashboard be easily read and viewed by the AI agent it can always consult previous examples of user preferences and use that as guidelines going forward.

- **Skills**:
- **Agent notes**:  