import json

from varro.data.disk_to_db import fact_tables_incremental_to_db as db_apply


class _InspectorMissing:
    def has_table(self, table, schema):
        return False


class _InspectorPresent:
    def has_table(self, table, schema):
        return True


def _patch_paths(monkeypatch, tmp_path):
    monkeypatch.setattr(db_apply, "DST_STATBANK_TABLES_DIR", tmp_path / "statbank_tables")
    monkeypatch.setattr(db_apply, "SYNC_DIR", tmp_path / "statbank_tables" / "_sync")
    monkeypatch.setattr(db_apply, "RUNS_DIR", tmp_path / "statbank_tables" / "_sync" / "runs")
    db_apply.RUNS_DIR.mkdir(parents=True, exist_ok=True)


def test_apply_incremental_run_skips_missing_fact_table(monkeypatch, tmp_path):
    _patch_paths(monkeypatch, tmp_path)
    monkeypatch.setattr(db_apply, "inspect", lambda _engine: _InspectorMissing())

    manifest = {
        "run_id": "run-1",
        "tables": {"TAB1": {"status": "synced", "changed_tids": ["2024"]}},
    }
    fp = db_apply.run_manifest_path("run-1")
    fp.write_text(json.dumps(manifest))

    result = db_apply.apply_incremental_run("run-1")

    assert result["status"] == "success"
    assert result["summary"]["tables_skipped"] == 1
    updated = json.loads(fp.read_text())
    assert updated["db_apply"]["tables"]["TAB1"]["reason"] == "missing_fact_table"


def test_apply_incremental_run_fails_when_partitions_missing(monkeypatch, tmp_path):
    _patch_paths(monkeypatch, tmp_path)
    monkeypatch.setattr(db_apply, "inspect", lambda _engine: _InspectorPresent())

    manifest = {
        "run_id": "run-2",
        "tables": {"TAB2": {"status": "synced", "changed_tids": ["2024"]}},
    }
    fp = db_apply.run_manifest_path("run-2")
    fp.write_text(json.dumps(manifest))

    result = db_apply.apply_incremental_run("run-2")

    assert result["status"] == "partial_failure"
    assert result["summary"]["tables_failed"] == 1
    updated = json.loads(fp.read_text())
    assert (
        updated["db_apply"]["tables"]["TAB2"]["reason"] == "missing_partition_files"
    )
