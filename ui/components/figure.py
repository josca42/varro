"""ui.components.figure

Plotly figure component for rendering charts.
"""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div, FT, NotStr, Span

from ui.core import cn


def Figure(
    fig: Any,
    *,
    include_plotlyjs: bool = False,
    cls: str = "",
    **kw,
) -> FT:
    """
    Render a Plotly figure.

    Args:
        fig: A Plotly figure object
        include_plotlyjs: Whether to include Plotly JS (default False, assumes loaded elsewhere)
        cls: Additional CSS classes
        **kw: Passed to underlying wrapper
    """
    html = fig.to_html(include_plotlyjs=include_plotlyjs, full_html=False)
    if cls or kw:
        return Div(NotStr(html), cls=cn(cls), data_slot="figure", **kw)
    return NotStr(html)


def FigureSkeleton(
    *,
    height_cls: str = "h-64",
    cls: str = "",
    **kw,
) -> FT:
    """
    Skeleton loading state for a figure.

    Args:
        height_cls: Tailwind height class for the skeleton (default "h-64")
        cls: Additional CSS classes
        **kw: Passed to underlying Div
    """
    return Div(
        Span(cls="loading loading-spinner"),
        cls=cn("flex justify-center items-center", height_cls, cls),
        data_slot="figure-skeleton",
        **kw,
    )

