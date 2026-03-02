table: fact.laby29a
description: Beskæftigede lønmodtagere (ultimo november) (andel i pct.) efter kommunegruppe, sektor og tid
measure: indhold (unit Andel i pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- sektor: join dim.esr_sekt on sektor::text=kode [approx]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/esr_sekt.md, /dim/kommunegrupper.md
notes:
- indhold is a share in percent (andel i pct.), NOT a count. Never sum indhold across rows.
- komgrp and sektor do NOT join their respective dim tables (dimension links listed are incorrect). Both are inline coded — see ColumnValues.
- komgrp: 0=Hele landet, 1-5=municipality group types, 950=Uden for Danmark.
- sektor: 1015-1050, same as ras305.
