table: fact.laby12
description: Nettoformue (median) efter kommunegruppe, alder og tid
measure: indhold (unit Kr.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- alder: values [1802=18 år og derover, 1829=18-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8099=80 år og derover]
- tid: date range 2014-01-01 to 2023-01-01
dim docs: /dim/kommunegrupper.md

notes:
- komgrp joins dim.kommunegrupper at two levels: niveau=1 (5 kommunegrupper) and niveau=2 (98 individual kommuner). komgrp=0 is the national aggregate — not in dim. Filter d.niveau to pick granularity.
- alder='1802' is the total (18+). The 7 age groups are broad (10-year bands). Filter to one alder value.
- indhold is median nettoformue in kr. No form1/enhed/popu selectors needed. Simpler structure than formue11-17.
- Unlike laby11, there is no age standardization here — values are raw medians by age group and kommunegruppe.
- Map: /geo/kommuner.parquet — merge on komgrp=dim_kode when filtered to niveau=2 in dim.kommunegrupper (niveau=2 codes match NUTS niveau=3 kommune codes). Exclude komgrp=0.
