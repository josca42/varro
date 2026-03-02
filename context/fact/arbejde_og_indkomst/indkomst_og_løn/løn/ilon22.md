table: fact.ilon22
description: Implicit lønindeks for den statslige sektor efter branche (DB07) og tid
measure: indhold (unit Indeks)
columns:
- branche07: join dim.db on branche07=kode::text
- tid: date range 2005-01-01 to 2025-04-01
dim docs: /dim/db.md
notes:
- branche07 codes are custom DST public sector groupings that do NOT correspond to standard dim.db codes. Codes: EE=Erhverv i alt (total), H=Transport, MB=Forskning og udvikling, O2=Statslig administration forsvar og politi (-2012), O6=Statslig administration forsvar og politi (inkl. sociale kasser), P=Undervisning, R=Kultur og fritid. Do not join to dim.db. Use ColumnValues("ilon22", "branche07") for labels.
- Only 2 dimensions: branche07 + tid. Covers the state sector (statslig sektor) only. Simple to query. Quarterly index from 2005.
- indhold is a wage index value (not kr/hour). For year-on-year change, use companion table ilon25.
