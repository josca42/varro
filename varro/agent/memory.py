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
    figs: Dict[str, Any] = field(default_factory=dict)
    dfs: Dict[str, pd.DataFrame] = field(default_factory=dict)
    dfs_added_to_notebook: List[str] = field(default_factory=list)
    cached_prompts: Dict[str, str] = field(default_factory=dict)

    def data_in_store(self) -> str:
        dfs = "\n".join([f"- {name}" for name in self.dfs.keys()])
        figs = "\n".join([f"- {name}" for name in self.figs.keys()])
        return f"DataFrames:\n{dfs}\n\nFigures:\n{figs}"
