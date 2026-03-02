table: fact.laby56
description: Familiernes sommerhus- og bilrådighed efter bopælskommunegruppe, uddannelse, rådighedsmønster, sommerhuskommunegruppe og tid
measure: indhold (unit Antal)
columns:
- bopkomgrp: join dim.kommunegrupper on bopkomgrp=kode; levels [1]
- uddannelse: values [0=Uddannelse i alt, 10=10 GRUNDSKOLE                                               , 20=20 ALMENGYMNASIAL UDDANNELSER                               , 25=25 ERHVERVSGYMNASIAL UDDANNELSER                            , 30=30 ERHVERVSFAGLIGE GRUNDFORLØB                              , 40=40 KORTE VIDEREGÅENDE UDDANNELSER                           , 50=50 MELLEMLANGE VIDEREGÅENDE UDDANNELSER                     , 60=60 BACHELOR                                                 , 65=65 LANGE VIDEREGÅENDE UDDANNELSER                           , 70=70 FORSKERUDDANNELSER                                       , 99=99       UDEN FOR NIVEAU]
- raadmoens: values [10000=Familier i alt, 10200=Familier uden bil i alt, 10210=Familier med bil i alt, 10211=Familier uden sommerhus i alt, 10212=Familier uden sommerhus og bil, 10213=Familier uden sommerhus med bil, 10214=Familier med sommerhus i alt, 10216=Familier med sommerhus uden bil, 10218=Familier med sommerhus og bil]
- somkom: values [0=Hele landet, 1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner]
- tid: date range 2022-01-01 to 2022-01-01
dim docs: /dim/kommunegrupper.md
notes:
- Single-year snapshot: only 2022 data.
- Two geographic dimensions: bopkomgrp (joins dim.kommunegrupper niveau 1) and somkom (inline 0-5, summer house location). Use 0 for national totals in each.
- uddannelse=0 is the total. Individual levels (10-99) have trailing whitespace in codes.
- raadmoens combines car + summer house combinations — see laby53 notes.
