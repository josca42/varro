"""ui.components.checkbox

Checkbox component with integrated label support.

This component wraps the DaisyUI checkbox primitive and optionally
includes a label for common form patterns.
"""

from __future__ import annotations

from typing import Literal, Optional

from fasthtml.common import *

from ui.core import cn
from ui.daisy import Checkbox as DaisyCheckbox


CheckboxSize = Literal[
    "default",
    "sm",
    "xs",
    "lg",
]

CheckboxColor = Optional[Literal[
    "primary",
    "secondary",
    "accent",
    "info",
    "success",
    "warning",
    "error",
]]


def Checkbox(
    *,
    name: str,
    label: Optional[str] = None,
    checked: bool = False,
    size: CheckboxSize = "default",
    color: CheckboxColor = "primary",
    disabled: bool = False,
    cls: str = "",
    **kw,
):
    """Checkbox component with optional label.

    When `label` is provided, returns a label-wrapped checkbox.
    Otherwise, returns just the checkbox input.

    Size mapping (compact by default):
    - default -> checkbox-sm
    - sm      -> checkbox-xs
    - xs      -> checkbox-xs
    - lg      -> checkbox-md
    """

    mods: list[str] = []

    # Size (compact defaults)
    if size == "default":
        mods.append("-sm")
    elif size == "sm":
        mods.append("-xs")
    elif size == "xs":
        mods.append("-xs")
    elif size == "lg":
        mods.append("-md")

    # Color
    if color:
        mods.append(f"-{color}")

    checkbox = DaisyCheckbox(
        name=name,
        checked=checked,
        disabled=disabled,
        value="true",
        cls=cn(*mods, cls),
        data_slot="checkbox",
        data_size=size,
        **kw,
    )

    if label:
        return Label(
            checkbox,
            Span(label, cls="label-text ml-2"),
            cls="label cursor-pointer justify-start gap-1",
        )

    return checkbox

