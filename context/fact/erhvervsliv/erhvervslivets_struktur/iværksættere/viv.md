table: fact.viv
description: Nye højvækstvirksomheder efter branche (DB07 10-grp), variable og tid
measure: indhold (unit -)
columns:
- branchedb0710: join dim.db_10 on branchedb0710=kode::text [approx]; levels [1]
- varia: values [A=Nye højvækstvirksomheder (antal), B=Fuldtidsansatte startår (antal), C=Fuldtidsansatte slutår (antal), D=Omsætning startår (kr.), E=Omsætning slutår (kr.)]
- tid: date range 2004 to 2024
dim docs: /dim/db_10.md

notes:
- varia is a measurement selector — each branche+tid combination repeats 5 times (A through E). Always filter to one value: A=antal højvækstvirksomheder, B=FTE startår, C=FTE slutår, D=omsætning startår (kr.), E=omsætning slutår (kr.). Summing across varia is meaningless.
- tid uses 4-year rolling windows like [2004,2008), [2005,2009) etc. Each window tracks firms founded in the start year over 4 years. Pick one window; don't sum across windows (same firm cohort appears in overlapping windows).
- branchedb0710 joins dim.db_10 at niveau 1 (koder 1–11). TOT is a national aggregate not in the dim. Only a subset of DB10 groups appear (industries without meaningful high-growth activity are absent).
- Use this for confirmed historical series from 2004. Use fviv for the latest preliminary year.