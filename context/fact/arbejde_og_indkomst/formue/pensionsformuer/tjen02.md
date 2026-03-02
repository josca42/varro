table: fact.tjen02
description: Optjent tjenestemandspension for pensionerede tjenestemænd efter sektor, enhed, køn og tid
measure: indhold (unit -)
columns:
- sektor: values [100=Alle tjenestemænd, 105=Tjenestemænd ansat i staten, 110=Tjenestemænd ansat i Kommuner/regioner, 115=Opsatte tjenestemænd i staten, 120=Opsatte tjenestemænd i kommuner/regioner]
- enhed: values [100=Pensionerede tjenestemænd (Antal), 105=Værdi af optjent pension (1.000 kr.), 110=Værdi af gennemsnitlig optjent pension (1.000 kr.)]
- koen: values [0=Mænd og kvinder i alt, 1=Mænd, 2=Kvinder]
- tid: date range 2014-01-01 to 2023-01-01

notes:
- enhed is a measurement selector — every sektor/koen/tid combination is repeated 3 times. Always filter to exactly one enhed: 100=antal pensionerede, 105=samlet pensionsværdi (1.000 kr.), 110=gennemsnit (1.000 kr.).
- sektor has a total (100=Alle tjenestemænd) and 4 components: 105=Staten aktive, 110=Kommuner/regioner aktive, 115=Opsatte tjenestemænd i staten, 120=Opsatte tjenestemænd i kommuner/regioner. Summing 105+110+115+120 equals 100. Filter to avoid double-counting.
- koen=0 is the total; 1=mænd, 2=kvinder.