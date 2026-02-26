"""Audit dimension joins for fact tables and update dimension_links JSON."""

import json
import re
import typer
from pathlib import Path
from varro.config import DST_DIMENSION_LINKS_DIR, SUBJECTS_DIR
from varro.context.fact_table import (
    get_column_dtypes,
    get_join_expression,
    load_dim_links,
)
from varro.db.db import dst_owner_engine

COMMON_AGGREGATES = {
    "tot", "ialt", "i alt", "alle", "total", "all",
    "0", "00", "000", "0000", "00000",
}

app = typer.Typer(add_completion=False, help="Audit and fix dimension join documentation.")


def diagnose_join(table: str, column: str, dim_table: str, link: dict) -> dict:
    fact_dtypes = get_column_dtypes(table, "fact")
    dim_dtypes = get_column_dtypes(dim_table, "dim")

    base_join = get_join_expression(
        column, fact_dtypes.get(column), dim_dtypes.get("kode"), "f", "d"
    )
    override = link.get("join_override")
    effective_join = _aliased(override, column) if override else base_join

    with dst_owner_engine.connect() as conn:
        total = conn.exec_driver_sql(
            f"SELECT COUNT(DISTINCT {column}) FROM fact.{table}"
        ).scalar()

        matched = conn.exec_driver_sql(
            f"SELECT COUNT(DISTINCT f.{column}) FROM fact.{table} f "
            f"JOIN dim.{dim_table} d ON {effective_join}"
        ).scalar()

        unmatched_rows = conn.exec_driver_sql(
            f"SELECT DISTINCT f.{column} FROM fact.{table} f "
            f"LEFT JOIN dim.{dim_table} d ON {effective_join} "
            f"WHERE d.kode IS NULL LIMIT 20"
        ).scalars().all()

    match_pct = round(matched / total * 100) if total else 0
    unmatched = [str(v) for v in unmatched_rows if v is not None]

    suggestions = _detect_patterns(table, column, dim_table, unmatched, base_join)

    return {
        "match_pct": match_pct,
        "total": total,
        "matched": matched,
        "unmatched": unmatched,
        "has_override": bool(override),
        "effective_join": effective_join,
        **suggestions,
    }


def _aliased(override: str, column: str) -> str:
    """Add f./d. aliases to a join_override if not already present."""
    expr = override
    if "f." not in expr and "d." not in expr:
        expr = re.sub(rf'\b{re.escape(column)}\b', f'f.{column}', expr, count=1)
        expr = re.sub(r'\bkode\b', 'd.kode', expr, count=1)
    return expr


def _detect_patterns(
    table: str, column: str, dim_table: str, unmatched: list[str], base_join: str
) -> dict:
    if not unmatched:
        return {"suggested_note": None, "suggested_override": None}

    lower_unmatched = {v.lower() for v in unmatched}
    if lower_unmatched <= COMMON_AGGREGATES:
        agg_list = ", ".join(sorted(unmatched))
        return {
            "suggested_note": f"Aggregate codes ({agg_list}) not in dimension",
            "suggested_override": None,
        }

    non_agg = [v for v in unmatched if v.lower() not in COMMON_AGGREGATES]

    fact_dtypes = get_column_dtypes(table, "fact")
    fact_is_text = "character" in (fact_dtypes.get(column) or "") or "text" in (fact_dtypes.get(column) or "")

    # V prefix pattern (only makes sense for text columns)
    if fact_is_text and all(v.startswith("V") and len(v) > 1 for v in non_agg):
        override = f"REPLACE(f.{column}, 'V', '')=d.kode::text"
        if _test_override(table, column, dim_table, override):
            agg_codes = [v for v in unmatched if v.lower() in COMMON_AGGREGATES]
            note = "V prefix on fact codes"
            if agg_codes:
                note += f"; aggregate codes ({', '.join(agg_codes)}) not in dimension"
            return {"suggested_note": note, "suggested_override": f"REPLACE({column}, 'V', '')=kode::text"}

    # Space removal pattern (only for text columns)
    if fact_is_text and any(" " in v for v in non_agg):
        override = f"f.{column}=REPLACE(d.kode, ' ', '')"
        if _test_override(table, column, dim_table, override):
            return {
                "suggested_note": "Spaces in dim codes removed for join",
                "suggested_override": f"{column}=REPLACE(kode, ' ', '')",
            }

    return {"suggested_note": None, "suggested_override": None}


def _test_override(table: str, column: str, dim_table: str, override_expr: str) -> bool:
    """Test if an override improves match rate significantly."""
    try:
        with dst_owner_engine.connect() as conn:
            total = conn.exec_driver_sql(
                f"SELECT COUNT(DISTINCT {column}) FROM fact.{table}"
            ).scalar()
            matched = conn.exec_driver_sql(
                f"SELECT COUNT(DISTINCT f.{column}) FROM fact.{table} f "
                f"JOIN dim.{dim_table} d ON {override_expr}"
            ).scalar()
        return total > 0 and (matched / total) > 0.8
    except Exception:
        return False


def _format_diagnostic(table: str, column: str, dim_table: str, diag: dict, link: dict):
    status = "OK" if diag["match_pct"] == 100 else f"{diag['match_pct']}%"
    note = link.get("note", "")
    lines = [
        f"  {column} -> dim.{dim_table}: {status} ({diag['matched']}/{diag['total']})",
        f"    join: {diag['effective_join']}",
    ]
    if note:
        lines.append(f"    note: {note}")
    if diag["unmatched"]:
        sample = ", ".join(diag["unmatched"][:10])
        lines.append(f"    unmatched: [{sample}]")
    if diag["suggested_note"]:
        lines.append(f"    suggested note: {diag['suggested_note']}")
    if diag["suggested_override"]:
        lines.append(f"    suggested override: {diag['suggested_override']}")
    return "\n".join(lines)


@app.command("audit-table")
def cli_audit_table(table_id: str = typer.Argument(..., help="Fact table ID (lowercase).")):
    """Audit dimension joins for a single fact table."""
    table = table_id.lower()
    dim_links = load_dim_links(table)

    if not dim_links:
        typer.echo(f"{table}: no dimension links")
        return

    typer.echo(f"\n{table}")
    typer.echo("=" * 40)
    for col, link in dim_links.items():
        dim_table = link["dimension"]
        diag = diagnose_join(table, col, dim_table, link)
        typer.echo(_format_diagnostic(table, col, dim_table, diag, link))
    typer.echo()


@app.command("audit-subject")
def cli_audit_subject(
    subject_path: str = typer.Argument(..., help="Path to subject .md file in context/subjects/."),
):
    """Audit all fact tables in a subject."""
    path = Path(subject_path)
    if not path.exists():
        path = SUBJECTS_DIR / subject_path
    if not path.exists() and not path.suffix:
        path = path.with_suffix(".md")
    if not path.exists():
        typer.secho(f"Not found: {subject_path}", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)

    tables = _extract_table_ids(path)
    if not tables:
        typer.echo(f"No tables found in {path}")
        return

    typer.echo(f"Subject: {path.stem} ({len(tables)} tables)")
    for table in tables:
        cli_audit_table(table)


def _extract_table_ids(subject_md: Path) -> list[str]:
    text = subject_md.read_text()
    return re.findall(r"^id:\s*(\S+)", text, re.MULTILINE)


@app.command("update-link")
def cli_update_link(
    table_id: str = typer.Argument(..., help="Fact table ID (uppercase for file)."),
    column: str = typer.Argument(..., help="Column name (as in JSON, usually UPPERCASE)."),
    note: str = typer.Option(None, "--note", "-n", help="Note to add."),
    override: str = typer.Option(None, "--override", "-o", help="Join override expression."),
):
    """Update note and/or join_override for a dimension link."""
    json_path = DST_DIMENSION_LINKS_DIR / f"{table_id.upper()}.json"
    if not json_path.exists():
        typer.secho(f"Not found: {json_path}", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)

    links = json.loads(json_path.read_text())
    col_upper = column.upper()
    found = False
    for link in links:
        if link["column"].upper() == col_upper:
            if note is not None:
                link["note"] = note
            if override is not None:
                link["join_override"] = override
            found = True
            break

    if not found:
        typer.secho(f"Column '{column}' not found in {json_path.name}", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)

    json_path.write_text(json.dumps(links, indent=2, ensure_ascii=False) + "\n")
    typer.echo(f"Updated {json_path.name}: {column}")



if __name__ == "__main__":
    app()
