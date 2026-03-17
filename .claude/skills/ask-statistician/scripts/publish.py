from __future__ import annotations

import argparse

from varro.config import DATA_DIR
from varro.dashboard.public_fs import copy_dashboard_source, public_dashboard_dir


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", required=True)
    parser.add_argument("--user-id", type=int, default=1)
    args = parser.parse_args()

    src = DATA_DIR / "user" / str(args.user_id) / "dashboard" / args.slug
    if not (src / "dashboard.md").exists():
        print(f"error: dashboard '{args.slug}' not found at {src}")
        raise SystemExit(1)

    dst = public_dashboard_dir(DATA_DIR, args.user_id, args.slug)
    copy_dashboard_source(src, dst)
    print(f"url: https://varro.dk/public/{args.user_id}/{args.slug}")


if __name__ == "__main__":
    main()
