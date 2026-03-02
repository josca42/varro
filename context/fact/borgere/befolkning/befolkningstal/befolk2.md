table: fact.befolk2
description: Befolkningen 1. januar efter køn, alder og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-84=80-84 år, 85-=85 år og derover]
- tid: date range 1901-01-01 to 2025-01-01

notes:
- Longest annual population series: back to 1901. No geographic breakdown, no civilstand.
- alder is in 5-year age groups (0-4, 5-9, ..., 85-) not individual years — can't drill to single ages.
- Filter non-target dims: kon='TOT', alder='TOT'.
- Use this for century-scale trends. For civilstand back to 1971 use befolk1; for regional breakdown use folk1a.