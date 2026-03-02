table: fact.ilon32
description: Implicit lønindeks for kommuner og regioner efter branche (DB07) og tid
measure: indhold (unit Indeks)
columns:
- branche07: join dim.db on branche07=kode::text
- tid: date range 2005-01-01 to 2025-04-01
dim docs: /dim/db.md
notes:
- branche07 codes are custom DST municipal/regional sector groupings: EE=total, N1=Forretningsservice mv., O1=Offentlig administration, P=Undervisning, QA=Sundhedsvæsen, QB=Sociale institutioner, R=Kultur og fritid. Do not join to dim.db. Use ColumnValues("ilon32", "branche07").
- Only 2 dimensions: branche07 + tid. Covers kommuner og regioner combined. Quarterly index from 2005. Companion pct-change table: ilon35.
