table: fact.ilon52
description: Implicit lønindeks og ændring i timefortjenesten for regioner efter enhed, branche (DB07) og tid
measure: indhold (unit -)
columns:
- enhed: values [2005=Lønindeks 2005=100, 1000=Årsstigning i procent]
- branche07: join dim.db on branche07=kode::text
- tid: date range 2007-01-01 to 2025-04-01
dim docs: /dim/db.md
notes:
- branche07 codes are custom DST region-specific groupings: EE=total, O8=Offentlig administration, QA=Sundhedsvæsen, QB=Sociale institutioner. Only 4 codes — much narrower than ilon42. Use ColumnValues("ilon52", "branche07").
- enhed is a measurement-type selector: 2005=lønindeks (2005=100), 1000=annual pct change. ALWAYS filter to one value.
- Only regioner (not kommuner). Quarterly from 2007.
