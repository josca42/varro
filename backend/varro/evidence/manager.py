import shutil
import socket
import subprocess
import asyncio
from pathlib import Path
from typing import Optional
from varro.config import EVIDENCE_USERS_DIR
import aiohttp

EVIDENCE_TEMPLATE = Path("/app/evidence-template")
PORT_RANGE_START = 3001
PORT_RANGE_END = 4000


class EvidenceManager:
    """Manages an Evidence dashboard for a single session."""

    _used_ports: set[int] = set()  # Class-level port tracking across all instances

    def __init__(self, user_id: int):
        self.user_id = user_id
        self.port: Optional[int] = None
        self.process: Optional[subprocess.Popen] = None

    @property
    def dashboard_path(self) -> Path:
        return EVIDENCE_USERS_DIR / str(self.user_id) / "dashboard"

    @property
    def pages_path(self) -> Path:
        return self.dashboard_path / "pages"

    def start_server(self, name: str = "Untitled Dashboard") -> int:
        """
        Create dashboard from template, start dev server, return port.

        Args:
            name: Name for the dashboard

        Returns:
            Port number the dev server is running on
        """
        self._setup_dashboard()
        self.port = self._find_free_port()
        EvidenceManager._used_ports.add(self.port)

        self.process = subprocess.Popen(
            ["npm", "run", "dev", "--", "--port", str(self.port)],
            cwd=self.dashboard_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        return self.port

    async def start_server_async(self, name: str = "Untitled Dashboard") -> int:
        """
        Async version that waits for the server to be ready.

        Args:
            name: Name for the dashboard

        Returns:
            Port number the dev server is running on
        """
        port = self.start_server(name)
        await self._wait_for_server(port)
        return port

    def _setup_dashboard(self):
        """Copy template and setup dashboard directory, or reuse existing."""
        if self.dashboard_path.exists():
            # Reuse existing dashboard
            return

        # Copy template (excluding node_modules)
        shutil.copytree(
            EVIDENCE_TEMPLATE,
            self.dashboard_path,
            ignore=shutil.ignore_patterns("node_modules"),
        )

        # Create symlink for node_modules
        node_modules_link = self.dashboard_path / "node_modules"
        node_modules_link.symlink_to(EVIDENCE_TEMPLATE / "node_modules")

    def _find_free_port(self) -> int:
        """Find an available port in the configured range."""
        for port in range(PORT_RANGE_START, PORT_RANGE_END):
            if port in EvidenceManager._used_ports:
                continue
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                if s.connect_ex(("localhost", port)) != 0:
                    return port
        raise RuntimeError("No free ports available in range")

    async def _wait_for_server(self, port: int, timeout: int = 60):
        """Wait for the Evidence dev server to respond."""
        start = asyncio.get_event_loop().time()
        while asyncio.get_event_loop().time() - start < timeout:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"http://localhost:{port}") as resp:
                        if resp.status in (200, 304):
                            return
            except Exception:
                pass
            await asyncio.sleep(1)
        raise TimeoutError(
            f"Evidence server on port {port} did not start in {timeout}s"
        )

    def stop(self):
        """Stop the dev server and cleanup resources."""
        if self.process:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
            self.process = None

        if self.port:
            EvidenceManager._used_ports.discard(self.port)
            self.port = None

    def __del__(self):
        """Ensure cleanup on garbage collection."""
        self.stop()
