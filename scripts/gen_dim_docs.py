"""Generate dimension table documentation from database + mapping table descriptions."""
import json
import os
import re
from pathlib import Path

import pandas as pd
from sqlalchemy import text

from varro.db.db import dst_owner_engine
from varro.config import DST_MAPPING_TABLES_DIR, DIM_TABLE_DESCR_DIR, DST_DIMENSION_LINKS_DIR

DIM_TABLE_DESCR_DIR.mkdir(parents=True, exist_ok=True)

RELATED_GROUPS = {
    "ddu_audd": "ddu_udd",
    "ddu_udd": "ddu_audd",
    "disco": "disco_ls",
    "disco_ls": "disco",
    "ecoicop": "ecoicop_dst",
    "ecoicop_dst": "ecoicop",
    "db": "db_10",
    "db_10": "db",
    "lande_psd": ["lande_uht_bb", "lande_uhv"],
    "lande_uht_bb": ["lande_psd", "lande_uhv"],
    "lande_uhv": ["lande_psd", "lande_uht_bb"],
    "icha": "icha_hp",
    "icha_hp": "icha",
}

DESCRIPTIVE_NAMES = {
    "benkod": "Benyttelseskoder",
    "byganv": "Bygningsanvendelse",
    "bygherre": "Bygherrekategorier",
    "cepa": "Miljøbeskyttelsesformål (CEPA)",
    "cofog": "Offentlige udgifter efter formål (COFOG)",
    "crema": "Miljøøkonomiske aktiviteter (CReMA)",
    "db": "Dansk Branchekode 2007 (DB07)",
    "db_10": "Branchekode 10-gruppering (DB07)",
    "ddu_audd": "Igangværende uddannelser (AUDD)",
    "ddu_udd": "Højest fuldførte uddannelser (UDD)",
    "degurba_dst": "Urbaniseringsgrad (DEGURBA)",
    "disco": "Stillingsbetegnelser (DISCO-08)",
    "disco_ls": "Lønstruktur-stillingsbetegnelser (DISCO-08 LS)",
    "ebops": "Tjenestehandel (EBOPS)",
    "ecoicop": "Forbrugsklassifikation (ECOICOP)",
    "ecoicop_dst": "Forbrugsklassifikation, dansk (ECOICOP-DST)",
    "ejendom": "Ejendomskategorier",
    "esa": "Sektorer i nationalregnskabet (ESA)",
    "esr_sekt": "Erhvervsstatistiske sektorer (ESR)",
    "esspros": "Social beskyttelse (ESSPROS)",
    "herkomst": "Herkomst",
    "icha": "Sundhedsregnskaber efter funktion (ICHA-HC)",
    "icha_hp": "Sundhedsregnskaber efter udbyder (ICHA-HP)",
    "kn": "Kombineret Nomenklatur (KN)",
    "kommunegrupper": "Kommunegrupper",
    "kulturemner": "Kulturemner",
    "landbrugslandsdele": "Landbrugslandsdele",
    "lande_psd": "Lande – personstatistik",
    "lande_uht_bb": "Lande – udenrigshandel",
    "lande_uhv": "Lande – udenrigshandel med varer",
    "nr_branche": "Nationalregnskabsbranche (NR)",
    "nst": "Godstransport (NST 2007)",
    "nuts": "Regioner og landsdele (NUTS)",
    "okologisketail": "Økologiske detailtal",
    "overtraedtype": "Overtrædelsestyper",
    "politikredse": "Politikredse",
    "sitc": "Udenrigshandel (SITC)",
    "socio": "Socioøkonomisk status",
    "soc_status": "Social status",
    "valuta_iso": "Valutaer (ISO)",
}

NIVEAU_LABELS = {
    "benkod": {1: "Benyttelseskode"},
    "byganv": {1: "Hovedgruppe", 2: "Undergruppe", 3: "Detailkode"},
    "bygherre": {1: "Hovedkategori", 2: "Underkategori"},
    "cepa": {1: "Hovedgruppe", 2: "Gruppe", 3: "Undergruppe"},
    "cofog": {1: "Hovedgruppe", 2: "Gruppe", 3: "Undergruppe"},
    "crema": {1: "Aktivitet"},
    "db": {2: "Afsnit", 3: "Hovedgruppe", 4: "Gruppe", 5: "Undergruppe"},
    "db_10": {1: "Hovedgruppe (10-gruppering)", 2: "Undergruppe"},
    "ddu_audd": {1: "Hovedområde", 2: "Niveau", 3: "Fagområde", 4: "Retning", 5: "Enkeltuddannelse"},
    "ddu_udd": {1: "Hovedområde", 2: "Niveau", 3: "Fagområde", 4: "Retning", 5: "Enkeltuddannelse"},
    "degurba_dst": {1: "Urbaniseringsgrad", 2: "Kommunetype", 3: "Kommune"},
    "disco": {1: "Hovedgruppe", 2: "Undergruppe", 3: "Enhed", 4: "Stillingskategori", 5: "Stilling"},
    "disco_ls": {1: "Hovedgruppe", 2: "Undergruppe", 3: "Enhed", 4: "Stillingskategori", 5: "Stilling"},
    "ebops": {1: "Hovedgruppe", 2: "Gruppe", 3: "Undergruppe", 4: "Detalje"},
    "ecoicop": {1: "Hovedgruppe", 2: "Gruppe", 3: "Klasse", 4: "Underklasse"},
    "ecoicop_dst": {1: "Hovedgruppe", 2: "Gruppe", 3: "Klasse", 4: "Underklasse", 5: "Detalje"},
    "ejendom": {1: "Hovedkategori", 2: "Underkategori"},
    "esa": {1: "Hovedsektor", 2: "Delsektor", 3: "Undersektor"},
    "esr_sekt": {1: "Hovedsektor", 2: "Delsektor"},
    "esspros": {1: "Hovedfunktion", 2: "Underfunktion"},
    "herkomst": {1: "Herkomsttype"},
    "icha": {1: "Hovedfunktion", 2: "Funktion", 3: "Underfunktion"},
    "icha_hp": {1: "Hovedudbyder", 2: "Udbyder", 3: "Underudbyder"},
    "kn": {1: "Afsnit", 2: "Kapitel", 3: "Position", 4: "Underposition", 5: "Varekode"},
    "kommunegrupper": {1: "Kommunegruppe", 2: "Kommune"},
    "kulturemner": {1: "Hovedemne", 2: "Underemne"},
    "landbrugslandsdele": {1: "Region", 2: "Landsdel", 3: "Landbrugslandsdel", 4: "Kommune"},
    "lande_psd": {1: "Verdensdel", 2: "Region", 3: "Land"},
    "lande_uht_bb": {1: "Verdensdel", 2: "Region", 3: "Underregion", 4: "Land"},
    "lande_uhv": {1: "Verdensdel", 2: "Region", 3: "Underregion", 4: "Land", 5: "Område"},
    "nr_branche": {1: "Hovedbranche", 2: "Branchegruppe", 3: "Branche", 4: "Underbranche", 5: "Detailbranche"},
    "nst": {1: "Hovedgruppe", 2: "Varegruppe"},
    "nuts": {1: "Region", 2: "Landsdel", 3: "Kommune"},
    "okologisketail": {1: "Hovedkategori", 2: "Underkategori"},
    "overtraedtype": {1: "Hovedkategori", 2: "Kategori", 3: "Underkategori", 4: "Overtrædelsestype"},
    "politikredse": {1: "Politikreds", 2: "Kommune"},
    "sitc": {1: "Afdeling", 2: "Gruppe", 3: "Undergruppe"},
    "socio": {1: "Hovedgruppe", 2: "Gruppe", 3: "Undergruppe"},
    "soc_status": {1: "Hovedstatus", 2: "Delstatus", 3: "Understatus"},
    "valuta_iso": {1: "Valuta"},
}


def query_df(sql, params=None):
    with dst_owner_engine.connect() as conn:
        return pd.read_sql_query(text(sql), conn, params=params or {})


def read_table_info(table_id):
    path = DST_MAPPING_TABLES_DIR / table_id / "table_info_da.md"
    if not path.exists():
        return ""
    content = path.read_text()
    content = re.sub(r'^```\s*markdown\s*\n', '', content)
    content = re.sub(r'\n```\s*$', '', content)
    return content.strip()


def extract_description(table_info_text):
    if not table_info_text:
        return ""
    match = re.search(r'(?:#+ *)?Beskrivelse:?\s*\n(.*?)(?:\n#|\n##|\n\*\*Gyldig|\nGyldig|\nKontor|\nKontakt|$)', table_info_text, re.DOTALL)
    if match:
        desc = match.group(1).strip()
        paragraphs = desc.split('\n\n')
        return paragraphs[0].strip() if paragraphs else desc[:300]
    return ""


def get_fact_tables(table_id):
    """Find fact tables that reference this dim table (via column name or dimension links)."""
    # Direct column name match
    df = query_df("""
        SELECT DISTINCT c.table_name
        FROM information_schema.columns c
        WHERE c.table_schema = 'fact' AND c.column_name = :tid
        ORDER BY c.table_name
    """, {"tid": table_id})
    tables = df['table_name'].tolist() if not df.empty else []

    # Also search dimension_links for references
    if DST_DIMENSION_LINKS_DIR.exists():
        for link_file in DST_DIMENSION_LINKS_DIR.glob("*.json"):
            for link in json.loads(link_file.read_text()):
                if link["dimension"] == table_id:
                    ft = link_file.stem.lower()
                    if ft not in tables:
                        tables.append(ft)

    return sorted(tables)


def get_fact_column_for_dim(dim_table_id, fact_tables):
    """Look up the actual fact column name from dimension_links JSON files."""
    for ft in fact_tables:
        link_path = DST_DIMENSION_LINKS_DIR / f"{ft.upper()}.json"
        if not link_path.exists():
            continue
        for link in json.loads(link_path.read_text()):
            if link["dimension"] == dim_table_id:
                return link["column"].lower()
    return dim_table_id


def get_niveau_counts(table_id):
    df = query_df(f"SELECT niveau, COUNT(*) as cnt FROM dim.{table_id} GROUP BY niveau ORDER BY niveau")
    return list(df.itertuples(index=False, name=None))


def get_niveau_data(table_id, niveau, limit=None):
    sql = f"SELECT kode, titel FROM dim.{table_id} WHERE niveau = :niv ORDER BY kode"
    if limit:
        sql += f" LIMIT {limit}"
    return query_df(sql, {"niv": niveau})


def get_hierarchy_example(table_id, niveaux):
    if len(niveaux) <= 1:
        return pd.DataFrame()
    max_niv = max(n for n, _ in niveaux)
    leaf = query_df(f"""
        SELECT kode, niveau, titel, parent_kode
        FROM dim.{table_id}
        WHERE niveau = :niv AND parent_kode IS NOT NULL
        ORDER BY kode
        LIMIT 1
    """, {"niv": max_niv})
    if leaf.empty:
        return pd.DataFrame()

    rows = [leaf.iloc[0].to_dict()]
    current_parent = rows[0]['parent_kode']
    for niv in sorted([n for n, _ in niveaux], reverse=True)[1:]:
        if current_parent is None:
            break
        parent = query_df(f"""
            SELECT kode, niveau, titel, parent_kode
            FROM dim.{table_id}
            WHERE kode = :kode AND niveau = :niv
            LIMIT 1
        """, {"kode": current_parent, "niv": niv})
        if parent.empty:
            parent = query_df(f"""
                SELECT kode, niveau, titel, parent_kode
                FROM dim.{table_id}
                WHERE kode = :kode
                ORDER BY niveau
                LIMIT 1
            """, {"kode": current_parent})
        if not parent.empty:
            rows.append(parent.iloc[0].to_dict())
            current_parent = parent.iloc[0]['parent_kode']
        else:
            break

    rows.reverse()
    return pd.DataFrame(rows)


def fmt_val(v):
    if pd.isna(v):
        return "NULL"
    if isinstance(v, float) and v == int(v):
        return str(int(v))
    return str(v)


def format_table(df, columns):
    if df.empty:
        return ""
    header = " | ".join(columns)
    sep = " | ".join("---" for _ in columns)
    lines = [header, sep]
    for _, row in df.iterrows():
        lines.append(" | ".join(fmt_val(row.get(c, "")) for c in columns))
    return "\n".join(lines)


def gen_aggregation_sql(table_id, niveaux, fact_table=None, fact_col=None):
    sorted_nivs = sorted([n for n, _ in niveaux])
    if len(sorted_nivs) <= 1:
        return ""
    labels = NIVEAU_LABELS.get(table_id, {})
    ft = fact_table or f"<fact_tabel>"
    fc = fact_col or table_id
    max_niv = sorted_nivs[-1]
    min_niv = sorted_nivs[0]

    alias_names = ["detail", "mid", "mid2", "mid3", "top"]
    aliases = []
    join_lines = []

    for i, niv in enumerate(reversed(sorted_nivs)):
        if i == 0:
            alias = "detail"
            aliases.append((alias, niv))
            join_lines.append(
                f"JOIN dim.{table_id} {alias} ON f.{fc} = {alias}.kode AND {alias}.niveau = {niv}"
            )
        else:
            if niv == min_niv:
                alias = "top"
            elif i == 1:
                alias = "mid"
            else:
                alias = f"mid{i}"
            prev_alias = aliases[-1][0]
            aliases.append((alias, niv))
            join_lines.append(
                f"JOIN dim.{table_id} {alias} ON {alias}.kode = {prev_alias}.parent_kode AND {alias}.niveau = {niv}"
            )

    joins = "\n".join(f"  {l}" for l in join_lines)
    return f"""```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.{ft} f
{joins}
GROUP BY top.titel
```"""


def generate_full_doc(table_id):
    name = DESCRIPTIVE_NAMES.get(table_id, table_id)
    table_info = read_table_info(table_id)
    description = extract_description(table_info)
    if not description:
        description = f"Dimensionstabel for {name.lower()}."

    niveaux = get_niveau_counts(table_id)
    labels = NIVEAU_LABELS.get(table_id, {})
    fact_tables = get_fact_tables(table_id)
    fact_example = fact_tables[0] if fact_tables else "<fact_tabel>"
    fact_col = get_fact_column_for_dim(table_id, fact_tables) if fact_tables else table_id
    max_niv = max(n for n, _ in niveaux) if niveaux else 1
    min_niv = min(n for n, _ in niveaux) if niveaux else 1

    lines = []
    lines.append(f"# {name} ({table_id})")
    lines.append("")
    lines.append(description)
    lines.append("")

    # Struktur
    lines.append("## Struktur")
    lines.append("")
    lines.append("Niveau | Beskrivelse | Antal kategorier")
    lines.append("--- | --- | ---")
    for niv, cnt in niveaux:
        label = labels.get(niv, f"Niveau {niv}")
        lines.append(f"{niv} | {label} | {cnt}")
    lines.append("")

    # Niveau 1 (or min niveau for tables like db)
    niv1_data = get_niveau_data(table_id, min_niv)
    lines.append(f"## Niveau {min_niv} — {labels.get(min_niv, 'Topniveau')}")
    lines.append("")
    lines.append("kode | titel")
    lines.append("--- | ---")
    for _, row in niv1_data.iterrows():
        lines.append(f"{row['kode']} | {row['titel']}")
    lines.append("")

    # Also show niveau 2 if <15 categories
    niv2_count = next((cnt for n, cnt in niveaux if n == min_niv + 1), 0)
    if niv2_count > 0 and niv2_count < 15:
        niv2_data = get_niveau_data(table_id, min_niv + 1)
        niv2_label = labels.get(min_niv + 1, f"Niveau {min_niv + 1}")
        lines.append(f"## Niveau {min_niv + 1} — {niv2_label}")
        lines.append("")
        lines.append("kode | titel | parent_kode")
        lines.append("--- | --- | ---")
        for _, row in niv2_data.iterrows():
            # get parent
            parent_df = query_df(f"SELECT parent_kode FROM dim.{table_id} WHERE kode = :k AND niveau = :n LIMIT 1",
                                 {"k": row['kode'], "n": min_niv + 1})
            pk = fmt_val(parent_df.iloc[0]['parent_kode']) if not parent_df.empty else "NULL"
            lines.append(f"{row['kode']} | {row['titel']} | {pk}")
        lines.append("")

    # Hierarki-eksempel
    if max_niv > min_niv:
        hier = get_hierarchy_example(table_id, niveaux)
        if not hier.empty:
            lines.append("## Hierarki-eksempel")
            lines.append("")
            lines.append(format_table(hier, ["kode", "niveau", "titel", "parent_kode"]))
            lines.append("")

    # Brug
    lines.append("## Brug")
    lines.append("")
    lines.append("Simpel join:")
    lines.append("")
    lines.append(f"""```sql
SELECT f.indhold, d.titel
FROM fact.{fact_example} f
JOIN dim.{table_id} d ON f.{fact_col} = d.kode
WHERE d.niveau = {min_niv}
```""")
    lines.append("")

    if max_niv > min_niv:
        lines.append("Aggregering via parent_kode (fra fineste til groveste niveau):")
        lines.append("")
        lines.append(gen_aggregation_sql(table_id, niveaux, fact_example, fact_col))
        lines.append("")

    # Cross-references
    related = RELATED_GROUPS.get(table_id)
    if related:
        lines.append("## Relaterede tabeller")
        lines.append("")
        if isinstance(related, list):
            for r in related:
                rname = DESCRIPTIVE_NAMES.get(r, r)
                lines.append(f"- **{r}**: {rname}")
        else:
            rname = DESCRIPTIVE_NAMES.get(related, related)
            lines.append(f"- **{related}**: {rname}")
        lines.append("")

    return "\n".join(lines)


def generate_short_doc(table_id):
    name = DESCRIPTIVE_NAMES.get(table_id, table_id)
    table_info = read_table_info(table_id)
    description = extract_description(table_info)
    if not description:
        description = f"Dimensionstabel for {name.lower()}."
    # Keep first sentence — avoid splitting on abbreviations/numbers like "1. januar"
    first_sentence = re.split(r'(?<=[a-zæøå])[.!?]\s', description)[0]
    if not first_sentence.endswith(('.', '!', '?')):
        # Re-add the period if we split on it
        first_sentence = first_sentence.rstrip() + "."
    if len(first_sentence) > 250:
        first_sentence = first_sentence[:247] + "..."

    niveaux = get_niveau_counts(table_id)
    labels = NIVEAU_LABELS.get(table_id, {})
    max_niv = max(n for n, _ in niveaux) if niveaux else 1

    lines = []
    lines.append(f"# {name} ({table_id})")
    lines.append("")
    lines.append(first_sentence)
    lines.append("")

    for niv, cnt in niveaux:
        label = labels.get(niv, f"Niveau {niv}")
        examples = get_niveau_data(table_id, niv, limit=3)
        ex_titles = ", ".join(examples['titel'].tolist())
        lines.append(f"- **Niveau {niv}:** {label} ({cnt}, fx {ex_titles})")

    if max_niv > min(n for n, _ in niveaux):
        lines.append(f"- **parent_kode:** peger på direkte forældreniveau (NULL for topniveau). Brug parent_kode-joins til at aggregere fra lavere til højere niveau.")

    return "\n".join(lines)


def main():
    tables = query_df("""
        SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'dim' ORDER BY table_name
    """)

    for table_id in tables['table_name']:
        print(f"Generating docs for {table_id}...")
        try:
            full = generate_full_doc(table_id)
            (DIM_TABLE_DESCR_DIR / f"{table_id}.md").write_text(full)

            short = generate_short_doc(table_id)
            (DIM_TABLE_DESCR_DIR / f"{table_id}_short.md").write_text(short)

            print(f"  ✓ {table_id}")
        except Exception as e:
            print(f"  ✗ {table_id}: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
