import argparse
import io
import re
import httpx
import pandas as pd
from pathlib import Path
from typing import Literal

data_dir = Path("/mnt/HC_Volume_103849439/mapping_tables")


def get_cat_table_data(url_descr: str, url_csv: str):
    table_name = url_descr.split("/")[-1].replace("-", "_")
    table_dir = data_dir / table_name
    table_dir.mkdir(parents=True, exist_ok=True)

    # Danish dumps
    try:
        dump_cat_table_description_as_markdown(url_descr, table_dir, "da")
    except Exception as e:
        print(f"Error dumping table description for {table_name} in Danish: {e}")
    else:
        try:
            dump_cat_table_csv(url_csv, table_dir, "da")
        except Exception as e:
            print(f"Error dumping CSV for {table_name} in Danish: {e}")

    # English dumps
    try:
        url_descr_en = url_descr.replace("/da/", "/en/")
        url_csv_en = url_csv.replace("csv_da", "csv_en")
        dump_cat_table_description_as_markdown(url_descr_en, table_dir, "en")
    except Exception as e:
        print(f"Error dumping table description for {table_name} in English: {e}")
    else:
        try:
            dump_cat_table_csv(url_csv_en, table_dir, "en")
        except Exception as e:
            print(f"Error dumping CSV for {table_name} in English: {e}")


def dump_cat_table_description_as_markdown(
    url: str, table_dir: str, lang: Literal["da", "en"]
):
    jina_url = "https://r.jina.ai/"
    headers = {
        "Authorization": "Bearer jina_f43e37353e164d3e8be83e005c322f995CHs0jLHp4t-ETQX0GRGccW_vdQo",
        "Content-Type": "application/json",
        "DNT": "1",
        "X-Engine": "browser",
        "X-Respond-With": "readerlm-v2",
        "X-Return-Format": "markdown",
        "X-Target-Selector": ".classificationheading",
    }
    data = {"url": url}
    response = httpx.post(jina_url, headers=headers, json=data, timeout=60 * 10)
    with open(table_dir / f"table_info_{lang}.md", "w") as f:
        f.write(response.text)


def dump_cat_table_csv(url: str, table_dir: str, lang: Literal["da", "en"]):
    assert lang in ["da", "en"], "Language must be either da or en"

    def _fetch_csv_text(u: str) -> str:
        with httpx.Client(follow_redirects=True, timeout=60) as client:
            r = client.get(u)
            r.raise_for_status()
            txt = r.text
            # Some endpoints return an HTML page with a manual redirect link
            if "Object moved" in txt and 'href="/Site/Dst/SingleFiles/' in txt:
                m = re.search(r"href=\"(\/Site\/Dst\/SingleFiles\/[^\"]+)", txt)
                if m:
                    new_url = "https://www.dst.dk" + m.group(1)
                    r = client.get(new_url)
                    r.raise_for_status()
                    return r.content.decode("utf-8-sig", errors="replace")
            # Normal path: treat response as CSV regardless of content-type
            return r.content.decode("utf-8-sig", errors="replace")

    csv_text = _fetch_csv_text(url)
    df = pd.read_csv(io.StringIO(csv_text), sep=";", decimal=",")
    df.to_parquet(table_dir / f"table_{lang}.parquet")


def _cli():
    parser = argparse.ArgumentParser(
        description="Download classification page markdown and CSV (as parquet).",
    )
    parser.add_argument(
        "--page",
        dest="page",
        help="Classification page URL (url_descr)",
    )
    parser.add_argument(
        "--csv",
        dest="csv",
        help="CSV download URL (url_csv)",
    )
    parser.add_argument(
        "--data-dir",
        dest="data_dir",
        default=None,
        help="Override output data directory (defaults to /mnt/HC_Volume_103849439/mapping_tables)",
    )

    args = parser.parse_args()

    global data_dir
    if args.data_dir:
        data_dir = Path(args.data_dir)

    if not args.page or not args.csv:
        parser.error("--page and --csv are required")

    get_cat_table_data(args.page, args.csv)


if __name__ == "__main__":
    _cli()
