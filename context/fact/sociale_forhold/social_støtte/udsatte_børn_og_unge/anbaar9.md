table: fact.anbaar9
description: Anbragte børn og unge pr. 31. december efter administrationskommune, alder og tid
measure: indhold (unit Antal)
columns:
- admkom: join dim.nuts on admkom=kode [approx]; levels [3]
- alerams: values [0=I alt, 9917=0-17 år, 1822=18-22 år, 999=Uoplyst alder]
- tid: date range 2011-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- admkom joins dim.nuts at niveau 3 (kommuner). Code 0 = national total, code 998 = unknown municipality.
- alerams: 0=I alt (total), 9917=0-17 år, 1822=18-22 år, 999=uoplyst. Only three age groups — coarse breakdown. For single-year or finer age groups, there is no kommuneniveau table; use anbaar2 (national) or anbaar16 (landsdele).
- Filter to alerams=0 for total placed children per kommune.
- Map: /geo/kommuner.parquet — merge on admkom=dim_kode. Exclude admkom=0 and admkom=998.