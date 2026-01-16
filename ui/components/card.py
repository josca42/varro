"""ui.components.card

Opinionated card components (shadcn-inspired) implemented using DaisyUI `card`.

Shadcn's Card is a compound component set:
- Card (root)
- CardHeader
- CardTitle
- CardDescription
- CardContent
- CardFooter

We keep the same mental model, but map to DaisyUI's `card` + `card-body` and use
Tailwind utilities to achieve the desired spacing.

Project-specific defaults:
- compact spacing
- flat surfaces (theme sets `--depth: 0`)
- border is opt-in (`variant='border'`)
"""

from __future__ import annotations

from typing import Literal, Optional

from fasthtml.common import *

from ui.core import cn
from ui.daisy import (
    CardRoot as DaisyCardRoot,
    CardBody as DaisyCardBody,
    CardTitle as DaisyCardTitle,
    CardActions as DaisyCardActions,
)


CardVariant = Literal[
    "default",
    "border",
    "dash",
]

CardSize = Literal["default", "sm", "lg"]


def Card(
    *c,
    variant: CardVariant = "default",
    size: CardSize = "default",
    cls: str = "",
    **kw,
):
    """Card root.

    DaisyUI uses:
    - `card` base
    - `card-border` or `card-dash` styles
    - `card-sm`, `card-md`, ... sizes
    """

    mods: list[str] = []

    if variant == "border":
        mods.append("-border")
    elif variant == "dash":
        mods.append("-dash")

    # Size tuning: we keep `card` itself at default; adjust padding via our subparts.
    # Still allow DaisyUI's card size modifiers if desired.
    if size == "sm":
        mods.append("-sm")
    elif size == "lg":
        mods.append("-lg")

    # Allow overriding data_slot (e.g., MetricCard uses data_slot="metric-card")
    if "data_slot" not in kw:
        kw["data_slot"] = "card"

    return DaisyCardRoot(
        *c,
        cls=cn(*mods, cls),
        data_variant=variant,
        data_size=size,
        **kw,
    )


def CardHeader(*c, cls: str = "", **kw):
    """Header region inside a Card.

    Implemented as a `div` within the DaisyUI card-body.
    """

    return Div(
        *c,
        cls=cn("space-y-1", cls),
        data_slot="card-header",
        **kw,
    )


def CardTitle(*c, cls: str = "", **kw):
    # Use DaisyUI's `card-title` part for consistent typography.
    return DaisyCardTitle(
        *c,
        cls=cn("", cls),
        data_slot="card-title",
        **kw,
    )


def CardDescription(*c, cls: str = "", **kw):
    return Div(
        *c,
        cls=cn("text-sm text-base-content/60", cls),
        data_slot="card-description",
        **kw,
    )


def CardContent(*c, cls: str = "", **kw):
    return Div(
        *c,
        cls=cn("", cls),
        data_slot="card-content",
        **kw,
    )


def CardFooter(*c, cls: str = "", **kw):
    # Shadcn-style footer: muted surface + border.
    # We keep it inside the card-body but expand with negative margins.
    return Div(
        *c,
        cls=cn(
            "bg-base-200/40 border-t border-base-300 -mx-4 -mb-4 mt-3 px-4 py-3 flex items-center justify-end gap-2",
            cls,
        ),
        data_slot="card-footer",
        **kw,
    )


def CardBody(
    *c,
    cls: str = "",
    **kw,
):
    """DaisyUI `card-body` with compact defaults."""

    return DaisyCardBody(
        *c,
        cls=cn("gap-3", cls),
        data_slot="card-body",
        **kw,
    )


def CardActions(*c, cls: str = "", **kw):
    """DaisyUI `card-actions`, lightly normalized."""

    return DaisyCardActions(
        *c,
        cls=cn("justify-end", cls),
        data_slot="card-actions",
        **kw,
    )


def CardSimple(
    title: str,
    *body,
    description: Optional[str] = None,
    actions: Optional[tuple] = None,
    variant: CardVariant = "border",
    cls: str = "",
    **kw,
):
    """A small convenience wrapper for common cards.

    This is intentionally narrow (personal project usage) rather than a generic card DSL.
    """

    header_bits = [CardTitle(title)]
    if description:
        header_bits.append(CardDescription(description))

    body_bits: list = []
    if header_bits:
        body_bits.append(CardHeader(*header_bits))

    body_bits.extend(body)

    if actions:
        body_bits.append(CardFooter(*actions))

    return Card(
        CardBody(*body_bits),
        variant=variant,
        cls=cls,
        **kw,
    )

