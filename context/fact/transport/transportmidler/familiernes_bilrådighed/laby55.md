table: fact.laby55
description: Familiernes sommerhus- og bilrådighed efter bopælskommunegruppe, indkomst, rådighedsmønster, sommerhuskommunegruppe og tid
measure: indhold (unit Antal)
columns:
- bopkomgrp: join dim.kommunegrupper on bopkomgrp=kode; levels [1]
- indkom: values [0DC=I alt, 1DC=1. decil, 2DC=2. decil, 3DC=3. decil, 4DC=4. decil, 5DC=5. decil, 6DC=6. decil, 7DC=7. decil, 8DC=8. decil, 9DC=9. decil, 10DC=10. decil, 1KV=1. kvartil, 2KV=2. kvartil, 3KV=3. kvartil, 4KV=4. kvartil]
- raadmoens: values [10000=Familier i alt, 10200=Familier uden bil i alt, 10210=Familier med bil i alt, 10211=Familier uden sommerhus i alt, 10212=Familier uden sommerhus og bil, 10213=Familier uden sommerhus med bil, 10214=Familier med sommerhus i alt, 10216=Familier med sommerhus uden bil, 10218=Familier med sommerhus og bil]
- somkom: values [0=Hele landet, 1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner]
- tid: date range 2022-01-01 to 2022-01-01
dim docs: /dim/kommunegrupper.md
notes:
- Single-year snapshot: only 2022 data.
- Two geographic dimensions: bopkomgrp (joins dim.kommunegrupper niveau 1) and somkom (inline 0-5, summer house location). Use 0 for national totals in each.
- indkom uses decils (1DC-10DC) and quartiles (1KV-4KV) only — simpler than bil86 which also has income bands. 0DC=I alt is the total. Decils and quartiles overlap; pick ONE scheme.
- raadmoens combines car + summer house combinations — see laby53 notes.
