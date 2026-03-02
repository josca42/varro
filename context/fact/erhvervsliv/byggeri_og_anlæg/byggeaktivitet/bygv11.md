table: fact.bygv11
description: Den samlede byggeaktivitet (ikke korrigeret for forsinkelser) efter område, byggefase, anvendelse, bygherreforhold og tid
measure: indhold (unit M2)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- bygfase: values [2=Påbegyndt byggeri, 3=Fuldført byggeri, 4=Byggeri under opførelse, 1=Tilladt byggeri]
- anvend: join dim.byganv on anvend=kode::text [approx]; levels [2, 3]
- bygherre: join dim.bygherre on bygherre=kode::text [approx]; levels [2]
- tid: date range 2006-01-01 to 2025-07-01
dim docs: /dim/byganv.md, /dim/bygherre.md, /dim/nuts.md

notes:
- omrade joins dim.nuts but code '0' (Denmark total) is not in the dim — it drops from inner joins. dim.nuts: niveau 1=5 regioner (kode 81-85), niveau 2=11 landsdele (kode 1-11), niveau 3=98 kommuner (kode 100+). Filter `WHERE d.niveau=3` to get kommuner only and avoid double-counting across levels.
- anvend joins dim.byganv at niveauer 2 and 3 only. Code 'UOPL' is not in the dim — filter or use LEFT JOIN. Use `ColumnValues("byganv", "titel", for_table="bygv11")` to see available codes.
- bygherre joins dim.bygherre at niveau 2 only (kode 10, 20, 30, 40, 41, 50, 60, 70, 80, 90). Code 'UOPL' is not in dim. Niveau 1 codes (1, 2, 3) are absent from this table.
- bygfase has 4 mutually exclusive phases — always filter to one when aggregating.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.