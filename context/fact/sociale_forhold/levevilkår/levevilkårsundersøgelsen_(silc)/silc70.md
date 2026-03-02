table: fact.silc70
description: Økonomisk byrde af forbrugslån efter baggrundsoplysninger, svarmulighed, enhed og tid
measure: indhold (unit -)
columns:
- bagopl: values [TOT=I alt, REG81=Region Nordjylland, REG82=Region Midtjylland, REG83=Region Syddanmark, REG84=Region Hovedstaden ... BOL1=Ejerbolig, BOL2=Lejebolig, URB1=Tæt befolket område, URB2=Medium befolket område, URB3=Tyndt befolket område]
- svar: values [UDF7=En tung byrde, UDF8=Noget af en byrde, UDF9=Ikke noget problem, UDF10=Betaler ikke afdrag]
- enhed: values [HAND=Procent af husstande, HANT=Antal husstande (1.000), STD=Standardfejl (pct.)]
- tid: date range 2021-01-01 to 2024-01-01
notes:
- svar (UDF7–UDF10) are mutually exclusive responses summing to ~100%: UDF7=tung byrde, UDF8=noget af en byrde, UDF9=ikke noget problem, UDF10=betaler ikke afdrag (no consumer loan repayments). UDF10 is a valid category, not a null — include it unless explicitly excluding households without consumer loans.
- enhed: HAND=Procent af husstande, HANT=Antal husstande (1.000), STD. Always filter enhed.
- bagopl: household-level categories (region, income quintile, household type, housing tenure, urbanization). TOT for overall.
- For percent finding consumer loans a heavy burden: WHERE svar='UDF7' AND bagopl='TOT' AND enhed='HAND'.
