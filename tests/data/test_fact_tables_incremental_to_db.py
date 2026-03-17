from varro.data.disk_to_db import fact_tables_incremental_to_db as db_apply


def test_normalize_changed_tids_monthly_codes():
    assert db_apply.normalize_changed_tids(["2025M03", "2025M04"]) == [
        "2025-03-01",
        "2025-04-01",
    ]


def test_normalize_changed_tids_deduplicates():
    assert db_apply.normalize_changed_tids(["2025M03", "2025M03"]) == ["2025-03-01"]


def test_apply_table_delta_skips_when_no_partitions(monkeypatch, tmp_path):
    monkeypatch.setattr(db_apply, "DST_STATBANK_TABLES_DIR", tmp_path / "statbank_tables")
    result = db_apply.apply_table_delta("NONEXISTENT", ["2024"])
    assert result["status"] == "skipped"
    assert result["reason"] == "no_partition_data"
