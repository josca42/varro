from __future__ import annotations

import json
from pathlib import Path

from varro.config import DATA_DIR


def runtime_state_fp(user_id: int, chat_id: int) -> Path:
    return DATA_DIR / "chat" / str(user_id) / str(chat_id) / "runtime.json"


def load_bash_cwd(user_id: int, chat_id: int) -> str:
    fp = runtime_state_fp(user_id, chat_id)
    if not fp.exists():
        return "/"
    try:
        raw = json.loads(fp.read_text())
    except Exception:
        return "/"
    cwd = raw.get("bash_cwd")
    if isinstance(cwd, str) and cwd.startswith("/"):
        return cwd
    return "/"


def save_bash_cwd(user_id: int, chat_id: int, cwd: str) -> None:
    fp = runtime_state_fp(user_id, chat_id)
    fp.parent.mkdir(parents=True, exist_ok=True)
    data = {"bash_cwd": cwd if cwd.startswith("/") else "/"}
    fp.write_text(json.dumps(data, ensure_ascii=False))
