table: fact.konk9
description: Erklærede konkurser (historisk sammendrag) efter sæsonkorrigering og tid
measure: indhold (unit Antal)
columns:
- saeson: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- tid: date range 1979-01-01 to 2025-09-01

notes:
- saeson is a measurement selector: EJSÆSON=unadjusted, SÆSON=seasonally adjusted. Both are present for every period — always filter to one. Summing both doubles every count.
- This is the only konkurser table going back to 1979. All other tables start at 2009. Use this when the question requires historical perspective (recessions, business cycles over decades).
- No breakdowns by sector, region, or company size — this is a national total-only table. For current data with dimensions, use konk4/konk8/konk15.