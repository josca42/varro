table: fact.camp1
description: Overnatninger på campingpladser efter område, gæstens nationalitet, enhed, periode og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- nation1: values [TOT=I alt, DAN=Danmark, UDLAN=Verden udenfor Danmark, BELU=Belgien, BUL=Bulgarien ... THA=Thailand, SØA=Asien uden Kina, Japan, Sydkorea, Indien og Thailand, AUS=Australien, OCEX=Oceanien uden Australien, ANDRE=Uoplyst land]
- overnat1: values [1030=Overnatninger, 1190=Heraf på faste standpladser]
- periode: values [1=Hele året, 2=År til dato, 1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December]
- tid: date range 1992-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts but only at niveau 1 (5 regioner: 81–85). omrade=0 is the national total (Hele landet) — not in dim.nuts. To query regions, use omrade IN (81,82,83,84,85) and join dim.nuts; to get the national figure use omrade=0 directly.
- periode is a critical overcounting trap: periode=1 is Hele året (annual total), periode=2 is År til dato, periode=3–12 are individual months (March–December). tid is always YYYY-01-01 (annual). Never SUM across all periode values — that adds the annual total on top of all months. For a yearly figure use WHERE periode=1; for monthly breakdown use WHERE periode BETWEEN 3 AND 12.
- overnat1 is a measurement selector — 1030=Overnatninger (total overnights), 1190=Heraf på faste standpladser (thereof on permanent pitches). Always filter to one value; never sum both.
- nation1 is a rich nationality breakdown (50+ codes). TOT=I alt is the all-nationalities total; DAN=Danmark, UDLAN=Verden udenfor Danmark. Use ColumnValues("camp1", "nation1") to browse codes. Filter nation1='TOT' for totals and don't sum TOT with individual countries.
- A clean annual total query: WHERE omrade=0 AND nation1='TOT' AND overnat1=1030 AND periode=1 — gives one row per year.
- Map: /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.