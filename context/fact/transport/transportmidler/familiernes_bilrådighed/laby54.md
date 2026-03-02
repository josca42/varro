table: fact.laby54
description: Familiernes sommerhus- og bilrådighed efter bopælskommunegruppe, boligforhold, rådighedsmønster, sommerhuskommunegruppe og tid
measure: indhold (unit Antal)
columns:
- bopkomgrp: join dim.kommunegrupper on bopkomgrp=kode; levels [1]
- bol: values [TOT1=Boligforhold i alt, 110=Stuehuse til landbrugsejendomme, 120=Parcelhuse, 130=Række-, kæde- og dobbelthuse, 140=Etageboliger, 150=Kollegier, 620=Ejerbolig, 630=Lejerbolig, 650=Uoplyste og andre boliger]
- raadmoens: values [10000=Familier i alt, 10200=Familier uden bil i alt, 10210=Familier med bil i alt, 10211=Familier uden sommerhus i alt, 10212=Familier uden sommerhus og bil, 10213=Familier uden sommerhus med bil, 10214=Familier med sommerhus i alt, 10216=Familier med sommerhus uden bil, 10218=Familier med sommerhus og bil]
- somkom: values [0=Hele landet, 1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner]
- tid: date range 2022-01-01 to 2022-01-01
dim docs: /dim/kommunegrupper.md
notes:
- Single-year snapshot: only 2022 data.
- Two geographic dimensions: bopkomgrp (joins dim.kommunegrupper niveau 1) and somkom (inline 0-5 coding for summer house location). Use bopkomgrp=0/somkom=0 for national totals.
- bol=TOT1 is the total. Unlike bil88, the bol codes here mix boligtype (110-150) and ejerforhold (620-630) — pick ONE scheme. 650=uoplyste og andre.
- raadmoens combines car + summer house combinations — see laby53 notes.
