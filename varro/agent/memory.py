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
from typing import Dict, Optional, TYPE_CHECKING
from varro.db.models.user import User
from varro.config import EVIDENCE_USERS_DIR, MEMORY_DIR
from pathlib import Path
import shutil
from varro.agent.ipython_shell import get_shell, TerminalInteractiveShell

if TYPE_CHECKING:
    from varro.evidence import EvidenceManager


@dataclass
class SessionStore:
    """Stores objects and jupyter kernel"""

    user: User
    shell: TerminalInteractiveShell | None = None
    memory: Memory | None = None
    cached_prompts: Dict[str, str] = field(default_factory=dict)
    shell_imports: bool = False

    def __init__(self, user: User):
        self.user = user
        self.memory = Memory(user.id)
        self.cached_prompts = {}
        self.shell = get_shell()
        self.shell_imports = False

    def cleanup(self):
        self.shell.reset(new_session=False)
        self.shell.history_manager.end_session()


class Memory(BetaAbstractMemoryTool):
    def __init__(self, user_id: int):
        super().__init__()
        self.root = MEMORY_DIR / str(user_id)
        self.evidence_root = EVIDENCE_USERS_DIR / str(user_id)
        self.root.mkdir(parents=True, exist_ok=True)
        self.evidence_root.mkdir(parents=True, exist_ok=True)

    def _resolve(self, virtual_path: str) -> Path:
        if virtual_path.startswith("/memories/d/"):
            relative = virtual_path.removeprefix("/memories/d/").lstrip("/")
            real_path = (self.evidence_root / relative).resolve()
            if not real_path.is_relative_to(self.evidence_root.resolve()):
                raise PermissionError(f"Access denied: {virtual_path}")
            return real_path

        relative = virtual_path.removeprefix("/memories").lstrip("/")
        real_path = (self.root / relative).resolve()
        if not real_path.is_relative_to(self.root.resolve()):
            raise PermissionError(f"Access denied: {virtual_path}")
        return real_path

    def view(self, command: BetaMemoryTool20250818ViewCommand) -> str:
        # Special handling for root - show dashboards + general memory
        if command.path.rstrip("/") == "/memories":
            lines = ["## Dashboards"]
            if self.evidence_root.exists():
                dashboards = sorted(
                    d for d in self.evidence_root.iterdir() if d.is_dir()
                )
                if dashboards:
                    for d in dashboards:
                        lines.append(f"- {d.name}/")
                else:
                    lines.append("(none)")
            else:
                lines.append("(none)")
            lines.append("\n## Notes")
            if self.root.exists():
                entries = sorted(self.root.iterdir())
                if entries:
                    for e in entries:
                        lines.append(f"- {e.name}{'/' if e.is_dir() else ''}")
                else:
                    lines.append("(empty)")
            else:
                lines.append("(empty)")
            return "\n".join(lines)

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
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(command.file_text or "")
        return f"Created {command.path}"

    def str_replace(self, command: BetaMemoryTool20250818StrReplaceCommand) -> str:
        path = self._resolve(command.path)
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
        lines = path.read_text().splitlines(keepends=True)
        text = command.insert_text or ""
        if not text.endswith("\n"):
            text += "\n"
        lines.insert(command.insert_line - 1, text)
        path.write_text("".join(lines))
        return f"Inserted at line {command.insert_line}"

    def delete(self, command: BetaMemoryTool20250818DeleteCommand) -> str:
        path = self._resolve(command.path)
        shutil.rmtree(path) if path.is_dir() else path.unlink()
        return f"Deleted {command.path}"

    def rename(self, command: BetaMemoryTool20250818RenameCommand) -> str:
        old, new = self._resolve(command.old_path), self._resolve(command.new_path)
        new.parent.mkdir(parents=True, exist_ok=True)
        old.rename(new)
        return f"Renamed {command.old_path} → {command.new_path}"
