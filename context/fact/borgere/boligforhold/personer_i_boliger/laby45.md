table: fact.laby45
description: Andel af befolkningen, der bor til leje efter kommunegruppe og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- tid: date range 2010-01-01 to 2025-01-01
dim docs: /dim/kommunegrupper.md

notes:
- komgrp=0 is "Hele landet" (national total) — not in dim.kommunegrupper (which only has kode 1-5). Use WHERE f.komgrp = 0 for national figure, or JOIN dim.kommunegrupper d ON f.komgrp = d.kode for the 5 kommunegrupper (skips komgrp=0).
- indhold is Pct. (share of population renting). Do not SUM across komgrp values — they are independent rates.
- Very simple table: 2 dimension columns only (komgrp + tid). Straightforward to query.