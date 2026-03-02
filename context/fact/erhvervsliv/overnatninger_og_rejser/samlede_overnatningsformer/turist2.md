table: fact.turist2
description: Gæster efter overnatningsform, område, gæstens nationalitet, periode og tid
measure: indhold (unit Antal)
columns:
- overnatf: values [100=Alle typer, 110=Hoteller og Feriecentre i alt, 120=Hoteller, 130=Feriecentre, 140=Camping, 150=Vandrerhjem, 160=Lystbådehavne, 170=Feriehuse]
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- nation1: values [TOT=I alt, DAN=Danmark, UDLAN=Verden udenfor Danmark, BELU=Belgien, BUL=Bulgarien ... THA=Thailand, SØA=Asien uden Kina, Japan, Sydkorea, Indien og Thailand, AUS=Australien, OCEX=Oceanien uden Australien, ANDRE=Ukendt land]
- periode: values [1=Hele året, 2=År til dato, 3=De sidste tolv måneder, 1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December]
- tid: date range 2018-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- This table counts gæster (guests/arrivals), NOT overnatninger (overnight stays). Use turist for overnight stays.
- periode CRITICAL: same ambiguous duplicate-key structure as turist. Codes 1, 2, 3 each appear twice per dimension combination — 1 = "Hele Året" + "Januar", 2 = "År til dato" + "Februar", 3 = "De sidste tolv måneder" + "Marts". Safe approach: filter to periode IN (4,5,6,7,8,9,10,11,12) for April–December monthly data. Never SUM all periode values.
- omrade has BOTH niveau 1 (5 regioner: kode 81–85) AND niveau 2 (11 landsdele: kode 1–11), plus omrade=0 (national total, not in dim.nuts). Always filter by niveau when joining: JOIN dim.nuts d ON f.omrade = d.kode WHERE d.niveau = 1 (or 2). Never SUM all omrade — double-counts across hierarchy levels.
- omrade=0 is the national aggregate, not in dim.nuts — use directly (WHERE omrade = 0) for national totals.
- overnatf hierarchy same as turist: 100 contains 110 (which contains 120+130), 140, 150, 160, 170. Filter to overnatf=100 for all-type total; never SUM parent and child codes.
- Shorter time series than turist — only from 2018. For pre-2018 guest data, this table cannot help; use turist (which covers overnight stays back to 1992).
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.