table: fact.laby09
description: Folketingsvalg efter kommunegruppe, valgresultat og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode [approx]; levels [1, 2]
- valres: values [STEMPCT=Stemmeprocent, UGYLPCT=Ugyldighedsprocent, BREVPCT=Brevstemmeprocent, BLANKPCT=Blank stemmeprocent, PERSPCT=Personlig stemmeprocent]
- tid: date range 2007-01-01 to 2022-01-01
dim docs: /dim/kommunegrupper.md

notes:
- komgrp joins dim.kommunegrupper. Both niveau 1 (5 kommunegrupper) and niveau 2 (98 kommuner) are present in the table. Filter d.niveau to pick one granularity and avoid double-counting rows.
- Two unmatched codes: 0 (national aggregate, "Hele landet") and 411 (unknown territory, not present in dim.kommunegrupper — likely a special administrative unit). Both appear 25 rows each. Exclude them when joining to dim, or handle separately.
- valres has 5 mutually exclusive percentage metrics. Filter to the one you need (usually STEMPCT for turnout). Never sum across valres.
- Use ColumnValues("kommunegrupper", "titel", for_table="laby09") to see which kommunegrupper are present (5 at niveau 1, 98 at niveau 2).
