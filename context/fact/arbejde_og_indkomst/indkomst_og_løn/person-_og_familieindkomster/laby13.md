table: fact.laby13
description: Personer med offentlige overførsler som hovedindkomstkilde efter kommunegruppe, alder og tid
measure: indhold (unit Andel i pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- alder: values [TOT=Alder i alt, 16-29=16-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-=60 år og derover]
- tid: date range 2005-01-01 to 2024-01-01
dim docs: /dim/kommunegrupper.md
notes:
- indhold = Andel i pct. (percentage of people whose main income is public transfers). Do not sum across komgrp or alder values.
- komgrp joins dim.kommunegrupper at levels 1 and 2. komgrp='0' is the national aggregate — not in dim. Filter WHERE d.niveau=2 for specific municipality groups.
- alder='TOT' is the total across all ages.
- Simple table with no enhed selector. Just filter komgrp and alder to one value each.
