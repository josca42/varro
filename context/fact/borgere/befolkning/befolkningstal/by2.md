table: fact.by2
description: Befolkningen 1. januar efter kommune, bystørrelse, alder, køn og tid
measure: indhold (unit Antal)
columns:
- komk: join dim.nuts on komk=kode; levels [3]
- byst: values [HOVEDS=Hovedstadsområdet, 100000=100.000 indbyggere og derover, 50000=50.000-99.999 indbyggere, 20000=20.000-49.999 indbyggere, 10000=10.000-19.999 indbyggere, 5000=5.000-9.999 indbyggere, 2000=2.000-4.999 indbyggere, 1000=1.000-1.999 indbyggere, 500=500-999 indbyggere, 250=250-499 indbyggere, 200=200-249 indbyggere, LAND=Landdistrikter, UFB=Uden fast bopæl]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- kon: values [1=Mænd, 2=Kvinder]
- tid: date range 2010-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- komk joins dim.nuts at niveau=3 (99 kommuner) — clean join, all 99 codes match.
- No total rows for alder (0–125 individual years) or kon (only 1/2, no TOT). Sum both kon values for total.
- byst is the city-size category within each municipality. Each person in a municipality is in exactly one byst bucket, so summing byst values within a komk gives the municipal total. No byst total code — sum all byst categories.
- Use this to understand how urban vs rural each municipality is: what fraction lives in areas of various city sizes.
- ColumnValues("nuts", "titel", for_table="by2") for municipality names.
- Map: /geo/kommuner.parquet — merge on komk=dim_kode. Exclude komk=0.