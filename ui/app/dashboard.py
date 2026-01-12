"""ui.app.dashboard

Dashboard panel compositions used by the demo app.

This module is intentionally *not* generic. It exists so the demo app can be
written as a composition of `ui.*` components rather than ad-hoc Div chains.

Key choices:
- Metric cards use `ui.components.Card` (DaisyUI `card`) with lightweight
  Tailwind layout utilities.
- "Charts" are shells/placeholder blocks (no charting lib included).
"""

from __future__ import annotations

from typing import Literal, Optional

from fasthtml.common import *

from ..core import cn
from ..components.button import Button
from ..components.card import Card, CardBody, CardHeader, CardTitle, CardDescription


Trend = Literal["up", "down"]


def MetricCard(
    title: str,
    value: str,
    change: str,
    trend: Trend = "up",
    icon: str = "$",
    cls: str = "",
    **kw,
):
    """Single metric card with a subtle tinted surface."""

    trend_color = "text-success" if trend == "up" else "text-error"
    trend_arrow = "⤴" if trend == "up" else "⤵"

    # Shadcn-esque: subtle border + very light tint.
    surface = "bg-success/[0.02] border-success/10" if trend == "up" else "bg-error/[0.02] border-error/10"

    return Card(
        CardBody(
            # Header
            Div(
                Div(title, cls="text-sm text-base-content/60"),
                Div(icon, cls="text-base-content/30 text-lg"),
                cls="flex justify-between items-start",
            ),
            Div(value, cls="text-2xl font-semibold mt-1"),
            Div(
                Span(f"{trend_arrow} {change}", cls=trend_color),
                Span(" vs last period", cls="text-base-content/50"),
                cls="text-sm mt-2",
            ),
        ),
        variant="border",
        cls=cn(surface, cls),
        data_slot="metric-card",
        **kw,
    )


def ChartShell(
    title: str,
    subtitle: str,
    height_cls: str = "h-64",
    cls: str = "",
    **kw,
):
    """A card-like shell for charts (placeholder)."""

    return Card(
        CardBody(
            Div(
                Div(title, cls="font-semibold"),
                Div(subtitle, cls="text-sm text-base-content/60"),
                cls="mb-4",
            ),
            Div(
                Div(cls="w-full h-full bg-gradient-to-t from-base-300/50 to-transparent rounded-box"),
                cls=cn(height_cls, "bg-base-200 rounded-box flex items-end p-4"),
            ),
        ),
        variant="border",
        cls=cn("shadow-none", cls),
        data_slot="chart-shell",
        **kw,
    )


def DashboardPanel(
    *,
    cls: str = "",
    **kw,
):
    """Dashboard content panel (right side of demo layout)."""

    header = Div(
        Div(
            Div("Dashboard", cls="text-2xl font-semibold"),
            Div("Analytics overview and key performance metrics", cls="text-sm text-base-content/60"),
        ),
        Div(
            Button("📅 Last 30 days ▾", variant="ghost", size="default"),
            Button("All Regions ▾", variant="ghost", size="default"),
            Button("↻", variant="ghost", size="icon"),
            Button("↓ Export", variant="ghost", size="default"),
            cls="flex gap-2",
        ),
        cls="flex justify-between items-start mb-6",
        data_slot="dashboard-header",
    )

    metrics = Div(
        MetricCard("Total Revenue", "$84,254", "+12.5%", "up", icon="$"),
        MetricCard("Active Users", "2,847", "+8.2%", "up", icon="⚇"),
        MetricCard("Orders", "1,234", "-2.4%", "down", icon="☐"),
        MetricCard("Conversion Rate", "3.24%", "+0.8%", "up", icon="↗"),
        cls="grid grid-cols-2 gap-4 mb-6",
        data_slot="dashboard-metrics",
    )

    charts = Div(
        ChartShell("Revenue Overview", "Monthly revenue and profit trends", "h-48"),
        Div(
            ChartShell("Sales by Category", "Product category performance", "h-40"),
            ChartShell("Traffic Sources", "Visitor acquisition channels", "h-40"),
            cls="grid grid-cols-2 gap-4 mt-4",
        ),
        data_slot="dashboard-charts",
    )

    return Div(
        header,
        metrics,
        charts,
        cls=cn("p-6", cls),
        data_slot="dashboard-panel",
        **kw,
    )


__all__ = ["MetricCard", "ChartShell", "DashboardPanel"]
