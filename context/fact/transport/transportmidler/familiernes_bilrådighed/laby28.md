table: fact.laby28
description: Familiernes bilrådighed (faktiske tal) efter kommunegruppe, rådighedsmønster og tid
measure: indhold (unit Antal)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- raadmoens: values [10000=Familier i alt, 10200=Familier uden bil i alt, 10210=Familier med bil i alt, 10220=Familier med 1 bil i alt, 10230=Familier med personbil, 10240=Familier med firmabil, 10250=Familier med varebil, 10260=Familier med 2 biler i alt, 10270=Familier med 2 personbiler, 10280=Familier med 2 firmabiler, 10290=Familier med 2 varebiler, 10300=Familier med 1 personbil og 1 firmabil, 10310=Familier med 1 personbil og en varebil, 10320=Familier med 1 firmabil og 1 varebil, 10330=Familier med 3 biler i alt, 10340=Familier med flere end 3 biler]
- tid: date range 2013-01-01 to 2024-01-01
dim docs: /dim/kommunegrupper.md
notes:
- komgrp joins dim.kommunegrupper (niveau 1 only: 5 kommunegrupper). komgrp=0 is the national total (Hele landet) — not in dim. For national totals, filter WHERE komgrp='0' without joining.
- raadmoens is hierarchical — pick one level. See bil800 for hierarchy.
- Only available 2013-2024. Use bil800 for regional (NUTS) breakdown or longer series.
