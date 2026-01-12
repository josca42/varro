"""ui.components.input

Opinionated input primitives.

Shadcn inputs are essentially:
- consistent height
- subtle border
- ring on focus

With DaisyUI v5, the base `input` component already does most of this.
We provide a narrow wrapper that:
- standardizes default size
- supports a small `variant` surface choice (default/ghost)
- supports semantic color states (error/success/...)
"""

from __future__ import annotations

from typing import Literal, Optional

from fasthtml.common import *

from ..core import cn
from ..daisy import Input as DaisyInput, Select as DaisySelect


InputVariant = Literal["default", "ghost"]
InputSize = Literal["default", "sm", "xs", "lg"]
InputColor = Optional[
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


def Input(
    *,
    name: str | None = None,
    id: str | None = None,
    type: str = "text",
    value: str | None = None,
    placeholder: str | None = None,
    variant: InputVariant = "default",
    size: InputSize = "default",
    color: InputColor = None,
    disabled: bool = False,
    required: bool = False,
    cls: str = "",
    **kw,
):
    """Text input.

    Args:
        variant: 'default' or 'ghost'
        size:    default (compact), xs/sm/lg
        color:   DaisyUI semantic color (e.g. 'error')
    """

    mods: list[str] = []

    if variant == "ghost":
        mods.append("-ghost")

    # Size (compact-by-default)
    # - default: input-sm (similar to shadcn default height)
    # - sm/xs:   input-xs
    # - lg:      input-md
    if size == "default":
        mods.append("-sm")
    elif size in ("sm", "xs"):
        mods.append("-xs")
    elif size == "lg":
        mods.append("-md")

    # Color
    if color:
        mods.append(f"-{color}")

    return DaisyInput(
        type=type,
        name=name,
        id=id,
        value=value,
        placeholder=placeholder,
        disabled=disabled,
        required=required,
        cls=cn(*mods, "w-full", cls),
        data_slot="input",
        data_variant=variant,
        data_size=size,
        **kw,
    )


SelectSize = Literal["default", "xs", "sm", "lg"]


def Select(
    *options,
    name: str | None = None,
    id: str | None = None,
    value: str | None = None,
    required: bool = False,
    disabled: bool = False,
    size: SelectSize = "default",
    color: InputColor = None,
    cls: str = "",
    **kw,
):
    """Select wrapper.

    DaisyUI v5: `select` supports color + size modifiers.
    """

    mods: list[str] = []

    # Keep selects aligned with inputs.
    if size == "default":
        mods.append("-sm")
    elif size in ("sm", "xs"):
        mods.append("-xs")
    elif size == "lg":
        mods.append("-md")

    if color:
        mods.append(f"-{color}")

    return DaisySelect(
        *options,
        name=name,
        id=id,
        value=value,
        required=required,
        disabled=disabled,
        cls=cn(*mods, "w-full", cls),
        data_slot="select",
        data_size=size,
        **kw,
    )


__all__ = [
    "Input",
    "Select",
    "InputVariant",
    "InputSize",
    "InputColor",
]
