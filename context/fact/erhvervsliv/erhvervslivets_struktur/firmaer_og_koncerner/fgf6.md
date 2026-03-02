table: fact.fgf6
description: Foreløbig generel firmastatistik efter region, branche (DB07 10-grp), enhed og tid
measure: indhold (unit -)
columns:
- region: join dim.nuts on region=kode; levels [1]
- branchedb0710: join dim.db_10 on branchedb0710=kode::text; levels [1]
- enhed: values [AFI=Firmaer (antal), AFU=Fuldtidsansatte (antal), OMS=Omsætning (mio kr.) ]
- tid: date range 2023-01-01 to 2023-01-01
dim docs: /dim/db_10.md, /dim/nuts.md

notes:
- Preliminary regional+sector table for 2023 only. region joins dim.nuts niveau 1 (5 regions); code 0 = national aggregate, not in dim.
- branchedb0710 joins dim.db_10 niveau 1; TOT = national total, not in dim.
- enhed is a measurement selector (AFI, AFU, OMS). Always filter to one value.
- Only covers 2023. For time-series with regional breakdown use gf14 (2019–2023, but no branche).
- Map: context/geo/regioner.parquet — merge on region=dim_kode. Exclude region=0.