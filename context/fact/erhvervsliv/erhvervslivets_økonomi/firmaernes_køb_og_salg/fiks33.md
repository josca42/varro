table: fact.fiks33
description: Firmaernes køb og salg (36 og 127-grupperingen) efter branche (DB07), beløb og tid
measure: indhold (unit Mio. kr.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [5]
- belob: values [4=Salg i alt, 1=Indenlandsk salg, 3=Køb i alt, 0=Indenlandsk køb]
- tid: date range 2009-01-01 to 2025-08-01
dim docs: /dim/db.md

notes:
- Monthly time series with 127 industry codes (the "36 og 127-grupperingen").
- belob is a measurement selector: pick exactly one per query (0=Indenlandsk køb, 1=Indenlandsk salg, 3=Køb i alt, 4=Salg i alt). No saeson column — only one adjustment is provided.
- branche07 uses a DST-specific 5-digit coding scheme that does NOT join to dim.db (only ~8% match). The codes follow a pattern: first 2 digits = NACE division number (zero-padded), last 3 digits = 000 for division-level aggregates or a sub-group index. Examples: 01000 = division 01 (Agriculture) aggregate, 10001/10002 = sub-groups within division 10 (Food manufacturing).
- 47 of the 127 codes end in '000' (division-level), 80 have finer sub-group codes. These are not the same as dim.db niveau 5 codes and no clean join exists.
- Use ColumnValues("fiks33", "branche07") for the full list of 127 codes with Danish labels.