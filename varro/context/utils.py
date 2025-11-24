import json
from varro.config import DATA_DIR

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
