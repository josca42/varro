from dotenv import dotenv_values, load_dotenv
from pathlib import Path

load_dotenv()
settings = dotenv_values()

DATA_DIR = Path(settings["DATA_DIR"])
DOCS_DIR = DATA_DIR / "docs"
COLUMN_VALUES_DIR = DOCS_DIR / "column_values"
SUBJECTS_DIR = DATA_DIR / "subjects"
FACTS_DIR = DATA_DIR / "facts"
DIMS_DIR = DATA_DIR / "dims"
DIM_TABLE_DESCR_DIR = DATA_DIR / "dim_table_descr"
MEMORY_DIR = DATA_DIR / "memories"
