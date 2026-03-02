table: fact.laby44
description: Beskæftigede (ultimo november) efter bopælskommunegruppe, køn, pendlingsafstand og tid
measure: indhold (unit Antal)
columns:
- bopkomgrp: join dim.kommunegrupper on bopkomgrp=kode; levels [1]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- pendafst: values [0=I alt, 10=Ingen pendling, 20=Indtil 5 km, 30=5-10 km, 40=10-20 km, 45=20-30 km, 50=30-40 km, 60=40-50 km, 70=Over 50 km, 80=Ikke beregnet]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/kommunegrupper.md

notes:
- bopkomgrp joins dim.kommunegrupper at niveau 1 only: 1=Hovedstadskommuner, 2=Storbykommuner, 3=Provinsbykommuner, 4=Oplandskommuner, 5=Landkommuner. Code 0='Hele landet' (national total) is NOT in the dim table — filter out or handle separately.
- pendafst=0 is total (I alt); pendafst=80 is 'Ikke beregnet'. kon has TOT, M, K — filter kon='TOT' for overall totals.