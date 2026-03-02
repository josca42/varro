table: fact.laby25
description: Nøgletal for husholdningsaffald efter kommunegruppe, nøgletal og tid
measure: indhold (unit -)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- bnogle: values [GENPCT=Husholdningsaffald indsamlet til genanvendelse (pct.), AFFALDIND=Husholdningsaffald (kg. pr. indbygger)]
- tid: date range 2013-01-01 to 2022-01-01
dim docs: /dim/kommunegrupper.md
notes:
- komgrp joins dim.kommunegrupper (99% match, same as laby24). komgrp=0 not in dim.
- bnogle has 2 values with different units: GENPCT=recycling rate (%), AFFALDIND=waste per capita (kg/person). Always filter to one — they cannot be summed.
- This is a rate/key-figure table. Do not sum indhold across kommuner — use weighted average or compare individual kommuner.
- Useful for comparing municipalities on recycling performance. Pair with laby24 for absolute tonnage.
- Map: context/geo/kommuner.parquet — filter dim.kommunegrupper to niveau=2, then merge on komgrp=dim_kode. Exclude komgrp=0.
