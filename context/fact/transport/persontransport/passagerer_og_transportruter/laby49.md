table: fact.laby49
description: Andel af befolkningen med adgang til offentlig transport efter kommunegruppe, serviceniveau og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- sdgservice: values [1345=Meget højt serviceniveau, 1350=Højt serviceniveau, 1355=Middel serviceniveau, 1360=Lavt serviceniveau, 1365=Intet serviceniveau]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/kommunegrupper.md

notes:
- komgrp joins dim.kommunegrupper at niveau 1 only (5 kommunegrupper: Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner). All 5 match cleanly.
- sdgservice values sum to ~100% per group per year — they form a complete distribution (mutually exclusive shares of the population). Never sum across all sdgservice as that gives ~100, not a meaningful total. To get "% with at least medium service" sum sdgservice IN (1345, 1350, 1355).
- Only 2 time points in the data: 2019 and 2023. Not useful for trend analysis.
- No "I alt" row for sdgservice — all 5 categories always present for each komgrp.