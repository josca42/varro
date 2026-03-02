table: fact.laby05
description: Personer, der bor i samme kommunegruppe som for 20 år siden efter kommunegruppe, alder og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- alder: values [35=35 år, 55=55 år, 75=75 år]
- tid: date range 2007-01-01 to 2025-01-01
dim docs: /dim/kommunegrupper.md

notes:
- indhold = % of people currently in this kommunegruppe who also lived in the same group 20 years ago. A measure of geographic stability/retention.
- Only 3 alder values (35, 55, 75) — these are snapshot cohort ages, not age ranges.
- komgrp=0 (national total) present but not in dim. niveau=1 only (5 group codes).
- Values are independent percentages per komgrp-alder combination — do not sum across komgrp or alder.