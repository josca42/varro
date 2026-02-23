from sqlalchemy import text
from varro.db.db import dst_read_engine
from pydantic_ai import BinaryContent
import plotly.io as pio
import plotly.graph_objects as go
from varro.agent.playwright_render import html_to_png
from varro.agent.images import (
    optimize_png_bytes,
    SNAPSHOT_MAX_PIXELS,
    JUPYTER_SHOW_MAX_PIXELS,
)
from varro.data.utils import df_preview
import pandas as pd
import matplotlib.pyplot as plt
import io
from typing import Any

from pathlib import Path
from varro.config import SUBJECTS_DIR


def generate_hierarchy() -> str:
    """
    Generate compact hierarchy with roots and mids only.

    The agent discovers leaves on demand via Bash("ls /subjects/{root}/{mid}/").

    Output format:
        root:
          mid1
          mid2
    """
    lines = []

    roots = sorted(d for d in SUBJECTS_DIR.iterdir() if d.is_dir())

    for root in roots:
        mids = sorted(d for d in root.iterdir() if d.is_dir())
        if not mids:
            continue
        lines.append(f"{root.name}:")
        for mid in mids:
            lines.append(f"  {mid.name}")
        lines.append("")

    return "\n".join(lines).rstrip()


def get_dim_tables() -> tuple[str, ...]:
    with dst_read_engine.connect() as conn:
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
        png_bytes = await plotly_figure_to_png(
            element, max_pixels=JUPYTER_SHOW_MAX_PIXELS
        )
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


async def plotly_figure_to_png(
    fig: go.Figure, *, max_pixels: int = SNAPSHOT_MAX_PIXELS
) -> bytes:
    html_str = pio.to_html(fig, full_html=True, include_plotlyjs="cdn")
    png_bytes = await html_to_png(html_str, width=600, height=600)
    return optimize_png_bytes(png_bytes, max_pixels=max_pixels)
