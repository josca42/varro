import pandas as pd
import httpx
import pickle
from time import sleep
from tqdm import tqdm
from pathlib import Path
import random
from varro.config import DST_METADATA_DIR

HEADER_VARS = ["id", "text", "description", "unit"]


def get_table_info_and_save(data_dir: Path):
    tables_info_dir = data_dir / "tables_info_raw_da"
    table_ids = get_all_table_ids()
    i = 0
    for table_id in tqdm(table_ids):
        fp = tables_info_dir / f"{table_id}.pkl"
        if fp.exists():
            continue

        try:
            table_info = get_table_info(table_id)
            with open(fp, "wb") as f:
                pickle.dump(table_info, f)
        except Exception as e:
            print(f"Error getting table info for {table_id}: {e}")
            continue


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


if __name__ == "__main__":
    data_dir = DST_METADATA_DIR
    get_table_info_and_save(data_dir)
