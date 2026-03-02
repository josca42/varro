table: fact.sitc2r4
description: Værdi af import og eksport (1000 kr.) efter SITC-hovedgrupper, land, im- og eksport, varebegreb og tid
measure: indhold (unit 1.000 kr.)
columns:
- sitc: join dim.sitc on sitc=kode [approx: Special codes TOT/8H not in dimension]; levels [2]
- land: join dim.lande_uhv on land=kode [approx: Aggregate codes W1/9A/QX missing from dimension]; levels [4]
- indud: values [1=Import, 2=Eksport]
- uhbegreb: values [GP=Udenrigshandel med varer (Grænsepassageprincip), ES=Udenrigshandel med varer (Ejerskifteprincip)]
- tid: date range 2022-01-01 to 2025-09-01
dim docs: /dim/lande_uhv.md, /dim/sitc.md

notes:
- sitc is at niveau 2 (66 SITC groups). TOT (all goods) and H-suffix codes (0H, 2H…8H) are not in dim.sitc — H-codes are confidential aggregates for specific countries (e.g. EU institutions at land=4A). Filter these out or handle explicitly.
- uhbegreb is a MEASUREMENT SELECTOR that exactly doubles the row count: GP=Grænsepassageprincip, ES=Ejerskifteprincip. These are two trade valuation methods for the same flows. Always filter to one — typically GP for standard foreign trade statistics.
- land aggregate codes (W1=World, 9A, QX, 4A, 4F, 4S, GG, IM, JE, RS etc.) are not in dim.lande_uhv. W1 is the world total. Filter or handle explicitly.
- land is at niveau 4 (individual countries). Use ColumnValues("lande_uhv", "titel", for_table="sitc2r4") to see which countries are present.
- Current monthly value series (2022–present). For historical monthly see sitc2r4m (2007–2021). For annual see sitc2r4y. For 5-digit SITC granularity see sitc5r4.