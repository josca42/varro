#!/usr/bin/env python3
from pathlib import Path
from typing import Literal, Optional

import pandas as pd
import typer

FACTS_DIR = Path("/mnt/HC_Volume_103849439/statbank_tables")
DIMENSIONS_DIR = Path("/mnt/HC_Volume_103849439/mapping_tables")
DIM_COLS = ["KODE", "NIVEAU", "TITEL"]


def look_at_table(
    table_id: str,
    table_type: Literal["fact", "dimension"],
    lang: Literal["da", "en"] = "da",
    max_rows: int = 10,
) -> str:
    """Load a parquet table and return a small, pipe-separated preview as text."""
    if table_type == "fact":
        path = FACTS_DIR / f"{table_id}.parquet"
    elif table_type == "dimension":
        path = DIMENSIONS_DIR / table_id / f"table_{lang}.parquet"
    else:
        raise ValueError(f"Invalid table type: {table_type!r}")

    if not path.exists():
        raise FileNotFoundError(f"Parquet not found: {path}")

    df = pd.read_parquet(path)
    if table_type == "dimension":
        df = df[DIM_COLS].copy()
    dtypes_str = df_dtypes(df)
    preview_str = df_preview(df, max_rows=max_rows, name=table_id)
    return f"{dtypes_str}\n\n{preview_str}"


def read_dimension_description(table_id: str, lang: Literal["da", "en"] = "da") -> str:
    """
    Read the markdown description for a dimension table and trim the first/last line.
    Falls back to 'da' if the requested language file doesn't exist.
    """
    md_path = DIMENSIONS_DIR / table_id / f"table_info_{lang}.md"
    if not md_path.exists() and lang != "da":
        # graceful fallback
        md_path = DIMENSIONS_DIR / table_id / "table_info_da.md"

    if not md_path.exists():
        raise FileNotFoundError(f"Description not found: {md_path}")

    with open(md_path, "r", encoding="utf-8") as f:
        return drop_first_last(f.read())


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


def drop_first_last(text: str) -> str:
    lines = text.splitlines()
    return "\n".join(lines[1:-1]) if len(lines) > 2 else ""


def df_dtypes(df: pd.DataFrame) -> str:
    """Return a pipe-separated 'column|dtype' listing."""
    parts = [f"{col}|{dtype}" for col, dtype in df.dtypes.items()]
    return "column|dtype\n" + "\n".join(parts)


# --- CLI Commands ---
app = typer.Typer(
    add_completion=False,
    help="Preview StatBank fact/dimension tables and read dimension descriptions.",
)


@app.command("preview")
def cli_preview(
    table_id: str = typer.Argument(
        ...,
        help="Table ID (e.g. FOLK1A for fact; dimension id folder name for dimension).",
    ),
    table_type: Literal["fact", "dimension"] = typer.Option(
        ..., "--type", "-t", help="Which kind of table to read."
    ),
    lang: Literal["da", "en"] = typer.Option(
        "da", help="Language for dimension parquet/description."
    ),
    rows: int = typer.Option(
        10, "--rows", "-n", min=1, help="Number of rows to preview."
    ),
):
    """Print a small preview of a fact or dimension parquet table."""
    try:
        text = look_at_table(table_id, table_type, lang=lang, max_rows=rows)
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)
    typer.echo(text)


@app.command("describe")
def cli_describe(
    table_id: str = typer.Argument(..., help="Dimension table folder name."),
    lang: Literal["da", "en"] = typer.Option(
        "da", help="Language to read (falls back to 'da' if missing)."
    ),
):
    """Print the markdown description (trimmed) for a dimension table."""
    try:
        text = read_dimension_description(table_id, lang=lang)
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)
    typer.echo(text)


@app.command("list")
def cli_list():
    """List all dimension tables."""
    typer.echo(", ".join([fp.stem for fp in DIMENSIONS_DIR.glob("*")]))


if __name__ == "__main__":
    app()
