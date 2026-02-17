from pathlib import Path
from varro.config import TABLES_DOCS_DIR, SUBJECTS_DOCS_DIR


def generate_hierarchy(docs_dir: Path = SUBJECTS_DOCS_DIR) -> str:
    """
    Generate compact hierarchy with roots and mids only.

    The agent discovers leaves on demand via Bash("ls /subjects/{root}/{mid}/").

    Output format:
        root:
          mid1
          mid2
    """
    lines = []

    roots = sorted(d for d in docs_dir.iterdir() if d.is_dir())

    for root in roots:
        mids = sorted(d for d in root.iterdir() if d.is_dir())
        if not mids:
            continue
        lines.append(f"{root.name}:")
        for mid in mids:
            lines.append(f"  {mid.name}")
        lines.append("")

    return "\n".join(lines).rstrip()


def subject_overview_tool(leaf: str) -> str:
    """
    Get docs for a leaf subject showing available tables.

    Args:
        leaf: Full path "arbejde_og_indkomst/indkomst_og_løn/løn"
              or unique leaf name "løn"

    Returns:
        Content of the subject's markdown file

    Raises:
        FileNotFoundError: No matching subject
        ValueError: Ambiguous leaf name
    """
    leaf = leaf.strip("/").lower()

    # Try as full path first (root/mid/leaf -> root/mid/leaf.md)
    parts = leaf.split("/")
    full_path = SUBJECTS_DOCS_DIR.joinpath(*parts[:-1], f"{parts[-1]}.md")
    if full_path.exists():
        return full_path.read_text()

    # Try as leaf name
    leaf_name = parts[-1]
    matches = list(SUBJECTS_DOCS_DIR.glob(f"**/{leaf_name}.md"))

    if len(matches) == 1:
        return matches[0].read_text()
    elif len(matches) > 1:
        paths = sorted(
            str(m.relative_to(SUBJECTS_DOCS_DIR).with_suffix(""))
            for m in matches
        )
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

    # Search through the subject hierarchy for the table doc
    matches = list(TABLES_DOCS_DIR.glob(f"**/{table_id}.md"))

    if len(matches) == 1:
        return matches[0].read_text()
    elif len(matches) > 1:
        return matches[0].read_text()

    raise FileNotFoundError(f"No docs for table: {table_id}")
