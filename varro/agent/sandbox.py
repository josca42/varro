from __future__ import annotations

import json
from collections import deque
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path, PurePosixPath
import posixpath
import resource
import shutil
import subprocess
import sys
import threading
from types import SimpleNamespace
from uuid import uuid4

import dill
import pandas as pd
import plotly.graph_objects as go
from pydantic_ai import BinaryContent
from safecmd.bashxtract import extract_commands
from varro.agent.shell import (
    BASH_TIMEOUT,
    JUPYTER_INITIAL_IMPORTS,
    _combine_output,
    _split_output_pwd,
    get_shell,
    run_bash_command as run_bash_command_vanilla,
)
from varro.agent.utils import show_element
from varro.agent.workspace import user_workspace_root
from varro.config import AGENT_DATA_DIR, PROJECT_ROOT, settings

SHELL_MODE = (settings.get("BASH_MODE") or "BWRAP").upper()
READONLY_DOCS_ROOTS = ("/subjects", "/fact", "/dim", "/geo")
BASH_ALLOWED_COMMANDS = {
    "awk",
    "basename",
    "cat",
    "cd",
    "cut",
    "diff",
    "dirname",
    "du",
    "echo",
    "egrep",
    "export",
    "false",
    "fd",
    "fgrep",
    "find",
    "grep",
    "head",
    "less",
    "ls",
    "mkdir",
    "more",
    "mv",
    "pwd",
    "printf",
    "readlink",
    "realpath",
    "rg",
    "rm",
    "rmdir",
    "sed",
    "sort",
    "stat",
    "tail",
    "tee",
    "test",
    "touch",
    "tr",
    "tree",
    "true",
    "unlink",
    "uniq",
    "wc",
    "xargs",
    "[",
}
BASH_ALLOWED_BINARIES = [
    "sh",
    "awk",
    "basename",
    "cat",
    "cut",
    "diff",
    "dirname",
    "du",
    "egrep",
    "fd",
    "fgrep",
    "find",
    "grep",
    "head",
    "less",
    "ls",
    "mkdir",
    "more",
    "mv",
    "printf",
    "readlink",
    "realpath",
    "rg",
    "rm",
    "rmdir",
    "sed",
    "sort",
    "stat",
    "tail",
    "tee",
    "touch",
    "tr",
    "tree",
    "uniq",
    "unlink",
    "wc",
    "xargs",
]
BASH_DELETE_COMMANDS = {"rm", "rmdir", "unlink"}
LIB_DIRS = (Path("/lib"), Path("/lib64"), Path("/usr/lib"), Path("/usr/lib64"))
EXCHANGE_ROOT_NAME = ".varro_exchange"
_MISSING = object()


def _int_setting(name: str, default: int) -> int:
    raw = settings.get(name)
    if raw is None or raw == "":
        return default
    return int(raw)


def _int_setting_with_fallback(name: str, fallback_name: str, default: int) -> int:
    raw = settings.get(name)
    if raw is not None and raw != "":
        return int(raw)
    fallback = settings.get(fallback_name)
    if fallback is not None and fallback != "":
        return int(fallback)
    return default


@dataclass(frozen=True)
class ResourceLimits:
    cpu_seconds: int | None = None
    memory_bytes: int | None = None
    nproc: int | None = None
    nofile: int | None = None
    fsize: int | None = None


BASH_LIMITS = ResourceLimits(
    cpu_seconds=_int_setting("SANDBOX_BASH_CPU_SECONDS", 30),
    memory_bytes=_int_setting("SANDBOX_MEMORY_MB", 2048) * 1024 * 1024,
    nproc=_int_setting("SANDBOX_NPROC", 256),
    nofile=_int_setting("SANDBOX_NOFILE", 1024),
    fsize=_int_setting("SANDBOX_FSIZE_MB", 256) * 1024 * 1024,
)
WORKER_LIMITS = ResourceLimits(
    memory_bytes=_int_setting("SANDBOX_MEMORY_MB", 2048) * 1024 * 1024,
    nproc=_int_setting_with_fallback("SANDBOX_WORKER_NPROC", "SANDBOX_NPROC", 1024),
    nofile=_int_setting_with_fallback("SANDBOX_WORKER_NOFILE", "SANDBOX_NOFILE", 4096),
    fsize=_int_setting("SANDBOX_FSIZE_MB", 256) * 1024 * 1024,
)


def _use_bwrap() -> bool:
    return SHELL_MODE == "BWRAP"


def _sanitize_cwd_rel(cwd_rel: str) -> str:
    if not cwd_rel or not cwd_rel.startswith("/"):
        return "/"
    norm = posixpath.normpath(cwd_rel)
    if not norm.startswith("/"):
        return "/"
    return norm


def _normalize_existing_cwd(user_root: Path, cwd_rel: str) -> str:
    safe_rel = _sanitize_cwd_rel(cwd_rel)
    rel = safe_rel.lstrip("/")
    host = (user_root / rel).resolve()
    try:
        host.relative_to(user_root.resolve())
    except ValueError:
        return "/"
    if not host.exists() or not host.is_dir():
        return "/"
    return safe_rel


def _is_readonly_root(path: str) -> bool:
    return any(path == root or path.startswith(f"{root}/") for root in READONLY_DOCS_ROOTS)


def _resolve_command_path(cwd_rel: str, arg: str) -> str | None:
    if not arg:
        return None
    if arg in {"-", "&1", "&2"}:
        return None
    if arg.startswith("$") or arg.startswith("~") or arg.startswith("&"):
        return None
    if arg.startswith("-"):
        return None
    if arg.startswith("/"):
        return _sanitize_cwd_rel(arg)
    return _sanitize_cwd_rel(posixpath.join(cwd_rel, arg))


def _arg_targets_readonly(cwd_rel: str, arg: str) -> bool:
    resolved = _resolve_command_path(cwd_rel, arg)
    if resolved is None:
        return False
    return _is_readonly_root(resolved)


def _next_cwd_from_cd(cwd_rel: str, tokens: list[str]) -> str:
    if len(tokens) < 2:
        return "/"
    target = _resolve_command_path(cwd_rel, tokens[1])
    if target is None:
        return cwd_rel
    return target


def _delete_targets_readonly(commands: list[list[str]], cwd_rel: str) -> bool:
    current_cwd = _sanitize_cwd_rel(cwd_rel)
    for tokens in commands:
        if not tokens:
            continue
        name = Path(tokens[0]).name
        if name == "cd":
            current_cwd = _next_cwd_from_cd(current_cwd, tokens)
            continue
        if name in BASH_DELETE_COMMANDS:
            args = [arg for arg in tokens[1:] if not arg.startswith("-")]
            if any(_arg_targets_readonly(current_cwd, arg) for arg in args):
                return True
            continue
        if name == "find" and "-delete" in tokens:
            paths = [arg for arg in tokens[1:] if not arg.startswith("-")]
            if not paths and _is_readonly_root(current_cwd):
                return True
            if any(_arg_targets_readonly(current_cwd, arg) for arg in paths):
                return True
    return False


def _commands_allowed(commands: list[list[str]]) -> tuple[bool, str | None]:
    for tokens in commands:
        if not tokens:
            continue
        name = Path(tokens[0]).name
        if name not in BASH_ALLOWED_COMMANDS:
            return False, tokens[0]
    return True, None


@lru_cache(maxsize=1)
def _resolve_allowed_bins() -> list[str]:
    bins = []
    prefixes = [Path("/usr/bin"), Path("/bin"), Path("/usr/local/bin")]
    for cmd in BASH_ALLOWED_BINARIES:
        for prefix in prefixes:
            full = prefix / cmd
            if full.exists():
                bins.append(str(full))
                break
    return bins


def _apply_limits(limits: ResourceLimits):
    def _preexec() -> None:
        if limits.cpu_seconds is not None:
            resource.setrlimit(resource.RLIMIT_CPU, (limits.cpu_seconds, limits.cpu_seconds))
        if limits.memory_bytes is not None:
            resource.setrlimit(
                resource.RLIMIT_AS,
                (limits.memory_bytes, limits.memory_bytes),
            )
        if limits.nproc is not None:
            resource.setrlimit(resource.RLIMIT_NPROC, (limits.nproc, limits.nproc))
        if limits.nofile is not None:
            resource.setrlimit(resource.RLIMIT_NOFILE, (limits.nofile, limits.nofile))
        if limits.fsize is not None:
            resource.setrlimit(resource.RLIMIT_FSIZE, (limits.fsize, limits.fsize))

    return _preexec


def _bwrap_base_args(user_root: Path, cwd_rel: str) -> list[str]:
    return [
        "bwrap",
        "--bind",
        str(user_root),
        "/",
        "--proc",
        "/proc",
        "--dev",
        "/dev",
        "--unshare-user",
        "--unshare-pid",
        "--unshare-ipc",
        "--unshare-uts",
        "--unshare-net",
        "--unshare-cgroup",
        "--die-with-parent",
        "--new-session",
        "--disable-userns",
        "--assert-userns-disabled",
        "--tmpfs",
        "/tmp",
        "--dir",
        "/bin",
        "--dir",
        "/usr",
        "--dir",
        "/usr/bin",
        "--dir",
        "/usr/local",
        "--dir",
        "/usr/local/bin",
        "--dir",
        "/agent_data",
        "--ro-bind",
        str(AGENT_DATA_DIR),
        "/agent_data",
        "--chdir",
        cwd_rel,
    ]


def _build_bwrap_bash_args(user_root: Path, cwd_rel: str) -> list[str]:
    args = _bwrap_base_args(user_root, cwd_rel)
    for bin_path in _resolve_allowed_bins():
        args += ["--ro-bind", bin_path, bin_path]
    for lib_dir in LIB_DIRS:
        if lib_dir.exists():
            lib_dir_str = str(lib_dir)
            args += ["--ro-bind", lib_dir_str, lib_dir_str]
    return args


def _build_bwrap_worker_args(
    user_root: Path,
    snapshot_dir: Path,
    exchange_dir_guest: str,
) -> list[str]:
    args = _bwrap_base_args(user_root, "/")
    args += [
        "--dir",
        "/etc",
        "--dir",
        "/home",
        "--dir",
        "/home/dev",
        "--dir",
        str(PROJECT_ROOT),
        "--dir",
        "/varro_state",
        "--bind",
        str(snapshot_dir),
        "/varro_state",
    ]
    for bind_path in (
        Path("/bin"),
        Path("/usr"),
        Path("/lib"),
        Path("/lib64"),
        Path("/etc"),
        PROJECT_ROOT,
    ):
        if bind_path.exists():
            path_str = str(bind_path)
            args += ["--ro-bind", path_str, path_str]
    args += [
        sys.executable,
        "-m",
        "varro.agent.ipython_worker",
        "--snapshot-path",
        "/varro_state/shell.pkl",
        "--exchange-dir",
        exchange_dir_guest,
    ]
    return args


def _minimal_env(*, cwd_rel: str = "/") -> dict[str, str]:
    python_bin = str(Path(sys.executable).resolve().parent)
    return {
        "PATH": f"/bin:/usr/bin:/usr/local/bin:{python_bin}",
        "HOME": "/",
        "LANG": "C.UTF-8",
        "PWD": cwd_rel,
        "PYTHONUNBUFFERED": "1",
        "MPLCONFIGDIR": "/tmp/matplotlib",
    }


def _worker_env() -> dict[str, str]:
    env = _minimal_env()
    env["HOME"] = "/home/dev"
    env["XDG_CACHE_HOME"] = "/home/dev/.cache"
    env["XDG_CONFIG_HOME"] = "/home/dev/.config"
    env["MPLCONFIGDIR"] = "/home/dev/.cache/matplotlib"
    env["ARROW_NUM_THREADS"] = "1"
    env["OMP_NUM_THREADS"] = "1"
    env["OPENBLAS_NUM_THREADS"] = "1"
    env["MKL_NUM_THREADS"] = "1"
    env["NUMEXPR_NUM_THREADS"] = "1"
    return env


def run_bash_command(user_id: int, cwd_rel: str, command: str) -> tuple[str, str]:
    if not _use_bwrap():
        return run_bash_command_vanilla(user_id, cwd_rel, command)
    if not command or not command.strip():
        return "Error: command is empty", _sanitize_cwd_rel(cwd_rel)

    user_root = user_workspace_root(user_id)
    cwd_rel = _normalize_existing_cwd(user_root, cwd_rel)
    commands, _, _ = extract_commands(command)

    ok, bad = _commands_allowed(commands)
    if not ok:
        return f"Error: command not allowed: {bad}", cwd_rel
    if _delete_targets_readonly(commands, cwd_rel):
        return "Error: path is read-only", cwd_rel

    sentinel = f"__VARRO_PWD_{uuid4().hex}__"
    wrapped = (
        f"{command}; varro_rc=$?; printf '\\n{sentinel}%s\\n' \"$PWD\"; exit $varro_rc"
    )
    env = _minimal_env(cwd_rel=cwd_rel)
    args = _build_bwrap_bash_args(user_root, cwd_rel)
    try:
        res = subprocess.run(
            args + ["sh", "-c", wrapped],
            text=True,
            capture_output=True,
            env=env,
            timeout=BASH_TIMEOUT,
            preexec_fn=_apply_limits(BASH_LIMITS),
        )
    except subprocess.TimeoutExpired:
        return f"Error: command timed out after {BASH_TIMEOUT}s", cwd_rel

    stdout, reported_pwd = _split_output_pwd(res.stdout or "", sentinel)
    output = _combine_output(stdout, res.stderr)
    if reported_pwd:
        cwd_rel = _sanitize_cwd_rel(reported_pwd)

    if res.returncode != 0:
        return (
            f"Error: command failed with exit code {res.returncode}\n{output}".rstrip(),
            cwd_rel,
        )
    return output, cwd_rel


class _SandboxNamespace:
    def __init__(self, shell: "SandboxShellProxy"):
        self._shell = shell

    def __setitem__(self, name: str, value) -> None:
        self._shell.set_user_ns_item(name, value)

    def get(self, name: str, default=None):
        value = self._shell.get_user_ns_item(name)
        if value is _MISSING:
            return default
        return value

    def update(self, values: dict) -> None:
        for key, value in values.items():
            self[key] = value


class SandboxShellProxy:
    is_sandbox_proxy = True

    def __init__(self, *, user_id: int, chat_id: int, snapshot_fp: Path):
        self.user_id = user_id
        self.chat_id = chat_id
        self.user_root = user_workspace_root(user_id).resolve()
        self.snapshot_fp = snapshot_fp
        self._exchange_root = self.user_root / EXCHANGE_ROOT_NAME
        self._exchange_root.mkdir(parents=True, exist_ok=True)
        self._exchange_dir = self._exchange_root / str(chat_id)
        if self._exchange_dir.exists():
            if self._exchange_dir.is_dir():
                shutil.rmtree(self._exchange_dir, ignore_errors=True)
            else:
                self._exchange_dir.unlink(missing_ok=True)
        self._exchange_dir.mkdir(parents=True, exist_ok=True)
        self._exchange_dir_guest = self._host_path_to_worker(self._exchange_dir)
        self._cache: dict[str, object] = {}
        self._io_lock = threading.Lock()
        self._stderr_lines: deque[str] = deque(maxlen=40)
        self.user_ns = _SandboxNamespace(self)
        self._proc = self._spawn_worker()
        self._stderr_thread = threading.Thread(target=self._drain_stderr, daemon=True)
        self._stderr_thread.start()
        self._request({"op": "ping"})

    def _spawn_worker(self) -> subprocess.Popen:
        snapshot_dir = self.snapshot_fp.parent
        snapshot_dir.mkdir(parents=True, exist_ok=True)
        args = _build_bwrap_worker_args(
            self.user_root,
            snapshot_dir,
            self._exchange_dir_guest,
        )
        return subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=_worker_env(),
            preexec_fn=_apply_limits(WORKER_LIMITS),
        )

    def _drain_stderr(self) -> None:
        if self._proc.stderr is None:
            return
        for line in self._proc.stderr:
            self._stderr_lines.append(line.rstrip("\n"))

    def _stderr_tail(self) -> str:
        if not self._stderr_lines:
            return ""
        return "\n".join(self._stderr_lines)

    def _request(self, payload: dict) -> dict:
        with self._io_lock:
            if self._proc.poll() is not None:
                detail = self._stderr_tail()
                suffix = f"\n{detail}" if detail else ""
                raise RuntimeError(f"sandbox worker exited before request{suffix}")
            if self._proc.stdin is None or self._proc.stdout is None:
                raise RuntimeError("sandbox worker I/O is unavailable")
            self._proc.stdin.write(json.dumps(payload, ensure_ascii=False) + "\n")
            self._proc.stdin.flush()
            line = self._proc.stdout.readline()
            if not line:
                detail = self._stderr_tail()
                suffix = f"\n{detail}" if detail else ""
                raise RuntimeError(f"sandbox worker closed response stream{suffix}")
        response = json.loads(line)
        if not response.get("ok", False):
            raise RuntimeError(response.get("error", "sandbox worker error"))
        return response

    def _host_path_to_worker(self, host_path: Path) -> str:
        host_resolved = host_path.resolve()
        rel = host_resolved.relative_to(self.user_root)
        return "/" if rel.as_posix() == "." else f"/{rel.as_posix()}"

    def _worker_path_to_host(self, worker_path: str) -> Path:
        path = PurePosixPath(worker_path)
        if not path.is_absolute():
            raise RuntimeError("worker returned non-absolute path")
        host = (self.user_root / str(path).lstrip("/")).resolve()
        host.relative_to(self.user_root)
        return host

    def run_cell(self, cell: str, timeout: int | None = None):
        self._cache.clear()
        response = self._request({"op": "run_cell", "code": cell, "timeout": timeout})
        error_before_exec = (
            RuntimeError(response["error_before_exec"])
            if response.get("error_before_exec")
            else None
        )
        error_in_exec = (
            RuntimeError(response["error_in_exec"]) if response.get("error_in_exec") else None
        )
        return SimpleNamespace(
            error_before_exec=error_before_exec,
            error_in_exec=error_in_exec,
            stdout=response.get("stdout", ""),
            outputs=[],
        )

    def reset(self, new_session: bool = False) -> None:
        self._cache.clear()
        self._request({"op": "reset", "new_session": bool(new_session)})

    def set_user_ns_item(self, name: str, value) -> None:
        self._cache.pop(name, None)
        if isinstance(value, pd.DataFrame):
            fp = self._exchange_dir / f"df_{name}_{uuid4().hex}.parquet"
            value.to_parquet(fp, index=True)
            self._request(
                {
                    "op": "set_dataframe",
                    "name": name,
                    "path": self._host_path_to_worker(fp),
                }
            )
            self._cache[name] = value
            return
        if isinstance(value, (str, int, float, bool)) or value is None:
            self._request({"op": "set_literal", "name": name, "value": value})
            self._cache[name] = value
            return
        raise TypeError(f"Unsupported namespace value type: {type(value)}")

    def get_user_ns_item(self, name: str):
        if name in self._cache:
            return self._cache[name]
        response = self._request({"op": "get_object", "name": name})
        kind = response.get("kind")
        if kind == "missing":
            return _MISSING
        if kind == "dataframe":
            obj = pd.read_parquet(self._worker_path_to_host(response["path"]))
        elif kind == "styler_df":
            df = pd.read_parquet(self._worker_path_to_host(response["path"]))
            obj = df.style
        elif kind == "plotly":
            obj = go.Figure(json.loads(response["json"]))
        else:
            return _MISSING
        self._cache[name] = obj
        return obj

    async def render_show(self, name: str):
        response = self._request({"op": "render_show", "name": name})
        kind = response.get("kind")
        if kind == "text":
            return response.get("text", "")
        if kind == "plotly":
            fig = go.Figure(json.loads(response["json"]))
            return await show_element(fig)
        if kind == "png":
            fp = self._worker_path_to_host(response["path"])
            return BinaryContent(data=fp.read_bytes(), media_type="image/png")
        raise ValueError(response.get("error", "Invalid output type"))

    def close(self, *, save_snapshot: bool) -> None:
        try:
            self._request({"op": "shutdown", "save_snapshot": bool(save_snapshot)})
        except Exception:
            pass
        finally:
            self._cache.clear()
            if self._proc.poll() is None:
                self._proc.terminate()
                try:
                    self._proc.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    self._proc.kill()
                    self._proc.wait(timeout=2)
            shutil.rmtree(self._exchange_dir, ignore_errors=True)
            try:
                self._exchange_root.rmdir()
            except OSError:
                pass


def _save_snapshot(shell, snapshot_fp: Path) -> None:
    snapshot_fp.parent.mkdir(parents=True, exist_ok=True)
    try:
        with snapshot_fp.open("wb") as f:
            dill.dump(getattr(shell, "user_ns", {}), f)
    except Exception:
        snapshot_fp.unlink(missing_ok=True)


def _load_snapshot(shell, snapshot_fp: Path) -> None:
    if not snapshot_fp.exists():
        return
    with snapshot_fp.open("rb") as f:
        value = dill.load(f)
    if isinstance(value, dict):
        shell.user_ns.update(value)


def create_shell(*, user_id: int, chat_id: int, snapshot_fp: Path):
    if _use_bwrap():
        return SandboxShellProxy(user_id=user_id, chat_id=chat_id, snapshot_fp=snapshot_fp)
    shell = get_shell()
    shell.run_cell(JUPYTER_INITIAL_IMPORTS)
    _load_snapshot(shell, snapshot_fp)
    return shell


def close_shell(shell, *, save_snapshot: bool, snapshot_fp: Path) -> None:
    if isinstance(shell, SandboxShellProxy):
        shell.close(save_snapshot=save_snapshot)
        return
    if save_snapshot:
        _save_snapshot(shell, snapshot_fp)
    try:
        shell.reset(new_session=False)
        if shell.history_manager:
            shell.history_manager.end_session()
    except Exception:
        return
