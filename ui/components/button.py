"""ui.components.button

Opinionated button component (shadcn-inspired) implemented using DaisyUI `btn`.

In shadcn, the button API is primarily `variant` + `size`. We keep that.

This file intentionally *does not* expose every DaisyUI button modifier.
If you need a special-case modifier, pass it via `cls` (e.g. cls='-dash -wide').
"""

from __future__ import annotations

from typing import Literal

from fasthtml.common import *

from ui.core import cn
from ui.daisy import Btn, LinkBtn, Loading


ButtonVariant = Literal[
    "default",
    "secondary",
    "destructive",
    "outline",
    "ghost",
    "link",
]

ButtonSize = Literal[
    "default",  # compact, shadcn-ish
    "sm",
    "xs",
    "lg",
    "icon",     # square icon button
]


def _button_mods(variant: ButtonVariant, size: ButtonSize) -> list[str]:
    mods: list[str] = []

    # Variant
    if variant == "default":
        mods.append("-primary")
    elif variant == "secondary":
        mods.append("-secondary")
    elif variant == "destructive":
        mods.append("-error")
        mods.append("-soft")
    elif variant == "outline":
        mods.append("-outline")
    elif variant == "ghost":
        mods.append("-ghost")
    elif variant == "link":
        mods.append("-link")

    # Size
    if size == "default":
        mods.append("-sm")
    elif size == "sm":
        mods.append("-xs")
    elif size == "xs":
        # DaisyUI does not document btn-2xs; keep it the same as sm.
        mods.append("-xs")
    elif size == "lg":
        mods.append("-md")
    elif size == "icon":
        mods.append("-square")
        mods.append("-sm")

    return mods


def Button(
    *c,
    variant: ButtonVariant = "default",
    size: ButtonSize = "default",
    loading: bool = False,
    disabled: bool = False,
    cls: str = "",
    **kw,
):
    """Primary button component.

    Mapping is intentionally project-specific:
    - default     -> btn-primary
    - secondary   -> btn-secondary
    - destructive -> btn-error btn-soft  (shadcn destructive is often "soft")
    - outline     -> btn-outline
    - ghost       -> btn-ghost
    - link        -> btn-link

    Sizes are tuned to match the project's compact density.
    """

    mods = _button_mods(variant, size)

    attrs = {
        "data_variant": variant,
        "data_size": size,
        "data_slot": "button",
        "disabled": disabled or loading,
    }

    content = c
    if loading:
        # Keep the spinner small and aligned.
        content = (
            Loading(cls="-spinner -xs", aria_hidden="true"),
            *c,
        )
        attrs["aria_busy"] = "true"

    return Btn(*content, cls=cn(*mods, cls), **attrs, **kw)


def LinkButton(
    *c,
    href: str | None = None,
    variant: ButtonVariant = "default",
    size: ButtonSize = "default",
    loading: bool = False,
    disabled: bool = False,
    cls: str = "",
    **kw,
):
    """Anchor styled as a button."""

    mods = _button_mods(variant, size)

    attrs = {
        "data_variant": variant,
        "data_size": size,
        "data_slot": "link-button",
        "href": href,
    }

    if disabled or loading:
        mods.append("-disabled")
        attrs["aria_disabled"] = "true"
        attrs["tabindex"] = "-1"

    content = c
    if loading:
        content = (
            Loading(cls="-spinner -xs", aria_hidden="true"),
            *c,
        )
        attrs["aria_busy"] = "true"

    return LinkBtn(*content, cls=cn(*mods, cls), **attrs, **kw)


def IconButton(
    *c,
    variant: ButtonVariant = "ghost",
    size: Literal["default", "sm"] = "default",
    cls: str = "",
    **kw,
):
    """Convenience wrapper for icon-only buttons."""

    return Button(
        *c,
        variant=variant,
        size="icon",
        cls=cn("[&_svg]:size-4", "" if size == "default" else "", cls),
        **kw,
    )

