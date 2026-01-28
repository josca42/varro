"""dashboard.components

Render dashboard components to FastHTML.
"""

from __future__ import annotations

from typing import Any
import pandas as pd
from fasthtml.common import (
    Div,
    Span,
    Button,
    NotStr,
    Form as HtmlForm,
)
import mistletoe

from ui.components import (
    Card,
    CardBody,
    Grid,
    MetricValue,
    DataTable,
    Figure,
    SelectFilter,
    DateRangeFilter,
    CheckboxFilter,
)

from varro.dashboard.models import Metric
from varro.dashboard.filters import (
    Filter,
    SelectFilter as SelectFilterDef,
    DateRangeFilter as DateRangeFilterDef,
    CheckboxFilter as CheckboxFilterDef,
)
from varro.dashboard.parser import ASTNode, ContainerNode, ComponentNode, MarkdownNode
from varro.dashboard.loader import Dashboard


def render_filter(
    f: Filter,
    options: dict[str, list[str]],
    filters: dict[str, Any],
) -> Any:
    """Render a single filter based on its type."""
    name = f.name
    label = f.label or name

    if isinstance(f, SelectFilterDef):
        opts = options.get(name, [])
        current = filters.get(name, f.default)
        return SelectFilter(name, label=label, options=opts, value=current)

    if isinstance(f, DateRangeFilterDef):
        current_from = filters.get(f"{name}_from")
        current_to = filters.get(f"{name}_to")
        return DateRangeFilter(
            name, label=label, from_value=current_from, to_value=current_to
        )

    if isinstance(f, CheckboxFilterDef):
        current = filters.get(name, f.default)
        return CheckboxFilter(name, label=label, checked=current)

    return None


def render_placeholder(dash_name: str, output_type: str, output_name: str) -> Any:
    """Render a placeholder card that lazy-loads via HTMX."""
    return Card(
        CardBody(
            Div(
                Span(cls="loading loading-spinner"),
                cls="flex justify-center items-center h-32",
            ),
            hx_get=f"/dash/{dash_name}/_/{output_type}/{output_name}",
            hx_include="#filters",
            hx_trigger="load, filtersChanged from:body",
            hx_swap="innerHTML",
        ),
        variant="border",
    )


def render_metric_card(m: Metric) -> Any:
    """Render a Metric as a card."""
    return MetricValue(
        m.value,
        format=m.format,
        label=m.label,
        change=m.change,
        change_label=m.change_label,
    )


def render_table(df: pd.DataFrame) -> Any:
    """Render a DataFrame as a DaisyUI table."""
    return DataTable(df)


def render_figure(fig: Any) -> Any:
    """Render a Plotly figure."""
    return Figure(fig)


def render_tabs(
    tab_nodes: list[ContainerNode],
    dash: Dashboard,
    filters: dict[str, Any],
    options: dict[str, list[str]],
) -> Any:
    """Render tabs with Alpine.js."""
    tab_buttons = []
    tab_contents = []

    for i, tab in enumerate(tab_nodes):
        name = tab.attrs.get("name", f"Tab {i + 1}")
        tab_buttons.append(
            Button(
                name,
                cls="tab",
                **{
                    ":class": f"active === {i} && 'tab-active'",
                    "@click": f"active = {i}",
                },
            )
        )
        tab_contents.append(
            Div(
                *render_ast(tab.children, dash, filters, options),
                x_show=f"active === {i}",
                x_cloak=True,
            )
        )

    return Div(
        Div(*tab_buttons, cls="tabs tabs-box", role="tablist"),
        *tab_contents,
        x_data="{ active: 0 }",
    )


def render_ast(
    nodes: list[ASTNode],
    dash: Dashboard,
    filters: dict[str, Any],
    options: dict[str, list[str]],
) -> list[Any]:
    """Render AST nodes to FastHTML """
    result = []

    for node in nodes:
        if isinstance(node, MarkdownNode):
            html = mistletoe.markdown(node.content)
            result.append(Div(NotStr(html), cls="prose prose-sm max-w-none"))

        elif isinstance(node, ComponentNode):
            output_map = {"fig": "figure", "df": "table", "metric": "metric"}
            if node.type in output_map:
                name = node.attrs.get("name", "")
                result.append(render_placeholder(dash.name, output_map[node.type], name))

        elif isinstance(node, ContainerNode):
            if node.type == "filters":
                filter_elements = []
                for f in node.children:
                    if isinstance(f, Filter):
                        el = render_filter(f, options, filters)
                        if el:
                            filter_elements.append(el)

                result.append(
                    HtmlForm(
                        *filter_elements,
                        id="filters",
                        hx_get=f"/dash/{dash.name}/_/filters",
                        hx_trigger="change delay:500ms",
                        hx_swap="none",
                        cls="flex flex-wrap gap-4 items-end mb-6 p-4 bg-base-200/50 rounded-box",
                    )
                )

            elif node.type == "grid":
                cols = node.attrs.get("cols", "2")
                children = render_ast(node.children, dash, filters, options)
                result.append(Grid(*children, cols=int(cols), gap=4))

            elif node.type == "tabs":
                tab_nodes = [
                    c
                    for c in node.children
                    if isinstance(c, ContainerNode) and c.type == "tab"
                ]
                if tab_nodes:
                    result.append(render_tabs(tab_nodes, dash, filters, options))

            elif node.type == "tab":
                pass

            else:
                children = render_ast(node.children, dash, filters, options)
                result.extend(children)

    return result


def render_shell(
    dash: Dashboard,
    filters: dict[str, Any],
    options: dict[str, list[str]],
) -> Any:
    """Render the full dashboard shell."""
    content = render_ast(dash.ast, dash, filters, options)
    return Div(*content, cls="p-6", data_slot="dashboard-shell")
