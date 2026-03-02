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
- indud must always be filtered: 415=Import, 430=Eksport. Never sum across both.
- nation mixes niveau 1 (5 continents: 51-55) and niveau 4 (20 individual countries). Filter WHERE d.niveau = 4 for specific countries or WHERE d.niveau = 1 for continental totals. TOT = overall total, not in dim — use WHERE nation = 'TOT' directly.
- sitc is consistently niveau 2 (SITC groups, 2-digit codes like 00, 01 ... 43). No level mixing — safe to join dim.sitc without a niveau filter. Use ColumnValues("sitc", "titel", for_table="oeko66") to see the 16 product groups available.
- sitc code '49' is present in the fact table but missing from dim.sitc — it appears to be a DST-specific residual oil/fats category. It cannot be labelled via a join; handle it as an inline code.
- TOT in sitc = total across all SITC groups; also not in dim. Use WHERE sitc = 'TOT' without a join for the all-goods total.
- oeko66 has a smaller set of countries than oeko55 (~21 nations vs ~112 lands) — it covers only the main trading partners.