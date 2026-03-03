table: fact.laby14
description: Negativ nettoformue (andel af befolkningen) efter kommunegruppe, alder og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- alder: values [1802=18 år og derover, 1829=18-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8099=80 år og derover]
- tid: date range 2014-01-01 to 2023-01-01
dim docs: /dim/kommunegrupper.md

notes:
- indhold is a percentage (Pct.) — the share of the population with negative nettoformue. Do not sum across rows.
- komgrp joins dim.kommunegrupper at two levels: niveau=1 (5 kommunegrupper) and niveau=2 (98 individual kommuner). komgrp=0 is the national aggregate — not in dim.
- alder='1802' is the total (18+). Filter to one alder value.
- Same structure as laby12 but measuring the share in debt rather than the median. Useful for understanding debt prevalence rather than central tendency.
- Map: /geo/kommuner.parquet — merge on komgrp=dim_kode when filtered to niveau=2 in dim.kommunegrupper (niveau=2 codes match NUTS niveau=3 kommune codes). Exclude komgrp=0.
