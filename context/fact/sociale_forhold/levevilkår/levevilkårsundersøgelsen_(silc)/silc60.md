table: fact.silc60
description: Helbredsproblemer efter spørgsmål, baggrundsoplysninger, enhed og tid
measure: indhold (unit -)
columns:
- sporg: values [PH010=Har dårligt eller meget dårligt helbred, PH020=Har langvarig sygdom eller helbredsproblem, PH030=Hæmmet grundet helbredsproblemer]
- bagopl: values [TOT=I alt, KON1=Mænd, KON2=Kvinder, ALD16=16-24 år, ALD25=25-39 år ... URB3=Tyndt befolket område, UDD1=Grundskole, UDD2=Gymnasie og erhvervsfaglige uddannelser, UDD3=Korte og mellemlange videregående uddannelser, UDD4=Lange videregående uddannelser]
- enhed: values [AND=Procent af befolkningen, 16+ år, ANT=Antal personer, 16+ år (1.000 personer), STD=Standardfejl (pct.)]
- tid: date range 2021-01-01 to 2024-01-01
notes:
- sporg is a question selector: PH010=dårligt/meget dårligt helbred, PH020=langvarig sygdom, PH030=hæmmet grundet helbredsproblemer. Always filter to one sporg — every bagopl+enhed combination appears 3 times (once per question).
- enhed: AND=Procent af befolkningen (16+), ANT=Antal (1.000), STD. Always filter enhed too — combined with sporg, each bagopl combination appears 9 times if unfiltered.
- bagopl: full demographic breakdown (gender, age, region, income, housing, urbanization, education). TOT for overall.
- For overall percent with chronic illness: WHERE sporg='PH020' AND bagopl='TOT' AND enhed='AND'.
