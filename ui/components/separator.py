"""ui.components.separator

Shadcn's Separator is a thin rule. DaisyUI's equivalent is `divider`.

We keep the API close to shadcn:
- orientation: 'horizontal' | 'vertical'
- decorative: bool (kept for parity; DaisyUI's divider is decorative by default)

If you pass children, DaisyUI renders the text in the divider.
"""

from __future__ import annotations

from typing import Literal, Optional

from fasthtml.common import *

from ..core import cn
from ..daisy import Divider


SeparatorOrientation = Literal["horizontal", "vertical"]
SeparatorColor = Optional[
    Literal[
        "neutral",
        "primary",
        "secondary",
        "accent",
        "success",
        "warning",
        "info",
        "error",
    ]
]


def Separator(
    *c,
    orientation: SeparatorOrientation = "horizontal",
    decorative: bool = True,
    color: SeparatorColor = None,
    cls: str = "",
    **kw,
):
    mods: list[str] = []

    if orientation == "horizontal":
        mods.append("-horizontal")
    else:
        mods.append("-vertical")

    if color:
        mods.append(f"-{color}")

    # NOTE: `decorative` is kept for parity; it doesn't change output.
    # If you need aria semantics, pass `role`/`aria_*` via **kw.
    return Divider(
        *c,
        cls=cn(*mods, cls),
        data_slot="separator",
        data_orientation=orientation,
        **kw,
    )


__all__ = ["Separator", "SeparatorOrientation", "SeparatorColor"]
