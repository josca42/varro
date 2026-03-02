table: fact.sitc2r4m
description: Værdi af import og eksport (1000 kr.) efter SITC-hovedgrupper, land, im- og eksport og tid
measure: indhold (unit 1.000 kr.)
columns:
- sitc: join dim.sitc on sitc=kode [approx: Special codes TOT/8H not in dimension]; levels [2]
- land: join dim.lande_uhv on land=kode [approx: Aggregate codes missing from dimension]; levels [4]
- indud: values [1=Import, 2=Eksport]
- tid: date range 2007-01-01 to 2021-12-01
dim docs: /dim/lande_uhv.md, /dim/sitc.md

notes:
- sitc is at niveau 2 (66 SITC groups). TOT and H-suffix codes not in dim.sitc.
- Unlike sitc2r4, this table has no uhbegreb column — no measurement selector doubling. Simpler to query.
- land aggregate codes (W1, 9A, etc.) are not in dim.lande_uhv. land codes are niveau 4 (countries).
- Monthly data 2007–2021. Use sitc2r4 for 2022–present. Use sitc2r4y for annual aggregates.