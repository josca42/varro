table: fact.laby42
description: Årsværk på folkebiblioteker pr. 1000 indbygger efter kommunegruppe, personalekategori og tid
measure: indhold (unit Antal)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- personkat: values [10000=Årsværk i alt, 10270=Assistenter, 10260=Bibliotekarer, 10290=Øvrigt akademisk personale, 10280=Øvrigt personale, 10297=Personale i beskæftigelsesordning]
- tid: date range 2016-01-01 to 2024-01-01
dim docs: /dim/kommunegrupper.md
notes:
- komgrp joins dim.kommunegrupper at niveau 1 only: 1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner. komgrp=0 = Hele landet (not in dim.kommunegrupper — use WHERE komgrp='0' directly).
- personkat: same categories as bib8. 10000=Årsværk i alt is the total — don't sum with other categories.
- indhold is FTE per 1000 inhabitants (a rate) — don't sum across kommunegrupper, as this is not additive.
- For absolute FTE counts, use bib8. For per-inhabitant comparison across municipality types, use this table.
