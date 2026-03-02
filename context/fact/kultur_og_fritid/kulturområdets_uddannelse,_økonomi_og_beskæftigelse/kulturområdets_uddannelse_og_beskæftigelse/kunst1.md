table: fact.kunst1
description: Kunstnere efter kunstområde, køn, aldersgruppe og tid
measure: indhold (unit Antal)
columns:
- kunstomr: values [TOTK=Kunstområde i alt, 1000=Musik, 1010=Forfattere og ord, 1020=Billedkunst og formgivere, 1030=Film og TV, 1040=Skuespil og scenekunst]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- agebygroup: values [TOT=Alder i alt, 0029=Under 30 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7099=70 år og derover]
- tid: date range 2022-01-01 to 2022-01-01

notes:
- Only covers a single year (2022). No time-series analysis possible.
- All dimensions have total rows: kunstomr=TOTK, kon=10, agebygroup=TOT. Filter unused dimensions to their total to avoid overcounting.
- 5 kunstområder plus TOTK. Can sum across agebygroup or kon only when filtering the other to its total.