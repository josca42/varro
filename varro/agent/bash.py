from __future__ import annotations

from functools import lru_cache
import os
from pathlib import Path
import posixpath
import shlex
import subprocess
from typing import Literal
from uuid import uuid4

from safecmd.bashxtract import extract_commands

from varro.agent.workspace import ensure_user_workspace

BASH_TIMEOUT_SECONDS = 30
BashMode = Literal["DEV", "BWRAP"]
USE_BWRAP: BashMode = "DEV"
DEV_ROOT = Path("/Users/josca/dev/varro/mnt/user/1")
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
    # "rm",
    # "rmdir",
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
    "wc",
    "xargs",
]
BASH_DELETE_COMMANDS = {"rm", "rmdir", "unlink"}
DEV_ABS_PATH_COMMANDS = (
    "cat",
    "cd",
    "du",
    "fd",
    "find",
    "head",
    "less",
    "ls",
    "mkdir",
    "more",
    "mv",
    "readlink",
    "realpath",
    "stat",
    "tail",
    "touch",
    "tree",
)


def _use_bwrap() -> bool:
    return USE_BWRAP == "BWRAP"


def _use_dev_root() -> bool:
    return USE_BWRAP == "DEV"


def _user_workdir(user_id: int) -> Path:
    if _use_dev_root():
        DEV_ROOT.mkdir(parents=True, exist_ok=True)
        return DEV_ROOT.resolve()
    return ensure_user_workspace(user_id)


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


def _build_dev_shell_prelude(user_root: Path) -> str:
    root = shlex.quote(str(user_root))
    wrappers = "\n".join(
        f'{name}() {{ _varro_exec "{name}" "$@"; }}'
        for name in DEV_ABS_PATH_COMMANDS
        if name != "cd"
    )
    return (
        f"VARRO_ROOT={root}\n"
        "_varro_map_path() {\n"
        '  local arg="$1"\n'
        '  if [[ "$arg" == "/" ]]; then\n'
        "    printf '%s\\n' \"$VARRO_ROOT\"\n"
        "    return\n"
        "  fi\n"
        '  if [[ "$arg" == /* ]]; then\n'
        '    printf \'%s/%s\\n\' "$VARRO_ROOT" "${arg#/}"\n'
        "    return\n"
        "  fi\n"
        "  printf '%s\\n' \"$arg\"\n"
        "}\n"
        "_varro_exec() {\n"
        '  local cmd="$1"\n'
        "  shift\n"
        "  local mapped=()\n"
        "  local arg\n"
        '  for arg in "$@"; do\n'
        '    mapped+=("$(_varro_map_path "$arg")")\n'
        "  done\n"
        '  command "$cmd" "${mapped[@]}"\n'
        "}\n"
        "cd() {\n"
        "  local mapped=()\n"
        "  local arg\n"
        '  for arg in "$@"; do\n'
        '    mapped+=("$(_varro_map_path "$arg")")\n'
        "  done\n"
        '  builtin cd "${mapped[@]}"\n'
        "}\n"
        "pwd() {\n"
        '  if [[ "$#" -gt 0 ]]; then\n'
        '    command pwd "$@"\n'
        "    return\n"
        "  fi\n"
        '  if [[ "$PWD" == "$VARRO_ROOT" ]]; then\n'
        "    printf '/\\n'\n"
        "    return\n"
        "  fi\n"
        '  if [[ "$PWD" == "$VARRO_ROOT/"* ]]; then\n'
        '    printf \'/%s\\n\' "${PWD#"$VARRO_ROOT/"}"\n'
        "    return\n"
        "  fi\n"
        "  command pwd\n"
        "}\n"
        f"{wrappers}\n"
    )


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


def _build_bwrap_args(user_root: Path, cwd_rel: str) -> list[str]:
    args = [
        "bwrap",
        "--bind",
        str(user_root),
        "/",
        "--proc",
        "/proc",
        "--dev",
        "/dev",
        "--unshare-all",
        "--die-with-parent",
        "--new-session",
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
        "--chdir",
        cwd_rel,
    ]
    for bin_path in _resolve_allowed_bins():
        args += ["--ro-bind", bin_path, bin_path]
    for lib_dir in (Path("/lib"), Path("/lib64"), Path("/usr/lib"), Path("/usr/lib64")):
        if lib_dir.exists():
            lib_dir_str = str(lib_dir)
            args += ["--ro-bind", lib_dir_str, lib_dir_str]
    return args


def _is_delete_command(tokens: list[str]) -> bool:
    if not tokens:
        return False
    name = Path(tokens[0]).name
    if name in BASH_DELETE_COMMANDS:
        return True
    if name == "find" and "-delete" in tokens:
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


def run_bash_command(user_id: int, cwd_rel: str, command: str) -> tuple[str, str]:
    if not command or not command.strip():
        return "Error: command is empty", cwd_rel

    user_root = _user_workdir(user_id)
    cwd_rel = _sanitize_cwd_rel(cwd_rel)
    host_cwd, cwd_rel = _host_cwd(user_root, cwd_rel)
    commands, _, _ = extract_commands(command)

    if any(_is_delete_command(tokens) for tokens in commands):
        return "warning: delete", cwd_rel
    if not _use_bwrap():
        ok, bad = _commands_allowed(commands)
        if not ok:
            return f"Error: command not allowed: {bad}", cwd_rel

    sentinel = f"__VARRO_PWD_{uuid4().hex}__"
    wrapped = (
        f"{command}; varro_rc=$?; printf '\\n{sentinel}%s\\n' \"$PWD\"; exit $varro_rc"
    )
    try:
        if _use_bwrap():
            env = {
                "PATH": "/bin:/usr/bin:/usr/local/bin",
                "HOME": "/",
                "LANG": "C.UTF-8",
                "PWD": cwd_rel,
            }
            args = _build_bwrap_args(user_root, cwd_rel)
            res = subprocess.run(
                args + ["sh", "-c", wrapped],
                text=True,
                capture_output=True,
                env=env,
                timeout=BASH_TIMEOUT_SECONDS,
            )
        else:
            env = os.environ.copy()
            env["HOME"] = str(user_root)
            script = f"{_build_dev_shell_prelude(user_root)}\n{wrapped}"
            res = subprocess.run(
                ["bash", "-lc", script],
                text=True,
                capture_output=True,
                cwd=host_cwd,
                env=env,
                timeout=BASH_TIMEOUT_SECONDS,
            )
    except subprocess.TimeoutExpired:
        return f"Error: command timed out after {BASH_TIMEOUT_SECONDS}s", cwd_rel

    stdout, reported_pwd = _split_output_pwd(res.stdout or "", sentinel)
    output = _combine_output(stdout, res.stderr)

    if reported_pwd:
        if _use_bwrap():
            cwd_rel = _sanitize_cwd_rel(reported_pwd)
        else:
            cwd_rel = _to_cwd_rel(user_root, reported_pwd)

    if res.returncode != 0:
        return (
            f"Error: command failed with exit code {res.returncode}\n{output}".rstrip(),
            cwd_rel,
        )
    return output, cwd_rel
