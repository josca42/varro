"""dashboard.components

Render dashboard components to FastHTML.
"""

from __future__ import annotations

from typing import Any, Optional

import pandas as pd
from fasthtml.common import (
    Div,
    Span,
    Button,
    Option,
    Table,
    Thead,
    Tbody,
    Tr,
    Th,
    Td,
    Label,
    NotStr,
    Form as HtmlForm,
)
import mistletoe

from ui import Card, CardBody, Select, Input, Checkbox, Grid, cn

from .models import Metric
from .parser import ASTNode, ContainerNode, ComponentNode, MarkdownNode
from .loader import Dashboard


# -----------------------------------------------------------------------------
# Value formatting
# -----------------------------------------------------------------------------


def abbrev(n: float | int) -> str:
    """Abbreviate large numbers with K/M/B suffixes."""
    if abs(n) >= 1_000_000_000:
        return f"{n / 1_000_000_000:.1f}B"
    if abs(n) >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if abs(n) >= 1_000:
        return f"{n / 1_000:.1f}K"
    return f"{n:,.0f}"


def format_value(value: float | int | str, fmt: str) -> str:
    """Format a value according to format type."""
    if isinstance(value, str):
        return value
    if fmt == "currency":
        return f"{abbrev(value)} kr."
    if fmt == "percent":
        return f"{value:.1%}"
    return abbrev(value)


# -----------------------------------------------------------------------------
# Filter rendering
# -----------------------------------------------------------------------------


def render_select_filter(
    filter_def: ComponentNode,
    options: list[str],
    current_value: str,
) -> Any:
    """Render a select filter."""
    name = filter_def.attrs.get("name", "")
    label = filter_def.attrs.get("label", name)
    default = filter_def.attrs.get("default", "all")

    # Build options list
    opt_elements = [Option("All", value="all", selected=(current_value == "all"))]
    for opt in options:
        opt_elements.append(Option(opt, value=opt, selected=(current_value == opt)))

    return Div(
        Label(label, cls="text-sm font-medium mb-1 block"),
        Select(*opt_elements, name=name, cls="min-w-32"),
        cls="flex flex-col",
    )


def render_daterange_filter(
    filter_def: ComponentNode,
    current_from: Optional[str],
    current_to: Optional[str],
) -> Any:
    """Render a date range filter."""
    name = filter_def.attrs.get("name", "")
    label = filter_def.attrs.get("label", name)

    return Div(
        Label(label, cls="text-sm font-medium mb-1 block"),
        Div(
            Input(
                name=f"{name}_from",
                type="date",
                value=current_from or "",
                cls="min-w-32",
            ),
            Span("to", cls="text-base-content/60 px-2"),
            Input(
                name=f"{name}_to",
                type="date",
                value=current_to or "",
                cls="min-w-32",
            ),
            cls="flex items-center gap-1",
        ),
        cls="flex flex-col",
    )


def render_checkbox_filter(
    filter_def: ComponentNode,
    current_value: bool,
) -> Any:
    """Render a checkbox filter."""
    name = filter_def.attrs.get("name", "")
    label = filter_def.attrs.get("label", name)

    return Div(
        Label(
            Checkbox(name=name, checked=current_value, value="true"),
            Span(label, cls="ml-2"),
            cls="flex items-center cursor-pointer",
        ),
        cls="flex items-end pb-1",
    )


def render_filter(
    filter_def: ComponentNode,
    options: dict[str, list[str]],
    filters: dict[str, Any],
) -> Any:
    """Render a single filter based on its type."""
    name = filter_def.attrs.get("name", "")
    filter_type = filter_def.type

    if filter_type == "select":
        opts = options.get(name, [])
        current = filters.get(name, filter_def.attrs.get("default", "all"))
        return render_select_filter(filter_def, opts, current)

    if filter_type == "daterange":
        current_from = filters.get(f"{name}_from")
        current_to = filters.get(f"{name}_to")
        return render_daterange_filter(filter_def, current_from, current_to)

    if filter_type == "checkbox":
        default_str = filter_def.attrs.get("default", "false")
        default = default_str.lower() == "true"
        current = filters.get(name, default)
        if isinstance(current, str):
            current = current.lower() == "true"
        return render_checkbox_filter(filter_def, current)

    return None


# -----------------------------------------------------------------------------
# Output rendering
# -----------------------------------------------------------------------------


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
    formatted = format_value(m.value, m.format)

    change_el = None
    if m.change is not None:
        sign = "+" if m.change >= 0 else ""
        color = "text-success" if m.change >= 0 else "text-error"
        change_el = Div(
            Span(f"{sign}{m.change:.1%}", cls=color),
            Span(m.change_label or "", cls="text-base-content/50 ml-1"),
            cls="text-sm mt-2",
        )

    return Div(
        Div(m.label, cls="text-sm text-base-content/60"),
        Div(formatted, cls="text-2xl font-semibold mt-1"),
        change_el,
    )


def render_table(df: pd.DataFrame) -> Any:
    """Render a DataFrame as a DaisyUI table."""
    return Div(
        Table(
            Thead(Tr(*[Th(col) for col in df.columns])),
            Tbody(
                *[
                    Tr(*[Td(str(v)) for v in row])
                    for row in df.itertuples(index=False)
                ]
            ),
            cls="table table-sm",
        ),
        cls="overflow-x-auto",
    )


def render_figure(fig: Any) -> Any:
    """Render a Plotly figure."""
    html = fig.to_html(include_plotlyjs=False, full_html=False)
    return NotStr(html)


# -----------------------------------------------------------------------------
# AST rendering
# -----------------------------------------------------------------------------


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
                **{":class": f"active === {i} && 'tab-active'", "@click": f"active = {i}"},
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
    """Render AST nodes to FastHTML components."""
    result = []

    for node in nodes:
        if isinstance(node, MarkdownNode):
            # Render markdown to HTML
            html = mistletoe.markdown(node.content)
            result.append(Div(NotStr(html), cls="prose prose-sm max-w-none"))

        elif isinstance(node, ComponentNode):
            # Output placeholders
            if node.type in ("figure", "table", "metric"):
                name = node.attrs.get("name", "")
                result.append(render_placeholder(dash.name, node.type, name))

        elif isinstance(node, ContainerNode):
            if node.type == "filters":
                # Render filter form
                filter_elements = []
                for child in node.children:
                    if isinstance(child, ComponentNode):
                        el = render_filter(child, options, filters)
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
                # Collect tab children
                tab_nodes = [
                    c
                    for c in node.children
                    if isinstance(c, ContainerNode) and c.type == "tab"
                ]
                if tab_nodes:
                    result.append(render_tabs(tab_nodes, dash, filters, options))

            elif node.type == "tab":
                # Tabs are handled by parent
                pass

            else:
                # Unknown container, render children
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


__all__ = [
    "render_shell",
    "render_ast",
    "render_metric_card",
    "render_table",
    "render_figure",
    "render_placeholder",
    "render_filter",
    "format_value",
    "abbrev",
]
