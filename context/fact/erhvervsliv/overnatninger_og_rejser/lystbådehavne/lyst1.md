table: fact.lyst1
description: Overnatninger i lystbådehavne efter område, gæstens nationalitet, periode og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- nation1: values [TOT=I alt, DAN=Danmark, UDLAN=Verden udenfor Danmark, BELU=Belgien, FIN=Finland ... ØST=Østrig, USA=USA, AUS=Australien, OCEX=Oceanien uden Australien, ANDRE=Uoplyst land]
- periode: values [1=Hele året, 2=År til dato, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September]
- tid: date range 1992-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 1 (5 regioner: 81-85) and niveau 2 (11 landsdele: 1-11). omrade=0 is "Hele landet" aggregate — not in dim, use WHERE f.omrade='0' to get national total.
- periode is a critical overcounting column. Values 1=Hele året (annual sum), 2=År til dato, 5-9=individual months May–Sep. Always filter to exactly one periode value. Never sum across periode values or you multiply counts.
- nation1 has 27 values including TOT=I alt (all nationalities), DAN=Danmark, UDLAN=Verden udenfor Danmark (non-DK subtotal), then individual countries. TOT is the grand total; DAN+UDLAN=TOT. Filter nation1='TOT' for overall counts.
- For a simple annual national total: WHERE f.omrade='0' AND f.nation1='TOT' AND f.periode='1'.
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.