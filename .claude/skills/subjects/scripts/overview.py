#!/usr/bin/env python3
"""Navigate subject hierarchy and retrieve subject overviews."""

from pathlib import Path
from typing import Optional
import difflib
import typer

DOCS_DIR = Path("/root/varro/docs/fact_tables")

app = typer.Typer(add_completion=False)


def _all_leaves() -> list[str]:
    """Get all leaf subject paths."""
    return sorted(
        str(p.parent.relative_to(DOCS_DIR))
        for p in DOCS_DIR.glob("**/subject_overview.md")
    )


def find(query: str = "", limit: int = 10) -> list[str]:
    """
    Find leaf subjects matching query.

    Args:
        query: Search term (matches against path segments)
        limit: Max results to return

    Returns:
        List of matching paths like "borgere/befolkning/befolkningstal"
    """
    all_paths = _all_leaves()

    if not query:
        return all_paths[:limit]

    query = query.lower().strip("/")

    # Exact segment match first
    exact = [p for p in all_paths if query in p.lower()]
    if exact:
        return exact[:limit]

    # Fuzzy fallback
    close = difflib.get_close_matches(query, all_paths, n=limit, cutoff=0.4)
    return close


def overview(path: str) -> str:
    """
    Get subject_overview.md content for a leaf subject.

    Args:
        path: Full path like "borgere/befolkning/befolkningstal"
              or unique leaf name like "befolkningstal"

    Returns:
        Content of subject_overview.md
    """
    path = path.strip("/").lower()

    # Try as full path
    full = DOCS_DIR / path / "subject_overview.md"
    if full.exists():
        return full.read_text()

    # Try as leaf name (search)
    matches = list(DOCS_DIR.glob(f"**/{path}/subject_overview.md"))
    if len(matches) == 1:
        return matches[0].read_text()
    elif len(matches) > 1:
        paths = sorted(str(m.parent.relative_to(DOCS_DIR)) for m in matches)
        raise ValueError(f"Ambiguous. Matches: {paths}")

    raise FileNotFoundError(f"No subject found: {path}")


@app.command("find")
def find_cmd(
    query: Optional[str] = typer.Argument(None, help="Search term"),
    limit: int = typer.Option(10, "-n", help="Max results"),
):
    """Find leaf subjects matching query."""
    results = find(query or "", limit)
    for path in results:
        typer.echo(path)


@app.command("get")
def get_cmd(
    path: str = typer.Argument(..., help="Subject path or leaf name"),
):
    """Get subject_overview.md content."""
    try:
        typer.echo(overview(path))
    except (FileNotFoundError, ValueError) as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
