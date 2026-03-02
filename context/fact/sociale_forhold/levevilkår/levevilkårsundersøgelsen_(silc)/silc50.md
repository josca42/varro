table: fact.silc50
description: Generel livstilfredshed efter baggrundsoplysninger, enhed og tid
measure: indhold (unit Gns.)
columns:
- bagopl: values [TOT=I alt, KON1=Mænd, KON2=Kvinder, ALD16=16-24 år, ALD25=25-39 år ... URB3=Tyndt befolket område, UDD1=Grundskole, UDD2=Gymnasie og erhvervsfaglige uddannelser, UDD3=Korte og mellemlange videregående uddannelser, UDD4=Lange videregående uddannelser]
- enhed: values [GNS=Gennemsnit for befolkningen (16+ år), STDG=Standardfejl på gennemsnittet]
- tid: date range 2021-01-01 to 2024-01-01
notes:
- enhed has only 2 values: GNS=Gennemsnit (average satisfaction score 0–10), STDG=Standardfejl på gennemsnittet. For the actual average, filter enhed='GNS'. Never aggregate across enhed.
- bagopl covers gender, age, region, income quintile, housing tenure, urbanization, education (no household type or socioeconomic status). TOT=I alt for overall.
- Measure is a mean score (0–10 scale), not a percentage. Cannot sum or average across bagopl values.
- For national average life satisfaction by year: WHERE bagopl='TOT' AND enhed='GNS'.
