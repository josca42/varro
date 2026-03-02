"""Run the audit-dim-joins skill on each subject file via claude CLI."""

import subprocess
from pathlib import Path
from varro.config import SUBJECTS_DIR
import time
import json

DONE_PATH = Path("varro/context/audit_done_subjects.json")


def all_subject_files() -> list[Path]:
    return sorted(SUBJECTS_DIR.rglob("*.md"))


def load_done() -> list[str]:
    if DONE_PATH.exists():
        return json.loads(DONE_PATH.read_text())
    return []


def save_done(done: list[str]):
    DONE_PATH.write_text(json.dumps(done, indent=2))


def main():
    subjects = all_subject_files()
    done = load_done()
    done_set = set(done)
    to_run = [s for s in subjects if str(s) not in done_set]

    print(f"Subjects: {len(subjects)} total, {len(done)} done, {len(to_run)} remaining")

    for i, subject_file in enumerate(to_run):
        rel = subject_file.relative_to(SUBJECTS_DIR)
        print(f"\n[{i + 1}/{len(to_run)}] {rel}")

        prompt = f"/add-map-notes Review this subject file and add notes: {subject_file}"

        subprocess.run(
            [
                "claude",
                "-p", prompt,
                "--allowedTools",
                "Bash Read Write Grep Edit",
                "--permission-mode",
                "acceptEdits",
            ],
            check=True,
        )

        done.append(str(subject_file))
        save_done(done)
        print(f"Done: {rel}")
        time.sleep(60 * 5)

if __name__ == "__main__":
    main()