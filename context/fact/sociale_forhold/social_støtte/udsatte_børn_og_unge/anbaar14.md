table: fact.anbaar14
description: Iværksatte anbringelser efter administrationskommune, alder og tid
measure: indhold (unit Antal)
columns:
- admkom: join dim.nuts on admkom=kode [approx]; levels [3]
- alerams: values [0=I alt, 9917=0-17 år, 1822=18-22 år, 999=Uoplyst alder]
- tid: date range 2011-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- FLOW table (iværksatte = newly initiated placements) at kommuneniveau, with only age breakdown.
- admkom joins dim.nuts at niveau 3 (kommuner). Code 0 = national total (no code 998 here — cleaner than the stock tables).
- alerams: 0=I alt, 9917=0-17 år, 1822=18-22 år, 999=uoplyst. Filter to alerams=0 for total new placements per kommune.
- Map: /geo/kommuner.parquet — merge on admkom=dim_kode. Exclude admkom=0.