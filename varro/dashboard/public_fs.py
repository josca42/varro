from __future__ import annotations

import shutil
from pathlib import Path


REQUIRED_FILES = ("dashboard.md", "outputs.py")
OPTIONAL_FILES = ("notes.md",)


def public_dashboard_dir(data_root: Path, owner_id: int, slug: str) -> Path:
    return data_root / "public" / str(owner_id) / slug


def has_public_dashboard(data_root: Path, owner_id: int, slug: str) -> bool:
    return (public_dashboard_dir(data_root, owner_id, slug) / "dashboard.md").exists()


def copy_dashboard_source(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True, exist_ok=True)

    for name in REQUIRED_FILES:
        shutil.copy2(src / name, dst / name)

    for name in OPTIONAL_FILES:
        source = src / name
        if source.exists():
            shutil.copy2(source, dst / name)

    src_queries = src / "queries"
    dst_queries = dst / "queries"
    dst_queries.mkdir(parents=True, exist_ok=True)
    for query in sorted(src_queries.glob("*.sql")):
        shutil.copy2(query, dst_queries / query.name)


def next_fork_slug(private_dashboards_dir: Path, base_slug: str) -> str:
    if not (private_dashboards_dir / base_slug).exists():
        return base_slug

    fork_slug = f"{base_slug}-fork"
    if not (private_dashboards_dir / fork_slug).exists():
        return fork_slug

    n = 2
    while (private_dashboards_dir / f"{fork_slug}-{n}").exists():
        n += 1
    return f"{fork_slug}-{n}"
