from pathlib import Path
from varro.config import SUBJECTS_DOCS_DIR
import difflib


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
                if d.is_dir() and (d / "subject_overview.md").exists()
            )
            if leaves:
                leaves_str = ", ".join(leaves)
                lines.append(f"  {mid.name}: {leaves_str}")

        lines.append("")  # blank line between roots

    return "\n".join(lines).rstrip()


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
    full = SUBJECTS_DOCS_DIR / path / "subject_overview.md"
    if full.exists():
        return full.read_text()

    # Try as leaf name (search)
    matches = list(SUBJECTS_DOCS_DIR.glob(f"**/{path}/subject_overview.md"))
    if len(matches) == 1:
        return matches[0].read_text()
    elif len(matches) > 1:
        paths = sorted(str(m.parent.relative_to(SUBJECTS_DOCS_DIR)) for m in matches)
        raise ValueError(f"Ambiguous. Matches: {paths}")

    raise FileNotFoundError(f"No subject found: {path}")


def _all_leaves() -> list[str]:
    """Get all leaf subject paths."""
    return sorted(
        str(p.parent.relative_to(SUBJECTS_DOCS_DIR))
        for p in SUBJECTS_DOCS_DIR.glob("**/subject_overview.md")
    )
