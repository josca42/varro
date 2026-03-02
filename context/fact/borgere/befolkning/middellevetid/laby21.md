table: fact.laby21
description: Middellevetid for 0-årige efter kommunegruppe, køn og tid
measure: indhold (unit År)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2006 to 2025
dim docs: /dim/kommunegrupper.md

notes:
- komgrp=0 is "Hele landet" (national aggregate) — not in dim.kommunegrupper. The 5 groups use codes 1–5 (niveau=1): Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner. dim.kommunegrupper also has niveau=2 (individual kommuner), but laby21 only uses niveau=1 codes.
- kon has TOT; must filter to one value to avoid tripling counts.
- Use ColumnValues("kommunegrupper", "titel", for_table="laby21") to confirm the 5 groups available.
