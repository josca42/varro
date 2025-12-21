# minio_storage.py
import base64
import io
import mimetypes
from typing import Any, Dict, Union

from chainlit import make_async
from chainlit.data.storage_clients.base import BaseStorageClient


DEFAULT_MIME = "application/octet-stream"


class PostgresStorageClient(BaseStorageClient):
    """
    Chainlit storage client that writes base64 encoded strings to the postgres database
    """

    def __init__(self):
        pass

    # ───────────────────────────── helpers ─────────────────────────────
    def _build_url(self, mime: str, payload_bytes: bytes) -> str:
        """
        Create a data-URI that is used to store data in the postgres database as base64 encoded string
        """
        b64 = base64.b64encode(payload_bytes).decode("ascii")
        return f"data:{mime};base64,{b64}"

    def _mime_for(self, object_key: str, provided: str | None) -> str:
        if provided and provided != DEFAULT_MIME:
            return provided
        guess, _ = mimetypes.guess_type(object_key)
        return guess or DEFAULT_MIME

    # ───────────────────────────── sync API ─────────────────────────────
    def sync_upload_file(
        self,
        object_key: str,
        data: Union[bytes, str],
        mime: str = DEFAULT_MIME,
        overwrite: bool = True,  # not enforced for S3—keys are overwritten by default
    ) -> Dict[str, Any]:
        if isinstance(data, (bytes, bytearray)):
            raise ValueError("data must be str")

        payload = data.encode()
        mime = self._mime_for(object_key, mime)
        url = self._build_url(mime=mime, payload_bytes=payload)
        return {"url": url}

    def sync_delete_file(self, object_key: str) -> bool:
        return True

    def sync_get_read_url(self, object_key: str) -> str:
        """
        Return the stable app-relative URL; the MinIO mount below (redirect or proxy)
        does the heavy lifting. We keep this deterministic so the same element
        URL works across sessions without re-signing here.
        """
        return object_key

    # ───────────────────────────── async wrappers ─────────────────────────────
    async def upload_file(self, *args, **kwargs):
        return await make_async(self.sync_upload_file)(*args, **kwargs)

    async def delete_file(self, *args, **kwargs):
        return await make_async(self.sync_delete_file)(*args, **kwargs)

    async def get_read_url(self, *args, **kwargs):
        return await make_async(self.sync_get_read_url)(*args, **kwargs)

    async def close(self):
        """Close the storage client and clean up resources."""
        pass
