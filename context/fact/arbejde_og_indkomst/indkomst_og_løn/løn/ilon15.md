table: fact.ilon15
description: Årlig ændring i timefortjenesten for virksomheder og organisationer efter branche og tid
measure: indhold (unit Pct.)
columns:
- erhverv: join dim.db on erhverv=kode::text; levels [2]
- tid: date range 2005-01-01 to 2025-04-01
dim docs: /dim/db.md
notes:
- WARNING: The documented dim.db join (erhverv=kode::text) is WRONG — same custom DST codes as ilon12. Use ColumnValues("ilon15", "erhverv") for correct labels.
- No measurement selector — indhold is already a single measure: annual pct change in hourly earnings. No filtering needed beyond choosing erhverv.
- Only 2 dimensions: erhverv + tid. Simple to query. Covers private sector only, quarterly from 2005.
