table: fact.straf11
description: Anmeldte forbrydelser efter område, overtrædelsens art og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx: Missing codes: 0, 998]; levels [1, 3]
- overtraed: join dim.overtraedtype on overtraed=kode::text [approx: Fact col is string, dim KODE is int64. Also has TOT placeholder.]; levels [1, 2, 3]
- tid: date range 2007-01-01 to 2025-07-01
dim docs: /dim/nuts.md, /dim/overtraedtype.md

notes:
- omrade joins dim.nuts. Only niveau 1 (5 regioner) and niveau 3 (99 kommuner) are present — niveau 2 (landsdele) is not. Filter `WHERE d.niveau = 1` or `WHERE d.niveau = 3` to pick granularity and avoid double-counting.
- omrade=0 is the national total (Hele landet) — confirmed to match straf10 values. Exclude it when doing regional analysis.
- omrade=998 is an unassigned/unknown location category — not a real region. Exclude it for geographic queries.
- overtraed joins dim.overtraedtype via `f.overtraed = d.kode::text`. Niveaux 1, 2, 3 coexist — always filter to one niveau to avoid double-counting. overtraed='TOT' is the grand total (not in dim), useful for region-level totals without offense breakdown.
- Only Straffelov and Særlov at niveau 1 — Færdselslov absent (same as straf10).
- For crimes by region: `JOIN dim.nuts d ON f.omrade = d.kode WHERE d.niveau = 1 AND f.overtraed = 'TOT'` gives 5-region totals. Add AND `f.omrade NOT IN ('0', '998')` to be safe.
- Covers 2007–2025, so shorter than straf10 (1995). Use straf10 for historical series.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0 and omrade=998.
- Map (indirect): kommune data can be aggregated to politikredse via dim.politikredse (JOIN ON f.omrade = dp.kode WHERE dp.niveau=2; dp.parent_kode maps to 12 politikredse). Use /geo/politikredse.parquet for boundaries.