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

from varro.db.crud.memory import CrudMemory
from varro.db.db import engine
from pathlib import Path, PurePosixPath
from collections import defaultdict
from varro.db import crud


@dataclass
class SessionStore:
    """Stores objects and jupyter kernel"""

    user: User
    jupyter: JupyterCodeExecutor | None = None
    memory: Memory | None = None
    dashboard_state: Dict[str, Any] | None = None
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
        self.crud = CrudMemory(engine, user_id)
        self.user_id = user_id
        self.has_pension_plans = crud.pension_plan.exists(user_id)

    def view(self, command: BetaMemoryTool20250818ViewCommand) -> str:
        path = command.path
        if Path(path).suffix:
            mf = self.crud.get_by_path(path)
            if not mf:
                return f"File not found: {path}"
            text = mf.file_text
            if command.view_range and len(command.view_range) == 2:
                start, end = command.view_range
                lines = text.splitlines(keepends=True)
                text = "".join(lines[start - 1 : end])
            return text

        # Else treat as directory
        entries = self.crud.list_paths_under_prefix(path)
        if not entries:
            return f"Not found: {path}"

        groups = defaultdict(list)
        for p in entries:
            pp = PurePosixPath(p)
            groups[str(pp.parent)].append(pp.name)

        blocks = []
        for folder in sorted(groups):
            lines = "\n".join(f"- {name}" for name in sorted(groups[folder]))
            blocks.append(f"Directory: {folder}\n{lines}")
        return "\n\n".join(blocks)

    def create(self, command: BetaMemoryTool20250818CreateCommand) -> str:
        if command.path.startswith("/memories/wiki"):
            return "You only have read access to the /memories/wiki directory"
        self.crud.upsert_file(command.path, command.file_text)
        return f"File created successfully at {command.path}"

    def str_replace(self, command: BetaMemoryTool20250818StrReplaceCommand) -> str:
        if command.path.startswith("/memories/wiki"):
            return "You only have read access to the /memories/wiki directory"
        path = command.path
        mf = self.crud.get_by_path(path)
        if not mf:
            return f"File not found: {path}"
        old, new = command.old_str or "", command.new_str or ""
        updated_text = (mf.file_text or "").replace(old, new)
        self.crud.set_text(path, updated_text)
        return f"File {path} has been edited"

    def insert(self, command: BetaMemoryTool20250818InsertCommand) -> str:
        if command.path.startswith("/memories/wiki"):
            return "You only have read access to the /memories/wiki directory"
        mf = self.crud.get_by_path(command.path)
        if not mf:
            return f"File not found: {command.path}"
        line_no, insert_text = command.insert_line, command.insert_text
        lines = mf.file_text.splitlines(keepends=True)
        new_text = "".join(lines[: line_no - 1] + [insert_text] + lines[line_no - 1 :])
        self.crud.set_text(command.path, new_text)
        return f"Text inserted at line {line_no} in {command.path}"

    def delete(self, command: BetaMemoryTool20250818DeleteCommand) -> str:
        if command.path.startswith("/memories/wiki"):
            return "You only have read access to the /memories/wiki directory"
        n = self.crud.delete_file(command.path)
        return (
            f"File deleted: {command.path}" if n else f"File not found: {command.path}"
        )

    def rename(self, command: BetaMemoryTool20250818RenameCommand) -> str:
        old, new = command.old_path, command.new_path
        if old.startswith("/memories/wiki") or new.startswith("/memories/wiki"):
            return "You only have read access to the /memories/wiki directory"

        ok = self.crud.rename_file(old, new)
        return f"Renamed {old} to {new}" if ok else f"File not found: {old}"

    def append_pension_plans_entry(self, path: str, entries: list[str]) -> list[str]:
        if path in "/memories/user/":
            user_has_pension_plans = crud.pension_plan.exists(self.user_id)
            if user_has_pension_plans:
                entries.append("/memories/user/pension_plans.xml")
                return entries
            else:
                return entries

        return entries
