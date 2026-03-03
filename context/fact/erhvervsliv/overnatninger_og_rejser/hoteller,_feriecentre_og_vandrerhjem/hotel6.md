table: fact.hotel6
description: Hoteller og feriecentre efter område, kapacitet, type og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- kapacitet: values [1130=Antal hoteller - max., 1140=Antal hoteller - min., 1150=Antal værelser - max., 1160=Antal værelser - min., 1170=Antal senge - max., 1180=Antal senge - min., 1110=Værelser (kapacitetsudnyttelse, pct.), 1120=Senge (kapacitetsudnyttelse, pct.)]
- type: values [110=Hoteller og Feriecentre i alt, 120=Hoteller, 130=Feriecentre]
- tid: date range 1992-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- tid is annual (one row per year). Last available year: 2024. Same annual min/max structure as hotel4 but adds type breakdown.
- omrade joins dim.nuts. Code 0 = Hele landet (not in dim). Only niveau 1 — 5 regioner (81–85). No landsdele.
- type is a structural dimension: 110=total, 120=Hoteller, 130=Feriecentre. Always filter to one value.
- kapacitet is a measurement selector with max/min seasonal ranges: 1130=hoteller max, 1140=hoteller min, 1150=værelser max, 1160=værelser min, 1170=senge max, 1180=senge min, 1110=værelsesbel. pct., 1120=sengebel. pct. Never SUM across kapacitet.
- Use hotel6 for annual min/max capacity broken down by hotel vs. feriecenter type (regioner only). Use hotel4 for same annual ranges with landsdele granularity but without type split.
- Map: /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.