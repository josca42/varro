table: fact.oeko55
description: Udenrigshandel med økologiske varer efter im- og eksport, land og tid
measure: indhold (unit 1.000 kr.)
columns:
- indud: values [415=Import, 430=Eksport]
- land: join dim.lande_uhv on land=kode [approx]; levels [1, 4]
- tid: date range 2003-01-01 to 2023-01-01
dim docs: /dim/lande_uhv.md

notes:
- indud uses non-standard codes: 415=Import, 430=Eksport.
- land has mixed hierarchy levels: niveau 1 (5 continents) and niveau 4 (106 individual countries) appear simultaneously. Filter by d.niveau to avoid double counting: niveau=4 for countries, niveau=1 for continent totals.
- land='TOT' (world total) is not in dim.lande_uhv. Exclude when joining or handle explicitly.
- Annual data 2003–2023. Organic goods only (value in 1.000 kr.). For product breakdown within organic see oeko66 (country+SITC). For product totals without country see oeko4.