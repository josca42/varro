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
    dashboards = mount_dashboards(app, engine, "dashboard")
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
    dashboards_root: str | Path = "mnt",
    user_id: int = 1,
) -> dict[str, Dashboard]:
    """Load all dashboards and mount routes.

    Args:
        app: FastHTML app
        engine: SQLAlchemy engine
        dashboards_root: Path to data root containing user workspaces
        user_id: User ID to pre-load dashboards for

    Returns:
        Dict mapping dashboard names to Dashboard objects
    """
    from varro.dashboard.routes import mount_dashboard_routes

    root = Path(dashboards_root)
    dashboards_dir = root / "user" / str(user_id) / "dashboard"
    dashboards = load_dashboards(dashboards_dir)
    mount_dashboard_routes(app, root, engine)
    return dashboards
