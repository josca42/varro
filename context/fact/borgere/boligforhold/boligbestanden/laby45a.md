table: fact.laby45a
description: Andel af familier med sommerhus efter kommunegruppe og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- tid: date range 2022-01-01 to 2022-01-01
dim docs: /dim/kommunegrupper.md

notes:
- indhold is a percentage (Pct.) — do not SUM across komgrp. Use individual group values or WHERE komgrp=0 for the national figure (kode=0 not in dim).
- Only one year of data (2022). Not suitable for trend analysis.
- komgrp joins dim.kommunegrupper, niveau=1 only (5 groups): Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner. kode=0 is the national total (not in dim). ColumnValues("kommunegrupper", "titel") lists all 5 groups.
- Very narrow table: share of families who own a holiday home, by kommune-group, single year. Useful only for that specific question.