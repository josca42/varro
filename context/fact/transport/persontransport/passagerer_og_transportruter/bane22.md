table: fact.bane22
description: International jernbanetransport af passagerer til og fra Danmark efter land og tid
measure: indhold (unit 1.000 personer)
columns:
- land: join dim.lande_uhv on land=kode [approx]; levels [4]
- tid: date range 2002-01-01 to 2024-01-01
dim docs: /dim/lande_uhv.md

notes:
- land joins dim.lande_uhv at niveau 4 only (individual countries). 28 countries match cleanly — all European rail partners (Norway, Sweden, Germany, etc.).
- Three unmatched codes: IA (I alt — grand total across all countries, has real data ~249k over all years), CS (former Czechoslovakia, zero data), OV (Øvrige/Other, zero data). IA is not in the dim table; use it directly as the total for all countries, or exclude it with WHERE land != 'IA' when summing individual countries.
- Use ColumnValues("lande_uhv", "titel", for_table="bane22") to browse the 28 matched countries.
- Annual data 2002–2024.
