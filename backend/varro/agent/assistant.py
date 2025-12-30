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
from varro.agent.memory import Memory, SessionStore
from varro.evidence import EvidenceManager
from pathlib import Path
import logfire
from varro.agent.playwright_render import html_to_png
from varro.agent.utils import get_dim_tables
from varro.db.db import engine
from varro.config import COLUMN_VALUES_DIR
from varro.db import crud
from varro.context.tools import (
    generate_hierarchy,
    subject_overview_tool,
    table_docs_tool,
)
from sqlalchemy import text
import matplotlib.pyplot as plt
import io
from pydantic_ai.builtin_tools import MemoryTool

logfire.configure(scrubbing=False)
logfire.instrument_pydantic_ai()

DIM_TABLES = get_dim_tables()


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
        MemoryTool(),
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


@agent.tool()
async def memory(ctx: RunContext[SessionStore], **command: Any) -> Any:
    if ctx.deps.memory is None:
        ctx.deps.memory = Memory(ctx.deps.user.id)

    return ctx.deps.memory.call(command)


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
    try:
        return subject_overview_tool(leaf)
    except FileNotFoundError as e:
        raise ModelRetry(
            f"No README.md found for subject: {leaf}. Could it be a root or mid subject?"
        )


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
    try:
        return table_docs_tool(table)
    except FileNotFoundError as e:
        raise ModelRetry(f"No table docs found for table: {table}.")


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
        ctx.deps.shell.user_ns[df_name] = df
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
    res = ctx.deps.shell.run_cell(code=code)
    if res.error_before_exec:
        return ModelRetry(repr(res.error_before_exec))
    if res.error_in_exec:
        return ModelRetry(repr(res.error_in_exec))

    if not res.result and not res.outputs:
        return res.stdout

    raw_outputs = [res.result] + res.outputs if res.result else res.outputs

    processed = []
    for output in raw_outputs:
        converted = await convert_output(output)
        if converted is not None:
            processed.append(converted)

    return ToolReturn(return_value=res.stdout, content=processed)


@agent.tool(docstring_format="google")
async def create_dashboard(ctx: RunContext[SessionStore], name: str) -> str:
    """
    Create an Evidence dashboard and start the dev server.

    After calling this, use the memory tool to write markdown pages:
    - /memories/d/dashboard/pages/index.md (main page)
    - /memories/d/dashboard/pages/other.md (additional pages)

    Evidence markdown syntax:
    - SQL queries: ```sql query_name SELECT ... ```
    - Components reference queries: <LineChart data={query_name} x="col" y="val" />

    Common components:
    - <LineChart data={query} x="date" y="value" />
    - <BarChart data={query} x="category" y="value" />
    - <BigValue data={query} value="total" />
    - <DataTable data={query} />

    SQL runs against fact.* and dim.* schemas.

    Args:
        name: Name for the dashboard.

    Returns:
        Instructions for writing dashboard content.
    """
    evidence = EvidenceManager(user_id=ctx.deps.user.id)
    port = await evidence.start_server_async(name=name)
    ctx.deps.evidence = evidence

    # Send port marker for frontend to detect
    await cl.Message(content=f"<!--DASHBOARD_PORT:{port}-->").send()

    return f"Dashboard started on port {port}. Use memory tool to write pages to /memories/d/dashboard/pages/index.md"


async def convert_output(output) -> Any | None:
    """Convert a cell output to a format suitable for ToolReturn content."""
    if isinstance(output, pd.DataFrame):
        return df_preview(output, max_rows=30)
    if isinstance(output, go.Figure):
        png_bytes = await plotly_figure_to_png(output)
        return BinaryContent(data=png_bytes, media_type="image/png")
    if isinstance(output, plt.Figure):
        png_bytes = matplotlib_figure_to_png(output)
        return BinaryContent(data=png_bytes, media_type="image/png")

    if hasattr(output, "data"):
        data = output.data
        if "image/png" in data:
            return BinaryContent(data=data["image/png"], media_type="image/png")
        if "application/vnd.plotly.v1+json" in data:
            png_bytes = await plotly_figure_to_png(
                go.Figure(data["application/vnd.plotly.v1+json"])
            )
            return BinaryContent(data=png_bytes, media_type="image/png")
        return None

    return output


def matplotlib_figure_to_png(fig: plt.Figure) -> bytes:
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return buf.getvalue()


async def plotly_figure_to_png(fig: go.Figure) -> bytes:
    html_str = pio.to_html(fig, full_html=True, include_plotlyjs="cdn")
    return await html_to_png(html_str, width=600, height=600)
