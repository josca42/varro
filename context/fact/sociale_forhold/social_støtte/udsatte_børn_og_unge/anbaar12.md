table: fact.anbaar12
description: Anbragte børn og unge pr. 31. december efter administrationskommune, anbringelsessted og tid
measure: indhold (unit Antal)
columns:
- admkom: join dim.nuts on admkom=kode [approx]; levels [3]
- anbringelse: values [0=I alt, 1=Netværksplejefamilie, 21=Almindelig plejefamlie, 22=Kommunal plejefamilie, 26=Plejefamilie efter §76 a (unge med funktionsnedsættelse), 23=Almen plejefamilie, 24=Forstærket plejefamilie, 25=Specialiseret plejefamlie, 9=Døgninstitution, almindelig afdeling, 7=Delvis lukket døgninstitution eller delvis lukket afdeling på åben døgninstitution, 8=Døgninstitution, sikret afdeling, 27=Opholdssted for børn og unge, 11=Kost- og eller efterskole, 6=Eget værelse, kollegium, kollegielignende opholdssted, 99=Uoplyst]
- tid: date range 2011-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- admkom joins dim.nuts at niveau 3 (kommuner, 94 of 96 codes matched). Code 0 = national total (not in dim), code 998 = unknown municipality (not in dim — exclude for geographic analyses).
- Use ColumnValues("nuts", "titel", for_table="anbaar12") to see the ~94 kommuner with data.
- anbringelse code 0 = I alt. Filter to anbringelse=0 for total placed children per kommune.
- No age or gender breakdown — for those, use anbaar16 (landsdele) or anbaar9 (age by kommune).
- Map: context/geo/kommuner.parquet — merge on admkom=dim_kode. Exclude admkom=0 and admkom=998.