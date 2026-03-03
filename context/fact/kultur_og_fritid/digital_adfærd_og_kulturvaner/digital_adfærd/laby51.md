table: fact.laby51
description: Boliger dækket af fastnetbredbånd efter kommunegruppe, bredbåndshastighed og tid
measure: indhold (unit Andel i pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- bredhast: values [100=Downloadhastighed mindst 500 Mbit/s, 105=Downloadhastighed mindst 1 Gbit/s, 110=Download- og uploadhastighed mindst 100/30 Mbit/s]
- tid: date range 2014-01-01 to 2024-01-01
dim docs: /dim/kommunegrupper.md
notes:
- komgrp joins dim.kommunegrupper. Both niveau 1 (5 kommunegrupper) and niveau 2 (98 kommuner) are present in the fact table. Filter WHERE d.niveau = 1 for kommunegruppe-level or d.niveau = 2 for individual kommuner. Mixing both levels doubles counts.
- komgrp=0 is the national total ("I alt") — not present in dim.kommunegrupper. Filter komgrp != '0' when joining, or use komgrp='0' to get the national figure without joining.
- bredhast has 3 threshold values (500 Mbit/s, 1 Gbit/s, 100/30 Mbit/s). These are not cumulative — each is an independent coverage measure. Do not sum.
- Use ColumnValues("kommunegrupper", "titel", for_table="laby51") to see which codes are present (note: kode 0 will be excluded as it is not in the dim table).
- Map: /geo/kommuner.parquet — merge on komgrp=dim_kode when filtered to niveau 2 (individual kommuner). Exclude komgrp=0.
