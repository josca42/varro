from datetime import datetime
from typing import Any
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
from varro.agent.ipython_shell import JUPYTER_INITIAL_IMPORTS
from varro.chat.session import UserSession

DIM_TABLES = get_dim_tables()

sonnet_model = AnthropicModel("claude-sonnet-4-5")
sonnet_settings = AnthropicModelSettings(
    anthropic_thinking={"type": "enabled", "budget_tokens": 3000},
    parallel_tool_calls=True,
)

agent = Agent(
    model=sonnet_model,
    model_settings=sonnet_settings,
    deps_type=UserSession,
    builtin_tools=[
        # MemoryTool(),
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
async def get_system_prompt(ctx: RunContext[UserSession]) -> str:
    prompts = ctx.deps.cached_prompts
    if not prompts:
        prompts = get_prompts(prompts)
        ctx.deps.cached_prompts = prompts

    return crud.prompt.render_prompt(name="rigsstatistiker", **prompts)


def get_prompts(prompts):
    prompts["CURRENT_DATE"] = datetime.now().strftime("%Y-%m-%d")
    prompts["SUBJECT_HIERARCHY"] = generate_hierarchy()
    return prompts


# @agent.tool()
# async def memory(ctx: RunContext[SessionStore], **command: Any) -> Any:
#     if ctx.deps.memory is None:
#         ctx.deps.memory = Memory(ctx.deps.user.id)

#     return ctx.deps.memory.call(command)


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
def sql_query(ctx: RunContext[UserSession], query: str, df_name: str | None = None):
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
        raise ModelRetry(str(e))
    if df_name:
        ctx.deps.shell.user_ns[df_name] = df
        max_rows = 20 if len(df) < 21 else 5
        return f"Stored as {df_name}\n{df_preview(df, max_rows=max_rows)}"
    else:
        return df_preview(df, max_rows=30)


@agent.tool(docstring_format="google")
async def jupyter_notebook(
    ctx: RunContext[UserSession], code: str, show: list[str] = []
):
    """
    Stateful Jupyter notebook environment. Each call executes as a new cell.
    All printed output in the notebook cell will be included in the response.

    To see figures and dataframes in the response then add the name of the figure or dataframe to the show list.

    The notebook has access to all dataframes added to it's name space by the sql_query tool. You can reference the dataframes by their name, df_name.

    The notebook is initialized by running the following code in the first cell.
    ```python
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    import matplotlib.pyplot as plt
    ```

    Args:
        code (str): The Python code to execute.
    """
    if not ctx.deps.shell_imports:
        ctx.deps.shell.run_cell(JUPYTER_INITIAL_IMPORTS)
        ctx.deps.shell_imports = True

    res = ctx.deps.shell.run_cell(code)
    if res.error_before_exec:
        raise ModelRetry(repr(res.error_before_exec))
    if res.error_in_exec:
        raise ModelRetry(repr(res.error_in_exec))

    if not show:
        return res.stdout

    elements_rendered = []
    for name in show:
        element = ctx.deps.shell.user_ns.get(name)
        rendered = await show_element(element)
        elements_rendered.append(rendered)

    return ToolReturn(return_value=res.stdout, content=elements_rendered)


async def show_element(element) -> Any | None:
    """Convert a cell output to a format suitable for ToolReturn content."""
    if isinstance(element, pd.DataFrame):
        return df_preview(element, max_rows=30)
    if isinstance(element, go.Figure):
        png_bytes = await plotly_figure_to_png(element)
        return BinaryContent(data=png_bytes, media_type="image/png")
    if isinstance(element, plt.Figure):
        png_bytes = matplotlib_figure_to_png(element)
        return BinaryContent(data=png_bytes, media_type="image/png")
    else:
        raise ValueError(f"Invalid output type: {type(element)}")


def matplotlib_figure_to_png(fig: plt.Figure) -> bytes:
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return buf.getvalue()


async def plotly_figure_to_png(fig: go.Figure) -> bytes:
    html_str = pio.to_html(fig, full_html=True, include_plotlyjs="cdn")
    return await html_to_png(html_str, width=600, height=600)
