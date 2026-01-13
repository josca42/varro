"""dashboard.routes

FastHTML routes for dashboards.
"""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

from fasthtml.common import Div, Response
from sqlalchemy.engine import Engine

from .loader import Dashboard
from .executor import execute_output, execute_options_query
from .components import (
    render_shell,
    render_metric_card,
    render_table,
    render_figure,
)
from .parser import ComponentNode


def parse_filters_from_request(
    req: Any,
    filter_defs: list[ComponentNode],
) -> dict[str, Any]:
    """Parse filter values from request query params.

    Applies defaults for missing values.
    """
    filters: dict[str, Any] = {}

    for f in filter_defs:
        name = f.attrs.get("name", "")

        if f.type == "select":
            default = f.attrs.get("default", "all")
            filters[name] = req.query_params.get(name, default)

        elif f.type == "daterange":
            default = f.attrs.get("default", "all")
            default_from = f.attrs.get("default_from", "")
            default_to = f.attrs.get("default_to", "")

            if default == "all":
                default_from = ""
                default_to = ""

            filters[f"{name}_from"] = (
                req.query_params.get(f"{name}_from", default_from) or None
            )
            filters[f"{name}_to"] = (
                req.query_params.get(f"{name}_to", default_to) or None
            )

        elif f.type == "checkbox":
            default_str = f.attrs.get("default", "false")
            default = default_str.lower() == "true"
            value = req.query_params.get(name)
            if value is not None:
                filters[name] = value.lower() == "true"
            else:
                filters[name] = default

    return filters


def build_filter_url(
    dash_name: str,
    filters: dict[str, Any],
    filter_defs: list[ComponentNode],
) -> str:
    """Build URL with filter params, omitting defaults."""
    params: dict[str, str] = {}

    for f in filter_defs:
        name = f.attrs.get("name", "")

        if f.type == "select":
            default = f.attrs.get("default", "all")
            value = filters.get(name, default)
            if value != default:
                params[name] = str(value)

        elif f.type == "daterange":
            default = f.attrs.get("default", "all")
            default_from = f.attrs.get("default_from", "")
            default_to = f.attrs.get("default_to", "")

            if default == "all":
                default_from = ""
                default_to = ""

            from_val = filters.get(f"{name}_from") or ""
            to_val = filters.get(f"{name}_to") or ""

            if from_val and from_val != default_from:
                params[f"{name}_from"] = from_val
            if to_val and to_val != default_to:
                params[f"{name}_to"] = to_val

        elif f.type == "checkbox":
            default_str = f.attrs.get("default", "false")
            default = default_str.lower() == "true"
            value = filters.get(name, default)
            if value != default:
                params[name] = "true" if value else "false"

    base = f"/dash/{dash_name}"
    if params:
        return f"{base}?{urlencode(params)}"
    return base


def mount_dashboard_routes(
    app: Any,
    dashboards: dict[str, Dashboard],
    engine: Engine,
) -> None:
    """Register dashboard routes on a FastHTML app."""

    @app.get("/dash/{name}")
    def dashboard_shell(name: str, req):
        if name not in dashboards:
            return Response("Dashboard not found", status_code=404)

        dash = dashboards[name]
        filters = parse_filters_from_request(req, dash.filter_defs)

        # Execute options queries for select filters
        options: dict[str, list[str]] = {}
        for f in dash.filter_defs:
            if f.type == "select":
                filter_name = f.attrs.get("name", "")
                options[filter_name] = execute_options_query(dash, f, engine)

        return render_shell(dash, filters, options)

    @app.get("/dash/{name}/_/filters")
    def filter_sync(name: str, req):
        if name not in dashboards:
            return Response("Dashboard not found", status_code=404)

        dash = dashboards[name]
        filters = parse_filters_from_request(req, dash.filter_defs)
        url = build_filter_url(name, filters, dash.filter_defs)

        return Response(
            "",
            headers={
                "HX-Replace-Url": url,
                "HX-Trigger": '{"filtersChanged": {}}',
            },
        )

    @app.get("/dash/{name}/_/figure/{output_name}")
    def render_figure_endpoint(name: str, output_name: str, req):
        if name not in dashboards:
            return Response("Dashboard not found", status_code=404)

        dash = dashboards[name]
        filters = parse_filters_from_request(req, dash.filter_defs)

        try:
            _, result = execute_output(dash, output_name, filters, engine)
            return render_figure(result)
        except Exception:
            return Div("Error loading chart", cls="text-error text-center p-4")

    @app.get("/dash/{name}/_/table/{output_name}")
    def render_table_endpoint(name: str, output_name: str, req):
        if name not in dashboards:
            return Response("Dashboard not found", status_code=404)

        dash = dashboards[name]
        filters = parse_filters_from_request(req, dash.filter_defs)

        try:
            _, result = execute_output(dash, output_name, filters, engine)
            return render_table(result)
        except Exception:
            return Div("Error loading table", cls="text-error text-center p-4")

    @app.get("/dash/{name}/_/metric/{output_name}")
    def render_metric_endpoint(name: str, output_name: str, req):
        if name not in dashboards:
            return Response("Dashboard not found", status_code=404)

        dash = dashboards[name]
        filters = parse_filters_from_request(req, dash.filter_defs)

        try:
            _, result = execute_output(dash, output_name, filters, engine)
            return render_metric_card(result)
        except Exception:
            return Div("Error loading metric", cls="text-error text-center p-4")


__all__ = [
    "mount_dashboard_routes",
    "parse_filters_from_request",
    "build_filter_url",
]
