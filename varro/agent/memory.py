from __future__ import annotations

from anthropic.lib.tools import BetaAbstractMemoryTool
from anthropic.types.beta import (
    BetaMemoryTool20250818CreateCommand,
    BetaMemoryTool20250818DeleteCommand,
    BetaMemoryTool20250818InsertCommand,
    BetaMemoryTool20250818RenameCommand,
    BetaMemoryTool20250818StrReplaceCommand,
    BetaMemoryTool20250818ViewCommand,
)
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List, Literal
import pandas as pd
from varro.agent.jupyter_kernel import JupyterCodeExecutor
from varro.db.models.user import User
from pathlib import Path
import shutil

MEMORY_DIR = Path("/mnt/HC_Volume_103849439/memories")
DOCS_DIR = Path("/root/varro/docs")


@dataclass
class SessionStore:
    """Stores objects and jupyter kernel"""

    user: User
    jupyter: JupyterCodeExecutor | None = None
    memory: Memory | None = None
    figs: Dict[str, Any] = field(default_factory=dict)
    dfs: Dict[str, pd.DataFrame] = field(default_factory=dict)
    dfs_added_to_notebook: List[str] = field(default_factory=list)
    cached_prompts: Dict[str, str] = field(default_factory=dict)

    def data_in_store(self) -> str:
        dfs = "\n".join([f"- {name}" for name in self.dfs.keys()])
        figs = "\n".join([f"- {name}" for name in self.figs.keys()])
        return f"DataFrames:\n{dfs}\n\nFigures:\n{figs}"


class Memory(BetaAbstractMemoryTool):
    def __init__(self, user_id: int):
        super().__init__()
        self.root = MEMORY_DIR / str(user_id)
        self.root.mkdir(parents=True, exist_ok=True)

    def _resolve(self, virtual_path: str) -> Path:
        if virtual_path.startswith("/memories/docs"):
            relative = virtual_path.removeprefix("/memories/docs").lstrip("/")
            real_path = (DOCS_DIR / relative).resolve()
            if not real_path.is_relative_to(DOCS_DIR.resolve()):
                raise PermissionError(f"Access denied: {virtual_path}")
            return real_path
        relative = virtual_path.removeprefix("/memories").lstrip("/")
        real_path = (self.root / relative).resolve()
        if not real_path.is_relative_to(self.root.resolve()):
            raise PermissionError(f"Access denied: {virtual_path}")
        return real_path

    def _is_docs_path(self, path: Path) -> bool:
        return path.resolve().is_relative_to(DOCS_DIR.resolve())

    def view(self, command: BetaMemoryTool20250818ViewCommand) -> str:
        path = self._resolve(command.path)
        if path.is_dir():
            entries = sorted(path.iterdir())
            return (
                "\n".join(f"- {e.name}{'/' if e.is_dir() else ''}" for e in entries)
                or "(empty)"
            )

        content = path.read_text()
        if command.view_range:
            lines = content.splitlines(keepends=True)
            start, end = command.view_range
            return "".join(lines[start - 1 : end])
        return content

    def create(self, command: BetaMemoryTool20250818CreateCommand) -> str:
        path = self._resolve(command.path)
        if self._is_docs_path(path):
            raise PermissionError("Write operations not allowed in /memories/docs")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(command.file_text or "")
        return f"Created {command.path}"

    def str_replace(self, command: BetaMemoryTool20250818StrReplaceCommand) -> str:
        path = self._resolve(command.path)
        if self._is_docs_path(path):
            raise PermissionError("Write operations not allowed in /memories/docs")
        content = path.read_text()
        old, new = command.old_str or "", command.new_str or ""
        if content.count(old) != 1:
            raise ValueError(
                f"String must appear exactly once (found {content.count(old)})"
            )
        path.write_text(content.replace(old, new, 1))
        return f"Replaced in {command.path}"

    def insert(self, command: BetaMemoryTool20250818InsertCommand) -> str:
        path = self._resolve(command.path)
        if self._is_docs_path(path):
            raise PermissionError("Write operations not allowed in /memories/docs")
        lines = path.read_text().splitlines(keepends=True)
        text = command.insert_text or ""
        if not text.endswith("\n"):
            text += "\n"
        lines.insert(command.insert_line - 1, text)
        path.write_text("".join(lines))
        return f"Inserted at line {command.insert_line}"

    def delete(self, command: BetaMemoryTool20250818DeleteCommand) -> str:
        path = self._resolve(command.path)
        if self._is_docs_path(path):
            raise PermissionError("Write operations not allowed in /memories/docs")
        shutil.rmtree(path) if path.is_dir() else path.unlink()
        return f"Deleted {command.path}"

    def rename(self, command: BetaMemoryTool20250818RenameCommand) -> str:
        old, new = self._resolve(command.old_path), self._resolve(command.new_path)
        if self._is_docs_path(old) or self._is_docs_path(new):
            raise PermissionError("Write operations not allowed in /memories/docs")
        new.parent.mkdir(parents=True, exist_ok=True)
        old.rename(new)
        return f"Renamed {command.old_path} → {command.new_path}"
