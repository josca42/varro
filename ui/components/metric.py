"""ui.components.metric

Metric value display component.
"""

from __future__ import annotations

from typing import Literal, Optional

from fasthtml.common import Div, FT, Span

from ui.core import cn
from ui.utils import abbrev, format_value

MetricFormat = Literal["number", "currency", "percent"]


def MetricValue(
    value: float | int | str,
    *,
    format: MetricFormat = "number",
    label: Optional[str] = None,
    change: Optional[float] = None,
    change_label: Optional[str] = None,
    cls: str = "",
    **kw,
) -> FT:
    """
    Display a formatted metric value with optional label and change indicator.

    Args:
        value: The metric value to display
        format: Format type - "number", "currency", or "percent"
        label: Label text shown above the value
        change: Optional change value (as decimal, e.g. 0.125 for +12.5%)
        change_label: Optional label for the change (e.g. "vs last month")
        cls: Additional CSS classes
        **kw: Passed to underlying Div
    """
    formatted = format_value(value, format)

    change_el = None
    if change is not None:
        sign = "+" if change >= 0 else ""
        color = "text-success" if change >= 0 else "text-error"
        change_el = Div(
            Span(f"{sign}{change:.1%}", cls=color),
            Span(change_label or "", cls="text-base-content/50 ml-1") if change_label else None,
            cls="text-sm mt-2",
        )

    return Div(
        Div(label, cls="text-sm text-base-content/60") if label else None,
        Div(formatted, cls="text-2xl font-semibold mt-1"),
        change_el,
        cls=cn(cls),
        data_slot="metric-value",
        **kw,
    )

