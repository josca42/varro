import chainlit as cl
from datetime import datetime
from typing import Any, Dict, List, Literal, Optional, Union

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from pydantic_ai import (
    Agent,
    RunContext,
    BinaryContent,
    WebSearchTool,
    WebSearchUserLocation,
    ModelRetry,
)
from pydantic_ai.messages import ToolReturn
from pydantic_ai.models.anthropic import AnthropicModel, AnthropicModelSettings
from varro.data.utils import df_preview
from varro.context.utils import fuzzy_match
from varro.agent.memory import SessionStore
from pathlib import Path
import logfire
from varro.agent.jupyter_kernel import JupyterCodeExecutor
from varro.agent.playwright_render import html_to_png
from varro.db.db import engine
from varro.config import COLUMN_VALUES_DIR
from varro.db import crud
from varro.context.tools import (
    generate_hierarchy,
    subject_overview_tool,
    table_docs_tool,
)
from sqlalchemy import text

logfire.configure(scrubbing=False)
logfire.instrument_pydantic_ai()

DIM_TABLES_DOCS_DIR = Path("/root/varro/docs/dim_tables")
DIM_TABLES = [md_file.stem for md_file in DIM_TABLES_DOCS_DIR.glob("*.md")]


sonnet_model = AnthropicModel("claude-sonnet-4-5")
sonnet_settings = AnthropicModelSettings(
    anthropic_thinking={"type": "enabled", "budget_tokens": 3000},
    parallel_tool_calls=True,
)

agent = Agent(
    model=sonnet_model,
    model_settings=sonnet_settings,
    deps_type=SessionStore,
    builtin_tools=[
        WebSearchTool(
            search_context_size="medium",
            user_location=WebSearchUserLocation(
                city="Copenhagen",
                country="DK",
                region="DK",
                timezone="Europe/Copenhagen",
            ),
            blocked_domains=None,
            allowed_domains=None,
            max_uses=None,
        ),
    ],
)


@agent.instructions
async def get_system_prompt(ctx: RunContext[SessionStore]) -> str:
    prompts = ctx.deps.cached_prompts
    if not prompts:
        prompts = get_prompts(prompts)
        ctx.deps.cached_prompts = prompts

    prompts["SESSION_STORE"] = ctx.deps.data_in_store()
    return crud.prompt.render_prompt(name="rigsstatistiker", **prompts)


def get_prompts(prompts):
    prompts["CURRENT_DATE"] = datetime.now().strftime("%Y-%m-%d")
    prompts["SUBJECT_HIERARCHY"] = generate_hierarchy()
    return prompts


@agent.tool_plain(docstring_format="google")
def subject_overview(leaf: str):
    """
    Get the README for a leaf subject showing available tables.

    Args:
        leaf: Full path "arbejde_og_indkomst/indkomst_og_løn/løn"
              or unique leaf name "løn"

    Returns:
        Content of the subject's README.md

    Raises:
        FileNotFoundError: No matching subject
        ValueError: Ambiguous leaf name
    """
    return subject_overview_tool(leaf)


@agent.tool_plain(docstring_format="google")
def table_docs(table: str):
    """
    Get documentation for any table (fact or dimension).

    Args:
        table_id: Table identifier like "lon10", "nuts",
                  or with schema prefix "fact.lon10", "dim.nuts"

    Returns:
        Content of the table's markdown documentation

    Raises:
        FileNotFoundError: Table docs don't exist
    """
    return table_docs_tool(table)


@agent.tool_plain(docstring_format="google")
def view_column_values(
    table: str, column: str, fuzzy_match_str: str | None = None, n: int | None = 5
):
    """
    View the unique values for a column in a dimension or fact table. If fuzzy_match_str is provided then the unique values are fuzzy matched against the fuzzy_match_str and the n best matches are returned. If no fuzzy_match_str is provided then the first n unique values are returned.

    Args:
        table: The name of the table.
        column: The name of the column.
        fuzzy_match_str: A string to fuzzy match against the unique values.
        n: The maximum number of unique values to return.
    """
    table = table.strip().lower().replace("fact.", "").replace("dim.", "")
    if table in DIM_TABLES:
        df = pd.read_parquet(COLUMN_VALUES_DIR / f"{table}.parquet")
        name = f"df_{table}_titel"
        schema = "dim"
    else:
        df = pd.read_parquet(COLUMN_VALUES_DIR / f"{table}/{column}.parquet")
        name = f"df_{table}_{column}"
        schema = "fact"
    if fuzzy_match_str:
        return fuzzy_match(fuzzy_match_str, df=df, limit=n, schema=schema, name=name)
    else:
        return df_preview(df, max_rows=n, name=name)


@agent.tool(docstring_format="google")
def sql_query(ctx: RunContext[SessionStore], query: str, df_name: str | None = None):
    """
    Execute a SQL query against the PostgreSQL database containing the dimension and fact tables. If df_name is provided then the result is stored in the <session_store> with the name specified by df_name.

    Args:
        query: The SQL query to execute.
        df_name: The name of the dataframe containing the data from the query.
    """
    try:
        with engine.connect() as conn:
            df = pd.read_sql(text(query), conn)
    except Exception as e:
        raise ModelRetry(e)
    if df_name:
        ctx.deps.dfs[df_name] = df
        max_rows = 20 if len(df) < 21 else 5
        return f"Stored as {df_name}\n{df_preview(df, max_rows=max_rows)}"
    else:
        return df_preview(df, max_rows=30)


@agent.tool(docstring_format="google")
async def jupyter_notebook(ctx: RunContext[SessionStore], code: str):
    """
    Stateful Jupyter notebook environment. Each message with python code will be executed as a new cell in the notebook.
    All printed output in the notebook cell will be included in the response. Likewise if a figure is shown - fig.show() - or displayed - display(fig) - it will be included in the response. And if the cell output is a dataframe it will be included in the response.

    All figure or dataframe content elements included in a response are added to the <session_store> with the name specified in the code.

    print statements are added in the response as <printed output>...</printed output>.
    rendered output and cell output are added as seperate content elements and an overview of the content elements are added in the response as <rendered output and cell output>...</rendered output and cell output>.

    The tool should be called sequentially to build up the analysis.

    The notebook is initialized by running the following code in the first cell.
    ```python
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    import matplotlib.pyplot as plt
    ```

    IMPORTANT: Only the figure you call show() on will be added to the <session_store>. If you want to rename a figure then rename the figure and call show() on the renamed figure.

    Args:
        code (str): The Python code to execute.
    """

    def print_output(x: str) -> str:
        return "<printed output>\n" + x + "\n</printed output>"

    # Start kernel first time the tool is used
    if ctx.deps.jupyter is None:
        executor = JupyterCodeExecutor(
            work_dir=Path(f"/home/jonathan/data/{ctx.deps.user.id}")
        )
        executor.start()
        ctx.deps.jupyter = executor  # persist for session reuse

    # Make sure all dataframes are added to the notebook
    for name, df in ctx.deps.dfs.items():
        if name not in ctx.deps.dfs_added_to_notebook:
            ctx.deps.jupyter.put_df(name, df)
            ctx.deps.dfs_added_to_notebook.append(name)

    # Execute the code
    jupyter_output = ctx.deps.jupyter.execute(code=code)
    if jupyter_output.exit_code != 0:
        return jupyter_output.prints

    out_str = print_output(jupyter_output.prints) if jupyter_output.prints else ""
    if not jupyter_output.objects:
        return out_str

    rendered_output = ""
    outputs = []
    for obj_name in jupyter_output.objects:
        obj_path = ctx.deps.jupyter.output_file_map[obj_name]
        try:
            obj, obj_type = ctx.deps.jupyter._load_output(obj_path)
        except Exception as e:
            print(f"Error loading output {obj_name} from {obj_path}: {e}")
            continue

        rendered_output += f"{obj_name}: {obj_type}\n"
        if obj_type == "matplotlib figure":
            ctx.deps.figs[obj_name] = obj
            outputs.append(
                BinaryContent(
                    identifier=obj_name,
                    data=obj,
                    media_type="image/png",
                )
            )
        elif obj_type == "plotly figure":
            ctx.deps.figs[obj_name] = go.Figure(obj)
            html_str = pio.to_html(obj, full_html=True, include_plotlyjs="cdn")
            png_bytes = await html_to_png(html_str, width=600, height=600)
            outputs.append(
                BinaryContent(
                    identifier=obj_name, data=png_bytes, media_type="image/png"
                )
            )
        elif obj_type == "pandas DataFrame":
            ctx.deps.dfs[obj_name] = obj
            outputs.append(df_preview(obj, max_rows=30, name=obj_name))
        else:
            raise ValueError(f"Unsupported object type: {obj_type}")

    out_str += (
        "\n<rendered output and cell output>\n"
        + rendered_output
        + "\n</rendered output and cell output>"
    )
    return ToolReturn(return_value=out_str, content=outputs)
