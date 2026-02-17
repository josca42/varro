"""ui.components.link

Link primitives for anchor elements.
"""

from __future__ import annotations

from typing import Literal, Optional

from fasthtml.common import A

from ui.core import cn


LinkColor = Optional[
    Literal[
        "neutral",
        "primary",
        "secondary",
        "accent",
        "info",
        "success",
        "warning",
        "error",
    ]
]


def Link(
    *c,
    href: str | None = None,
    color: LinkColor = None,
    underline: bool = True,
    cls: str = "",
    **kw,
):
    """Text link using DaisyUI `link` styles."""

    mods: list[str] = ["link"]

    if underline:
        mods.append("link-hover")

    if color:
        mods.append(f"link-{color}")

    return A(
        *c,
        href=href,
        cls=cn(*mods, cls),
        data_slot="link",
        data_color=color or "default",
        **kw,
    )

