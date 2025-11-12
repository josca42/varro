import pandas as pd
import httpx
import pickle
from time import sleep
from tqdm import tqdm
from pathlib import Path
import random

HEADER_VARS = ["id", "text", "description", "unit"]


def create_tables_info_dict(data_dir: Path):
    tables_info_dir = data_dir / "tables_info_raw_da"
    fp = data_dir / "tables_info_da.pkl"

    if fp.exists():
        with open(fp, "rb") as f:
            tables_info = pickle.load(f)
    else:
        tables_info = {}


    table_ids = get_all_table_ids()
    i = 0
    for table_id in tqdm(table_ids):
        if table_id in tables_info:
            continue

        try:
            table_info = get_table_info(table_id)
            dump_pickle(tables_info_dir / f"{table_id}.pkl", table_info)

            tables_info[table_id] = create_table_info_dict(table_info)
        except Exception as e:
            print(f"Error getting table info for {table_id}: {e}")
            continue

        sleep(2 + random.random() * 5)
        i += 1
        if i % 50 == 0:
            dump_pickle(fp, tables_info)

    dump_pickle(fp, tables_info)


def dump_pickle(fp: Path, tables_info: dict):
    with open(fp, "wb") as f:
        pickle.dump(tables_info, f)


def get_all_table_ids():
    # Get all tables
    r = httpx.get("https://api.statbank.dk/v1/tables", params={"lang": "da"}).json()
    df_tables = pd.DataFrame(r)
    return df_tables["id"].tolist()


def get_table_info(table_id):
    return httpx.get(
        "https://api.statbank.dk/v1" + "/tableinfo",
        params={"id": table_id, "format": "JSON", "lang": "da"},
        timeout=90,
    ).json()

def create_table_info_dict(table_info):
    info = {v: table_info[v] for v in HEADER_VARS}
    info["dimensions"] = {}
    for var in table_info["variables"]:
        info["dimensions"][var["text"]] = values_text_repr(var["values"])
    return info


def values_text_repr(values):
    if len(values) <= 10:
        values_text = ", ".join([v["text"] for v in values])
    else:
        values_start = ", ".join([v["text"] for v in values[:5]])
        values_end = ", ".join([v["text"] for v in values[-5:]])
        values_text = values_start + " ... " + values_end

    return values_text

if __name__ == "__main__":
    data_dir = Path("/root/varro/data")
    create_tables_info_dict(data_dir)