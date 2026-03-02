table: fact.fly55
description: Flytninger mellem regioner efter køn, alder, tilflytningsregion, fraflytningsregion og tid
measure: indhold (unit Antal)
columns:
- koen: values [1=Mænd, 2=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- tilreg: join dim.nuts on tilreg=kode; levels [1]
- frareg: join dim.nuts on frareg=kode; levels [1]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- tilreg and frareg join dim.nuts at niveau 1 (5 regioner). Perfect 5/5 match. Use `JOIN dim.nuts d ON f.tilreg = d.kode AND d.niveau = 1`.
- koen uses integer codes 1=Mænd, 2=Kvinder — NOT the M/K used in all other fly* tables. Don't mix with kon from fly/fly33/fly66.
- alder contains only individual ages (0–125), no total row.
- This is an origin-destination matrix: each row is moves from frareg to tilreg. To get "moves into Region X" filter `tilreg = X`. To get "moves out of Region X" filter `frareg = X`. Summing across all rows gives national inter-regional move total without double-counting.
- This table covers only *inter-regional* moves. Moves within a region are not represented here.
- Map: context/geo/regioner.parquet — OD matrix; merge on tilreg=dim_kode (moves into) or frareg=dim_kode (moves out of) for choropleth. Exclude omrade=0.