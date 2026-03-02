table: fact.fgf1
description: Foreløbig generel firmastatistik efter branche (DB07 19-grp), enhed og tid
measure: indhold (unit -)
columns:
- branchedb0738: join dim.db on branchedb0738=kode::text
- maengde4: values [AFI=Firmaer (antal), AFU=Fuldtidsansatte (antal), OMS=Omsætning (mio kr.) ]
- tid: date range 2023-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- Preliminary (foreløbig) version of gf13 for 2023. Same structure but uses maengde4 as the measurement selector (not enhed) — same three values: AFI, AFU, OMS. Always filter to one.
- branchedb0738 uses 19-group letter codes (A–S, TOT, X). Does NOT match dim.db. Use ColumnValues("fgf1", "branchedb0738") for labels.
- Only covers 2023 (single year). For time-series use gf13 (2019–2023).