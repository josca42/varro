table: fact.laby20
description: Hjemmehjælp i eget hjem og plejebolig/plejehjem, andel af befolkning på 67 år og derover efter kommunegruppe, serviceydelser og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- servyd: values [300=Modtagere visiteret til hjemmehjælp, frit valg, 310=Modtagere af hjemmehjælp på plejehjem og plejebolig]
- tid: date range 2022-01-01 to 2024-01-01
dim docs: /dim/kommunegrupper.md

notes:
- komgrp joins dim.kommunegrupper. niveau 1 = 5 kommunegrupper (Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner); niveau 2 = 98 individuelle kommuner. Filter WHERE d.niveau=1 for gruppe-level, d.niveau=2 for kommune-level. komgrp=0 is the national total (not in dim).
- servyd has only 2 values — both are independent percentages of the 67+ population (frit valg hjemmehjælp vs. plejehjem/plejebolig hjemmehjælp). Do not sum them; pick the one relevant to the question.
- Data only from 2022 (3 years). For longer history use aed06/aed07 or aed022/aed021. This is the only table in the subject that breaks down by kommunegruppe type rather than by geographic region.
