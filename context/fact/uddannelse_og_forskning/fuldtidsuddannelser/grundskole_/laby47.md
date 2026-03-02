table: fact.laby47
description: Andel af børn i grundskolen, som har mindre end 2 km til skole efter kommunegruppe og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- tid: date range 2008-01-01 to 2021-01-01
dim docs: /dim/kommunegrupper.md

notes:
- indhold is pct. (percentage of children within 2 km of school). Do not sum — report each komgrp value separately.
- komgrp niveau 1 only (5 kommunegrupper), full match with dim. Very simple table: 5 rows per year.
- Data ends 2021 — use for historical trend, not current year.