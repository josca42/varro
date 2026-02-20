from dotenv import dotenv_values, load_dotenv
from pathlib import Path

load_dotenv()
settings = dotenv_values()

DATA_DIR = Path(settings["DATA_DIR"])
CONTEXT_DIR = Path(settings["CONTEXT_DIR"])
COLUMN_VALUES_DIR = CONTEXT_DIR / "column_values"
SUBJECTS_DIR = CONTEXT_DIR / "subjects"
FACTS_DIR = CONTEXT_DIR / "fact"
DIMS_DIR = CONTEXT_DIR / "dim"
GEO_DIR = CONTEXT_DIR / "geo"
DIM_TABLE_DESCR_DIR = DATA_DIR / "dst" / "dim_table_descr"
TRAJECTORIES_DIR = DATA_DIR / "trajectory"
USER_WORKSPACE_INIT_DIR = Path(__file__).parent / "user_workspace"
