<fact tables>
<table>
id: lag8
description: Engroshandlens handelsvarelagre efter branche (DB07), prisenhed og tid
columns: branche07, prisenhed, tid (time), indhold (unit Mio. kr.)
tid range: 2001-01-01 to 2025-04-01
</table>
<table>
id: lag8s
description: Engroshandlens handelsvarelagre efter branche (DB07), sæsonkorrigering og tid
columns: branche07, saeson, tid (time), indhold (unit Mio. kr.)
tid range: 2001-01-01 to 2025-04-01
</table>
</fact tables>

notes:
- Both tables measure quarterly CHANGE in wholesale inventory (lagertilvækst, Mio. kr.), not the inventory stock level. Negative values are normal inventory drawdowns.
- lag8: use when you need price-basis comparison — ÅRPRIS (current prices) vs 2015-fixed prices.
- lag8s: use when you need seasonal adjustment — EJSÆSON (unadjusted) vs SÆSON (seasonally adjusted). Preferred for trend analysis.
- Both tables have identical branch coverage and time range (Q1 2001–Q2 2025).
- branche07 codes (10–17) look like DB07 sector codes but are engroshandel-specific labels. Do NOT join to dim.db — use ColumnValues("lag8", "branche07") to get readable names. Code 17 is the "Engroshandel i alt" total — exclude it when summing across branches.
- The selector column (prisenhed in lag8, saeson in lag8s) doubles all rows. Always filter to one value before aggregating.