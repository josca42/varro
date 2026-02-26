from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from uuid import uuid4

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from starlette.testclient import TestClient

from ui.core import daisy_app
from varro.dashboard.routes import mount_dashboard_routes
from varro.db.db import POSTGRES_USER_SQLALCHEMY


@dataclass
class DashboardTestEnv:
    client: TestClient
    engine: Engine
    dashboards_root: Path
    dashboard_name: str
    user_id: int = 1

    @property
    def dashboard_path(self) -> Path:
        return self.dashboards_root / "user" / str(self.user_id) / "dashboard" / self.dashboard_name

    @property
    def base_url(self) -> str:
        return f"/dashboard/{self.dashboard_name}"


def _seed_db(engine: Engine, table_name: str) -> None:
    with engine.begin() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS {table_name}"))
        conn.execute(
            text(
                f"""
                CREATE TABLE {table_name} (
                    period DATE NOT NULL,
                    region TEXT NOT NULL,
                    population INTEGER NOT NULL,
                    include_estimate BOOLEAN NOT NULL
                )
                """
            )
        )
        conn.execute(
            text(
                f"""
                INSERT INTO {table_name} (period, region, population, include_estimate)
                VALUES
                  ('2024-01-01', 'North', 100, FALSE),
                  ('2024-01-01', 'South', 120, FALSE),
                  ('2024-04-01', 'North', 110, FALSE),
                  ('2024-04-01', 'South', 130, TRUE),
                  ('2024-07-01', 'North', 115, FALSE),
                  ('2024-07-01', 'South', 135, TRUE)
                """
            )
        )


def _write_dashboard(dashboard_path: Path, table_name: str) -> None:
    queries_dir = dashboard_path / "queries"
    queries_dir.mkdir(parents=True)

    (queries_dir / "regions.sql").write_text(
        dedent(
            f"""
            SELECT DISTINCT region, ('Label ' || region) AS label
            FROM {table_name}
            ORDER BY region
            """
        ).strip()
    )

    (queries_dir / "population_trend.sql").write_text(
        dedent(
            f"""
            SELECT period, SUM(population) AS population
            FROM {table_name}
            WHERE (:region IS NULL OR region = :region)
              AND (:period_from IS NULL OR period >= :period_from)
              AND (:period_to IS NULL OR period <= :period_to)
            GROUP BY period
            ORDER BY period
            """
        ).strip()
    )

    (queries_dir / "population_by_region.sql").write_text(
        dedent(
            f"""
            SELECT region, SUM(population) AS population
            FROM {table_name}
            WHERE (:include_estimate IS NULL OR include_estimate = :include_estimate)
            GROUP BY region
            ORDER BY region
            """
        ).strip()
    )

    (dashboard_path / "outputs.py").write_text(
        dedent(
            """
            from varro.dashboard import Metric, output
            import plotly.express as px

            @output
            def total_population(population_trend, filters):
                return Metric(
                    value=int(population_trend["population"].sum()),
                    label="Total Population",
                    format="number",
                )

            @output
            def periods_shown(population_trend, filters):
                return Metric(value=len(population_trend), label="Periods", format="number")

            @output
            def population_trend_chart(population_trend, filters):
                return px.line(
                    population_trend,
                    x="period",
                    y="population",
                    title="Population Trend",
                )

            @output
            def region_table(population_by_region, filters):
                return population_by_region
            """
        ).strip()
    )

    (dashboard_path / "dashboard.md").write_text(
        dedent(
            """
            # Population Dashboard

            Simple test dashboard.

            ::: filters
            <filter-select name="region" label="Region" options="query:regions" default="all" />
            <filter-date name="period" label="Period" default="all" />
            <filter-checkbox name="include_estimate" label="Include estimate rows" default=false />
            :::

            ::: grid cols=2
            <metric name="total_population" />
            <metric name="periods_shown" />
            :::

            ::: tabs
            ::: tab name="Trend"
            <fig name="population_trend_chart" />
            :::
            ::: tab name="Regions"
            <df name="region_table" />
            :::
            :::
            """
        ).strip()
    )


@pytest.fixture
def dashboard_env(tmp_path: Path) -> DashboardTestEnv:
    engine = create_engine(POSTGRES_USER_SQLALCHEMY)
    table_name = f"dashboard_test_population_{uuid4().hex[:10]}"
    _seed_db(engine, table_name)

    user_id = 1
    dashboards_root = tmp_path
    dashboard_name = "population"
    dashboards_dir = dashboards_root / "user" / str(user_id) / "dashboard"
    _write_dashboard(dashboards_dir / dashboard_name, table_name)

    app, _ = daisy_app()
    mount_dashboard_routes(app, dashboards_root, engine)
    client = TestClient(app)

    yield DashboardTestEnv(
        client=client,
        engine=engine,
        dashboards_root=dashboards_root,
        dashboard_name=dashboard_name,
        user_id=user_id,
    )

    client.close()
    with engine.begin() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS {table_name}"))
    engine.dispose()
