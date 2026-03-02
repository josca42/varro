table: fact.laby23a
description: Uddannelsesaktivitet i grundskolen pr. 1. oktober (andel i procent) efter kommunegruppe, grundskoleinstitutionstype og tid
measure: indhold (unit Andel i pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode [approx]; levels [1]
- grundskol: values [TOT=I alt, 1011=Efterskoler, 1012=Folkeskoler, 1013=Friskoler og private grundskoler, 1999=Andre skoler]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/kommunegrupper.md

notes:
- indhold is percentage (andel i pct.), not a count. Do not sum across rows — report each komgrp/grundskol cell individually.
- komgrp only niveau 1 (5 kommunegrupper). Codes 0 and 995 are not in dim (national/special aggregates).
- grundskol='TOT' for all school types combined. Very simple table: 5 kommunegrupper × 4 skoleinstitutionstyper × tid.