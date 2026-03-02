table: fact.hisbk
description: Middellevetid for 0-årige efter område, køn og tid
measure: indhold (unit År)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2000 to 2025
dim docs: /dim/nuts.md

notes:
- omrade=0 is "Hele landet" (national aggregate) — not in dim.nuts. All other omrade values are kommune codes (niveau=3, ~94 kommuner). Filter out omrade=0 when joining dim.nuts.
- kon has TOT; must filter to one value to avoid tripling counts.
- Use ColumnValues("nuts", "titel", for_table="hisbk") to see the ~94 kommuner available. This is the most granular of the three omrade-based tables (hisbr=regioner, hisb77=landsdele, hisbk=kommuner).
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
