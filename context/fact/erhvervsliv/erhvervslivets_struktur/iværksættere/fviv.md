table: fact.fviv
description: Foreløbige nye højvækstvirksomheder efter branche (DB07 10-grp), variable og tid
measure: indhold (unit -)
columns:
- branchedb0710: join dim.db_10 on branchedb0710=kode::text [approx]; levels [1]
- varia: values [A=Nye højvækstvirksomheder (antal), B=Fuldtidsansatte startår (antal), C=Fuldtidsansatte slutår (antal), D=Omsætning startår (kr.), E=Omsætning slutår (kr.)]
- tid: date range 2020 to 2024
dim docs: /dim/db_10.md

notes:
- varia is a measurement selector — each branche+tid combination repeats 5 times (A through E). Always filter to one value: A=antal højvækstvirksomheder, B=FTE startår, C=FTE slutår, D=omsætning startår (kr.), E=omsætning slutår (kr.). Summing across varia is meaningless.
- tid uses 4-year windows in interval notation: e.g. [2020,2024) means firms founded 2020 tracked over 4 years to 2024. Filter to one specific window when computing counts.
- branchedb0710 joins dim.db_10 at niveau 1 (koder 1–11). TOT is a national aggregate not in the dim — filter it out when joining. Only 8 of 11 DB10 groups appear (landbrug, finansiering, offentlig are absent — high-growth firms are rare there).
- This is preliminary data (foreløbig). Use viv for the confirmed historical series from 2004.