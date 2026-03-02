table: fact.laby07
description: Relativ fattigdom (andel af befolkningen) efter kommunegruppe, alder og tid
measure: indhold (unit Pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- alder: values [IALT=Alder i alt, 0117=0-17 år, 1829=18-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8099=80 år og derover]
- tid: date range 2015-01-01 to 2023-01-01
dim docs: /dim/kommunegrupper.md
notes:
- komgrp joins dim.kommunegrupper at BOTH niveau=1 (5 kommunegruppe-types: Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner) and niveau=2 (individual kommuner). Mixing niveaux inflates results — filter to one: WHERE d.niveau = 1 for group comparisons or d.niveau = 2 for individual kommuner.
- alder includes IALT (total) plus 8 age bands. Filter to alder = 'IALT' for overall rates, or pick individual age bands. Do not sum age bands as they are mutually exclusive and IALT already aggregates them.
- indhold is Pct. of population in relative poverty (60% of median income threshold). No indkn column — threshold is fixed at 60%.
- Only covers 2015–2023. See ifor12p for municipality-level poverty shares back to 2000 (at kommune, not kommunegruppe level).
- ColumnValues("kommunegrupper", "titel", for_table="laby07") to see all groups and individual kommuner available.
