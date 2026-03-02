table: fact.silc20
description: Husstandenes økonomiske afsavn efter afsavnsmål, baggrundsoplysninger, enhed og tid
measure: indhold (unit -)
columns:
- afsavn: values [HD080=Har ikke råd til at erstatte slidte møbler, HH050=Har ikke råd til at holde hjemmet tilstrækkeligt opvarmet, HS011=Bagud med husleje eller renter og afdrag på gæld i boligen, HS021=Bagud med regninger vedr. el, varme, vand eller gas, HS031=Bagud med afdrag på forbrugslån eller anden gæld (undtagen boliggæld), HS040=Har ikke råd til en uges ferie væk fra hjemmet årligt, HS050=Har ikke råd til kød, kylling, fisk eller tilsvarende vegetarret hver anden dag, HS060=Kan ikke betale en uforudset udgift på 10.000 kr., HS090=Har ikke råd til computer, HS110=Har ikke råd til bil, HS120=Har svært eller meget svært ved at få pengene til at slå til]
- bagopl: values [TOT=I alt, REG81=Region Nordjylland, REG82=Region Midtjylland, REG83=Region Syddanmark, REG84=Region Hovedstaden ... BOL1=Ejerbolig, BOL2=Lejebolig, URB1=Tæt befolket område, URB2=Medium befolket område, URB3=Tyndt befolket område]
- enhed: values [HAND=Procent af husstande, HANT=Antal husstande (1.000), STD=Standardfejl (pct.)]
- tid: date range 2021-01-01 to 2024-01-01
notes:
- Household-level deprivations (unit: husstande). bagopl has 21 values covering region, income quintile, household type, housing tenure, and urbanization — no gender, age, education, or socioeconomic status (those are person-level, see silc10/silc30).
- enhed: HAND=Procent af husstande, HANT=Antal husstande (1.000), STD. Always filter enhed — every afsavn+bagopl combination appears 3 times.
- afsavn has 11 independent household deprivation indicators (HD*, HH*, HS*). They are NOT mutually exclusive — a household can have multiple deprivations simultaneously. Summing across afsavn gives >100%. Analyze one item at a time.
- For overall rate of inability to pay an unexpected 10,000 kr. expense: WHERE afsavn='HS060' AND bagopl='TOT' AND enhed='HAND'.
