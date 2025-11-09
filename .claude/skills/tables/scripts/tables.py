#!/usr/bin/env python3
from pathlib import Path
from typing import Literal, Optional
import pandas as pd
import typer
from varro.disk_to_db.process_tables import (
    process_fact_table,
    check_if_dim_fits_fact_col,
    process_kode_col,
)
from varro.utils import df_preview
import json

FACTS_DIR = Path("/mnt/HC_Volume_103849439/statbank_tables")
DIMENSIONS_DIR = Path("/mnt/HC_Volume_103849439/mapping_tables")
DIM_COLS = ["KODE", "NIVEAU", "TITEL"]
DIMENSION_LINKS_DIR = Path("/mnt/HC_Volume_103849439/dimension_links")


def look_at_table(
    table_id: str,
    table_type: Literal["fact", "dimension"],
    lang: Literal["da", "en"] = "da",
    max_rows: int = 10,
    processed: bool = False,
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
    if processed:
        df = process_fact_table(df)
    if table_type == "dimension":
        df = df[DIM_COLS].copy()
        df = process_kode_col(df)

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
    processed: bool = typer.Option(
        False, "--processed", "-p", help="Process the table before previewing."
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


@app.command("save-dimension-links")
def cli_save_dimension_links(
    table_id: str = typer.Argument(..., help="Table ID."),
    dimension_links: str = typer.Option(..., help="Dimension links as JSON string."),
):
    links_data = json.loads(dimension_links)
    DIMENSION_LINKS_DIR.mkdir(parents=True, exist_ok=True)
    with open(DIMENSION_LINKS_DIR / f"{table_id}.json", "w") as f:
        json.dump(links_data, f, indent=2)
    typer.echo(f"Dimension links saved to {DIMENSION_LINKS_DIR / f'{table_id}.json'}")


@app.command("check-dimension-links")
def cli_check_dimension_links(
    fact_table_id: str = typer.Argument(..., help="Fact table ID."),
    dim_table_id: str = typer.Option(..., help="Dimension table ID."),
    fact_col: str = typer.Option(..., help="Fact column name."),
):
    df_fact = pd.read_parquet(FACTS_DIR / f"{fact_table_id}.parquet")
    df_dim = pd.read_parquet(
        DIMENSIONS_DIR / f"{dim_table_id}" / "table_da.parquet"
    ).rename(columns={"KODE": "kode"})
    try:
        result = check_if_dim_fits_fact_col(df_fact, df_dim, fact_col)
        typer.echo(
            f"Values in fact column {fact_col} are in dimension table {dim_table_id}"
        )
    except ValueError as e:
        typer.echo(e)


if __name__ == "__main__":
    app()
