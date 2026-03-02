table: fact.sitc5r4
description: Im- og eksport (1.000 kr.) efter SITC-hovedgrupper, land, im- og eksport, enhed, varebegreb og tid
measure: indhold (unit -)
columns:
- sitc: join dim.sitc on sitc=kode [approx: 5-digit codes match; special codes HHHHH/TOT not in dimension]; levels [3]
- land: join dim.lande_uhv on land=kode [approx: Aggregate codes W1/9A/QX missing from dimension]; levels [4]
- indud: values [1=Import, 2=Eksport]
- enhed: values [98=Kilo, 99=Kroner]
- uhbegreb: values [GP=Udenrigshandel med varer (Grænsepassageprincip), ES=Udenrigshandel med varer (Ejerskifteprincip)]
- tid: date range 2022-01-01 to 2025-08-01
dim docs: /dim/lande_uhv.md, /dim/sitc.md

notes:
- sitc is at niveau 3 (5-digit SITC subgroups, ~2925 codes) — most granular. HH-suffix codes (e.g. 025HH, 033HH) and HHHHH/TOT are confidential aggregates not in dim.sitc. Use ColumnValues("sitc", "titel", for_table="sitc5r4") to browse available subgroups.
- enhed is a MEASUREMENT SELECTOR: every combination appears twice (98=Kilo, 99=Kroner). Always filter — enhed='99' for DKK, enhed='98' for quantity in kg.
- uhbegreb is a MEASUREMENT SELECTOR: every combination appears twice more (GP vs ES trade valuation). Always filter — typically GP.
- Combined: without filtering enhed and uhbegreb, row counts are 4× inflated.
- land aggregate codes (W1, RS, etc.) not in dim.lande_uhv. land codes are niveau 4.
- Current monthly series 2022–present. For historical monthly see sitc5r4m (2007–2013). For annual see sitc5r4y (2007–2021).