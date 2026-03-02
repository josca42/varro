table: fact.laby41
description: Elevers aktiviteter på musikskoler pr. 1000 indbygger efter kommunegruppe, fag og tid
measure: indhold (unit Antal)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- faget: values [TOT=Fag i alt, 855=Sang, 860=Strygeinstrument, 875=Træblæser, 880=Messingblæser, 885=Slagtøj, 890=Tasteinstrument, 920=Strengeinstrument, 900=Øvrige musikfag, 910=Øvrige kunstfag, 930=Sammenspil, 940=Forskole, 999=Uoplyst]
- tid: date range 2021 to 2025
dim docs: /dim/kommunegrupper.md

notes:
- indhold is a rate per 1,000 inhabitants, not a raw count. Do not SUM across komgrp rows — values are rates, not additive counts.
- komgrp joins dim.kommunegrupper at niveau 1 only (5 kommunegrupper: Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner). komgrp='0' is the national average, not in the dim.
- faget='TOT' for total activity rate across all subjects. Use to compare overall music school participation across kommunegrupper.