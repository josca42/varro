table: fact.sbs1
description: Sammenlignende folkebiblioteksstatistik efter område, nøgletal og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2, 3]
- bnogle: values [14110=Folketal (i 1.000), 14120=Arbejdsstationer, 14130=Personaleårsværk, 14140=Aktive personlige lånere, 14150=Fysiske besøg (i 1.000) ... 14380=Lønudgifter (pr. 1.000 indbyggere, 1.000 kr.), 14390=Materialeudgifter (pr. 1.000 indbyggere, 1.000 kr.), 14400=Øvrige udgifter (pr. 1.000 indbyggere, 1.000 kr.), 14410=Indtægter (pr. 1.000 indbyggere, 1.000 kr.), 14420=Nettoudgifter (pr. 1.000 indbyggere, 1.000 kr.)]
- tid: date range 2009-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau 2 (11 landsdele) and niveau 3 (97 kommuner). omrade=0 = Hele landet. No niveau 1 (regioner) — unlike most other bib tables.
- bnogle contains both absolute counts and per-1000-inhabitant normalized rates (codes 14340–14420 are per-1000 rates). Never sum per-1000 rates across areas.
- Designed for cross-municipality comparison. Each bnogle is a distinct KPI — always filter to one.
- Use ColumnValues("sbs1", "bnogle") to see the full list of ~40 KPIs available.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.
