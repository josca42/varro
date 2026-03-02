table: fact.lag8s
description: Engroshandlens handelsvarelagre efter branche (DB07), sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- branche07: join dim.db on branche07=kode [approx]; levels [2, 3]
- saeson: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- tid: date range 2001-01-01 to 2025-04-01
dim docs: /dim/db.md

notes:
- DO NOT join branche07 to dim.db. The numeric codes (10–17) match dim.db entries but with completely wrong labels. Use ColumnValues("lag8s", "branche07") to get the correct engroshandel branch names (same 8-code scheme as lag8).
- branche07=17 is "Engroshandel i alt" (total). Exclude it when aggregating across branches.
- saeson is a measurement selector: every branche07/tid combination appears twice (EJSÆSON and SÆSON). Always filter to one value — use EJSÆSON for raw figures, SÆSON for seasonal-adjusted trend analysis.
- indhold is quarterly change in inventory (Mio. kr.), not inventory stock level. Negative values are normal (inventory drawdowns).
- lag8s and lag8 cover identical branches and time range. The difference is the selector dimension: lag8 has prisenhed (ÅRPRIS vs 2015-fixed-prices), lag8s has saeson (seasonal adjustment).