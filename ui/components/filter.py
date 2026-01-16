"""ui.components.filter

Filter components for dashboards and data views.
"""

from __future__ import annotations

from typing import Optional, Sequence

from fasthtml.common import Div, FT, Label, Option, Span

from ..core import cn
from .input import Input, Select
from .checkbox import Checkbox


def SelectFilter(
    name: str,
    *,
    label: Optional[str] = None,
    options: Sequence[str] = (),
    value: str = "all",
    include_all: bool = True,
    all_label: str = "All",
    cls: str = "",
    **kw,
) -> FT:
    """
    Select dropdown filter.

    Args:
        name: Form field name
        label: Label text (defaults to name)
        options: List of option values
        value: Currently selected value
        include_all: Whether to include an "All" option (default True)
        all_label: Label for the all option (default "All")
        cls: Additional CSS classes
        **kw: Passed to underlying Select
    """
    display_label = label or name

    opt_elements = []
    if include_all:
        opt_elements.append(Option(all_label, value="all", selected=(value == "all")))
    for opt in options:
        opt_elements.append(Option(opt, value=opt, selected=(value == opt)))

    return Div(
        Label(display_label, cls="text-sm font-medium mb-1 block"),
        Select(*opt_elements, name=name, cls="min-w-32", **kw),
        cls=cn("flex flex-col", cls),
        data_slot="select-filter",
    )


def DateRangeFilter(
    name: str,
    *,
    label: Optional[str] = None,
    from_value: Optional[str] = None,
    to_value: Optional[str] = None,
    cls: str = "",
    **kw,
) -> FT:
    """
    Date range filter with from/to inputs.

    Args:
        name: Base form field name (creates {name}_from and {name}_to)
        label: Label text (defaults to name)
        from_value: Current from date value
        to_value: Current to date value
        cls: Additional CSS classes
        **kw: Passed to underlying inputs
    """
    display_label = label or name

    return Div(
        Label(display_label, cls="text-sm font-medium mb-1 block"),
        Div(
            Input(
                name=f"{name}_from",
                type="date",
                value=from_value or "",
                cls="min-w-32",
                **kw,
            ),
            Span("to", cls="text-base-content/60 px-2"),
            Input(
                name=f"{name}_to",
                type="date",
                value=to_value or "",
                cls="min-w-32",
                **kw,
            ),
            cls="flex items-center gap-1",
        ),
        cls=cn("flex flex-col", cls),
        data_slot="daterange-filter",
    )


def CheckboxFilter(
    name: str,
    *,
    label: Optional[str] = None,
    checked: bool = False,
    cls: str = "",
    **kw,
) -> FT:
    """
    Checkbox filter.

    Args:
        name: Form field name
        label: Label text (defaults to name)
        checked: Whether the checkbox is checked
        cls: Additional CSS classes
        **kw: Passed to underlying Checkbox
    """
    display_label = label or name

    return Div(
        Label(
            Checkbox(name=name, checked=checked, value="true", **kw),
            Span(display_label, cls="ml-2"),
            cls="flex items-center cursor-pointer",
        ),
        cls=cn("flex items-end pb-1", cls),
        data_slot="checkbox-filter",
    )


__all__ = ["SelectFilter", "DateRangeFilter", "CheckboxFilter"]
