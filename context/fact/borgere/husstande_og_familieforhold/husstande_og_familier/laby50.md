table: fact.laby50
description: Husstandes afstand til nærmeste dagligvarebutik efter kommunegruppe, afstand og tid
measure: indhold (unit Antal)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- afstand: values [600=Under 0,5 km, 605=0,5-1 km, 610=1-2 km, 615=2-3 km, 620=3-4 km, 625=4 km og derover, 630=Uoplyst]
- tid: date range 2009-01-01 to 2022-01-01
dim docs: /dim/kommunegrupper.md

notes:
- komgrp joins dim.kommunegrupper at niveau 1 (5 kommunegrupper: Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner). komgrp='0' is the national total — not in dim.kommunegrupper.
- afstand has 7 values including 630=Uoplyst (unknown distance). The Uoplyst category is very small (~550 households nationally in 2022 for Hovedstadskommuner). When computing distributions, decide whether to include or exclude it.
- indhold is a count of households. The 6 known distance bands are mutually exclusive — summing them gives total households with a known distance. Data ends at 2022.
- Pair with laby50a for percentage shares, but note that laby50a's percentages are NOT within-komgrp shares — see laby50a notes.