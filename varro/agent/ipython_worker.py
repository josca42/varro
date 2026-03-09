from __future__ import annotations

import argparse
import json
from pathlib import Path
from uuid import uuid4

import dill
import pandas as pd
import plotly.graph_objects as go
from pandas.io.formats.style import Styler
import matplotlib.pyplot as plt
from varro.agent.shell import JUPYTER_INITIAL_IMPORTS, get_shell
from varro.data.utils import df_preview

EXCHANGE_DIR = Path("/.varro_exchange")


def _send_response(payload: dict) -> None:
    print(json.dumps(payload, ensure_ascii=False), flush=True)


def _read_request() -> dict | None:
    line = input()
    if not line:
        return None
    return json.loads(line)


def _save_snapshot(shell, snapshot_path: Path) -> None:
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    user_ns = getattr(shell, "user_ns", {})
    serializable = {}
    for key, value in user_ns.items():
        if key.startswith("__"):
            continue
        try:
            dill.dumps(value)
        except Exception:
            continue
        serializable[key] = value
    tmp_path = snapshot_path.with_suffix(".tmp")
    with tmp_path.open("wb") as f:
        dill.dump(serializable, f)
    tmp_path.replace(snapshot_path)


def _load_snapshot(shell, snapshot_path: Path) -> None:
    if not snapshot_path.exists():
        return
    with snapshot_path.open("rb") as f:
        value = dill.load(f)
    if isinstance(value, dict):
        shell.user_ns.update(value)


def _export_dataframe(df: pd.DataFrame) -> str:
    EXCHANGE_DIR.mkdir(parents=True, exist_ok=True)
    fp = EXCHANGE_DIR / f"df_{uuid4().hex}.parquet"
    df.to_parquet(fp, index=True)
    return fp.as_posix()


def _export_png(fig: plt.Figure) -> str:
    EXCHANGE_DIR.mkdir(parents=True, exist_ok=True)
    fp = EXCHANGE_DIR / f"fig_{uuid4().hex}.png"
    fig.savefig(fp, format="png")
    return fp.as_posix()


def _handle_get_object(shell, name: str) -> dict:
    value = shell.user_ns.get(name)
    if value is None:
        return {"ok": True, "kind": "missing"}
    if isinstance(value, pd.DataFrame):
        return {"ok": True, "kind": "dataframe", "path": _export_dataframe(value)}
    if isinstance(value, Styler):
        return {"ok": True, "kind": "styler_df", "path": _export_dataframe(value.data)}
    if isinstance(value, go.Figure):
        return {"ok": True, "kind": "plotly", "json": value.to_json()}
    return {"ok": True, "kind": "unsupported"}


def _handle_render_show(shell, name: str) -> dict:
    value = shell.user_ns.get(name)
    if value is None:
        return {"ok": False, "error": f"Invalid output type: {type(value)}"}
    if isinstance(value, pd.DataFrame):
        return {"ok": True, "kind": "text", "text": df_preview(value, max_rows=30)}
    if isinstance(value, Styler):
        return {"ok": True, "kind": "text", "text": df_preview(value.data, max_rows=30)}
    if isinstance(value, go.Figure):
        return {"ok": True, "kind": "plotly", "json": value.to_json()}
    if isinstance(value, plt.Figure):
        return {"ok": True, "kind": "png", "path": _export_png(value)}
    return {"ok": False, "error": f"Invalid output type: {type(value)}"}


def serve(snapshot_path: Path, exchange_dir: Path) -> int:
    global EXCHANGE_DIR
    EXCHANGE_DIR = exchange_dir
    shell = get_shell()
    shell.run_cell(JUPYTER_INITIAL_IMPORTS)
    _load_snapshot(shell, snapshot_path)
    while True:
        try:
            request = _read_request()
        except EOFError:
            break
        if request is None:
            break
        op = request.get("op")
        try:
            if op == "ping":
                _send_response({"ok": True})
                continue
            if op == "run_cell":
                result = shell.run_cell(
                    request.get("code", ""),
                    timeout=request.get("timeout"),
                )
                _send_response(
                    {
                        "ok": True,
                        "stdout": getattr(result, "stdout", ""),
                        "error_before_exec": repr(result.error_before_exec)
                        if result.error_before_exec
                        else None,
                        "error_in_exec": repr(result.error_in_exec)
                        if result.error_in_exec
                        else None,
                    }
                )
                continue
            if op == "set_dataframe":
                shell.user_ns[request["name"]] = pd.read_parquet(request["path"])
                _send_response({"ok": True})
                continue
            if op == "set_literal":
                shell.user_ns[request["name"]] = request.get("value")
                _send_response({"ok": True})
                continue
            if op == "get_object":
                _send_response(_handle_get_object(shell, request["name"]))
                continue
            if op == "render_show":
                _send_response(_handle_render_show(shell, request["name"]))
                continue
            if op == "reset":
                shell.reset(new_session=bool(request.get("new_session", False)))
                _send_response({"ok": True})
                continue
            if op == "shutdown":
                if request.get("save_snapshot"):
                    _save_snapshot(shell, snapshot_path)
                _send_response({"ok": True})
                break
            _send_response({"ok": False, "error": f"unknown op: {op}"})
        except Exception as exc:
            _send_response({"ok": False, "error": str(exc)})
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot-path", required=True)
    parser.add_argument("--exchange-dir", required=True)
    args = parser.parse_args()
    return serve(Path(args.snapshot_path), Path(args.exchange_dir))


if __name__ == "__main__":
    raise SystemExit(main())
