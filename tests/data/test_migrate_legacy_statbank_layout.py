import pandas as pd

from varro.data.statbank_to_disk import copy_tables_statbank as sync
from varro.data.statbank_to_disk import migrate_legacy_statbank_layout as migration


def _patch_sync_paths(monkeypatch, tmp_path):
    monkeypatch.setattr(sync, "TABLES_INFO_DIR", tmp_path / "metadata")
    monkeypatch.setattr(sync, "FACT_TABLES_DIR", tmp_path / "statbank_tables")
    monkeypatch.setattr(sync, "SYNC_DIR", tmp_path / "statbank_tables" / "_sync")
    monkeypatch.setattr(sync, "RUNS_DIR", tmp_path / "statbank_tables" / "_sync" / "runs")
    monkeypatch.setattr(sync, "STATE_FP", tmp_path / "statbank_tables" / "_sync" / "state.json")
    monkeypatch.setattr(
        sync,
        "FREQUENCY_OVERRIDES_FP",
        tmp_path / "statbank_tables" / "_sync" / "frequency_overrides.json",
    )
    sync.ensure_dirs()


def test_iter_legacy_sources_discovers_root_and_partition_files(monkeypatch, tmp_path):
    _patch_sync_paths(monkeypatch, tmp_path)
    base = sync.FACT_TABLES_DIR
    (base / "_sync").mkdir(parents=True, exist_ok=True)
    (base / "initial_copy").mkdir(parents=True, exist_ok=True)
    (base / "TABA.parquet").write_text("x")
    (base / "TABB").mkdir(parents=True, exist_ok=True)
    (base / "TABB" / "partition_0.parquet").write_text("x")
    (base / "TABB" / "2025.parquet").write_text("x")
    (base / "initial_copy" / "TABC.parquet").write_text("x")

    sources = list(migration.iter_legacy_sources(base, only_tables=set()))

    assert ("TABA", base / "TABA.parquet") in sources
    assert ("TABB", base / "TABB" / "partition_0.parquet") in sources
    assert all("initial_copy" not in str(fp) for _, fp in sources)


def test_migrate_source_file_writes_canonical_tid_files(monkeypatch, tmp_path):
    _patch_sync_paths(monkeypatch, tmp_path)
    source_fp = sync.FACT_TABLES_DIR / "TABX.parquet"
    pd.DataFrame({"Tid": ["2024", "2024", "2025"], "INDHOLD": [1, 2, 3]}).to_parquet(source_fp)

    result = migration.migrate_source_file(
        table_id="TABX",
        source_fp=source_fp,
        overwrite_canonical=False,
        dry_run=False,
    )

    fp_2024 = sync.tid_to_partition_fp("TABX", "2024")
    fp_2025 = sync.tid_to_partition_fp("TABX", "2025")
    assert fp_2024.exists()
    assert fp_2025.exists()
    assert len(pd.read_parquet(fp_2024)) == 2
    assert len(pd.read_parquet(fp_2025)) == 1
    assert result["files_written"] == 2
    assert result["files_skipped_existing"] == 0


def test_build_bootstrap_state_sets_table_state_from_canonical_tids(monkeypatch, tmp_path):
    _patch_sync_paths(monkeypatch, tmp_path)
    table_dir = sync.table_dir("TABY")
    table_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"Tid": ["2024"], "INDHOLD": [1]}).to_parquet(table_dir / "2024.parquet")
    pd.DataFrame({"Tid": ["2025"], "INDHOLD": [1]}).to_parquet(table_dir / "2025.parquet")

    state = sync.default_state()
    reports = migration.build_bootstrap_state(
        state=state,
        run_id="bootstrap-1",
        catalog_by_table={"TABY": "2026-02-01T00:00:00"},
    )

    assert reports["TABY"]["status"] == "bootstrapped"
    assert reports["TABY"]["canonical_tid_count"] == 2
    assert state["tables"]["TABY"]["frequency"] == "yearly"
    assert state["tables"]["TABY"]["last_seen_updated"] == "2026-02-01T00:00:00"
    assert state["tables"]["TABY"]["last_status"] == "bootstrapped"
