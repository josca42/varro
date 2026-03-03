table: fact.vandrer
description: Overnatninger på vandrerhjem efter område, gæstens nationalitet, periode og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- nation1: values [TOT=I alt, DAN=Danmark, UDLAN=Verden udenfor Danmark, BELU=Belgien, BUL=Bulgarien ... THA=Thailand, SØA=Asien uden Kina, Japan, Sydkorea, Indien og Thailand, AUS=Australien, OCEX=Oceanien uden Australien, ANDRE=Uoplyst land]
- periode: values [1=Hele året, 2=År til dato, 1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December]
- tid: date range 1998-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. Code 0 = Hele landet (not in dim). Only niveau 1 — 5 regioner (81–85). No landsdele breakdown.
- periode has the same encoding collision as hotel1: codes 1 and 2 each return 2 rows per combination (Hele-året + Januar; År-til-dato + Februar). For annual totals, filter periode=1 and take MAX(indhold) per group. Periods 3–12 are unambiguous.
- nation1 has 54 values including TOT, DAN, UDLAN aggregates. Same set as hotel1/hotel2. Filter nation1='TOT' for all guests combined.
- No tal selector here (unlike hotel1) — indhold always means overnights (antal). Simpler to query than hotel1.
- Data starts 1998 (vs. 1992 for hotel1). Only covers youth hostels (vandrerhjem) — not hotels or holiday centers.
- Map: /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.