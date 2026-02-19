from __future__ import annotations

from pathlib import Path

import msgpack
import zstandard as zstd
from pydantic_ai import ModelMessagesTypeAdapter
from pydantic_ai.messages import ModelMessage
from pydantic_core import to_jsonable_python

from varro.config import DATA_DIR

_zstd_compressor = zstd.ZstdCompressor(level=3)
_zstd_decompressor = zstd.ZstdDecompressor()


def chat_turn_dir(user_id: int, chat_id: int) -> Path:
    return DATA_DIR / "chat" / str(user_id) / str(chat_id)


def turn_fp(user_id: int, chat_id: int, turn_idx: int) -> Path:
    base = chat_turn_dir(user_id, chat_id)
    base.mkdir(parents=True, exist_ok=True)
    return base / f"{turn_idx}.mpk"


def save_turn_messages(msgs: list[ModelMessage], fp: Path) -> None:
    msg_objs = to_jsonable_python(msgs, bytes_mode="base64")
    packed = msgpack.packb(msg_objs, use_bin_type=True, strict_types=True)
    compressed = _zstd_compressor.compress(packed)
    fp.write_bytes(compressed)


def load_turn_messages(fp: Path) -> list[ModelMessage]:
    compressed = fp.read_bytes()
    packed = _zstd_decompressor.decompress(compressed)
    obj = msgpack.unpackb(packed, raw=False)
    return ModelMessagesTypeAdapter.validate_python(obj)


def load_messages_for_turns(turns) -> list[ModelMessage]:
    msgs: list[ModelMessage] = []
    for turn in turns:
        msgs.extend(load_turn_messages(DATA_DIR / turn.obj_fp))
    return msgs
