table: fact.hotel7
description: Overnatninger på hoteller og feriecentre efter område, formål med rejse, periode og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- seg: values [TOT=I alt, 1000=Forretning - individuelt, 1010=Forretning - gruppe, 1020=Ferie - individuelt, 1030=Ferie - gruppe, 1040=Andet]
- periode: values [1=Hele året, 2=År til dato, 1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December]
- tid: date range 2004-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. Code 0 = Hele landet (not in dim). Levels 1 and 2: 5 regioner (81–85) and 11 landsdele (1–11). Use ColumnValues("nuts", "titel", for_table="hotel7") to see available codes.
- seg is the trip purpose dimension: TOT=I alt, 1000=Forretning individuelt, 1010=Forretning gruppe, 1020=Ferie individuelt, 1030=Ferie gruppe, 1040=Andet. Always filter seg; TOT for total overnights. The four non-TOT values (forretning + ferie × individuelt/gruppe) are mutually exclusive and sum to TOT.
- periode has the same encoding collision as hotel1: codes 1 and 2 each return 2 rows per combination (Hele-året + Januar; År-til-dato + Februar). For annual totals, filter periode=1 and take MAX(indhold) per group. Periods 3–12 are unambiguous monthly values.
- Data starts 2004 (later than hotel1's 1992). Use hotel1 for nationality breakdown; use hotel7 for travel purpose (business vs. leisure) from 2004 onwards.
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.