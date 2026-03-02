table: fact.laby19a
description: Befolkningens højest fuldførte uddannelse (15-69 år) (andel i procent)) efter kommunegruppe, højest fuldførte uddannelse og tid
measure: indhold (unit Andel i pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- hfudd2: join dim.ddu_udd on hfudd2=kode [approx: H prefix needs stripping]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/ddu_udd.md, /dim/kommunegrupper.md

notes:
- indhold is percentage (Andel i pct.) — never sum across rows. Each value is the share of a kommunegruppe's population with that education level.
- komgrp has only the 5 kommunegruppe types (1-5) + 0 (national total, not in dim.kommunegrupper). No individual municipality codes (use laby19 for municipality detail).
- hfudd2 does NOT join dim.ddu_udd — see laby19 notes. In this table hfudd2 has only 11 top-level codes (H10-H90 + TOT), no subcodes, so the hierarchy issue doesn't apply here.
- Comparing kommunegrupper percentages: filter komgrp to each of 1-5 and a specific hfudd2, then compare indhold values across groups. Code 0 gives the national reference value.