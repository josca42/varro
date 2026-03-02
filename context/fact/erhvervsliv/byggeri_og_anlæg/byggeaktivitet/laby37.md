table: fact.laby37
description: Nybyggeri (ikke korrigeret for forsinkelser) efter kommunegruppe, anvendelse og tid
measure: indhold (unit M2)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- anvend: join dim.byganv on anvend=kode::text [approx]; levels [2, 3]
- tid: date range 2006-01-01 to 2025-04-01
dim docs: /dim/byganv.md, /dim/kommunegrupper.md
notes:
- komgrp joins dim.kommunegrupper but code '0' (national total) is not in the dim. dim.kommunegrupper: niveau 1=5 kommunegrupper (Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner), niveau 2=individual kommuner. Filter `WHERE d.niveau=1` for the 5 groups, niveau 2 for individual kommuner; avoid mixing levels in aggregates.
- anvend joins dim.byganv at niveauer 2 and 3. Code 'UOPL' is not in the dim.
- This table only covers nybyggeri (new construction), not tilbygning or ombygning. For all byggeri types by region use bygv11 (m2) or bygv33 (boliger antal).
