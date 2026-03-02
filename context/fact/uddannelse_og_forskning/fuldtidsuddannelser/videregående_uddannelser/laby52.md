table: fact.laby52
description: Gennemsnitlig afstand til videregående uddannelse efter kommunegruppe, uddannelse og tid
measure: indhold (unit Km)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- uddannelse: values [H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser]
- tid: date range 2008-01-01 to 2021-01-01
dim docs: /dim/kommunegrupper.md

notes:
- indhold is average distance in km — not a count. Do not SUM across rows; each (komgrp, uddannelse, tid) cell is already an average. Use the values directly or compare across groups.
- komgrp joins dim.kommunegrupper at niveau=1 only (5 kommunegrupper: Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner). No finer geography is available in this table.
- uddannelse uses only the 5 top-level education type codes (H40/H50/H60/H70/H80). No sub-categories — one row per education type per kommunegruppe per year.
- This is the only table in the subject with geography — use it when the question involves regional variation in access to education. Data ends 2021.
- Sample query: SELECT f.tid, d.titel, f.uddannelse, f.indhold FROM fact.laby52 f JOIN dim.kommunegrupper d ON f.komgrp=d.kode WHERE f.uddannelse='H60' ORDER BY f.tid, f.komgrp;