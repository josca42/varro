table: fact.straf22
description: Anmeldte forbrydelser og sigtelser efter område, overtrædelsens art, anmeldte og sigtede og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx: Missing codes: 0, 998]; levels [1, 3]
- overtraed: join dim.overtraedtype on overtraed=kode::text [approx: Fact col is string, dim KODE is int64. Also has TOT placeholder.]; levels [1, 2, 3]
- anmsigt: values [ANM=Anmeldt, SIG=Sigtelser]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md, /dim/overtraedtype.md

notes:
- Combines regional breakdown (omrade) with reported vs. charged split (anmsigt). Both dimensions must be filtered to avoid double-counting.
- anmsigt: always filter to ANM (reported) or SIG (charged) — never sum across both.
- omrade: niveau 1 (5 regioner) and niveau 3 (99 kommuner) only — no landsdele. omrade=0 = national total, omrade=998 = unknown location. Exclude both for geographic analysis.
- overtraed: niveaux 1, 2, 3 coexist — filter to one niveau. overtraed='TOT' = grand total (not in dim).
- Only Straffelov and Særlov at niveau 1 — Færdselslov absent.
- Covers 2007–2024. Use straf20 (no regional breakdown, goes to 2024) or straf10 (goes to 2025) when geography is not needed.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0 and omrade=998.
- Map (indirect): kommune data can be aggregated to politikredse via dim.politikredse (JOIN ON f.omrade = dp.kode WHERE dp.niveau=2; dp.parent_kode maps to 12 politikredse). Use context/geo/politikredse.parquet for boundaries.