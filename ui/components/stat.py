"""ui.components.stat

Stat card component for displaying metrics/KPIs.

Uses DaisyUI's stat classes.
"""

from __future__ import annotations

from typing import Optional

from fasthtml.common import Div, FT, Span

from ..core import cn


def Stat(
    *c,
    title: Optional[str] = None,
    value: Optional[str] = None,
    desc: Optional[str] = None,
    figure: Optional[FT] = None,
    cls: str = "",
    **kw,
) -> FT:
    """
    Stat card for displaying metrics.

    Args:
        title: Stat label/title (rendered as stat-title)
        value: Main value (rendered as stat-value)
        desc: Description/change text (rendered as stat-desc)
        figure: Optional figure/icon (rendered as stat-figure)
        cls: Additional CSS classes
        **kw: Passed to underlying Div (useful for HTMX attrs)

    Example:
        Stat(
            title="Total Revenue",
            value="$84,254",
            desc="+12.5% from last month",
        )
    """
    children = []

    if figure:
        children.append(Div(figure, cls="stat-figure"))

    if title:
        children.append(Div(title, cls="stat-title"))

    if value:
        children.append(Div(value, cls="stat-value"))

    if desc:
        children.append(Div(desc, cls="stat-desc"))

    # Add any additional children
    children.extend(c)

    return Div(
        *children,
        cls=cn("stat bg-base-100 rounded-box shadow-sm", cls),
        data_slot="stat",
        **kw,
    )


def StatSkeleton(
    title: Optional[str] = None,
    cls: str = "",
    **kw,
) -> FT:
    """
    Stat card with skeleton loading state.

    Args:
        title: Optional title to show while loading
        cls: Additional CSS classes
        **kw: Passed to underlying Stat (useful for HTMX attrs)
    """
    return Stat(
        title=title,
        cls=cls,
        **kw,
    )(
        Div(
            Span(cls="skeleton inline-block w-32 h-8"),
            cls="stat-value",
        ),
    )


__all__ = ["Stat", "StatSkeleton"]
