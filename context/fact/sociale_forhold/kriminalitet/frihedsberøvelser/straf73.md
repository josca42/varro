table: fact.straf73
description: Anholdelser efter køn, alder, uddannelse og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70OV=70 år og derover]
- uddannelse: values [TOT=I alt, 10=Grundskole, 20=Gymnasial uddannelse, 35=Erhvervsuddannelse, 40=Videregående uddannelse, 00=Uoplyst uddannelse]
- tid: date range 2015-01-01 to 2024-01-01

notes:
- No dim joins — all columns are inline coded.
- All 3 dimension columns have total rows: kon='TOT', alder='TOT', uddannelse='TOT'. Filter non-target dimensions to their total to avoid overcounting.
- uddannelse: TOT=I alt, 10=Grundskole, 20=Gymnasial, 35=Erhvervsuddannelse, 40=Videregående, 00=Uoplyst. Note that 00 (uoplyst) is a substantive category, not a total — it counts persons whose education level is unknown.
- alder: individual years 15–24 plus grouped bands (25-29 … 70+) plus TOT. Do not sum individual ages and groups together.
- No offense type column — use straf73/straf74 pairing: straf73 for demographics, straf74 for offense×education cross.