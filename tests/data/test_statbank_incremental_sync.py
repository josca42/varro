import pandas as pd
import pytest

from varro.data.statbank_to_disk import copy_tables_statbank as sync


def _patch_sync_paths(monkeypatch, tmp_path):
    monkeypatch.setattr(sync, "TABLES_INFO_DIR", tmp_path / "metadata")
    monkeypatch.setattr(sync, "FACT_TABLES_DIR", tmp_path / "statbank_tables")
    monkeypatch.setattr(sync, "SYNC_DIR", tmp_path / "statbank_tables" / "_sync")
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


def test_pick_periods_bootstrap():
    remote = ["2021", "2022", "2023", "2024"]
    periods = sync.pick_periods_to_fetch(remote, local_tids=[], frequency="yearly")
    assert periods == remote


def test_pick_periods_incremental():
    remote = [f"t{i}" for i in range(1, 11)]
    local = [f"t{i}" for i in range(1, 9)]
    periods = sync.pick_periods_to_fetch(remote, local, frequency="other")
    assert "t9" in periods
    assert "t10" in periods
    assert "t1" not in periods


def test_pick_periods_includes_lag():
    remote = [f"2020M{i:02d}" for i in range(1, 13)]
    local = [f"2020M{i:02d}" for i in range(1, 13)]
    periods = sync.pick_periods_to_fetch(remote, local, frequency="monthly")
    assert periods == ["2020M10", "2020M11", "2020M12"]


def test_load_save_state(monkeypatch, tmp_path):
    _patch_sync_paths(monkeypatch, tmp_path)
    sync.ensure_dirs()
    assert sync.load_state() == {}
    state = {"FOLK1A": {"updated": "2025-01-01", "frequency": "quarterly"}}
    sync.save_state(state)
    assert sync.load_state() == state


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
