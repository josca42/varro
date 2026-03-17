import json
import math
import pickle
import re
from io import StringIO
from pathlib import Path
from time import sleep
from urllib.parse import quote, unquote
from uuid import uuid4

import httpx
import pandas as pd

from varro.config import DST_METADATA_DIR, DST_STATBANK_TABLES_DIR, settings

TABLES_INFO_DIR = DST_METADATA_DIR / "tables_info_raw_da"
FACT_TABLES_DIR = DST_STATBANK_TABLES_DIR
SYNC_DIR = FACT_TABLES_DIR / "_sync"
STATE_FP = SYNC_DIR / "state.json"
FREQUENCY_OVERRIDES_FP = SYNC_DIR / "frequency_overrides.json"
MAX_ROWS_PER_CALL = 50_000_000
DST_API_SLEEP_SECONDS = float(settings.get("DST_API_SLEEP_SECONDS", "30"))

LAG_WINDOWS = {
    "daily": 7,
    "weekly": 4,
    "monthly": 3,
    "quarterly": 2,
    "half_yearly": 2,
    "yearly": 2,
    "other": 2,
}

YEARLY_RE = re.compile(r"^\d{4}$")
QUARTERLY_RE = re.compile(r"^\d{4}K[1-4]$")
MONTHLY_RE = re.compile(r"^\d{4}M\d{2}$")
WEEKLY_RE = re.compile(r"^\d{4}U\d{2}$")
DAILY_RE = re.compile(r"^\d{4}M\d{2}D\d{2}$")
HALF_YEARLY_RE = re.compile(r"^\d{4}H[12]$")


def chunk(values: list[str], size: int) -> list[list[str]]:
    return [values[i : i + size] for i in range(0, len(values), size)]


def ensure_dirs() -> None:
    TABLES_INFO_DIR.mkdir(parents=True, exist_ok=True)
    FACT_TABLES_DIR.mkdir(parents=True, exist_ok=True)
    SYNC_DIR.mkdir(parents=True, exist_ok=True)


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


def load_state() -> dict:
    if not STATE_FP.exists():
        return {}
    return json.loads(STATE_FP.read_text())


def save_state(state: dict) -> None:
    write_json_atomic(STATE_FP, state)


def load_frequency_overrides() -> dict[str, str]:
    if not FREQUENCY_OVERRIDES_FP.exists():
        return {}
    raw = json.loads(FREQUENCY_OVERRIDES_FP.read_text())
    return {
        table_id: freq
        for table_id, freq in raw.items()
        if freq in LAG_WINDOWS
    }


def statbank_request(method: str, url: str, **kwargs) -> httpx.Response:
    request = getattr(httpx, method)
    try:
        return request(url, **kwargs)
    finally:
        if DST_API_SLEEP_SECONDS > 0:
            sleep(DST_API_SLEEP_SECONDS)


def fetch_catalog() -> list[dict]:
    response = statbank_request(
        "get",
        "https://api.statbank.dk/v1/tables",
        params={"lang": "da"},
        timeout=120,
    )
    response.raise_for_status()
    return sorted(response.json(), key=lambda row: row["id"])


def fetch_table_info(table_id: str) -> dict:
    response = statbank_request(
        "get",
        "https://api.statbank.dk/v1/tableinfo",
        params={"id": table_id, "format": "JSON", "lang": "da"},
        timeout=120,
    )
    response.raise_for_status()
    table_info = response.json()
    if table_info.get("errorTypeCode"):
        raise RuntimeError(f"{table_info['errorTypeCode']}: {table_info.get('message', '')}")
    if not isinstance(table_info.get("variables"), list):
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
    response = statbank_request(
        "post",
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
) -> list[str]:
    local_set = set(local_tids)
    bootstrap = len(local_tids) == 0

    if bootstrap:
        return remote_tids

    new_periods = [tid for tid in remote_tids if tid not in local_set]
    lag_periods = remote_tids[-LAG_WINDOWS[frequency] :]
    target_set = set(new_periods) | set(lag_periods)
    return [tid for tid in remote_tids if tid in target_set]


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
