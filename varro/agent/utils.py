from sqlalchemy import text
from varro.db.db import engine
from pydantic_ai import BinaryContent
import plotly.io as pio
import plotly.graph_objects as go
from varro.agent.playwright_render import html_to_png
from varro.data.utils import df_preview
import pandas as pd
import matplotlib.pyplot as plt
import io
from typing import Any


def get_dim_tables() -> tuple[str, ...]:
    with engine.connect() as conn:
        return tuple(
            row[0]
            for row in conn.execute(
                text(
                    "SELECT table_name FROM information_schema.tables WHERE table_schema = 'dim'"
                )
            )
        )


# Helper functions for allowing the agent to view plotly and matplotlib figures
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
