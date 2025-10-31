import httpx
import pandas as pd
from io import StringIO
from create_table_info_dict import get_all_table_ids
import pickle
from tqdm import tqdm
from pathlib import Path
from time import sleep

def get_table_info(table_id):
    with open(f"/root/varro/data/tables_info_raw_da/{table_id}.pkl", "rb") as f:
        table_info = pickle.load(f)
    return table_info


data_dir = Path("/mnt/HC_Volume_103849439/statbank_tables")
already_cloned_table_ids = set(fp.stem for fp in data_dir.glob("*.parquet"))
for table_id in tqdm(get_all_table_ids()):
    if table_id in already_cloned_table_ids:
        continue

    try:
        table_info = get_table_info(table_id)
        get_all_data = [{"code": var["id"], "values": ["*"]} for var in table_info["variables"]]
        r = httpx.post(
            "https://api.statbank.dk/v1/data",
            json={
                "table": table_id,
                "format": "BULK",
                "lang": "da",
                "valuePresentation": "Code",
                "variables": get_all_data,
            },
        )
        df = pd.read_csv(StringIO(r.text), sep=";", decimal=",")
        df.to_parquet(data_dir / f"{table_id}.parquet")

    except:
        sleep(60)
        continue