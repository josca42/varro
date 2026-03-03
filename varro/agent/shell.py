import os
import posixpath
import signal
import subprocess
from pathlib import Path
from uuid import uuid4

from IPython.terminal.interactiveshell import TerminalInteractiveShell
from IPython.utils.capture import capture_output
from varro.agent.workspace import user_workspace_root

TerminalInteractiveShell.orig_run = TerminalInteractiveShell.run_cell

JUPYTER_INITIAL_IMPORTS = """
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import geopandas as gpd
from varro.agent.utils import get_geo

import plotly.io as pio
pio.renderers.default = None
pio.templates.default = "plotly_white"
pio.templates["plotly_white"].layout.legend = dict(
    orientation="h",
    yanchor="top",
    y=-0.15,
    xanchor="center",
    x=0.5,
)
"""


def run_cell(self, cell, timeout=None):
    "Wrapper for original `run_cell` which adds timeout"
    if timeout:

        def handler(*args):
            raise TimeoutError()

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(timeout)
    try:
        with capture_output() as io:
            result = self.orig_run(cell, silent=True)
        result.stdout = io.stdout
        result.outputs = io.outputs
        return result
    except TimeoutError as e:
        result = self.ExecutionResult(error_before_exec=None, error_in_exec=e)
    finally:
        if timeout:
            signal.alarm(0)


TerminalInteractiveShell.run_cell = run_cell


def get_shell() -> TerminalInteractiveShell:
    "Get a `TerminalInteractiveShell` with minimal functionality"
    sh = TerminalInteractiveShell()
    sh.logger.log_output = sh.history_manager.enabled = False
    dh = sh.displayhook
    dh.finish_displayhook = dh.write_output_prompt = dh.start_displayhook = lambda: None
    dh.write_format_data = lambda format_dict, md_dict=None: None
    sh.logstart = sh.automagic = sh.autoindent = False
    sh.autocall = 0
    sh.system = lambda cmd: None
    return sh


# ── Basic bash execution ──────────────────────────────────────────────

BASH_TIMEOUT = 30


def _combine_output(stdout: str | None, stderr: str | None) -> str:
    out = (stdout or "").rstrip("\n")
    err = (stderr or "").rstrip("\n")
    if out and err:
        return f"{out}\n{err}"
    return out or err


def _split_output_pwd(output: str, sentinel: str) -> tuple[str, str | None]:
    if sentinel not in output:
        return output.rstrip("\n"), None
    before, _, after = output.rpartition(sentinel)
    after_lines = after.splitlines()
    new_pwd = after_lines[0].strip() if after_lines else None
    return before.rstrip("\n"), new_pwd


def run_bash(
    command: str,
    *,
    cwd: Path | str | None = None,
    env: dict[str, str] | None = None,
    timeout: int = BASH_TIMEOUT,
) -> tuple[str, str | None, int]:
    sentinel = f"__VARRO_PWD_{uuid4().hex}__"
    wrapped = (
        f"{command}; varro_rc=$?; printf '\\n{sentinel}%s\\n' \"$PWD\"; exit $varro_rc"
    )
    try:
        res = subprocess.run(
            ["bash", "-c", wrapped],
            text=True,
            capture_output=True,
            cwd=cwd,
            env=env,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return f"Error: command timed out after {timeout}s", None, 1

    stdout, reported_pwd = _split_output_pwd(res.stdout or "", sentinel)
    output = _combine_output(stdout, res.stderr)
    return output, reported_pwd, res.returncode


def _sanitize_cwd_rel(cwd_rel: str) -> str:
    if not cwd_rel or not cwd_rel.startswith("/"):
        return "/"
    norm = posixpath.normpath(cwd_rel)
    if not norm.startswith("/"):
        return "/"
    return norm


def _host_cwd(user_root: Path, cwd_rel: str) -> tuple[Path, str]:
    safe_rel = _sanitize_cwd_rel(cwd_rel)
    rel = safe_rel.lstrip("/")
    host = (user_root / rel).resolve()
    try:
        host.relative_to(user_root.resolve())
    except ValueError:
        return user_root, "/"
    if not host.exists():
        return user_root, "/"
    return host, safe_rel


def _to_cwd_rel(user_root: Path, reported_pwd: str) -> str:
    reported = Path(reported_pwd).resolve()
    try:
        rel = reported.relative_to(user_root.resolve())
    except ValueError:
        return "/"
    rel_posix = rel.as_posix()
    return "/" if rel_posix == "." else f"/{rel_posix}"


def run_bash_command(user_id: int, cwd_rel: str, command: str) -> tuple[str, str]:
    if not command or not command.strip():
        return "Error: command is empty", _sanitize_cwd_rel(cwd_rel)

    user_root = user_workspace_root(user_id)
    cwd_rel = _sanitize_cwd_rel(cwd_rel)
    host_cwd, cwd_rel = _host_cwd(user_root, cwd_rel)

    sentinel = f"__VARRO_PWD_{uuid4().hex}__"
    wrapped = (
        f"{command}; varro_rc=$?; printf '\\n{sentinel}%s\\n' \"$PWD\"; exit $varro_rc"
    )
    env = os.environ.copy()
    env["HOME"] = str(user_root)

    try:
        res = subprocess.run(
            ["bash", "-lc", wrapped],
            text=True,
            capture_output=True,
            cwd=host_cwd,
            env=env,
            timeout=BASH_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return f"Error: command timed out after {BASH_TIMEOUT}s", cwd_rel

    stdout, reported_pwd = _split_output_pwd(res.stdout or "", sentinel)
    output = _combine_output(stdout, res.stderr)

    if reported_pwd:
        cwd_rel = _to_cwd_rel(user_root, reported_pwd)

    if res.returncode != 0:
        return (
            f"Error: command failed with exit code {res.returncode}\n{output}".rstrip(),
            cwd_rel,
        )
    return output, cwd_rel
