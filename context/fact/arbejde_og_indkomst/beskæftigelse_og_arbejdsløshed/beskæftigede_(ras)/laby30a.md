table: fact.laby30a
description: Beskæftigede lønmodtagere (60 år og derover) i offentlig forvaltning og service (ultimo november) (andel i pct.) efter kommunegruppe, sektor og tid
measure: indhold (unit Andel i pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- sektor: join dim.esr_sekt on sektor::text=kode [approx]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/esr_sekt.md, /dim/kommunegrupper.md
notes:
- indhold is a share in percent (andel i pct.), NOT a count. Never sum indhold across rows.
- Covers only employees aged 60+ in public sector (offentlig forvaltning og service).
- komgrp and sektor do NOT join their respective dim tables — use inline values. komgrp: 0=Hele landet, 1-5 groups, 950=Uden for Danmark. sektor: 1015=Stat, 1020=Regioner, 1025=Kommuner, 1030=Sociale kasser.
