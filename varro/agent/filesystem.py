from pathlib import Path

from pydantic_ai import BinaryContent
from pydantic_ai.messages import ToolReturn
from itertools import islice

TEXT_EXTENSIONS = {".md", ".txt"}
IMAGE_EXTENSIONS = {".png"}
MAX_LINES_DEFAULT = 2000
MAX_LINE_LENGTH = 2000


def _error(message: str) -> str:
    return f"Error: {message}"


def read_file(
    file_path: str, offset: int | None = None, limit: int | None = None
) -> str | ToolReturn:
    path = Path(file_path)
    if not path.is_absolute():
        return _error("file_path must be an absolute path")
    if path.exists() and path.is_dir():
        return _error("path is a directory")
    if not path.exists():
        return _error("file does not exist")

    suffix = path.suffix.lower()
    if suffix in IMAGE_EXTENSIONS:
        try:
            data = path.read_bytes()
        except OSError as exc:
            return _error(str(exc))
        return ToolReturn(
            return_value=f"Read image: {path.name}",
            content=[BinaryContent(data=data, media_type="image/png")],
        )

    if suffix not in TEXT_EXTENSIONS:
        return _error("unsupported file type")

    if path.stat().st_size == 0:
        return "Warning: file is empty."

    start = max(1, offset or 1)
    max_lines = MAX_LINES_DEFAULT if limit is None else max(0, limit)
    try:
        lines = []
        with path.open("r", encoding="utf-8") as handle:
            for line_no, line in enumerate(handle, start=1):
                if line_no < start:
                    continue
                if len(lines) >= max_lines:
                    break
                lines.append(f"{line_no:>6}\t{line.rstrip('\n')[:MAX_LINE_LENGTH]}")
    except OSError as exc:
        return _error(str(exc))

    return "\n".join(lines)


def write_file(file_path: str, content: str) -> str:
    path = Path(file_path)
    if not path.is_absolute():
        return _error("file_path must be an absolute path")
    if path.exists() and path.is_dir():
        return _error("path is a directory")
    if not path.parent.exists():
        return _error("parent directory does not exist")
    try:
        path.write_text(content, encoding="utf-8")
    except OSError as exc:
        return _error(str(exc))
    return f"Wrote {len(content)} bytes."


def edit_file(
    file_path: str,
    old_string: str,
    new_string: str,
    replace_all: bool = False,
) -> str:
    path = Path(file_path)
    if not path.is_absolute():
        return _error("file_path must be an absolute path")
    if path.exists() and path.is_dir():
        return _error("path is a directory")
    if not path.exists():
        return _error("file does not exist")
    if old_string == new_string:
        return _error("new_string must be different from old_string")
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        return _error(str(exc))
    occurrences = content.count(old_string)
    if occurrences == 0:
        return _error("old_string not found in file")
    if occurrences > 1 and not replace_all:
        return _error("old_string is not unique; set replace_all=True to replace all")

    if replace_all:
        new_content = content.replace(old_string, new_string)
        replaced = occurrences
    else:
        new_content = content.replace(old_string, new_string, 1)
        replaced = 1

    try:
        path.write_text(new_content, encoding="utf-8")
    except OSError as exc:
        return _error(str(exc))
    return f"Replaced {replaced} occurrence(s)."
