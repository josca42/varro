"""ui.components.grid

Simple CSS grid layout wrapper.
"""

from __future__ import annotations

from typing import Union

from fasthtml.common import Div, FT

from ui.core import cn


def Grid(
    *c,
    cols: Union[int, str] = 2,
    gap: Union[int, str] = 4,
    cls: str = "",
    **kw,
) -> FT:
    """
    Grid layout container.

    Args:
        cols: Number of columns (int) or Tailwind grid-cols class suffix
        gap: Gap size (int) or Tailwind gap class suffix
        cls: Additional CSS classes
        **kw: Passed to underlying Div

    Example:
        Grid(Card(...), Card(...), cols=3, gap=6)
    """
    cols_cls = f"grid-cols-{cols}" if isinstance(cols, int) else cols
    gap_cls = f"gap-{gap}" if isinstance(gap, int) else gap

    return Div(
        *c,
        cls=cn("grid", cols_cls, gap_cls, cls),
        data_slot="grid",
        **kw,
    )

