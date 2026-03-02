table: fact.silc52
description: Tillid til fremmede efter baggrundsoplysninger, enhed og tid
measure: indhold (unit Gns.)
columns:
- bagopl: values [TOT=I alt, KON1=Mænd, KON2=Kvinder, ALD16=16-24 år, ALD25=25-39 år ... URB3=Tyndt befolket område, UDD1=Grundskole, UDD2=Gymnasie og erhvervsfaglige uddannelser, UDD3=Korte og mellemlange videregående uddannelser, UDD4=Lange videregående uddannelser]
- enhed: values [GNS=Gennemsnit for befolkningen (16+ år), STDG=Standardfejl på gennemsnittet]
- tid: date range 2021-01-01 to 2024-01-01
notes:
- Identical structure to silc50 (life satisfaction). enhed: GNS=average trust score (0–10), STDG=standard error. Always filter enhed='GNS' for the mean.
- bagopl covers gender, age, region, income quintile, housing tenure, urbanization, education. TOT=I alt for overall.
- Values are mean scores on a 0–10 scale — not percentages. Do not sum across bagopl.
- For national average trust in strangers: WHERE bagopl='TOT' AND enhed='GNS'.
