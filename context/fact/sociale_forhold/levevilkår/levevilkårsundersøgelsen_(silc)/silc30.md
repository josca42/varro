table: fact.silc30
description: Befolkningens økonomiske afsavn efter afsavnsmål, baggrundsoplysninger, enhed og tid
measure: indhold (unit -)
columns:
- afsavn: values [PD020=Har ikke råd til at udskifte slidt tøj, PD030=Har ikke råd til mindst to par sko, PD050=Har ikke råd til regelmæssigt at mødes med venner eller familie, PD060=Har ikke råd til regelmæssigt at deltage i fritidsaktiviteter, PD070=Har ikke råd til at bruge penge for egen fornøjelse, PD080=Har ikke råd til internet til eget brug]
- bagopl: values [TOT=I alt, KON1=Mænd, KON2=Kvinder, ALD16=16-24 år, ALD25=25-39 år ... URB3=Tyndt befolket område, UDD1=Grundskole, UDD2=Gymnasie og erhvervsfaglige uddannelser, UDD3=Korte og mellemlange videregående uddannelser, UDD4=Lange videregående uddannelser]
- enhed: values [AND=Procent af befolkningen, 16+ år, ANT=Antal personer, 16+ år (1.000 personer), STD=Standardfejl (pct.)]
- tid: date range 2021-01-01 to 2024-01-01
notes:
- Person-level personal deprivations (PD*): clothing, shoes, social activities, leisure, personal spending, internet. Six independent yes/no indicators — NOT mutually exclusive. Never sum across afsavn.
- enhed: AND=Procent af befolkningen (16+), ANT=Antal personer (1.000), STD. Always filter enhed.
- bagopl covers gender, age, region, income quintile, housing tenure, urbanization, education (but not household type or socioeconomic status — contrast with silc10 which has more categories). TOT for overall.
- For percent unable to afford regular leisure activities: WHERE afsavn='PD060' AND bagopl='TOT' AND enhed='AND'.
