table: fact.silc40
description: Slår pengene til efter baggrundsoplysninger, svarmulighed, enhed og tid
measure: indhold (unit -)
columns:
- bagopl: values [TOT=I alt, REG81=Region Nordjylland, REG82=Region Midtjylland, REG83=Region Syddanmark, REG84=Region Hovedstaden ... BOL1=Ejerbolig, BOL2=Lejebolig, URB1=Tæt befolket område, URB2=Medium befolket område, URB3=Tyndt befolket område]
- svar: values [UDF1=Meget svært, UDF2=Svært, UDF3=Lidt svært, UDF4=Nogenlunde let, UDF5=Let, UDF6=Meget Let]
- enhed: values [HAND=Procent af husstande, HANT=Antal husstande (1.000), STD=Standardfejl (pct.)]
- tid: date range 2021-01-01 to 2024-01-01
notes:
- svar (UDF1–UDF6: Meget svært → Meget let) are mutually exclusive responses that sum to ~100% within each bagopl group. You can sum them to build "struggling" subgroups (e.g. UDF1+UDF2 = "svært eller meget svært").
- enhed: HAND=Procent af husstande, HANT=Antal husstande (1.000), STD. Always filter enhed.
- bagopl has 21 household-level categories (region, income quintile, household type, housing tenure, urbanization). No gender, age, or education.
- For the overall distribution of households by financial difficulty: WHERE bagopl='TOT' AND enhed='HAND'. Returns 6 rows (one per response), summing to 100%.
