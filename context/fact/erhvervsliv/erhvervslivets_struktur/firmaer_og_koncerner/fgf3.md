table: fact.fgf3
description: Foreløbig generel firmastatistik efter branche (DB07 10-grp.), enhed, firmastørrelse (fuldtidsansatte) og tid
measure: indhold (unit -)
columns:
- branche0710: join dim.db_10 on branche0710=kode::text; levels [1]
- enhed: values [AFI=Firmaer (antal), AFU=Fuldtidsansatte (antal), OMS=Omsætning (mio kr.) ]
- firmstr: values [TOT=I alt, 0000=Ingen ansatte, 010=Under 10 ansatte, 101=10-49 ansatte, 102=50-249 ansatte, 103=250 ansatte og derover]
- tid: date range 2023-01-01 to 2023-01-01
dim docs: /dim/db_10.md

notes:
- Preliminary version of gf13 for 2023 at 10-group granularity. branche0710 joins dim.db_10 (TOT not in dim — use as inline filter for national total).
- enhed is a measurement selector (AFI, AFU, OMS). Always filter to one value.
- firmstr includes TOT plus 5 size buckets. Filter to TOT for overall totals.
- Only covers 2023. For time-series (2019–2023) use gf13 instead.