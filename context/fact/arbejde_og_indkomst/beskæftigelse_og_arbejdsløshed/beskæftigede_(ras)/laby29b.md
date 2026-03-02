table: fact.laby29b
description: Beskæftigede lønmodtagere (ultimo november) (andel i pct.) efter kommunegruppe, alder og tid
measure: indhold (unit Andel i pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- alder: values [029=29 år og derunder, 3044=30-44 år, 4559=45-59 år, 6099=60 år og derover, 9999=Uoplyst alder]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/kommunegrupper.md
notes:
- indhold is a share in percent (andel i pct.), NOT a count. Never sum indhold across rows.
- komgrp does NOT join dim.kommunegrupper — use inline values (0=Hele landet, 1-5=municipality groups, 950=Uden for Danmark).
- alder uses coarse groups: 029=29 år og derunder, 3044=30-44 år, 4559=45-59 år, 6099=60 år og derover, 9999=Uoplyst.
- These are age distribution shares within each municipality group.
