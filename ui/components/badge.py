"""ui.components.badge

Opinionated badge component (shadcn-inspired) implemented using DaisyUI `badge`.

In shadcn, badges have `variant` as the primary API. We keep that pattern
and add `size` and `color` for flexibility.
"""

from __future__ import annotations

from typing import Literal, Optional

from fasthtml.common import *

from ..core import cn
from ..daisy import Badge as DaisyBadge


BadgeVariant = Literal[
    "default",
    "secondary",
    "outline",
    "soft",
]

BadgeSize = Literal[
    "default",
    "sm",
    "lg",
]

BadgeColor = Optional[Literal[
    "primary",
    "secondary",
    "accent",
    "neutral",
    "info",
    "success",
    "warning",
    "error",
]]


def Badge(
    *c,
    variant: BadgeVariant = "default",
    size: BadgeSize = "default",
    color: BadgeColor = None,
    cls: str = "",
    **kw,
):
    """Badge component for status indicators, labels, and tags.

    Mapping:
    - default   -> badge-primary (or color if specified)
    - secondary -> badge-secondary
    - outline   -> badge-outline
    - soft      -> badge-soft

    Sizes are DaisyUI badge sizes.
    """

    mods: list[str] = []

    # Variant
    if variant == "default":
        if color:
            mods.append(f"-{color}")
        else:
            mods.append("-primary")
    elif variant == "secondary":
        mods.append("-secondary")
    elif variant == "outline":
        mods.append("-outline")
        if color:
            mods.append(f"-{color}")
    elif variant == "soft":
        mods.append("-soft")
        if color:
            mods.append(f"-{color}")

    # Size
    if size == "sm":
        mods.append("-sm")
    elif size == "lg":
        mods.append("-lg")

    return DaisyBadge(
        *c,
        cls=cn(*mods, cls),
        data_slot="badge",
        data_variant=variant,
        data_size=size,
        **kw,
    )


__all__ = ["Badge", "BadgeVariant", "BadgeSize", "BadgeColor"]
