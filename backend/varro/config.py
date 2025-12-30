from dotenv import dotenv_values, load_dotenv
from pathlib import Path

load_dotenv()
settings = dotenv_values()

DATA_DIR = Path(settings["DATA_DIR"])
DOCS_DIR = Path.home() / "docs"
COLUMN_VALUES_DIR = DOCS_DIR / "column_values"
SUBJECTS_DOCS_DIR = DOCS_DIR / "subjects"
TABLES_DOCS_DIR = DOCS_DIR / "tables"
EVIDENCE_USERS_DIR = DATA_DIR / "dashboards"
MEMORY_DIR = DATA_DIR / "memories"