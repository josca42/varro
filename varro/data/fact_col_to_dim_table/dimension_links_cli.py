from varro.data.utils import df_preview, df_dtypes
import pandas as pd
import typer
from varro.config import DATA_DIR
import json
from typing import Literal
from varro.data.disk_to_db.process_tables import (
    check_if_dim_fits_fact_col,
    process_dim_table,
)

FACTS_DIR = DATA_DIR / "statbank_tables"
DIMENSIONS_DIR = DATA_DIR / "mapping_tables"
DIMENSION_LINKS_DIR = DATA_DIR / "dimension_links"
DIM_COLS = ["KODE", "NIVEAU", "TITEL"]


# --- Helper functions ---
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


# --- CLI Commands ---
app = typer.Typer(
    add_completion=False,
    help="Preview denmark statistics dimension tables and read dimension descriptions.",
)


@app.command("view")
def cli_view(
    table_id: str = typer.Argument(..., help="Table ID."),
    rows: int = typer.Option(
        10, "--rows", "-n", min=1, help="Number of rows to preview."
    ),
    db_format: bool = typer.Option(
        False,
        "--db-format",
        "-d",
        help="Process the table for inserting into the database. This will show how the table will look in the database.",
    ),
):
    """View a dimension table."""

    try:
        df = pd.read_parquet(DIMENSIONS_DIR / f"{table_id}" / "table_da.parquet")
    except FileNotFoundError as exc:
        typer.secho(f"Error: {exc}", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)

    df = df[DIM_COLS].copy()
    if db_format:
        df = process_dim_table(df)

    dtypes_str = df_dtypes(df)
    preview_str = df_preview(df, max_rows=rows, name=table_id)
    typer.echo(f"{dtypes_str}\n\n{preview_str}")


@app.command("list")
def cli_list():
    """List all dimension tables."""
    typer.echo(", ".join([fp.stem for fp in DIMENSIONS_DIR.glob("*")]))


@app.command("describe")
def cli_describe(
    table_id: str = typer.Argument(..., help="Dimension table folder name."),
):
    """Print the markdown description (trimmed) for a dimension table."""
    try:
        text = read_dimension_description(table_id)
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)
    typer.echo(text)


@app.command("save-links")
def cli_save_dimension_links(
    table_id: str = typer.Argument(..., help="Table ID."),
    dimension_links: str = typer.Option(..., help="Dimension links as JSON string."),
):
    links_data = json.loads(dimension_links)
    DIMENSION_LINKS_DIR.mkdir(parents=True, exist_ok=True)
    with open(DIMENSION_LINKS_DIR / f"{table_id}.json", "w") as f:
        json.dump(links_data, f, indent=2)
    typer.echo(f"Dimension links saved to {DIMENSION_LINKS_DIR / f'{table_id}.json'}")


@app.command("check-links")
def cli_check_dimension_links(
    fact_table_id: str = typer.Argument(..., help="Fact table ID."),
    dim_table_id: str = typer.Option(..., help="Dimension table ID."),
    fact_col: str = typer.Option(..., help="Fact column name."),
):
    df_fact = pd.read_parquet(
        FACTS_DIR / f"{fact_table_id}.parquet", columns=[fact_col]
    )
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
