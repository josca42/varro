table: fact.hisbr
description: Middellevetid for 0-årige efter område, køn og tid
measure: indhold (unit År)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2000 to 2025
dim docs: /dim/nuts.md

notes:
- omrade=0 is "Hele landet" (national aggregate) — not in dim.nuts. The 5 regions use codes 81–85 (niveau=1). Filter out omrade=0 when joining, or use it directly for national totals without a join.
- kon has TOT; must filter to one value (TOT, M, or K) to avoid tripling counts.
- Sample: SELECT d.titel, f.kon, f.tid, f.indhold FROM fact.hisbr f JOIN dim.nuts d ON f.omrade=d.kode WHERE f.kon='TOT' ORDER BY f.tid DESC, d.titel;
- Map: context/geo/regioner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
