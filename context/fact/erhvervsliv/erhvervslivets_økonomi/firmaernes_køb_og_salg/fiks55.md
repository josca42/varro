table: fact.fiks55
description: Firmaernes køb og salg efter branche (DB07), beløb og tid
measure: indhold (unit Mio. kr.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [2, 3]
- belob: values [4=Salg i alt, 1=Indenlandsk salg, 3=Køb i alt, 0=Indenlandsk køb]
- tid: date range 2009-01-01 to 2024-01-01
dim docs: /dim/db.md

notes:
- Annual time series (tid steps are yearly, 2009–2024). Same branche structure as fiks11 but no saeson column and lower frequency.
- belob is a measurement selector: pick exactly one per query (0=Indenlandsk køb, 1=Indenlandsk salg, 3=Køb i alt, 4=Salg i alt).
- branche07 same two-type structure as fiks11: 13 numeric division codes + 9 letter/aggregate codes (B, C, DE, G, H, I, BDE, TOT, 4). Do not mix types when aggregating — they overlap.
- Join to dim.db: ON f.branche07=d.kode::text AND d.niveau=2. The niveau=2 filter is required because '11' exists at both niveau 2 and niveau 3 in dim.db.
- Use ColumnValues("fiks55", "branche07") to see all 22 codes with labels.