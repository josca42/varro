table: fact.straf71
description: Anholdelser efter køn, alder, bopæl i Danmark og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70OV=70 år og derover]
- bopdk: values [0=I alt, 90=Personer med bopæl i Danmark, 91=Personer uden bopæl i Danmark]
- tid: date range 2015-01-01 to 2024-01-01

notes:
- No dim joins — all columns are inline coded.
- All 3 dimension columns have total rows: kon='TOT', alder='TOT', bopdk=0 (I alt). Filter non-target dimensions to their total to avoid overcounting.
- bopdk: 0=I alt, 90=bopæl i Danmark, 91=uden bopæl i Danmark. For "persons residing in Denmark" use bopdk='90'. The two substantive values (90+91) sum to the total (0).
- alder: individual years 15–24 plus grouped bands (25-29 … 70+) plus TOT. Do not sum individual ages and groups together.
- This table has no offense type — use straf70 or straf72 if crime type is needed.