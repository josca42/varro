import httpx
import numpy as np
import pandas as pd
from io import StringIO
from create_table_info_dict import get_all_table_ids
import pickle
from tqdm import tqdm
from pathlib import Path
from time import sleep
from varro.config import DATA_DIR

TABLES_INFO_DIR = DATA_DIR / "metadata" / "tables_info_raw_da"
MAX_TOTAL_ROWS = 100_000_000
MAX_ROWS_PER_CALL = 50_000_000


def get_table_info(table_id):
    with open(TABLES_INFO_DIR / f"{table_id}.pkl", "rb") as f:
        table_info = pickle.load(f)
    return table_info


def build_variables_payload(table_info, time_values=None):
    payload = []
    for var in table_info["variables"]:
        values = ["*"]
        if time_values is not None and var["id"] == "Tid":
            values = time_values
        payload.append({"code": var["id"], "values": values})
    return payload


def get_time_partitions(table_info, total_rows):
    time_var = next(
        (var for var in table_info["variables"] if var["id"] == "Tid"), None
    )
    if not time_var:
        return None
    time_values = time_var["values"] or []
    if not time_values:
        return None
    rows_per_time = max(1, int(np.ceil(total_rows / len(time_values))))
    max_time_values_per_call = max(1, MAX_ROWS_PER_CALL // rows_per_time)
    time_ids = [
        value["id"] if isinstance(value, dict) else value for value in time_values
    ]
    partitions = [
        time_ids[i : i + max_time_values_per_call]
        for i in range(0, len(time_ids), max_time_values_per_call)
    ]
    return partitions


def copy_table(table_id, variables):
    r = httpx.post(
        "https://api.statbank.dk/v1/data",
        json={
            "table": table_id,
            "format": "BULK",
            "lang": "da",
            "valuePresentation": "Code",
            "variables": variables,
        },
        # timeout=60 * 10,
    )
    df = pd.read_csv(StringIO(r.text), sep=";", decimal=",", low_memory=False)
    return df


data_dir = Path("/mnt/HC_Volume_103849439/statbank_tables")
already_cloned_table_ids = set(fp.stem for fp in data_dir.glob("*.parquet"))
for table_id in tqdm(get_all_table_ids()):
    if table_id in already_cloned_table_ids:
        continue

    try:
        table_info = get_table_info(table_id)
        total_rows = int(
            np.prod([len(var["values"]) for var in table_info["variables"]])
        )
        partitions = None
        if total_rows > MAX_TOTAL_ROWS:
            partitioned_times = get_time_partitions(table_info, total_rows)
            if partitioned_times:
                partitions = partitioned_times

        if partitions is None:
            variables = build_variables_payload(table_info, time_values=None)
            df = copy_table(table_id, variables)
            df.to_parquet(data_dir / f"{table_id}.parquet")
        else:
            df_folder = data_dir / f"{table_id}"
            df_folder.mkdir(parents=True, exist_ok=True)
            for i, time_values in enumerate(partitions):
                variables = build_variables_payload(table_info, time_values=time_values)
                df = copy_table(table_id, variables)

                df.to_parquet(df_folder / f"partition_{i}.parquet")

    except:
        print(f"Error copying table {table_id}")
        sleep(60 * 10)
        continue
