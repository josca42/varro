table: fact.ligeii4
description: Ligestillingsindikator for indkomst i parforhold efter aldersgrupper, indikator og tid
measure: indhold (unit Pct.)
columns:
- aldgrp: values [TOT3=20-64 år i alt, 2029=20-29 år, 3044=30-44 år, 4559=45-59 år, 6064=60-64 år]
- kvindandel: values [P0050=Manden har størst indkomst, P50100=Kvinden har størst indkomst, D0025=Kvinden har under 25 pct., D2535=Kvinden har 25-35 pct. af parrets indkomst, D3540=Kvinden har 35-40 pct. af parrets indkomst, D4045=Kvinden har 40-45 pct. af parrets indkomst, D4550=Kvinden har 45-50 pct. af parrets indkomst, D5055=Kvinden har 50-55 pct. af parrets indkomst, D5560=Kvinden har 55-60 pct. af parrets indkomst, D6065=Kvinden har 60-65 pct. af parrets indkomst, D6575=Kvinden har 65-75 pct. af parrets indkomst, D75100=Kvinden har over 75 pct. af parrets indkomst]
- tid: date range 1987-01-01 to 2024-01-01
notes:
- indhold = Pct. (percentage of couples in each income-share category). Do not sum across kvindandel values.
- kvindandel has two summary codes (P0050=manden størst, P50100=kvinden størst) and 10 detailed brackets (D0025 through D75100) of the woman's income share. The summary codes are independent of the D-codes — don't mix them in sums.
- aldgrp='TOT3' covers 20-64 år i alt. Only 4 age groups (all broad).
- No geography and no enhed/prisenhed selectors — simpler than other tables in this subject.
- Goes back to 1987.
