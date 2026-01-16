"""ui.components.table

Data table component for displaying pandas DataFrames.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from fasthtml.common import Div, FT, Table, Thead, Tbody, Tr, Th, Td

from ..core import cn

if TYPE_CHECKING:
    import pandas as pd

TableVariant = Literal["default", "zebra", "pin-rows", "pin-cols"]
TableSize = Literal["default", "xs", "sm", "lg"]


def DataTable(
    df: "pd.DataFrame",
    *,
    variant: TableVariant = "default",
    size: TableSize = "default",
    cls: str = "",
    **kw,
) -> FT:
    """
    Render a pandas DataFrame as a DaisyUI table.

    Args:
        df: The pandas DataFrame to render
        variant: Table style - "default", "zebra", "pin-rows", "pin-cols"
        size: Table size - "default" (sm), "xs", "sm", "lg"
        cls: Additional CSS classes
        **kw: Passed to underlying Div wrapper
    """
    table_mods = ["table"]

    if size == "default":
        table_mods.append("table-sm")
    elif size == "xs":
        table_mods.append("table-xs")
    elif size == "sm":
        table_mods.append("table-sm")
    elif size == "lg":
        table_mods.append("table-lg")

    if variant == "zebra":
        table_mods.append("table-zebra")
    elif variant == "pin-rows":
        table_mods.append("table-pin-rows")
    elif variant == "pin-cols":
        table_mods.append("table-pin-cols")

    return Div(
        Table(
            Thead(Tr(*[Th(col) for col in df.columns])),
            Tbody(
                *[
                    Tr(*[Td(str(v)) for v in row])
                    for row in df.itertuples(index=False)
                ]
            ),
            cls=" ".join(table_mods),
        ),
        cls=cn("overflow-x-auto", cls),
        data_slot="data-table",
        data_variant=variant,
        data_size=size,
        **kw,
    )


__all__ = ["DataTable", "TableVariant", "TableSize"]
