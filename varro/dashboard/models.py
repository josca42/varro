"""dashboard.models

Metric model and @output decorator.
"""

from __future__ import annotations

from typing import Callable, Optional

from pydantic import BaseModel


class Metric(BaseModel):
    """Result type for metric outputs.

    Attributes:
        value: The metric value (number or string)
        label: Display label
        format: "number", "currency", or "percent"
        change: Optional change value (decimal, e.g. 0.12 for +12%)
        change_label: Optional label for change (e.g. "vs last period")
    """

    value: float | int | str
    label: str
    format: str = "number"
    change: Optional[float] = None
    change_label: Optional[str] = None


def output(fn: Callable) -> Callable:
    """Marker decorator for dashboard output functions.

    Usage:
        @output
        def revenue_trend(monthly_revenue, filters):
            return px.line(monthly_revenue, x="month", y="revenue")
    """
    fn._is_output = True
    return fn


def get_outputs(module) -> dict[str, Callable]:
    """Extract @output-decorated functions from a module."""
    return {
        name: fn
        for name, fn in vars(module).items()
        if callable(fn) and getattr(fn, "_is_output", False)
    }

