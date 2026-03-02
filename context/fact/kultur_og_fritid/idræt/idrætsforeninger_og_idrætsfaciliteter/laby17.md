table: fact.laby17
description: Idrætsforeningernes medlemmer (andel af befolkningen) efter kommunegruppe og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- tid: date range 2014-01-01 to 2024-01-01
dim docs: /dim/kommunegrupper.md

notes:
- indhold is a percentage (Pct.) — share of the population that are sports club members. Do NOT sum across kommunegrupper; compare them instead.
- komgrp joins dim.kommunegrupper at niveau 1 only (5 groups: Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner). komgrp=0 is the national total, not in dim.kommunegrupper.
- Very simple two-column table. A bare query with no filters other than tid is valid for a national trend.