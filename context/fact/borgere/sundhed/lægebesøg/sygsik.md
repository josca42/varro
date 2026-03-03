table: fact.sygsik
description: Befolkningen efter område, sygesikringsgruppe og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- sygsik: values [1=Sygesikringsgruppe 1, 2=Sygesikringsgruppe 2, 99=Øvrige sygesikringsgrupper]
- tid: date range 2007-01-01 to 2025-01-01
dim docs: /dim/nuts.md
notes:
- Simple table: population at commune level by health insurance group. No age or gender breakdown.
- omrade joins dim.nuts niveau 3 only (98 kommuner, 3-digit kode). No total row — join clean, 98/98 match.
- sygsik=1 is the standard group (fixed GP, must get referral for specialists); sygsik=2 is the free-choice group (can go directly to specialists). 99=other (small). To get total population, sum sygsik=1+2+99 or filter for each.
- The most current table in this subject — data through 2025.
- Map: /geo/kommuner.parquet — merge on omrade=dim_kode.
