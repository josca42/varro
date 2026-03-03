table: fact.aulk03
description: Fuldtidsledige efter område, oprindelsesland, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [2]
- ieland: join dim.lande_uhv on ieland=kode [approx]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2025-04-01
dim docs: /dim/lande_uhv.md, /dim/nuts.md

notes:
- ieland does NOT join dim.lande_uhv. Uses a custom 39-code origin-country classification (30=Dansk oprindelse, 1=Vestlige lande, 2=Ikke-vestlige lande, TOT=I alt, plus ~25 specific countries). Use ColumnValues("aulk03", "ieland") for the full list. Do not join dim.lande_uhv.
- omrade joins dim.nuts at niveau=2 only (11 landsdele). Extra code 0=Hele landet not in dim.
- Current series superseding aul03. This is the only active (updated) origin-country count table.
- Map: /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.