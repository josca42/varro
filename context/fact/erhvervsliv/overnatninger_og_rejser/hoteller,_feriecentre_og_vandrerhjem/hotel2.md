table: fact.hotel2
description: Overnatninger på hoteller og feriecentre efter område, gæstens nationalitet, type, enhed, periode og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- nation1: values [TOT=I alt, DAN=Danmark, UDLAN=Verden udenfor Danmark, BELU=Belgien, BUL=Bulgarien ... THA=Thailand, SØA=Asien uden Kina, Japan, Sydkorea, Indien og Thailand, AUS=Australien, OCEX=Oceanien uden Australien, ANDRE=Uoplyst land]
- type: values [110=Hoteller og Feriecentre i alt, 120=Hoteller, 130=Feriecentre]
- tal: values [1030=Overnatninger, 1070=Solgte værelser]
- periode: values [1=Hele året, 2=År til dato, 1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December]
- tid: date range 1992-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. Code 0 = Hele landet (not in dim). This table only has niveau 1 (5 regioner: 81–85) — no landsdele breakdown. Use ColumnValues("nuts", "titel", for_table="hotel2") to confirm available regions.
- type is a measurement-selector-like dimension: 110=total, 120=Hoteller only, 130=Feriecentre only. Always filter to one value to avoid tripling counts. For combined totals, use type='110'.
- tal is a measurement selector — always filter it. As in hotel1: tal=1070 (Solgte værelser) is only available for nation1='TOT'. Never SUM across tal values.
- periode has the same encoding collision as hotel1: codes 1 and 2 each return 2 rows per combination (Hele-året + Januar; År-til-dato + Februar). For annual totals, filter periode=1 and take MAX(indhold) per group. Never SUM all periode 1–12.
- nation1 has 54 values including TOT, DAN, UDLAN. Use ColumnValues("hotel2", "nation1") to browse.
- This table adds the type breakdown vs hotel1, but sacrifices the landsdele granularity (only regioner here).
- Map: context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.