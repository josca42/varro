import json
import subprocess
from time import sleep
from pathlib import Path
from varro.db import crud

with open("/root/varro/agents/notes/subject_tables_dict.json", "r") as f:
    subject_tables_dict = json.load(f)

DIM_LINKS_DIR = Path("/mnt/HC_Volume_103849439/dimension_links")
dim_links_created = set(fp.stem for fp in DIM_LINKS_DIR.glob("*.json"))


for k, v in subject_tables_dict.items():
    table_ids = [table_id for table_id in v if table_id not in dim_links_created]
    if not table_ids:
        continue

    prompt = crud.prompt.render_prompt(
        name="link_dimensions_prompt",
        table_ids=table_ids,
        subject_name=k.replace("/", " "),
    )
    subprocess.run(["claude", "-p", prompt], check=True)
    sleep(5 * 60)
