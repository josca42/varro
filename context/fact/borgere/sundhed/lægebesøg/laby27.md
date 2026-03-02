table: fact.laby27
description: Borgere pr. lægekapacitet efter kommunegruppe og tid
measure: indhold (unit Antal)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- tid: date range 2015-01-01 to 2023-01-01
dim docs: /dim/kommunegrupper.md
notes:
- indhold = number of citizens per doctor capacity (ratio, not a headcount). Represents how loaded each doctor is.
- komgrp joins dim.kommunegrupper with niveau 1 (5 kommunegrupper) and niveau 2 (individual kommuner). komgrp=0 is a national total not in the dim — exclude when joining.
- No age/gender breakdown. Data 2015-2023.
