table: fact.fiks44
description: Firmaernes køb og salg (detaljeret) efter branche (DB07), beløb og tid
measure: indhold (unit Mio. kr.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [5]
- belob: values [4=Salg i alt, 1=Indenlandsk salg, 3=Køb i alt, 0=Indenlandsk køb]
- tid: date range 2009-01-01 to 2025-04-01
dim docs: /dim/db.md

notes:
- Quarterly time series (tid steps are quarterly) — the most granular branche breakdown available.
- belob is a measurement selector: pick exactly one per query (0/1/3/4). No saeson column.
- branche07 uses 6-digit codes that are the standard DB07 niveau 5 (5-digit) codes with a leading zero prepended: '011100' → dim.db kode '11100'. Join with: LTRIM(f.branche07, '0') = d.kode::text AND d.niveau = 5. This works for 524 of the 527 distinct codes (99.4%).
- 3 codes have no dim match: 'TOT' (total across all branches), '999999' (uoplyst/unknown industry), '429000' (a custom aggregate for anlægsarbejder).
- To get labelled results: JOIN dim.db d ON LTRIM(f.branche07,'0') = d.kode::text AND d.niveau = 5, then handle TOT/999999/429000 separately if needed.
- Use ColumnValues("db", "titel", for_table="fiks44") is NOT reliable here due to the 6-digit vs 5-digit mismatch. Instead use ColumnValues("fiks44", "branche07") for raw codes, or query dim.db directly with the stripped join.