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

from varro.dashboard.models import Metric, output
from varro.dashboard.loader import load_dashboards, Dashboard

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
    from varro.dashboard.routes import mount_dashboard_routes

    dashboards = load_dashboards(dashboards_dir)
    mount_dashboard_routes(app, dashboards_dir, engine)
    return dashboards
