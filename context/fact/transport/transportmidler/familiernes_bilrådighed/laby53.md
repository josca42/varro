table: fact.laby53
description: Familiernes sommerhus- og bilrådighed efter bopælskommunegruppe, socioøkonomisk status, rådighedsmønster, sommerhuskommunegruppe og tid
measure: indhold (unit Antal)
columns:
- bopkomgrp: join dim.kommunegrupper on bopkomgrp=kode; levels [1]
- socio: values [TOT=I ALT, 110=Selvstændige, 111=Selvstændige med ansatte, 112=Selvstændige uden ansatte, 130=Lønmodtagere i alt, 131=Topledere, 132=Lønmodtagere højeste niveau, 133=Lønmodtagere mellemniveau, 134=Lønmodtagere grundniveau, 135=Lønmodtagere i øvrigt, 136=Lønmodtagere uden nærmere angivelse, 500=Arbejdsløse , 505=Uden for arbejdsstyrken, 510=Uddannelsessøgende, 515=Pensionister i alt, 520=Folkepensionister, 522=Førtidspensionist, 525=Efterlønsmodtagere mv., 530=Øvrige uden for arbejdsstyrken, 535=Uoplyst socioøkonomisk gruppe]
- raadmoens: values [10000=Familier i alt, 10200=Familier uden bil i alt, 10210=Familier med bil i alt, 10211=Familier uden sommerhus i alt, 10212=Familier uden sommerhus og bil, 10213=Familier uden sommerhus med bil, 10214=Familier med sommerhus i alt, 10216=Familier med sommerhus uden bil, 10218=Familier med sommerhus og bil]
- somkom: values [0=Hele landet, 1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner]
- tid: date range 2022-01-01 to 2022-01-01
dim docs: /dim/kommunegrupper.md
notes:
- Single-year snapshot: only 2022 data.
- Two geographic dimensions: bopkomgrp (family's residence, joins dim.kommunegrupper niveau 1) and somkom (location of summer house, same 1-5 coding as kommunegrupper but NOT a dim join — inline values). bopkomgrp=0 and somkom=0 are both national totals.
- raadmoens combines car and summer house categories: 10000=alle familier, 10210=med bil, 10200=uden bil, 10214=med sommerhus, 10211=uden sommerhus, 10212/10213/10216/10218=cross-combinations. These are overlapping categories — pick the specific combination you need.
- socio=TOT is the total. Sub-groups have hierarchy (110/130/515 are sub-totals containing 111-112/131-136/520-530). Pick one level.
