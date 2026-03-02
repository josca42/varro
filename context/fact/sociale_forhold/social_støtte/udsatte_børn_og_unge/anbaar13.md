table: fact.anbaar13
description: Anbragte børn og unge pr. 31. december efter administrationskommune, foranstaltning og tid
measure: indhold (unit Antal)
columns:
- admkom: join dim.nuts on admkom=kode [approx]; levels [3]
- foran: values [0=I alt, 101=Afgørelse med samtykke , 102=Afgørelse uden samtykke , 200=Øvrige, 99=Uoplyst]
- tid: date range 2011-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- admkom joins dim.nuts at niveau 3 (kommuner). Code 0 = national total, code 998 = unknown municipality.
- foran is simplified here (only 5 codes: 0=total, 101=med samtykke, 102=uden samtykke, 200=øvrige, 99=uoplyst) compared to anbaar2/anbaar16's full legal basis list. Use foran=0 for total per kommune.
- No age or gender breakdown.
- Map: context/geo/kommuner.parquet — merge on admkom=dim_kode. Exclude admkom=0 and admkom=998.