table: fact.laby16
description: Andel af børn mellem 0-18 år med underretninger efter kommunegruppe og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/kommunegrupper.md

notes:
- Percentage table (Pct.) — indhold is share of 0-18 yr olds with notifications. Never sum; compare directly.
- komgrp joins dim.kommunegrupper which has TWO hierarchy levels in the same table: niveau 1 = 5 kommunetyper (Hovedstad, Storby, Provinsbykommune, Opland, Land); niveau 2 = individual kommuner (~99). Both levels appear in the same query result. Filter WHERE d.niveau=1 for the 5-group comparison, or WHERE d.niveau=2 for individual kommuner.
- Code 0 = national total (not in dim — not returned by JOIN).
- This is the only table in this subject that uses dim.kommunegrupper instead of dim.nuts. It cannot be joined to dim.nuts for regional (landsdel/region) groupings.