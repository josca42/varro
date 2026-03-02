table: fact.hotel1
description: Overnatninger på hoteller og feriecentre efter område, gæstens nationalitet, enhed, periode og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- nation1: values [TOT=I alt, DAN=Danmark, UDLAN=Verden udenfor Danmark, BELU=Belgien, BUL=Bulgarien ... THA=Thailand, SØA=Asien uden Kina, Japan, Sydkorea, Indien og Thailand, AUS=Australien, OCEX=Oceanien uden Australien, ANDRE=Uoplyst land]
- tal: values [1030=Overnatninger, 1070=Solgte værelser]
- periode: values [1=Hele året, 2=År til dato, 1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December]
- tid: date range 1992-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. Code 0 = Hele landet (not in dim table, no join). niveau 1 = 5 regioner (81-85), niveau 2 = 11 landsdele (1-11). This table has both levels. Use ColumnValues("nuts", "titel", for_table="hotel1") to see the 16 joinable regions/landsdele.
- tal is a measurement selector — always filter it. tal=1030 (Overnatninger) is fully broken down by nation1. tal=1070 (Solgte værelser) is only available for nation1='TOT' (total), all regions. Never SUM across tal values.
- periode has a critical encoding collision: code 1 maps to BOTH "Hele året" (annual total) AND "Januar" (January); code 2 maps to BOTH "År til dato" (YTD) AND "Februar" (February). This means every query returns 2 rows per dimension combination at periode=1 and periode=2. Never SUM across all periode values — you'll double-count.
- For annual totals: filter WHERE periode=1 and use MAX(indhold) per group (the larger value is "Hele året", the smaller is "Januar"). For monthly breakdown: periode 3–12 are unambiguous (one row per combo); periode 1 and 2 require picking the smaller indhold for the monthly value.
- nation1 has 54 values including aggregate codes: TOT (all), DAN (Danish), UDLAN (all foreign). Use ColumnValues("hotel1", "nation1") to browse all nationalities. For total overnights regardless of origin, filter nation1='TOT'.
- Typical query for annual overnights by region: WHERE tal='1030' AND nation1='TOT' AND periode=1, then JOIN dim.nuts and take MAX(indhold) per omrade to get "Hele året" rows only.
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.