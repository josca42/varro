"""dashboard

Markdown dashboard framework for FastHTML.

Usage:
    from dashboard import output, Metric, mount_dashboards

    # In your outputs.py:
    @output
    def revenue_trend(monthly_revenue, filters):
        return px.line(monthly_revenue, x="month", y="revenue")

    # In your app:
    from sqlalchemy import create_engine
    engine = create_engine(DATABASE_URL)
    dashboards = mount_dashboards(app, engine, "dashboards")
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from .models import Metric, output
from .loader import load_dashboards, load_dashboard, Dashboard
from .routes import ar as dashboard_routes, configure as configure_dashboards

if TYPE_CHECKING:
    from sqlalchemy.engine import Engine


def mount_dashboards(
    app,
    engine: "Engine",
    dashboards_dir: str | Path = "dashboards",
) -> dict[str, Dashboard]:
    """Load all dashboards and mount routes.

    Args:
        app: FastHTML app
        engine: SQLAlchemy engine
        dashboards_dir: Path to dashboards folder

    Returns:
        Dict mapping dashboard names to Dashboard objects
    """
    from .routes import mount_dashboard_routes

    dashboards = load_dashboards(dashboards_dir)
    mount_dashboard_routes(app, dashboards, engine)
    return dashboards


__all__ = [
    "Metric",
    "output",
    "mount_dashboards",
    "Dashboard",
    "load_dashboard",
    "dashboard_routes",
    "configure_dashboards",
]
