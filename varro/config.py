from dotenv import dotenv_values, load_dotenv
from pathlib import Path

load_dotenv()
settings = dotenv_values()

DATA_DIR = Path(settings["DATA_DIR"])
DOCS_DIR = DATA_DIR / "docs_template"
COLUMN_VALUES_DIR = DATA_DIR / "column_values"
SUBJECTS_DIR = DOCS_DIR / "subjects"
FACTS_DIR = DOCS_DIR / "fact"
DIMS_DIR = DOCS_DIR / "dim"
SUBJECTS_DOCS_DIR = SUBJECTS_DIR
TABLES_DOCS_DIR = FACTS_DIR
DIM_TABLE_DESCR_DIR = DATA_DIR / "dim_table_descr"
