import json
import subprocess
from jinja2 import Environment, FileSystemLoader
from time import sleep

with open("/root/varro/agents/notes/subject_tables_dict.json", "r") as f:
    subject_tables_dict = json.load(f)


template = Environment(loader=FileSystemLoader("/root/varro/scripts")).get_template(
    "link_dimensions_prompt.j2"
)

for k, v in subject_tables_dict.items():
    prompt = template.render(table_ids=v, subject_name=k.replace("/", " "))
    subprocess.run(["claude", "-p", prompt], check=True)
    sleep(10 * 60)
