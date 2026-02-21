from dotenv import dotenv_values, load_dotenv
from pathlib import Path

load_dotenv()
settings = dotenv_values()

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _resolve_path(value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return PROJECT_ROOT / path


DATA_DIR = _resolve_path(settings["DATA_DIR"])
CONTEXT_DIR = _resolve_path(settings["CONTEXT_DIR"])

DST_DIR = DATA_DIR / "dst"
DST_METADATA_DIR = DST_DIR / "metadata"
DST_MAPPING_TABLES_DIR = DST_DIR / "mapping_tables"
DST_STATBANK_TABLES_DIR = DST_DIR / "statbank_tables"
DST_DIMENSION_LINKS_DIR = DST_DIR / "dimension_links"

COLUMN_VALUES_DIR = CONTEXT_DIR / "column_values"
SUBJECTS_DIR = CONTEXT_DIR / "subjects"
FACTS_DIR = CONTEXT_DIR / "fact"
DIMS_DIR = CONTEXT_DIR / "dim"
GEO_DIR = CONTEXT_DIR / "geo"
DIM_TABLE_DESCR_DIR = DST_DIR / "dim_table_descr"
TRAJECTORIES_DIR = DATA_DIR / "trajectory"
USER_WORKSPACE_INIT_DIR = Path(__file__).parent / "user_workspace"
