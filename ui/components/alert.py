"""ui.components.alert

Alert/Callout component (shadcn-inspired) implemented using DaisyUI `alert`.

Alerts display important messages to users, typically for feedback,
warnings, or informational notices.
"""

from __future__ import annotations

from typing import Literal, Optional

from fasthtml.common import *

from ui.core import cn
from ui.daisy import Alert as DaisyAlert


AlertVariant = Literal[
    "default",
    "info",
    "success",
    "warning",
    "error",
]


def Alert(
    *c,
    variant: AlertVariant = "default",
    title: Optional[str] = None,
    cls: str = "",
    **kw,
):
    """Alert component for feedback messages.

    Mapping:
    - default -> base alert styling
    - info    -> alert-info
    - success -> alert-success
    - warning -> alert-warning
    - error   -> alert-error

    If `title` is provided, it renders as a bold span before content.
    """

    mods: list[str] = []

    # Variant
    if variant != "default":
        mods.append(f"-{variant}")

    # Build content
    content = []
    if title:
        content.append(Span(title, cls="font-semibold"))
    content.extend(c)

    return DaisyAlert(
        Div(*content),
        cls=cn(*mods, cls),
        data_slot="alert",
        data_variant=variant,
        role="alert",
        **kw,
    )


# Alias for dashboard markdown compatibility
Callout = Alert

