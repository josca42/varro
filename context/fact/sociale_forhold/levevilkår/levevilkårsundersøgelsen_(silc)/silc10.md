table: fact.silc10
description: Økonomisk sårbare efter afsavnsmål, baggrundsoplysninger, enhed og tid
measure: indhold (unit -)
columns:
- afsavn: values [A0=Økonomisk sårbare (mindst 3 af 5 afsavnsmål), A1=1. Svært/meget svært at få pengene til at slå til, A2=2. Ubetalte regninger det seneste år, A3=3. Kan ikke betale uforudset udgift på 10.000 kr., A4=4. Har af økonomiske grunde ingen bil, A5=5. Har ikke råd til en uges årlig ferie væk fra hjemmet]
- bagopl: values [TOT=I alt, KON1=Mænd, KON2=Kvinder, ALD00=Under 16 år, ALD16=16-24 år ... URB3=Tyndt befolket område, UDD1=Grundskole, UDD2=Gymnasie og erhvervsfaglige uddannelser, UDD3=Korte og mellemlange videregående uddannelser, UDD4=Lange videregående uddannelser]
- enhed: values [AND=Procent af befolkningen, 16+ år, ANT=Antal personer, 16+ år (1.000 personer), STD=Standardfejl (pct.)]
- tid: date range 2021-01-01 to 2024-01-01

notes:
- enhed is a measurement selector — every afsavn+bagopl combination appears 3 times: AND=Procent af befolkningen (16+), ANT=Antal personer (1.000), STD=Standardfejl. Always filter enhed to avoid triple-counting. For most queries use enhed='AND'.
- bagopl packs 38 values from 9 different category groups (gender, age, region, income quintile, household type, socioeconomic status, housing tenure, urbanization, education). They are NOT additive — TOT is not the sum of KON1+KON2 etc. Always pick one bagopl value at a time. TOT=I alt gives the overall figure.
- afsavn: A0 is the composite "economically vulnerable" indicator (≥3 of 5 deprivations met). A1–A5 are the five individual deprivation items. These are NOT mutually exclusive — a person can satisfy multiple items simultaneously. Never sum across A0–A5.
- For a simple national economic vulnerability percentage: WHERE afsavn='A0' AND bagopl='TOT' AND enhed='AND'. This gives one row per year.