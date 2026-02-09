from __future__ import annotations

import importlib
from pathlib import Path


def _seed_dev_root(dev_root: Path) -> None:
    (dev_root / "subjects").mkdir(parents=True)
    (dev_root / "subjects" / "topic.md").write_text("# Topic\n", encoding="utf-8")


def _patch_dev_mode(monkeypatch, dev_root: Path):
    bash = importlib.import_module("varro.agent.bash")
    monkeypatch.setattr(bash, "USE_BWRAP", "DEV")
    monkeypatch.setattr(bash, "DEV_ROOT", dev_root)
    return bash


def test_run_bash_command_maps_absolute_paths_to_dev_root(tmp_path: Path, monkeypatch):
    dev_root = tmp_path / "dev_root"
    _seed_dev_root(dev_root)
    bash = _patch_dev_mode(monkeypatch, dev_root)

    output, cwd = bash.run_bash_command(1, "/", "ls /subjects")

    assert output.strip() == "topic.md"
    assert cwd == "/"


def test_run_bash_command_preserves_errors_with_pwd_sentinel(tmp_path: Path, monkeypatch):
    dev_root = tmp_path / "dev_root"
    _seed_dev_root(dev_root)
    bash = _patch_dev_mode(monkeypatch, dev_root)

    output, cwd = bash.run_bash_command(1, "/", "ls /subjects; ls /missing")

    assert output.startswith("Error: command failed with exit code")
    assert "topic.md" in output
    assert "No such file or directory" in output
    assert cwd == "/"
