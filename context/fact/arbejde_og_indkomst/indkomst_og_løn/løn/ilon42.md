table: fact.ilon42
description: Implicit lønindeks og ændring i timefortjenesten for kommuner efter enhed, branche (DB07) og tid
measure: indhold (unit -)
columns:
- enhed: values [2005=Lønindeks 2005=100, 1000=Årsstigning i procent]
- branche07: join dim.db on branche07=kode::text
- tid: date range 2007-01-01 to 2025-04-01
dim docs: /dim/db.md
notes:
- branche07 codes are custom DST municipality-specific groupings: EE=total, N1=Forretningsservice mv., O5=Offentlig administration, P=Undervisning, QA=Sundhedsvæsen, QB=Sociale institutioner, R=Kultur og fritid. Slightly different from ilon32/35 (O5 vs O1). Do not join to dim.db. Use ColumnValues("ilon42", "branche07").
- enhed is a measurement-type selector: 2005=lønindeks (2005=100), 1000=annual pct change. ALWAYS filter to one value — each branche07 appears twice (once per measure type). This replaces the separate index/pct-change split seen in ilon32/ilon35.
- Only kommuner (not regions). Quarterly from 2007.
