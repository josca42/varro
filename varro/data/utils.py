import pandas as pd
from typing import Literal

HEADER_VARS = ["id", "text", "description", "unit"]


def normalize_column_name(col_name: str) -> str:
    return col_name.lower().replace("å", "a").replace("ø", "o").replace("æ", "ae")


def df_preview(df: pd.DataFrame, max_rows: int = 10, name: str = "df") -> str:
    """Generate a pipe-separated DataFrame preview."""
    if df.index.name:
        df = df.reset_index()
    n_rows = min(max_rows, len(df))
    csv_string = df.head(n_rows).to_csv(
        sep="|",
        index=False,
        float_format="%.3f",
        na_rep="N/A",
    )
    if n_rows == len(df):
        return csv_string
    else:
        return f"{name}.head({n_rows})\n" + csv_string


def df_dtypes(df: pd.DataFrame) -> str:
    """Generate a string of the DataFrame's dtypes."""
    return "\n".join([f"{col}|{dtype}" for col, dtype in df.dtypes.items()])


def create_table_info_dict(table_info, normalize_col_names: bool = False):
    info = {v: table_info[v] for v in HEADER_VARS}
    info["dimensions"] = {}
    for var in table_info["variables"]:
        values_text = {
            "text": values_text_repr(var["values"], type_="text"),
            "id": values_text_repr(var["values"], type_="id"),
        }
        col_name = (
            normalize_column_name(var["id"]) if normalize_col_names else var["id"]
        )
        info["dimensions"][col_name] = values_text
    return info


def values_text_repr(values, type_: Literal["text", "id"] = "text"):
    if len(values) <= 10:
        values_text = ", ".join([v[type_] for v in values])
    else:
        values_start = ", ".join([v[type_] for v in values[:5]])
        values_end = ", ".join([v[type_] for v in values[-5:]])
        values_text = values_start + " ... " + values_end

    return values_text


def show_column_values(table_info, column: str):
    for var in table_info["variables"]:
        if var["text"] == column:
            var_vals = (
                var["values"][:500] if len(var["values"]) > 500 else var["values"]
            )
            return "\n".join(
                f"<value id={d['id']}>{d['text']}</value>" for d in var_vals
            )
    return None
