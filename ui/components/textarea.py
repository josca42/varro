"""ui.components.textarea

Opinionated textarea wrapper using DaisyUI `textarea`.

We keep a compact default (`textarea-sm`) and expose a minimal surface API.
"""

from __future__ import annotations

from typing import Literal, Optional

from fasthtml.common import *

from ..core import cn
from ..daisy import Textarea as DaisyTextarea


TextareaVariant = Literal["default", "ghost"]
TextareaSize = Literal["default", "sm", "xs", "lg"]
TextareaColor = Optional[
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


def Textarea(
    *c,
    name: str | None = None,
    id: str | None = None,
    placeholder: str | None = None,
    rows: int | None = None,
    variant: TextareaVariant = "default",
    size: TextareaSize = "default",
    color: TextareaColor = None,
    disabled: bool = False,
    required: bool = False,
    cls: str = "",
    **kw,
):
    mods: list[str] = []

    if variant == "ghost":
        mods.append("-ghost")

    if size == "default":
        mods.append("-sm")
    elif size in ("sm", "xs"):
        mods.append("-xs")
    elif size == "lg":
        mods.append("-md")

    if color:
        mods.append(f"-{color}")

    return DaisyTextarea(
        *c,
        name=name,
        id=id,
        placeholder=placeholder,
        rows=rows,
        disabled=disabled,
        required=required,
        cls=cn(*mods, "w-full", cls),
        data_slot="textarea",
        data_variant=variant,
        data_size=size,
        **kw,
    )


__all__ = ["Textarea", "TextareaVariant", "TextareaSize", "TextareaColor"]
