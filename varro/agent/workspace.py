from __future__ import annotations

from pathlib import Path, PurePosixPath
import shutil

from varro.config import DATA_DIR, DOCS_DIR

DEMO_USER_ID = 1


def user_workspace_root(user_id: int) -> Path:
    return DATA_DIR / "user" / str(user_id)


def ensure_user_workspace(user_id: int) -> Path:
    root = user_workspace_root(user_id)
    root.mkdir(parents=True, exist_ok=True)
    if not DOCS_DIR.exists():
        return root

    for source in DOCS_DIR.iterdir():
        target = root / source.name
        if target.exists():
            continue
        if source.is_dir():
            shutil.copytree(source, target)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    return root


def resolve_user_path(user_id: int, file_path: str) -> Path | str:
    path = PurePosixPath(file_path)
    if not path.is_absolute():
        return "file_path must be an absolute path"
    if ".." in path.parts:
        return "file_path escapes sandbox root"

    user_root = ensure_user_workspace(user_id).resolve()
    rel_path = file_path.lstrip("/")
    host_path = (user_root / rel_path).resolve()

    try:
        host_path.relative_to(user_root)
    except ValueError:
        return "file_path escapes sandbox root"

    return host_path
