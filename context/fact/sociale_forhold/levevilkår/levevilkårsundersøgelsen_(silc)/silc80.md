table: fact.silc80
description: Ændring i husstandsindkomst efter spørgsmål, baggrundsoplysninger, svarmulighed, enhed og tid
measure: indhold (unit -)
columns:
- sporg: values [HI010=Oplevet ændring i husstandens indkomst seneste 12 måneder, HI040=Forventning til husstandens indkomst de kommende 12 måneder]
- bagopl: values [TOT=I alt, REG81=Region Nordjylland, REG82=Region Midtjylland, REG83=Region Syddanmark, REG84=Region Hovedstaden ... BOL1=Ejerbolig, BOL2=Lejebolig, URB1=Tæt befolket område, URB2=Medium befolket område, URB3=Tyndt befolket område]
- svar: values [UDF11=En stigning i husstandens indkomst, UDF12=Uændret, UDF13=Et fald i hustandens indkomst]
- enhed: values [HAND=Procent af husstande, HANT=Antal husstande (1.000), STD=Standardfejl (pct.)]
- tid: date range 2021-01-01 to 2024-01-01
notes:
- sporg selects the time horizon: HI010=oplevet ændring seneste 12 måneder (experienced), HI040=forventning de kommende 12 måneder (expected). Always filter to one sporg.
- svar (UDF11=stigning, UDF12=uændret, UDF13=fald) are mutually exclusive responses summing to ~100% within each sporg+bagopl group.
- enhed: HAND=Procent af husstande, HANT=Antal husstande (1.000), STD. Always filter enhed. Combined with sporg, each bagopl combination appears 9 times if unfiltered.
- bagopl: household-level categories (region, income quintile, household type, housing tenure, urbanization). TOT for overall.
- For percent of households expecting income to fall: WHERE sporg='HI040' AND svar='UDF13' AND bagopl='TOT' AND enhed='HAND'.
