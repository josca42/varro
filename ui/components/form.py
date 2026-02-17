"""ui.components.form

Form container component with layout options.
"""

from __future__ import annotations

from typing import Literal, Optional

from fasthtml.common import Form as HtmlForm, FT

from ui.core import cn


FormLayout = Literal["horizontal", "vertical"]


def Form(
    *c,
    id: Optional[str] = None,
    layout: FormLayout = "horizontal",
    action: Optional[str] = None,
    method: str = "get",
    cls: str = "",
    **kw,
) -> FT:
    """
    Form container with layout options.

    Args:
        id: Form ID (useful for HTMX hx-include references)
        layout: "horizontal" for inline filters, "vertical" for stacked
        action: Form action URL
        method: HTTP method
        cls: Additional CSS classes
        **kw: Passed to underlying form element

    Example:
        Form(
            Input(name="search", placeholder="Search..."),
            Button("Go"),
            id="filters",
            layout="horizontal",
        )
    """
    if layout == "horizontal":
        layout_cls = "flex flex-wrap gap-4 items-end"
    else:
        layout_cls = "flex flex-col gap-3"

    return HtmlForm(
        *c,
        id=id,
        action=action,
        method=method,
        cls=cn(layout_cls, cls),
        data_slot="form",
        data_layout=layout,
        **kw,
    )

