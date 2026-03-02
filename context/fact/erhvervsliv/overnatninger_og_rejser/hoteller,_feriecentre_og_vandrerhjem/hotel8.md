table: fact.hotel8
description: Overnatninger på hoteller og feriecentre efter område, formål med rejse, type, periode og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- seg: values [TOT=I alt, 1000=Forretning - individuelt, 1010=Forretning - gruppe, 1020=Ferie - individuelt, 1030=Ferie - gruppe, 1040=Andet]
- type: values [110=Hoteller og Feriecentre i alt, 120=Hoteller, 130=Feriecentre]
- periode: values [1=Hele året, 2=År til dato, 1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December]
- tid: date range 2004-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. Code 0 = Hele landet (not in dim). Only niveau 1 — 5 regioner (81–85). No landsdele breakdown.
- type is a structural dimension: 110=Hoteller og Feriecentre i alt (total), 120=Hoteller, 130=Feriecentre. Always filter to one value.
- seg (rejseformål): TOT=I alt, 1000=Forretning individuelt, 1010=Forretning gruppe, 1020=Ferie individuelt, 1030=Ferie gruppe, 1040=Andet. The four non-TOT values are mutually exclusive and sum to TOT. Filter seg to avoid overcounting.
- periode has the same encoding collision as hotel1/hotel7: codes 1 and 2 each return 2 rows per combination. For annual totals, filter periode=1 and take MAX(indhold). Periods 3–12 are unambiguous monthly.
- Use hotel8 when you need travel purpose × hotel-type breakdown (regioner only). Use hotel7 for the same purpose data with landsdele granularity but without type split.
- Map: context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.