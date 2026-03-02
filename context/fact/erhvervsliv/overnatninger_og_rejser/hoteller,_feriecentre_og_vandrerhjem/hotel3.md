table: fact.hotel3
description: Hoteller og feriecentre efter område, kapacitet og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- kapacitet: values [1080=Hoteller og feriecentre (antal), 1090=Værelser (antal), 1100=Senge (antal), 1110=Værelser (kapacitetsudnyttelse, pct.), 1120=Senge (kapacitetsudnyttelse, pct.)]
- tid: date range 1992-01-01 to 2025-08-01
dim docs: /dim/nuts.md

notes:
- tid is monthly (e.g., 2025-08-01, 2025-07-01). Unlike hotel4 which is annual, this table has a row per month — no periode column needed. Use WHERE tid BETWEEN '2024-01-01' AND '2024-12-01' for a full year.
- omrade joins dim.nuts. Code 0 = Hele landet (not in dim). Levels 1 and 2: 5 regioner (81–85) and 11 landsdele (1–11). Use ColumnValues("nuts", "titel", for_table="hotel3") to see the 16 joinable codes.
- kapacitet is a measurement selector — always filter to exactly one value. The 5 values mix counts (antal) and percentages (kapacitetsudnyttelse pct.): 1080=antal hoteller/feriecentre, 1090=antal værelser, 1100=antal senge, 1110=værelsesbel. pct., 1120=sengebel. pct. Never SUM across kapacitet values.
- For capacity utilization questions, use 1110 or 1120. For structural counts (how many hotels, rooms, beds), use 1080–1100.
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.