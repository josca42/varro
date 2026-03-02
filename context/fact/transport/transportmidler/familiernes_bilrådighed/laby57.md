table: fact.laby57
description: Familiernes sommerhus- og bilrådighed efter bopælskommunegruppe, familietype, rådighedsmønster, sommerhuskommunegruppe og tid
measure: indhold (unit Antal)
columns:
- bopkomgrp: join dim.kommunegrupper on bopkomgrp=kode; levels [1]
- famtyp: values [FAIA=Familier i alt, FAUB=Familier uden børn, FAMB=Familier med børn, PAUB=Par uden børn, PAMB=Par med børn, PAFA=Parfamilier i alt, IHJB=Ikke-hjemmeboende børn, ENIA=Enlige i alt, ENUB=Enlige uden børn, ENMB=Enlige med børn]
- raadmoens: values [10000=Familier i alt, 10200=Familier uden bil i alt, 10210=Familier med bil i alt, 10211=Familier uden sommerhus i alt, 10212=Familier uden sommerhus og bil, 10213=Familier uden sommerhus med bil, 10214=Familier med sommerhus i alt, 10216=Familier med sommerhus uden bil, 10218=Familier med sommerhus og bil]
- somkom: values [0=Hele landet, 1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner]
- tid: date range 2022-01-01 to 2022-01-01
dim docs: /dim/kommunegrupper.md
notes:
- Single-year snapshot: only 2022 data.
- Two geographic dimensions: bopkomgrp (joins dim.kommunegrupper niveau 1) and somkom (inline 0-5, summer house location). Use 0 for national totals in each.
- famtyp has overlapping aggregates: FAIA=all, PAFA=all couples, ENIA=all singles. Pick one level of granularity.
- raadmoens combines car + summer house combinations — see laby53 notes.
