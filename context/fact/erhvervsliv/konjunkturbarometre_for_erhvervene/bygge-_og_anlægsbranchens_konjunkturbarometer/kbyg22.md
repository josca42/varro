table: fact.kbyg22
description: Vurdering af ordrebeholdningen i bygge og anlæg efter branche (DB07), bedømmelse og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db_10 on branche07=kode::text [approx]; levels [2]
- bedommelse: values [MN1=Ikke tilstrækkelig, NOR1=Tilstrækkelig, SNO1=Mere end tilstrækkelig, NET=Nettotal]
- tid: date range 2005-01-01 to 2025-10-01
dim docs: /dim/db_10.md

notes:
- branche07 does NOT join dim.db_10 — same DST survey groupings as kbyg11. Use ColumnValues("kbyg22", "branche07") for labels. F = total sector.
- bedommelse contains NET (derived: NET = %SNO1 − %MN1). Never sum across bedommelse values — MN1/NOR1/SNO1/NET are four views of the same survey responses. Use NET for trend analysis.
- To get a single series: filter branche07 and bedommelse=NET, then SELECT tid, indhold.