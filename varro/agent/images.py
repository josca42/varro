from __future__ import annotations

import io
import math
from pathlib import Path

from PIL import Image

SNAPSHOT_MAX_PIXELS = 1_500_000
JUPYTER_SHOW_MAX_PIXELS = 1_000_000


def optimize_png_bytes(png_bytes: bytes, *, max_pixels: int) -> bytes:
    with Image.open(io.BytesIO(png_bytes)) as image:
        width, height = image.size
        area = width * height
        if area > max_pixels:
            scale = math.sqrt(max_pixels / area)
            width = max(1, int(width * scale))
            height = max(1, int(height * scale))
            image = image.resize((width, height), Image.Resampling.LANCZOS)

        buf = io.BytesIO()
        image.save(buf, format="PNG", optimize=True)
        return buf.getvalue()


def save_png(path: Path, png_bytes: bytes, *, max_pixels: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(optimize_png_bytes(png_bytes, max_pixels=max_pixels))
