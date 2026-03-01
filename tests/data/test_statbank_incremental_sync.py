import json
from datetime import timedelta

import pandas as pd
import pytest

from varro.data.statbank_to_disk import copy_tables_statbank as sync


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


def test_infer_frequency_from_tid_patterns():
    assert sync.infer_frequency(["2024"]) == "yearly"
    assert sync.infer_frequency(["2024K4"]) == "quarterly"
    assert sync.infer_frequency(["2024M12"]) == "monthly"
    assert sync.infer_frequency(["2024U52"]) == "weekly"
    assert sync.infer_frequency(["2024M12D31"]) == "daily"
    assert sync.infer_frequency(["2024H2"]) == "half_yearly"
    assert sync.infer_frequency(["2024/2025"]) == "other"


def test_pick_periods_to_fetch_bootstrap():
    remote = ["2021", "2022", "2023", "2024"]
    new_periods, refresh_periods, periods_to_fetch = sync.pick_periods_to_fetch(
        remote_tids=remote,
        local_tids=[],
        frequency="yearly",
        bootstrap=True,
    )

    assert new_periods == remote
    assert refresh_periods == remote
    assert periods_to_fetch == remote


def test_pick_periods_to_fetch_incremental():
    remote = [f"t{i}" for i in range(1, 11)]
    new_periods, refresh_periods, periods_to_fetch = sync.pick_periods_to_fetch(
        remote_tids=remote,
        local_tids=[f"t{i}" for i in range(1, 9)],
        frequency="other",
        bootstrap=False,
    )

    assert new_periods == ["t9", "t10"]
    assert refresh_periods == ["t9", "t10"]
    assert periods_to_fetch == ["t9", "t10"]


def test_run_sync_cycle_weekly_gate_writes_manifest(monkeypatch, tmp_path):
    _patch_sync_paths(monkeypatch, tmp_path)
    sync.ensure_dirs()

    state = sync.default_state()
    state["last_catalog_poll_at"] = sync.iso_utc(sync.now_utc() - timedelta(days=1))
    sync.save_state(state)

    def _fail_fetch_catalog():
        raise AssertionError("fetch_catalog should not be called")

    monkeypatch.setattr(sync, "fetch_catalog", _fail_fetch_catalog)

    manifest = sync.run_sync_cycle(force_catalog_poll=False, run_id="run-weekly-gate")

    assert manifest["status"] == "skipped"
    run_fp = sync.run_manifest_path("run-weekly-gate")
    assert run_fp.exists()
    loaded = json.loads(run_fp.read_text())
    assert loaded["catalog"]["reason"] == "weekly_gate"


def test_sync_table_skips_when_updated_unchanged(monkeypatch, tmp_path):
    _patch_sync_paths(monkeypatch, tmp_path)
    sync.ensure_dirs()

    table_id = "TEST1"
    partition_dir = sync.table_dir(table_id)
    partition_dir.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"Tid": ["2024"], "INDHOLD": [1]}).to_parquet(
        partition_dir / "2024.parquet"
    )

    state = sync.default_state()
    state["tables"][table_id] = {
        "last_seen_updated": "2025-01-01T00:00:00",
        "frequency": "yearly",
    }

    def _fail_fetch_table_info(_table_id):
        raise AssertionError("fetch_table_info should not be called")

    monkeypatch.setattr(sync, "fetch_table_info", _fail_fetch_table_info)

    result, _next_state = sync._sync_table(
        table_id=table_id,
        catalog_updated="2025-01-01T00:00:00",
        run_id="run-1",
        state=state,
        overrides={},
        now=sync.now_utc(),
    )

    assert result["status"] == "skipped"
    assert result["reason"] == "unchanged_updated"


def test_statbank_request_sleeps_after_success(monkeypatch):
    sleeps = []
    response = object()
    monkeypatch.setattr(sync, "DST_API_SLEEP_SECONDS", 2.0)
    monkeypatch.setattr(sync, "sleep", sleeps.append)
    monkeypatch.setattr(sync.httpx, "get", lambda _url, **_kwargs: response)

    result = sync.statbank_request("get", "https://example.com", timeout=1)

    assert result is response
    assert sleeps == [2.0]


def test_statbank_request_sleeps_after_error(monkeypatch):
    sleeps = []
    monkeypatch.setattr(sync, "DST_API_SLEEP_SECONDS", 2.0)
    monkeypatch.setattr(sync, "sleep", sleeps.append)

    def _raise(_url, **_kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr(sync.httpx, "post", _raise)

    with pytest.raises(RuntimeError, match="boom"):
        sync.statbank_request("post", "https://example.com", json={})

    assert sleeps == [2.0]
