table: fact.lyst10
description: Overnatninger i lystbådehavne efter område, gæstens nationalitet, periode, overnatningsform og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- nation1: values [TOT=I alt, DAN=Danmark, UDLAN=Verden udenfor Danmark, BELU=Belgien, FIN=Finland ... ØST=Østrig, USA=USA, AUS=Australien, OCEX=Oceanien uden Australien, ANDRE=Uoplyst land]
- periode: values [1=Hele året, 2=År til dato, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September]
- overnatf: values [210=Personovernatninger, 215=Gæstebådsovernatninger]
- tid: date range 1992-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 2 (11 landsdele). omrade=0 is "Hele landet" — not in dim.
- overnatf is a measure selector with two independent metrics: 210=Personovernatninger (person nights), 215=Gæstebådsovernatninger (guest boat nights). These count different things — never sum them together. Always filter to one overnatf value.
- periode: same critical overcounting risk as lyst1. Filter to one value: 1=Hele året, 2=År til dato, or monthly 5-9.
- nation1: 27 values, TOT=I alt is the grand total.
- For annual person-nights nationally: WHERE f.omrade='0' AND f.nation1='TOT' AND f.periode='1' AND f.overnatf='210'.
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.