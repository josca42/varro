table: fact.laby10
description: Andel af unge (16-24 år) uden for beskæftigelse og uddannelse (NEET) efter kommunegruppe, alder og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- alder: values [T1624=16-24 år i alt, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/kommunegrupper.md

notes:
- indhold is a percentage (Pct.), not a count. Do not sum rows — you get meaningless averages, not aggregated rates. Use neet1/neet2 for counts.
- komgrp joins dim.kommunegrupper. komgrp='0' is the national total, not in the dim table. Two hierarchy levels: niveau=1 (5 kommunegruppe types: Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner), niveau=2 (98 individual kommuner). Filter d.niveau to pick the right granularity.
- This is the only table in this subject with individual municipality-level NEET percentages. Use it when the question asks for kommuneniveau data.
- alder: T1624=16-24 year olds total, plus 9 individual ages (16-24). Filter to alder='T1624' for the overall NEET percentage. The national NEET rate for 2023 (komgrp='0', alder='T1624') is 9.6%.
- Sample: NEET pct by kommunegruppe type 2023 → JOIN dim.kommunegrupper WHERE d.niveau=1 AND alder='T1624' AND tid='2023-01-01'.
- Map: /geo/kommuner.parquet — merge on komgrp=dim_kode for niveau=2 data (98 kommuner; kodes match dim.nuts niveau=3). Exclude komgrp=0.