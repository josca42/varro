table: fact.dod
description: Døde efter alder, køn og tid
measure: indhold (unit Antal)
columns:
- alder: values [TOT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 95=95 år, 96=96 år, 97=97 år, 98=98 år, 99-=99 år og derover]
- kon: values [M=Mænd, K=Kvinder]
- tid: date range 1974-01-01 to 2024-01-01

notes:
- kon has no total row — only M and K. To get both sexes combined, SUM(indhold) across M and K.
- alder has 101 values: individual years 0–98, plus '99-' (99 og derover), plus 'TOT'. Filter alder='TOT' for all-ages totals; avoid mixing TOT with individual years.
- Simplest all-ages count by year: SELECT tid, kon, SUM(indhold) FROM fact.dod WHERE alder='TOT' GROUP BY tid, kon.