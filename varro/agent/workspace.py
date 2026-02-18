import os
from pathlib import Path, PurePosixPath
import shutil
from varro.config import DATA_DIR, DOCS_DIR, USER_WORKSPACE_INIT_DIR


READONLY_DOCS_DIRS = {"subjects", "fact", "dim", "geo"}


def is_readonly_user_path(file_path: str) -> bool:
    path = PurePosixPath(file_path)
    if not path.is_absolute():
        return False
    parts = [part for part in path.parts if part != "/"]
    if not parts:
        return False
    return parts[0] in READONLY_DOCS_DIRS


def user_workspace_root(user_id: int) -> Path:
    return DATA_DIR / "user" / str(user_id)


def ensure_user_workspace(user_id: int) -> Path:
    root = user_workspace_root(user_id)
    root.mkdir(parents=True, exist_ok=True)

    for source in DOCS_DIR.iterdir():
        target = root / source.name
        rel_source = Path(os.path.relpath(source, start=target.parent))
        target.symlink_to(rel_source, target_is_directory=True)

    for source in USER_WORKSPACE_INIT_DIR.iterdir():
        target = root / source.name
        shutil.copytree(source, target)

    return root


def resolve_user_path(
    user_id: int,
    file_path: str,
    allow_readonly_symlink_read: bool = False,
) -> Path | str:
    path = PurePosixPath(file_path)
    if not path.is_absolute():
        return "file_path must be an absolute path"
    if ".." in path.parts:
        return "file_path escapes sandbox root"

    user_root = user_workspace_root(user_id).resolve()
    rel_path = file_path.lstrip("/")
    lexical_host_path = user_root / rel_path

    if allow_readonly_symlink_read and is_readonly_user_path(file_path):
        try:
            lexical_host_path.relative_to(user_root)
        except ValueError:
            return "file_path escapes sandbox root"
        return lexical_host_path

    host_path = lexical_host_path.resolve()

    try:
        host_path.relative_to(user_root)
    except ValueError:
        return "file_path escapes sandbox root"

    return host_path
