table: fact.laby46
description: Gennemsnitlig boligareal pr. person efter kommunegruppe og tid
measure: indhold (unit M2)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- tid: date range 2010-01-01 to 2025-01-01
dim docs: /dim/kommunegrupper.md

notes:
- komgrp=0 is "Hele landet" (national average) — not in dim.kommunegrupper (which only has kode 1-5). Use WHERE f.komgrp = 0 for the national figure, or JOIN dim.kommunegrupper d ON f.komgrp = d.kode for the 5 kommunegrupper.
- indhold is M2 (average floor area per person). Do not SUM — this is an average, not a count.
- Very simple table: 2 dimension columns only (komgrp + tid).