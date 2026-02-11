from __future__ import annotations

import importlib
from pathlib import Path


def _seed_dev_root(dev_root: Path) -> None:
    (dev_root / "subjects").mkdir(parents=True)
    (dev_root / "dashboards").mkdir(parents=True)
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


def test_run_bash_command_allows_read_commands_in_readonly_docs(
    tmp_path: Path, monkeypatch
):
    dev_root = tmp_path / "dev_root"
    _seed_dev_root(dev_root)
    bash = _patch_dev_mode(monkeypatch, dev_root)

    find_output, find_cwd = bash.run_bash_command(1, "/", "find /subjects -type f")
    grep_output, grep_cwd = bash.run_bash_command(
        1, "/", "grep -n Topic /subjects/topic.md"
    )

    assert "topic.md" in find_output
    assert "1:# Topic" in grep_output
    assert find_cwd == "/"
    assert grep_cwd == "/"


def test_run_bash_command_blocks_touch_in_readonly_docs(tmp_path: Path, monkeypatch):
    dev_root = tmp_path / "dev_root"
    _seed_dev_root(dev_root)
    bash = _patch_dev_mode(monkeypatch, dev_root)

    output, cwd = bash.run_bash_command(1, "/", "touch /subjects/new.md")

    assert output == "Error: path is read-only"
    assert cwd == "/"
    assert not (dev_root / "subjects" / "new.md").exists()


def test_run_bash_command_blocks_mv_in_readonly_docs(tmp_path: Path, monkeypatch):
    dev_root = tmp_path / "dev_root"
    _seed_dev_root(dev_root)
    bash = _patch_dev_mode(monkeypatch, dev_root)

    output, cwd = bash.run_bash_command(
        1, "/", "mv /subjects/topic.md /dashboards/topic.md"
    )

    assert output == "Error: path is read-only"
    assert cwd == "/"
    assert (dev_root / "subjects" / "topic.md").exists()
    assert not (dev_root / "dashboards" / "topic.md").exists()


def test_run_bash_command_blocks_redirection_in_readonly_docs(
    tmp_path: Path, monkeypatch
):
    dev_root = tmp_path / "dev_root"
    _seed_dev_root(dev_root)
    bash = _patch_dev_mode(monkeypatch, dev_root)

    output, cwd = bash.run_bash_command(1, "/", "echo hej > /subjects/new.md")

    assert output == "Error: path is read-only"
    assert cwd == "/"
    assert not (dev_root / "subjects" / "new.md").exists()


def test_run_bash_command_blocks_relative_mutation_after_cd_to_readonly(
    tmp_path: Path, monkeypatch
):
    dev_root = tmp_path / "dev_root"
    _seed_dev_root(dev_root)
    bash = _patch_dev_mode(monkeypatch, dev_root)

    output, cwd = bash.run_bash_command(1, "/", "cd /subjects && touch new.md")

    assert output == "Error: path is read-only"
    assert cwd == "/"
    assert not (dev_root / "subjects" / "new.md").exists()
