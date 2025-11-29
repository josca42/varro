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
)
from pydantic_ai.messages import ToolReturn
from pydantic_ai.models.anthropic import AnthropicModel, AnthropicModelSettings
from varro.data.utils import df_preview
from varro.agent.memory import SessionStore
from pydantic_ai.builtin_tools import MemoryTool
from pathlib import Path
import logfire
from varro.db import crud
from varro.agent.memory import Memory
from varro.agent.jupyter_kernel import JupyterCodeExecutor
from varro.agent.playwright_render import html_to_png
from varro.db.db import engine

logfire.configure(scrubbing=False)
logfire.instrument_pydantic_ai()


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


@agent.tool()
async def memory(ctx: RunContext[SessionStore], **command: Any) -> Any:
    if ctx.deps.memory is None:
        ctx.deps.memory = Memory(ctx.deps.user.id)

    try:
        return ctx.deps.memory.call(command)
    except Exception as e:
        return f"Error: {e}"


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


def sql_query(ctx: RunContext[SessionStore], query: str, df_name: str):
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df_preview(df, max_rows=30, name=query)
