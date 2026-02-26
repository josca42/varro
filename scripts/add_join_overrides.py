"""
Reads dimension link JSONs with notes containing known transformation patterns
and adds join_override fields where applicable.
"""

import json
import re
from pathlib import Path

DIM_LINKS_DIR = Path("data/dst/dimension_links")

PATTERNS = [
    {
        "match": re.compile(r"[Vv] prefix.*needs? stripping|[Ss]trip V prefix|prefixed with V", re.IGNORECASE),
        "override": lambda col: f"REPLACE({col}, 'V', '')=kode::text",
    },
    {
        "match": re.compile(r"no spaces.*uses spaces|uses no spaces.*uses spaces", re.IGNORECASE),
        "override": lambda col: f"{col}=REPLACE(kode, ' ', '')",
    },
]


def add_overrides():
    updated = 0
    for path in sorted(DIM_LINKS_DIR.glob("*.json")):
        with open(path) as f:
            links = json.load(f)

        changed = False
        for link in links:
            note = link.get("note", "")
            if not note or link.get("join_override"):
                continue
            for pattern in PATTERNS:
                if pattern["match"].search(note):
                    col = link["column"].lower()
                    link["join_override"] = pattern["override"](col)
                    changed = True
                    break

        if changed:
            with open(path, "w") as f:
                json.dump(links, f, indent=2, ensure_ascii=False)
            updated += 1
            print(f"Updated {path.name}: {[l.get('join_override') for l in links if l.get('join_override')]}")

    print(f"\nTotal files updated: {updated}")


if __name__ == "__main__":
    add_overrides()
