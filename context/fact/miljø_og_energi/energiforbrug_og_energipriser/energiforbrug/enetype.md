table: fact.enetype
description: Industriens energiforbrug efter energitype, enhed og tid
measure: indhold (unit -)
columns:
- energi1: values [EET=Alle energityper, EEL=El, EFJV=Fjernvarme, ELPGRAF=LPG inkl. raffinaderigas, ENBBG=Natur-, bio- og bygas, EFB=Flydende brændsel, EKK=Kul og koks, ETA=Træ og affald]
- enhed: values [GJFAK=Faktisk forbrug (1.000 GJ (gigajoule)), PCTAEND=Ændring i forhold til for to år siden (pct.)]
- tid: date range 2012-01-01 to 2024-01-01

notes:
- enhed is a measurement selector — every energi1/tid combination appears twice: GJFAK (faktisk forbrug i 1.000 GJ) and PCTAEND (ændring ift. for to år siden i pct.). Always filter to one: WHERE enhed = 'GJFAK' for energy amounts.
- energi1=EET is the aggregate for alle energityper. Filter it out when summing individual types: WHERE energi1 != 'EET'.
- Data is biennial (2012-2024 in 2-year steps).