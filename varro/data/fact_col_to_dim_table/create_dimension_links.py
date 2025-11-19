import json
import subprocess
from time import sleep
from pathlib import Path
from varro.db import crud
from varro.config import DATA_DIR

DIM_LINKS_DIR = DATA_DIR / "dimension_links"
with open("/root/varro/agents/notes/subject_tables_dict.json", "r") as f:
    subject_tables_dict = json.load(f)

dim_links_created = set(fp.stem for fp in DIM_LINKS_DIR.glob("*.json"))


for k, v in subject_tables_dict.items():
    table_ids = [table_id for table_id in v if table_id not in dim_links_created]
    if not table_ids:
        continue

    subject_name = k.lower().replace("/", "_")
    prompt = crud.prompt.render_prompt(
        name="link_dimensions",
        table_ids=table_ids,
        subject_name=subject_name,
    )
    subprocess.run(
        [
            "claude",
            "-p",
            prompt,
            "--allowedTools",
            "Bash Read Write Grep",
            "--permission-mode",
            "acceptEdits",
        ],
        check=True,
    )
    sleep(5 * 60)
