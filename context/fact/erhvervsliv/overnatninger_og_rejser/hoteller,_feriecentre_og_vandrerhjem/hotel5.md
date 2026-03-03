table: fact.hotel5
description: Hoteller og feriecentre efter område, kapacitet, type og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- kapacitet: values [1080=Hoteller og feriecentre (antal), 1090=Værelser (antal), 1100=Senge (antal), 1110=Værelser (kapacitetsudnyttelse, pct.), 1120=Senge (kapacitetsudnyttelse, pct.)]
- type: values [110=Hoteller og Feriecentre i alt, 120=Hoteller, 130=Feriecentre]
- tid: date range 1992-01-01 to 2025-08-01
dim docs: /dim/nuts.md

notes:
- tid is monthly (e.g., 2025-08-01). Same monthly granularity as hotel3 but adds a type breakdown.
- omrade joins dim.nuts. Code 0 = Hele landet (not in dim). Only niveau 1 — 5 regioner (81–85). No landsdele breakdown.
- type is a structural dimension: 110=Hoteller og Feriecentre i alt (total), 120=Hoteller, 130=Feriecentre. Always filter to one value; type=110 for combined totals.
- kapacitet is a measurement selector: 1080=antal hoteller/feriecentre, 1090=antal værelser, 1100=antal senge, 1110=værelsesbel. pct., 1120=sengebel. pct. Never SUM across kapacitet values.
- Use hotel5 when you need monthly capacity broken down by hotel vs. feriecenter type. Use hotel3 for the same monthly data with landsdele granularity but without type split.
- Map: /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.