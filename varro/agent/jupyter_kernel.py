from __future__ import annotations
import base64
import json
import re
import tempfile
import threading
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union, List, Dict, Literal

from attrs import field
from nbclient import NotebookClient
from nbformat import NotebookNode
from nbformat import v4 as nbformat
import pandas as pd
from pydantic import Field

JUPYTER_INITIAL_IMPORTS = """
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
"""


@dataclass
class CodeBlock:
    code: str


@dataclass
class JupyterCodeResult:
    exit_code: int
    prints: str
    objects: list[str] = Field(default_factory=list)


# --------------------------------
# Stateful Jupyter kernel executor (synchronous)
# --------------------------------
class JupyterCodeExecutor:
    """
    Stateful Jupyter code executor using nbclient (synchronous).
    - Keeps one live kernel across messages
    - No pip installs; uses current environment
    - Parquet-based DataFrame transfer to/from kernel
    """

    def __init__(
        self,
        work_dir: Path,
        kernel_name: str = "python3",
        timeout: int = 3 * 60,
    ) -> None:
        if timeout < 1:
            raise ValueError("timeout must be >= 1 second")

        self._kernel_name = kernel_name
        self._timeout = timeout
        self._work_dir: Path = work_dir
        self._work_dir.mkdir(parents=True, exist_ok=True)

        self._client: Optional[NotebookClient] = None
        self._kernel_ctx = None
        self._started = False

        # Prevent concurrent cell execution (nbclient is not concurrent-safe)
        self._exec_lock = threading.Lock()

        # Map variable/output names -> saved file paths (accumulated)
        self.output_file_map: Dict[str, Path] = {}

    # -------------------------
    # Lifecycle
    # -------------------------

    def start(self) -> None:
        """Start the kernel once per chat/session."""
        if self._started:
            return
        nb: NotebookNode = nbformat.new_notebook()  # type: ignore
        self._client = NotebookClient(
            nb=nb,
            kernel_name=self._kernel_name,
            timeout=self._timeout,
            allow_errors=True,
        )
        # Keep the kernel alive between calls
        self._kernel_ctx = self._client.setup_kernel()
        self._kernel_ctx.__enter__()
        self._started = True

        result = self.execute(JUPYTER_INITIAL_IMPORTS)
        if result.exit_code != 0:
            raise RuntimeError(f"Failed to execute initial imports: {result.output}")

    def stop(self) -> None:
        """Gracefully stop the kernel (call on chat end)."""
        if not self._started:
            return
        if self._kernel_ctx is not None:
            self._kernel_ctx.__exit__(None, None, None)
            self._kernel_ctx = None
        self._client = None
        self._started = False
        self._work_dir.rmdir()

    def restart(self) -> None:
        self.stop()
        self.start()

    def execute(self, code: str) -> JupyterCodeResult:
        """Execute a single code string."""
        return self._execute_code_block(CodeBlock(code=code))

    # -------------------------
    # DataFrame transfer (Parquet)
    # -------------------------
    def put_df(self, name: str, df: pd.DataFrame) -> Path:
        """Load a host DataFrame into the live kernel as variable `name` using Parquet."""
        parquet_path = self._parquet_path(name=name)
        df.to_parquet(parquet_path)
        code = f"{name} = pd.read_parquet('{parquet_path}')"
        result = self.execute(code)
        if result.exit_code != 0:
            raise RuntimeError(f"Failed to put DataFrame into kernel: {result.output}")
        return parquet_path

    def get_dataframe(self, name: str) -> "pd.DataFrame":
        """Fetch a kernel DataFrame variable back into host via Parquet."""
        parquet_path = self.save_dataframe(name)
        return pd.read_parquet(parquet_path)

    def save_dataframe(self, name: str) -> Path:
        parquet_path = self._parquet_path(name=name)
        code = f"{name}.to_parquet('{parquet_path}')"
        self.execute(code)
        return parquet_path

    # -------------------------
    # Internals
    # -------------------------
    def _execute_code_block(self, code_block: CodeBlock) -> JupyterCodeResult:
        """Execute a single cell, capture text + PNG/HTML/Plotly displays."""
        if not self._started or not self._client:
            raise RuntimeError("Executor not started. Call executor.start() first.")

        with self._exec_lock:
            # Build and append the cell
            cell = nbformat.new_code_cell(code_block.code)  # type: ignore
            self._client.nb.cells.append(cell)
            cell_index = len(self._client.nb.cells) - 1
            output_cell = self._client.execute_cell(cell, cell_index=cell_index)
            self._client.nb.cells.pop()

        # Parse outputs
        outputs: List[str] = []
        inferred_names = self._infer_output_names(code_block.code)
        name_index = 0
        exit_code = 0
        output_objects: List[str] = []

        for out in output_cell.get("outputs", []):
            ot = out.get("output_type")
            if ot == "stream":
                outputs.append(out.get("text", ""))
            elif ot == "error":
                tb = "\n".join(out.get("traceback", []))
                tb = re.sub(r"\x1b\[[0-9;]*[A-Za-z]", "", tb)  # strip ANSI
                outputs.append(tb)
                exit_code = 1
            elif ot in ("execute_result", "display_data"):
                data = out.get("data", {})
                for mime, payload in data.items():
                    if mime == "text/plain":
                        outputs.append(payload)
                    elif mime == "text/html" and "dataframe" in payload:
                        key = self._next_output_key(inferred_names, name_index)
                        if key is not None:
                            p = self.save_dataframe(key)
                            output_objects.append(key)
                            self.output_file_map[key] = p
                            name_index += 1
                    elif mime == "image/png":
                        p = self._save_image(payload)
                        key = self._next_output_key(inferred_names, name_index)
                        if key is not None:
                            output_objects.append(key)
                            self.output_file_map[key] = p
                            name_index += 1
                    elif mime == "application/vnd.plotly.v1+json":
                        p = self._save_plotly_json(payload)
                        key = self._next_output_key(inferred_names, name_index)
                        if key is not None:
                            output_objects.append(key)
                            self.output_file_map[key] = p
                            name_index += 1
                    else:
                        # Be conservative: emit JSON for other mimes
                        print(f"Unknown mime type: {mime}")

        return JupyterCodeResult(
            exit_code=exit_code,
            prints="\n".join(outputs),
            objects=output_objects,
        )

    def _save_image(self, b64: str) -> Path:
        raw = base64.b64decode(b64)
        path = self._work_dir / f"{uuid.uuid4().hex}.png"
        path.write_bytes(raw)
        return path.absolute()

    def _save_plotly_json(self, plotly_json: dict) -> Path:
        json_text = json.dumps(plotly_json)
        path = self._work_dir / f"{uuid.uuid4().hex}.plotly"
        path.write_text(json_text)
        return path.absolute()

    def _load_output(self, path: Path):
        file_type = path.suffix.replace(".", "")
        if file_type == "png":
            return path.read_bytes(), "matplotlib figure"
        elif file_type == "plotly":
            json_text = path.read_text()
            plotly_json = json.loads(json_text)
            return plotly_json, "plotly figure"
        elif file_type == "parquet":
            return pd.read_parquet(path), "pandas DataFrame"
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

    def _parquet_path(self, name: str) -> Path:
        return (self._work_dir / f"{name}.parquet").absolute()

    # -------------------------
    # Output name inference helpers
    # -------------------------

    def _infer_output_names(self, code: str) -> List[str]:
        """Infer output variable names in the order they likely display.

        Heuristics (simple and intentionally conservative):
        - `name.show()` -> captures `name` in encountered order
        - `display(name)` -> captures `name` in encountered order
        - Last bare expression that is a simple identifier -> captures that name
        """
        names: List[str] = []
        try:
            # .show() patterns (e.g., plotly or matplotlib figures)
            for m in re.finditer(
                r"(?m)\b([A-Za-z_][A-Za-z0-9_]*)\s*\.\s*show\s*\(\s*\)", code
            ):
                names.append(m.group(1))

            # display(var) patterns
            for m in re.finditer(
                r"(?m)\bdisplay\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)", code
            ):
                names.append(m.group(1))

            # Last bare name expression (if any)
            lines = [
                ln
                for ln in code.splitlines()
                if ln.strip() and not ln.strip().startswith("#")
            ]
            if lines:
                last = lines[-1].strip()
                m = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_]*)", last)
                if m:
                    names.append(m.group(1))
        except Exception:
            # Fallback: best-effort only
            pass

        return names

    def _next_output_key(self, inferred_names: List[str], idx: int) -> Optional[str]:
        """Return the next mapping key for an output file, ensuring uniqueness."""
        key: Optional[str] = inferred_names[idx] if idx < len(inferred_names) else None
        if key:
            if key in self.output_file_map:
                suffix = 2
                new_key = f"{key}_{suffix}"
                while new_key in self.output_file_map:
                    suffix += 1
                    new_key = f"{key}_{suffix}"
                key = new_key
            return key

        # print(f"############ No next output key found for {inferred_names} and {idx}")
        return None
