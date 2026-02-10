from __future__ import annotations

import importlib
from pathlib import Path

import pandas as pd


def _seed_docs_template(data_dir: Path) -> Path:
    docs_dir = data_dir / "docs_template"
    (docs_dir / "subjects").mkdir(parents=True)
    (docs_dir / "fact").mkdir()
    (docs_dir / "dim").mkdir()
    (docs_dir / "dashboards").mkdir()
    (docs_dir / "skills").mkdir()
    (docs_dir / "subjects" / "topic.md").write_text("# Topic\n", encoding="utf-8")
    return docs_dir


def _patch_workspace_paths(monkeypatch, data_dir: Path) -> None:
    workspace = importlib.import_module("varro.agent.workspace")
    docs_dir = data_dir / "docs_template"
    monkeypatch.setattr(workspace, "DATA_DIR", data_dir)
    monkeypatch.setattr(workspace, "DOCS_DIR", docs_dir)


def test_ensure_user_workspace_seeds_docs_template(tmp_path: Path, monkeypatch) -> None:
    data_dir = tmp_path / "data"
    _seed_docs_template(data_dir)
    _patch_workspace_paths(monkeypatch, data_dir)

    workspace = importlib.import_module("varro.agent.workspace")
    user_root = workspace.ensure_user_workspace(1)

    assert user_root == data_dir / "user" / "1"
    assert (user_root / "subjects" / "topic.md").read_text(encoding="utf-8") == "# Topic\n"
    assert (user_root / "fact").is_dir()
    assert (user_root / "dim").is_dir()
    assert (user_root / "dashboards").is_dir()


def test_read_file_uses_demo_user_workspace_root(tmp_path: Path, monkeypatch) -> None:
    data_dir = tmp_path / "data"
    _seed_docs_template(data_dir)
    _patch_workspace_paths(monkeypatch, data_dir)

    filesystem = importlib.import_module("varro.agent.filesystem")
    output = filesystem.read_file("/subjects/topic.md")

    assert "Topic" in output
    assert (data_dir / "user" / "1" / "subjects" / "topic.md").exists()


def test_read_file_allows_text_files_without_extension_allowlist(
    tmp_path: Path, monkeypatch
) -> None:
    data_dir = tmp_path / "data"
    _seed_docs_template(data_dir)
    _patch_workspace_paths(monkeypatch, data_dir)
    py_file = data_dir / "user" / "1" / "subjects" / "script.py"
    py_file.parent.mkdir(parents=True, exist_ok=True)
    py_file.write_text("print('hej')\n", encoding="utf-8")

    filesystem = importlib.import_module("varro.agent.filesystem")
    output = filesystem.read_file("/subjects/script.py", user_id=1)

    assert "print('hej')" in output


def test_read_file_returns_error_for_binary_content(tmp_path: Path, monkeypatch) -> None:
    data_dir = tmp_path / "data"
    _seed_docs_template(data_dir)
    _patch_workspace_paths(monkeypatch, data_dir)
    parquet_file = data_dir / "user" / "1" / "subjects" / "table.parquet"
    parquet_file.parent.mkdir(parents=True, exist_ok=True)
    parquet_file.write_bytes(b"\xff\xfe\x00\x01")

    filesystem = importlib.import_module("varro.agent.filesystem")
    output = filesystem.read_file("/subjects/table.parquet", user_id=1)

    assert output.startswith("Error:")


def test_read_file_returns_parquet_preview(tmp_path: Path, monkeypatch) -> None:
    data_dir = tmp_path / "data"
    _seed_docs_template(data_dir)
    _patch_workspace_paths(monkeypatch, data_dir)
    parquet_file = data_dir / "user" / "1" / "subjects" / "table.parquet"
    parquet_file.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"region": ["North", "South"], "value": [1, 2]}).to_parquet(
        parquet_file, index=False
    )

    filesystem = importlib.import_module("varro.agent.filesystem")
    output = filesystem.read_file("/subjects/table.parquet", user_id=1)

    assert "region|value" in output
    assert "North|1" in output


def test_write_and_edit_file_use_user_workspace_root(
    tmp_path: Path, monkeypatch
) -> None:
    data_dir = tmp_path / "data"
    _seed_docs_template(data_dir)
    _patch_workspace_paths(monkeypatch, data_dir)

    filesystem = importlib.import_module("varro.agent.filesystem")
    write_res = filesystem.write_file("/dashboards/note.txt", "alpha", user_id=1)
    edit_res = filesystem.edit_file(
        "/dashboards/note.txt",
        old_string="alpha",
        new_string="beta",
        user_id=1,
    )

    assert write_res == "Wrote 5 bytes."
    assert edit_res == "Replaced 1 occurrence(s)."
    assert (data_dir / "user" / "1" / "dashboards" / "note.txt").read_text(
        encoding="utf-8"
    ) == "beta"


def test_read_write_edit_reject_paths_outside_sandbox(
    tmp_path: Path, monkeypatch
) -> None:
    data_dir = tmp_path / "data"
    _seed_docs_template(data_dir)
    _patch_workspace_paths(monkeypatch, data_dir)

    filesystem = importlib.import_module("varro.agent.filesystem")
    read_res = filesystem.read_file("/../outside.txt", user_id=1)
    write_res = filesystem.write_file("/../outside.txt", "x", user_id=1)
    edit_res = filesystem.edit_file(
        "/../outside.txt",
        old_string="a",
        new_string="b",
        user_id=1,
    )

    assert read_res == "Error: file_path escapes sandbox root"
    assert write_res == "Error: file_path escapes sandbox root"
    assert edit_res == "Error: file_path escapes sandbox root"
