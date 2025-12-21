from pathlib import Path
from varro.config import TABLES_DOCS_DIR, SUBJECTS_DOCS_DIR


def generate_hierarchy(docs_dir: Path = SUBJECTS_DOCS_DIR) -> str:
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
                d.name
                for d in mid.iterdir()
                if d.is_dir() and (d / "README.md").exists()
            )
            if leaves:
                leaves_str = ", ".join(leaves)
                lines.append(f"  {mid.name}: {leaves_str}")

        lines.append("")  # blank line between roots

    return "\n".join(lines).rstrip()


def subject_overview_tool(leaf: str) -> str:
    """
    Get the README for a leaf subject showing available tables.

    Args:
        leaf: Full path "arbejde_og_indkomst/indkomst_og_løn/løn"
              or unique leaf name "løn"

    Returns:
        Content of the subject's README.md

    Raises:
        FileNotFoundError: No matching subject
        ValueError: Ambiguous leaf name
    """
    leaf = leaf.strip("/").lower()

    # Try as full path first
    full_path = SUBJECTS_DOCS_DIR / leaf / "README.md"
    if full_path.exists():
        return full_path.read_text()

    # Try as leaf name
    matches = list(SUBJECTS_DOCS_DIR.glob(f"**/{leaf}/README.md"))

    if len(matches) == 1:
        return matches[0].read_text()
    elif len(matches) > 1:
        paths = sorted(str(m.parent.relative_to(SUBJECTS_DOCS_DIR)) for m in matches)
        raise ValueError(f"Ambiguous: {leaf!r} matches {paths}")

    raise FileNotFoundError(f"Subject not found: {leaf}")


def table_docs_tool(table_id: str) -> str:
    """
    Get documentation for any table (fact or dimension).

    Args:
        table_id: Table identifier like "lon10", "nuts",
                  or with schema prefix "fact.lon10", "dim.nuts"

    Returns:
        Content of the table's markdown documentation

    Raises:
        FileNotFoundError: Table docs don't exist
    """
    table_id = table_id.strip().lower()

    # Strip schema prefix if present
    if "." in table_id:
        table_id = table_id.split(".")[-1]

    path = TABLES_DOCS_DIR / f"{table_id}.md"

    if not path.exists():
        raise FileNotFoundError(f"No docs for table: {table_id}")

    return path.read_text()
