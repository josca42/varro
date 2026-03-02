table: fact.aulp03
description: Fuldtidsledige i pct. af arbejdsstyrken efter område, oprindelsesland, køn og tid
measure: indhold (unit Pct.)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [2]
- ieland: join dim.lande_uhv on ieland=kode [approx]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2023-01-01
dim docs: /dim/lande_uhv.md, /dim/nuts.md

notes:
- ieland does NOT join dim.lande_uhv. Uses same custom 39-code origin-country classification as aulk03/aul03. Use ColumnValues("aulp03", "ieland") for the full list.
- indhold is a percentage (pct. of workforce). Do not sum rates.
- omrade at niveau=2 only (11 landsdele). Stopped at 2023-01 — no active replacement.
- Map: context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.