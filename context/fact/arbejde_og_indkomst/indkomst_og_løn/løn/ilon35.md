table: fact.ilon35
description: Årlig procentvis ændring i timefortjenesten for ansatte i kommuner og regioner efter branche (DB07) og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text
- tid: date range 2005-01-01 to 2025-04-01
dim docs: /dim/db.md
notes:
- branche07 codes are the same custom DST municipal/regional groupings as ilon32. Do not join to dim.db. Use ColumnValues("ilon35", "branche07").
- Only 2 dimensions: branche07 + tid. indhold is pct change. Companion to ilon32. Quarterly from 2005.
