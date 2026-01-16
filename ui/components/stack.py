"""ui.components.stack

Flexbox stack layout wrapper (vertical or horizontal).
"""

from __future__ import annotations

from typing import Literal, Union

from fasthtml.common import Div, FT

from ui.core import cn


StackDirection = Literal["vertical", "horizontal", "row", "col"]


def Stack(
    *c,
    direction: StackDirection = "vertical",
    gap: Union[int, str] = 2,
    align: str = "",
    justify: str = "",
    wrap: bool = False,
    cls: str = "",
    **kw,
) -> FT:
    """
    Flex stack container.

    Args:
        direction: Stack direction - "vertical"/"col" or "horizontal"/"row"
        gap: Gap size (int) or Tailwind gap class suffix
        align: Tailwind align-items class (e.g., "items-center")
        justify: Tailwind justify-content class (e.g., "justify-between")
        wrap: Whether to allow wrapping
        cls: Additional CSS classes
        **kw: Passed to underlying Div

    Example:
        Stack(Button("A"), Button("B"), direction="horizontal", gap=4)
    """
    dir_cls = "flex-col" if direction in ("vertical", "col") else "flex-row"
    gap_cls = f"gap-{gap}" if isinstance(gap, int) else gap
    wrap_cls = "flex-wrap" if wrap else ""

    return Div(
        *c,
        cls=cn("flex", dir_cls, gap_cls, wrap_cls, align, justify, cls),
        data_slot="stack",
        data_direction=direction,
        **kw,
    )


# Convenience aliases
def HStack(*c, gap: Union[int, str] = 2, **kw) -> FT:
    """Horizontal stack (shorthand for Stack with direction='horizontal')."""
    return Stack(*c, direction="horizontal", gap=gap, **kw)


def VStack(*c, gap: Union[int, str] = 2, **kw) -> FT:
    """Vertical stack (shorthand for Stack with direction='vertical')."""
    return Stack(*c, direction="vertical", gap=gap, **kw)

