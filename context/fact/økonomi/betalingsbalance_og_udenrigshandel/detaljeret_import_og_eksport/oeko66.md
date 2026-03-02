table: fact.oeko66
description: Udenrigshandel med økologiske varer efter im- og eksport, land, SITC-hovedgrupper og tid
measure: indhold (unit 1.000 kr.)
columns:
- indud: values [415=Import, 430=Eksport]
- nation: join dim.lande_uhv on nation=kode [approx]; levels [1, 4]
- sitc: join dim.sitc on sitc=kode [approx]; levels [2]
- tid: date range 2003-01-01 to 2023-01-01
dim docs: /dim/lande_uhv.md, /dim/sitc.md

notes:
- The country column is named `nation` (not `land` like most other tables). Join: JOIN dim.lande_uhv d ON f.nation = d.kode.
- nation has mixed hierarchy: niveau 1 (continent totals) and niveau 4 (countries) appear simultaneously. Filter by d.niveau to avoid double counting.
- nation='TOT' (world total) not in dim.lande_uhv.
- sitc is at niveau 2 (SITC groups, ~16 codes). sitc='TOT' and sitc='49' are not in dim.sitc — exclude or handle explicitly.
- indud: 415=Import, 430=Eksport (non-standard, same as oeko4/oeko55).
- Annual 2003–2023. Organic goods only. For totals by country without product breakdown see oeko55. For totals by product without country see oeko4.