table: fact.hisb77
description: Middellevetid for 0-årige efter område, køn og tid
measure: indhold (unit År)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2000 to 2025
dim docs: /dim/nuts.md

notes:
- omrade=0 is "Hele landet" (national aggregate) — not in dim.nuts. The 11 landsdele use codes 1–11 (niveau=2: e.g. Landsdel Byen København, Landsdel Nordjylland, etc.). Filter out omrade=0 when joining dim.nuts.
- kon has TOT; must filter to one value to avoid tripling counts.
- Use ColumnValues("nuts", "titel", for_table="hisb77") to see the 11 landsdele available.
- Map: /geo/landsdele.parquet — merge on omrade=dim_kode. Exclude omrade=0.
