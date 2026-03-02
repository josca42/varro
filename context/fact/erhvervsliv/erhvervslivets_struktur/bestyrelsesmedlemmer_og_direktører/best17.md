table: fact.best17
description: Bestyrelsesmedlemmer efter valgform, køn, virksomhedsstørrelse, branche (DB07 19-grp) og tid
measure: indhold (unit Antal)
columns:
- vform: values [1=Valgt på generalforsamling, 2=Medarbejdervalgt, 3=Andre valgformer, 9=Uoplyst]
- kon: values [100=Køn i alt, 200=Mænd, 300=Kvinder, 400=Uoplyst køn]
- virkstr: values [3001=I alt, 3005=Ingen ansatte, 3010=Under 10 årsværk, 3020=10-49 årsværk, 3030=50-249 årsværk, 3040=250 årsværk og derover]
- branchedb0721: join dim.db on branchedb0721=kode::text [approx]
- tid: date range 2023-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- Only covers 2023.
- branchedb0721 uses DB07 letter codes (A–S, X, TOT) — dim.db join does not work. Use ColumnValues("best17", "branchedb0721").
- vform has no "I alt" total row — sum across all vform values to get the total. vform=9 (Uoplyst) should be included in totals.
- Filter kon='100' and virkstr='3001' for overall counts.