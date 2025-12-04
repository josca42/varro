#!/usr/bin/env python3
"""Generate compact inline hierarchy from subject folders."""

from pathlib import Path
import typer

DOCS_DIR = Path("/root/varro/docs/fact_tables")

app = typer.Typer(add_completion=False)


def generate_hierarchy(docs_dir: Path = DOCS_DIR) -> str:
    """
    Generate compact inline format from folder structure.

    Output format:
        root:
          mid: leaf1, leaf2, leaf3
          mid2: leaf4, leaf5
    """
    lines = []

    roots = sorted(d for d in docs_dir.iterdir() if d.is_dir())

    for root in roots:
        lines.append(f"{root.name}:")

        mids = sorted(d for d in root.iterdir() if d.is_dir())
        for mid in mids:
            leaves = sorted(
                d.name for d in mid.iterdir()
                if d.is_dir() and (d / "subject_overview.md").exists()
            )
            if leaves:
                leaves_str = ", ".join(leaves)
                lines.append(f"  {mid.name}: {leaves_str}")

        lines.append("")  # blank line between roots

    return "\n".join(lines).rstrip()


@app.command()
def main(
    docs_dir: Path = typer.Option(DOCS_DIR, "--dir", "-d", help="Docs directory"),
    output: Path = typer.Option(None, "--output", "-o", help="Output file (stdout if omitted)"),
):
    """Generate compact subject hierarchy."""
    hierarchy = generate_hierarchy(docs_dir)

    if output:
        output.write_text(hierarchy)
        typer.echo(f"Written to {output}")
    else:
        typer.echo(hierarchy)


if __name__ == "__main__":
    app()
