table: fact.hotel4
description: Hoteller og feriecentre efter område, kapacitet og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- kapacitet: values [1130=Antal hoteller - max., 1140=Antal hoteller - min., 1150=Antal værelser - max., 1160=Antal værelser - min., 1170=Antal senge - max., 1180=Antal senge - min., 1110=Værelser (kapacitetsudnyttelse, pct.), 1120=Senge (kapacitetsudnyttelse, pct.)]
- tid: date range 1992-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- tid is annual (one row per year, e.g., 2024-01-01, 2023-01-01). Unlike hotel3 which is monthly, this table gives annual aggregates. Last available year: 2024.
- omrade joins dim.nuts. Code 0 = Hele landet (not in dim). Levels 1 and 2: 5 regioner (81–85) and 11 landsdele (1–11).
- kapacitet is a measurement selector — always filter to one value. This table has max/min capacity ranges (seasonal variability) plus utilization pct: 1130=hoteller max, 1140=hoteller min, 1150=værelser max, 1160=værelser min, 1170=senge max, 1180=senge min, 1110=værelsesbel. pct., 1120=sengebel. pct. The max/min values capture peak vs. off-season capacity differences across the year. Never SUM across kapacitet.
- Use hotel3 for monthly capacity trends; use hotel4 for annual min/max seasonal ranges.
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.