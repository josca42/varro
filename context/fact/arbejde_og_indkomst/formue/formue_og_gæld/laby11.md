table: fact.laby11
description: Median for Nettoformue, 18 år+ efter kommunegruppe, aldersstandardisering og tid
measure: indhold (unit Kr.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- aldersstand: values [3000=Aldersstandardiseret, 3010=Ikke aldersstandardiseret]
- tid: date range 2014-01-01 to 2023-01-01
dim docs: /dim/kommunegrupper.md

notes:
- komgrp joins dim.kommunegrupper at two levels: niveau=1 (5 kommunegrupper: Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner) and niveau=2 (98 individual kommuner). komgrp=0 is the national aggregate — not in dim.
- aldersstand must be filtered: 3000=aldersstandardiseret (accounts for different age distributions across groups), 3010=ikke aldersstandardiseret. For fair comparison across kommunegrupper, use aldersstandardiseret. All rows are doubled — one for each value.
- indhold is always median nettoformue in kr. for adults 18+. No form1/enhed/popu selectors — this table is pre-filtered to a single measure.
- Simpler than formue11-17: only 3 columns to filter (komgrp, aldersstand, tid).
- Map: context/geo/kommuner.parquet — merge on komgrp=dim_kode when filtered to niveau=2 in dim.kommunegrupper (niveau=2 codes match NUTS niveau=3 kommune codes). Exclude komgrp=0.
