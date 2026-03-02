table: fact.laby31
description: Beskæftigede lønmodtagere i virksomheder og organisationer (ultimo november) efter kommunegruppe, branche (DB07), alder og tid
measure: indhold (unit Antal)
columns:
- komgrp: values [0=Hele landet, 1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner, 950=Uden for Danmark]
- branche07: join dim.db on branche07=kode::text
- alder: values [TOT=Alder i alt, 029=29 år og derunder, 3044=30-44 år, 4559=45-59 år, 6099=60 år og derover, 9999=Uoplyst alder]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- Covers only lønmodtagere in virksomheder og organisationer (private sector). Complements laby30 which covers the public sector.
- branche07 uses DB07-37-group letter codes (A, B, CA...) — does NOT join dim.db. Use ColumnValues("laby31", "branche07").
- komgrp: 0=Hele landet, 1-5 groups, 950=Uden for Danmark. Filter to komgrp=0 for national.
- alder has TOT plus 4 coarse groups (029, 3044, 4559, 6099) plus 9999=Uoplyst.
