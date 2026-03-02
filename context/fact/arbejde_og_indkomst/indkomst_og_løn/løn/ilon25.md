table: fact.ilon25
description: Årlig procentvis ændring i timefortjenesten for statsansatte efter branche (DB07) og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text
- tid: date range 2005-01-01 to 2025-04-01
dim docs: /dim/db.md
notes:
- branche07 codes are the same custom DST state-sector groupings as ilon22 (EE, H, MB, O2, O6, P, R). Do not join to dim.db. Use ColumnValues("ilon25", "branche07") for labels.
- Only 2 dimensions: branche07 + tid. indhold is pct change (already a rate). Simple companion to ilon22. Quarterly from 2005.
