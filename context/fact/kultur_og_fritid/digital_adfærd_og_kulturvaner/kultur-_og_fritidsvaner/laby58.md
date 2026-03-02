table: fact.laby58
description: Frivilligt arbejde efter kommunegruppe og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- tid: date range 2024-01-01 to 2024-01-01
dim docs: /dim/kommunegrupper.md
notes:
- komgrp joins dim.kommunegrupper at niveau=1 only (5 kommunegruppe groups: Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner). komgrp=0 is the national total — not in dim.kommunegrupper, dropped by an inner join.
- Very simple table: only (komgrp, tid). indhold is % who do voluntary work overall. Single 2024 annual observation.
- For the full frequency breakdown of voluntary work use kv2fr1; for voluntary work by area use kv2fr2.
