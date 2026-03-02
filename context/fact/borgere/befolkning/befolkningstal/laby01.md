table: fact.laby01
description: Befolkningstilvækst pr. 1.000 indbyggere efter kommunegruppe, bevægelsesart og tid
measure: indhold (unit Pr. 1.000 indb.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode [approx]; levels [1, 2]
- bevaegelse: values [B04=Fødselsoverskud, B07=Nettotilflyttede, B10=Nettoindvandrede, B11=Befolkningstilvækst]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/kommunegrupper.md

notes:
- indhold is a rate (per 1,000 inhabitants), not a count. Do NOT sum across komgrp — rates at different levels are not additive.
- komgrp contains three distinct levels mixed together: 0=national total (not in dim), 1–5=kommunegruppe categories (niveau=1 in dim), individual municipality codes 101–860 (niveau=2 in dim). Always filter to one level.
- bevaegelse B11=Befolkningstilvækst = B04+B07+B10 (the three components sum to total growth). Never sum all four bevaegelse codes as B11 is already a composite.
- komgrp=411 is an unmatched code (likely a historical municipality) — appears in data but not in dim.kommunegrupper.
- ColumnValues("kommunegrupper", "titel") for the 5 group names; ColumnValues("kommunegrupper", "titel", for_table="laby01") for all individual municipality codes present.