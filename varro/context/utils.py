import json
from varro.config import DATA_DIR
from varro.data.utils import df_preview
from rapidfuzz import process
import pandas as pd
from pathlib import Path

DIM_LINKS_DIR = DATA_DIR / "dimension_links"


def load_dimension_links(table_id: str) -> dict[str, str] | None:
    path = DIM_LINKS_DIR / f"{table_id}.json"
    if not path.exists():
        return None
    entries = json.loads(path.read_text())
    links: dict[str, str] = {}
    for entry in entries or []:
        col = normalize_fact_col_name(entry["column"])
        links[col] = entry["dimension"].strip().lower()
    return links or None


def normalize_fact_col_name(name: str) -> str:
    return name.lower().replace("å", "a").replace("ø", "o").replace("æ", "ae")


def fuzzy_match(
    query: str, df: pd.DataFrame, limit: int = 5, schema: str = "fact", name: str = "df"
) -> str:
    if schema == "fact":
        col = "text"
        id_col = "id"
        label_name = "label"
    elif schema == "dim":
        col = "titel"
        id_col = "kode"
        label_name = "titel"
    else:
        raise ValueError(f"Invalid schema: {schema}")

    search_results = process.extract(query, df[col], limit=limit)
    matches = []
    for choice, similarity, index in search_results:
        matches.append(
            {
                id_col: df.iloc[index][id_col],
                label_name: choice,
            }
        )
    return df_preview(pd.DataFrame(matches), max_rows=limit, name=name)


FACT_TABLES_NOT_IN_DB = [
    "fam44ba",
    "kas302",
    "kas310",
    "lons20",
    "nasd21",
    "vnasfk",
    "vnksfk",
    "bbm",
    "vuhm",
    "kn8m",
    "dnruupi",
    "dnvpdkr2",
    "barsel05",
    "barsel24",
    "und3",
    "hfudd11",
    "hfudd21",
    "uddall10",
    "inst10",
    "kveu20",
    "afg5",
    "dnpud",
    "dnruddks",
    "dnifhvem",
    "dnifinve",
    "aftryk2",
]
