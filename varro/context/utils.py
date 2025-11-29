import json
from varro.config import DATA_DIR
from rapidfuzz import process
import pandas as pd

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


def fuzzy_match(fp: str, query: str, limit: int = 5) -> str:
    df = pd.read_parquet(fp)
    search_results = process.extract(query, df["text"], limit=limit)
    matches = []
    for choice, similarity, index in search_results:
        matches.append(
            {
                "id": df.iloc[index]["id"],
                "label": choice,
            }
        )
    return matches


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
