from dotenv import dotenv_values, load_dotenv
from pathlib import Path

load_dotenv()
settings = dotenv_values()

DATA_DIR = Path(settings["DATA_DIR"])
DOCS_DIR = Path("root/docs")
COLUMN_VALUES_DIR = DATA_DIR / "column_values"
SUBJECTS_DIR = DOCS_DIR / "subjects"
FACTS_DIR = DOCS_DIR / "fact"
DIMS_DIR = DOCS_DIR / "dim"
GEO_DIR = DOCS_DIR / "geo"
DIM_TABLE_DESCR_DIR = DATA_DIR / "dst" / "dim_table_descr"
TRAJECTORIES_DIR = DATA_DIR / "trajectory"
USER_WORKSPACE_INIT_DIR = Path(__file__).parent / "user_workspace_init"
