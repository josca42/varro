table: fact.turist
description: Overnatninger efter overnatningsform, område, gæstens nationalitet, periode og tid
measure: indhold (unit Antal)
columns:
- overnatf: values [100=Alle typer, 110=Hoteller og Feriecentre i alt, 120=Hoteller, 130=Feriecentre, 140=Camping, 150=Vandrerhjem, 160=Lystbådehavne, 170=Feriehuse]
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- nation1: values [TOT=I alt, DAN=Danmark, UDLAN=Verden udenfor Danmark, BELU=Belgien, BUL=Bulgarien ... THA=Thailand, SØA=Asien uden Kina, Japan, Sydkorea, Indien og Thailand, AUS=Australien, OCEX=Oceanien uden Australien, ANDRE=Ukendt land]
- periode: values [1=Hele året, 2=År til dato, 3=De sidste tolv måneder, 1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December]
- tid: date range 1992-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- periode CRITICAL: codes 1, 2, 3 are ambiguous — each appears twice per dimension combination (confirmed duplicate rows). Code 1 = both "Hele Året" AND "Januar", code 2 = both "År til dato" AND "Februar", code 3 = both "De sidste tolv måneder" AND "Marts". There are 270k duplicate rows in this table as a result. Never SUM across all periode values. To get safe monthly data, filter to periode IN (4,5,6,7,8,9,10,11,12) for April–December. If you need Jan–Mar monthly data, be aware you'll get both the monthly and aggregate row and must choose by magnitude or exclude the aggregate.
- For a clean annual total: summing months 4–12 is safer than using periode=1 (which returns two rows). Period code 1 with the large value (~60–65M for all types) is the annual total; with the small value (~2M) is January — but you can't filter programmatically.
- omrade has BOTH niveau 1 (5 regioner: kode 81–85) AND niveau 2 (11 landsdele: kode 1–11) in the same table, plus omrade=0 (national total, not in dim.nuts). Always join with: JOIN dim.nuts d ON f.omrade = d.kode AND filter WHERE d.niveau = 1 OR d.niveau = 2 as needed. Never SUM all omrade codes — you'll double-count (regioner contain landsdele).
- omrade=0 is the national aggregate and NOT in dim.nuts — use it directly as a filter (WHERE omrade = 0) for national totals without joining.
- overnatf hierarchy: 100=Alle typer contains 110=Hoteller og Feriecentre (which contains 120=Hoteller and 130=Feriecentre), 140=Camping, 150=Vandrerhjem, 160=Lystbådehavne, 170=Feriehuse. Never SUM multiple overnatf codes that are parent/child — double-counts. Filter to overnatf=100 for a total across all types.
- This table counts overnatninger (overnight stays). For guest counts (number of guests, not nights), use turist2 which has the same structure but from 2018 only.
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.