from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import time

from varro.config import settings

SNAPSHOT_TOKEN_TTL_SECONDS = 120


def _config_value(key: str) -> str | None:
    return settings.get(key) or os.environ.get(key)


def _token_secret() -> str:
    secret = _config_value("AUTH_TOKEN_SECRET") or _config_value("SESSION_SECRET")
    if not secret:
        raise RuntimeError("AUTH_TOKEN_SECRET or SESSION_SECRET is required.")
    return secret


def _b64encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def _b64decode(data: str) -> bytes:
    pad = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + pad)


def make_snapshot_token(
    user_id: int,
    slug: str,
    *,
    ttl_seconds: int = SNAPSHOT_TOKEN_TTL_SECONDS,
) -> str:
    payload = {
        "uid": int(user_id),
        "slug": slug,
        "purpose": "snapshot",
        "exp": int(time.time()) + ttl_seconds,
    }
    body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode()
    sig = hmac.new(_token_secret().encode(), body, hashlib.sha256).digest()
    return f"{_b64encode(body)}.{_b64encode(sig)}"


def verify_snapshot_token(token: str | None, slug: str) -> int | None:
    if not token or "." not in token:
        return None

    body_b64, sig_b64 = token.split(".", 1)
    try:
        body = _b64decode(body_b64)
        sig = _b64decode(sig_b64)
        payload = json.loads(body)
    except Exception:
        return None

    expected = hmac.new(_token_secret().encode(), body, hashlib.sha256).digest()
    if not hmac.compare_digest(sig, expected):
        return None
    if payload.get("purpose") != "snapshot":
        return None
    if payload.get("slug") != slug:
        return None
    if payload.get("exp", 0) < int(time.time()):
        return None

    user_id = payload.get("uid")
    if not isinstance(user_id, int):
        return None
    return user_id
