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
    print(f"Processing {k}")

    if k == "Arbejde og indkomst/Indkomst og løn/Person- og familieindkomster":
        continue
    table_ids = [table_id for table_id in v if table_id not in dim_links_created]
    if not table_ids:
        continue

    if len(table_ids) > 7:
        chunks = [table_ids[i : i + 7] for i in range(0, len(table_ids), 7)]
    else:
        chunks = [table_ids]

    for chunk in chunks:
        subject_name = k.lower().replace("/", "_")
        prompt = crud.prompt.render_prompt(
            name="link_dimensions",
            table_ids=chunk,
            subject_name=subject_name,
        )

        proc = subprocess.run(
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

    print(f"Created links for {k}")
    sleep(5 * 60)
