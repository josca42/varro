import json
import math
import pickle
import re
from datetime import datetime, timedelta, timezone
from io import StringIO
from pathlib import Path
from urllib.parse import quote, unquote
from uuid import uuid4

import httpx
import pandas as pd

from varro.config import DST_METADATA_DIR, DST_STATBANK_TABLES_DIR

TABLES_INFO_DIR = DST_METADATA_DIR / "tables_info_raw_da"
FACT_TABLES_DIR = DST_STATBANK_TABLES_DIR
SYNC_DIR = FACT_TABLES_DIR / "_sync"
RUNS_DIR = SYNC_DIR / "runs"
STATE_FP = SYNC_DIR / "state.json"
FREQUENCY_OVERRIDES_FP = SYNC_DIR / "frequency_overrides.json"
CATALOG_POLL_INTERVAL = timedelta(days=7)
MAX_ROWS_PER_CALL = 50_000_000
REFRESH_WINDOWS = {
    "daily": 14,
    "weekly": 12,
    "monthly": 18,
    "quarterly": 8,
    "half_yearly": 6,
    "yearly": 4,
    "other": 2,
}
YEARLY_RE = re.compile(r"^\d{4}$")
QUARTERLY_RE = re.compile(r"^\d{4}K[1-4]$")
MONTHLY_RE = re.compile(r"^\d{4}M\d{2}$")
WEEKLY_RE = re.compile(r"^\d{4}U\d{2}$")
DAILY_RE = re.compile(r"^\d{4}M\d{2}D\d{2}$")
HALF_YEARLY_RE = re.compile(r"^\d{4}H[12]$")


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def parse_utc(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def make_run_id(now: datetime) -> str:
    return now.strftime("%Y%m%dT%H%M%SZ")


def chunk(values: list[str], size: int) -> list[list[str]]:
    return [values[i : i + size] for i in range(0, len(values), size)]


def ensure_dirs() -> None:
    TABLES_INFO_DIR.mkdir(parents=True, exist_ok=True)
    FACT_TABLES_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)


def write_json_atomic(fp: Path, data: dict) -> None:
    fp.parent.mkdir(parents=True, exist_ok=True)
    tmp = fp.parent / f"{fp.name}.{uuid4().hex}.tmp"
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    tmp.replace(fp)


def write_pickle_atomic(fp: Path, data: dict) -> None:
    fp.parent.mkdir(parents=True, exist_ok=True)
    tmp = fp.parent / f"{fp.name}.{uuid4().hex}.tmp"
    with open(tmp, "wb") as f:
        pickle.dump(data, f)
    tmp.replace(fp)


def write_parquet_atomic(df: pd.DataFrame, fp: Path) -> None:
    fp.parent.mkdir(parents=True, exist_ok=True)
    tmp = fp.parent / f"{fp.name}.{uuid4().hex}.tmp"
    df.to_parquet(tmp)
    tmp.replace(fp)


def default_state() -> dict:
    return {"last_catalog_poll_at": None, "last_run_id": None, "tables": {}}


def load_state() -> dict:
    if not STATE_FP.exists():
        return default_state()
    return json.loads(STATE_FP.read_text())


def save_state(state: dict) -> None:
    write_json_atomic(STATE_FP, state)


def load_frequency_overrides() -> dict[str, str]:
    if not FREQUENCY_OVERRIDES_FP.exists():
        return {}
    raw = json.loads(FREQUENCY_OVERRIDES_FP.read_text())
    overrides = {}
    for table_id, frequency in raw.items():
        if frequency in REFRESH_WINDOWS:
            overrides[table_id] = frequency
    return overrides


def run_manifest_path(run_id: str) -> Path:
    return RUNS_DIR / f"{run_id}.json"


def write_run_manifest(run_id: str, manifest: dict) -> None:
    write_json_atomic(run_manifest_path(run_id), manifest)


def latest_run_manifest_path() -> Path:
    runs = sorted(RUNS_DIR.glob("*.json"))
    if not runs:
        raise FileNotFoundError("No run manifests found")
    return runs[-1]


def should_poll_catalog(state: dict, now: datetime, force_catalog_poll: bool) -> bool:
    if force_catalog_poll:
        return True
    last = state.get("last_catalog_poll_at")
    if last is None:
        return True
    return now - parse_utc(last) >= CATALOG_POLL_INTERVAL


def fetch_catalog() -> list[dict]:
    response = httpx.get("https://api.statbank.dk/v1/tables", params={"lang": "da"}, timeout=120)
    response.raise_for_status()
    rows = response.json()
    return sorted(rows, key=lambda row: row["id"])


def fetch_table_info(table_id: str) -> dict:
    response = httpx.get(
        "https://api.statbank.dk/v1/tableinfo",
        params={"id": table_id, "format": "JSON", "lang": "da"},
        timeout=120,
    )
    response.raise_for_status()
    table_info = response.json()
    if table_info.get("errorTypeCode"):
        raise RuntimeError(f"{table_info['errorTypeCode']}: {table_info.get('message', '')}")
    variables = table_info.get("variables")
    if not isinstance(variables, list):
        raise RuntimeError("Missing variables in tableinfo")
    return table_info


def save_table_info(table_id: str, table_info: dict) -> None:
    write_pickle_atomic(TABLES_INFO_DIR / f"{table_id}.pkl", table_info)


def get_tid_values(table_info: dict) -> list[str]:
    time_var = next(
        (var for var in table_info["variables"] if str(var.get("id", "")).lower() == "tid"),
        None,
    )
    if time_var is None:
        raise RuntimeError("Table has no Tid variable")
    values = []
    for value in time_var.get("values") or []:
        if isinstance(value, dict):
            values.append(str(value["id"]))
        else:
            values.append(str(value))
    if not values:
        raise RuntimeError("Tid has no values")
    return values


def infer_frequency(tid_values: list[str]) -> str:
    sample = next((value for value in reversed(tid_values) if value), "")
    if DAILY_RE.fullmatch(sample):
        return "daily"
    if WEEKLY_RE.fullmatch(sample):
        return "weekly"
    if MONTHLY_RE.fullmatch(sample):
        return "monthly"
    if QUARTERLY_RE.fullmatch(sample):
        return "quarterly"
    if HALF_YEARLY_RE.fullmatch(sample):
        return "half_yearly"
    if YEARLY_RE.fullmatch(sample):
        return "yearly"
    return "other"


def resolve_frequency(table_id: str, tid_values: list[str], overrides: dict[str, str]) -> str:
    if table_id in overrides:
        return overrides[table_id]
    return infer_frequency(tid_values)


def table_dir(table_id: str) -> Path:
    return FACT_TABLES_DIR / table_id


def tid_to_partition_fp(table_id: str, tid: str) -> Path:
    encoded = quote(tid, safe="")
    return table_dir(table_id) / f"{encoded}.parquet"


def list_local_tids(table_id: str) -> list[str]:
    table_folder = table_dir(table_id)
    if not table_folder.exists():
        return []
    return sorted(unquote(fp.stem) for fp in table_folder.glob("*.parquet"))


def estimate_rows_per_time(table_info: dict, tid_values: list[str]) -> int:
    cardinalities = [len(var.get("values") or []) for var in table_info["variables"]]
    total_rows = math.prod(cardinalities) if cardinalities else 1
    return max(1, math.ceil(total_rows / max(1, len(tid_values))))


def max_tid_values_per_call(table_info: dict, tid_values: list[str]) -> int:
    rows_per_time = estimate_rows_per_time(table_info, tid_values)
    return max(1, MAX_ROWS_PER_CALL // rows_per_time)


def build_variables_payload(table_info: dict, tids: list[str]) -> list[dict]:
    payload = []
    for var in table_info["variables"]:
        values = tids if str(var["id"]).lower() == "tid" else ["*"]
        payload.append({"code": var["id"], "values": values})
    return payload


def copy_table_batch(table_id: str, table_info: dict, tids: list[str]) -> pd.DataFrame:
    response = httpx.post(
        "https://api.statbank.dk/v1/data",
        json={
            "table": table_id,
            "format": "BULK",
            "lang": "da",
            "valuePresentation": "Code",
            "variables": build_variables_payload(table_info, tids),
        },
        timeout=60 * 10,
    )
    response.raise_for_status()
    return pd.read_csv(StringIO(response.text), sep=";", decimal=",", low_memory=False)


def tid_column_name(df: pd.DataFrame) -> str:
    for col in df.columns:
        if str(col).lower() == "tid":
            return str(col)
    raise RuntimeError("Missing Tid column in StatBank response")


def pick_periods_to_fetch(
    remote_tids: list[str],
    local_tids: list[str],
    frequency: str,
    bootstrap: bool,
) -> tuple[list[str], list[str], list[str]]:
    new_periods = [tid for tid in remote_tids if tid not in set(local_tids)]
    if bootstrap:
        refresh_periods = remote_tids[-REFRESH_WINDOWS[frequency] :]
        return new_periods, refresh_periods, remote_tids
    refresh_periods = remote_tids[-REFRESH_WINDOWS[frequency] :]
    target_set = set(new_periods) | set(refresh_periods)
    periods_to_fetch = [tid for tid in remote_tids if tid in target_set]
    return new_periods, refresh_periods, periods_to_fetch


def write_batch_partitions(table_id: str, periods: list[str], df: pd.DataFrame) -> tuple[int, int]:
    tid_col = tid_column_name(df)
    observed = set()
    rows_written = 0
    files_written = 0
    for tid, group in df.groupby(tid_col, sort=False):
        tid_str = str(tid)
        observed.add(tid_str)
        rows_written += len(group)
        files_written += 1
        write_parquet_atomic(group, tid_to_partition_fp(table_id, tid_str))

    empty = df.iloc[0:0].copy()
    if len(empty.columns) > 0:
        for tid in periods:
            if tid in observed:
                continue
            files_written += 1
            write_parquet_atomic(empty, tid_to_partition_fp(table_id, tid))

    return rows_written, files_written


def build_table_state(
    table_state: dict,
    *,
    catalog_updated: str,
    frequency: str,
    run_id: str,
    now: datetime,
    status: str,
    error: str | None,
) -> dict:
    next_state = dict(table_state)
    next_state["last_seen_updated"] = catalog_updated
    next_state["last_sync_at"] = iso_utc(now)
    next_state["frequency"] = frequency
    next_state["bootstrap_complete"] = True
    next_state["last_status"] = status
    next_state["last_error"] = error
    next_state["last_run_id"] = run_id
    return next_state


def _sync_table(
    table_id: str,
    catalog_updated: str,
    run_id: str,
    state: dict,
    overrides: dict[str, str],
    now: datetime,
) -> tuple[dict, dict]:
    table_state = state["tables"].get(table_id, {})
    local_tids = list_local_tids(table_id)
    bootstrap = len(local_tids) == 0
    if not bootstrap and table_state.get("last_seen_updated") == catalog_updated:
        return (
            {
                "status": "skipped",
                "reason": "unchanged_updated",
                "catalog_updated": catalog_updated,
                "bootstrap": False,
                "changed_tids": [],
            },
            table_state,
        )

    info = fetch_table_info(table_id)
    save_table_info(table_id, info)
    remote_tids = get_tid_values(info)
    frequency = resolve_frequency(table_id, remote_tids, overrides)
    new_periods, refresh_periods, periods_to_fetch = pick_periods_to_fetch(
        remote_tids, local_tids, frequency, bootstrap
    )

    rows_written = 0
    files_written = 0
    if periods_to_fetch:
        per_call = max_tid_values_per_call(info, remote_tids)
        for periods in chunk(periods_to_fetch, per_call):
            df = copy_table_batch(table_id, info, periods)
            batch_rows, batch_files = write_batch_partitions(table_id, periods, df)
            rows_written += batch_rows
            files_written += batch_files

    result = {
        "status": "synced",
        "catalog_updated": catalog_updated,
        "bootstrap": bootstrap,
        "frequency": frequency,
        "remote_tid_count": len(remote_tids),
        "local_tid_count_before": len(local_tids),
        "new_periods": new_periods,
        "refresh_periods": refresh_periods,
        "changed_tids": periods_to_fetch,
        "rows_written": rows_written,
        "files_written": files_written,
    }
    next_state = build_table_state(
        table_state,
        catalog_updated=catalog_updated,
        frequency=frequency,
        run_id=run_id,
        now=now,
        status="synced",
        error=None,
    )
    return result, next_state


def sync_table(table_id: str, catalog_updated: str, run_id: str) -> dict:
    ensure_dirs()
    state = load_state()
    overrides = load_frequency_overrides()
    now = now_utc()
    result, next_state = _sync_table(table_id, catalog_updated, run_id, state, overrides, now)
    state["tables"][table_id] = next_state
    state["last_run_id"] = run_id
    save_state(state)
    return result


def run_sync_cycle(force_catalog_poll: bool = False, run_id: str | None = None) -> dict:
    ensure_dirs()
    now = now_utc()
    run_id = run_id or make_run_id(now)
    state = load_state()
    overrides = load_frequency_overrides()
    manifest = {
        "run_id": run_id,
        "started_at": iso_utc(now),
        "finished_at": None,
        "force_catalog_poll": force_catalog_poll,
        "status": "running",
        "catalog": {},
        "tables": {},
        "summary": {},
    }

    try:
        if not should_poll_catalog(state, now, force_catalog_poll):
            manifest["status"] = "skipped"
            manifest["catalog"] = {
                "polled": False,
                "reason": "weekly_gate",
                "last_catalog_poll_at": state.get("last_catalog_poll_at"),
            }
            manifest["summary"] = {
                "tables_total": 0,
                "tables_synced": 0,
                "tables_skipped": 0,
                "tables_failed": 0,
                "tables_with_changed_tids": 0,
            }
            return manifest

        catalog = fetch_catalog()
        state["last_catalog_poll_at"] = iso_utc(now)
        manifest["catalog"] = {
            "polled": True,
            "table_count": len(catalog),
            "polled_at": iso_utc(now),
        }

        for row in catalog:
            table_id = row["id"]
            catalog_updated = row.get("updated")
            try:
                result, next_state = _sync_table(
                    table_id=table_id,
                    catalog_updated=catalog_updated,
                    run_id=run_id,
                    state=state,
                    overrides=overrides,
                    now=now_utc(),
                )
            except Exception as exc:
                result = {
                    "status": "failed",
                    "catalog_updated": catalog_updated,
                    "error": str(exc),
                    "changed_tids": [],
                }
                previous = state["tables"].get(table_id, {})
                frequency = previous.get("frequency", "other")
                next_state = build_table_state(
                    previous,
                    catalog_updated=catalog_updated,
                    frequency=frequency,
                    run_id=run_id,
                    now=now_utc(),
                    status="failed",
                    error=str(exc),
                )

            manifest["tables"][table_id] = result
            state["tables"][table_id] = next_state

        table_results = list(manifest["tables"].values())
        synced = sum(1 for r in table_results if r["status"] == "synced")
        skipped = sum(1 for r in table_results if r["status"] == "skipped")
        failed = sum(1 for r in table_results if r["status"] == "failed")
        changed_tables = sum(1 for r in table_results if r.get("changed_tids"))
        manifest["summary"] = {
            "tables_total": len(table_results),
            "tables_synced": synced,
            "tables_skipped": skipped,
            "tables_failed": failed,
            "tables_with_changed_tids": changed_tables,
        }
        manifest["status"] = "partial_failure" if failed else "success"
        return manifest
    except Exception as exc:
        manifest["status"] = "failed"
        manifest["error"] = str(exc)
        raise
    finally:
        manifest["finished_at"] = iso_utc(now_utc())
        state["last_run_id"] = run_id
        write_run_manifest(run_id, manifest)
        save_state(state)


if __name__ == "__main__":
    run_sync_cycle(force_catalog_poll=True)
