table: fact.jord2
description: Resultatopgørelse for heltidsbedrifter (gennemsnit) efter bedriftstype årsværk, kvartilgruppe, regnskabsposter og tid
measure: indhold (unit Gns.)
columns:
- bedriftaars: values [1=Landbrug, 2=Konventionelt landbrug, 3=Økologisk landbrug, 4=Gartneri, 5=Landbrug, 1-3 årsværk ... 560=Væksthusgrøntsager, 563=Frilandsgartneri, 565=Frilandsgrøntsager, 570=Frugt og bær, 575=Planteskole]
- kvartil: values [1000=Gennemsnit, alle, 1010=1. kvartilgruppe efter driftsresultat, 1015=2. kvartilgruppe efter driftsresultat, 1020=3. kvartilgruppe efter driftsresultat, 1025=4. kvartilgruppe efter driftsresultat]
- regnskposter: values [0=1. POPULATION, ANTAL BEDRIFTER, 5=2. STIKPRØVE, ANTAL BEDRIFTER, 10=3. JORDBRUGSAREAL, HA, PRIMO, 15=3.1. Selveje, ha, primo (Jordbrugsareal), 20=3.2. Forpagtning, ha, primo (jordbrugsareal) ... 1150=24.1.2. Løbende opsparing (egenkapitalforskydninger) 1.000 kr., 1155=24.2. Kapitalændringer på aktiver (egenkapital forskydninger) 1000 kr., 1160=24.3. Kapitalændringer på gæld (egenkapitalforskydninger) 1000 kr., 1165=24.4. Andre kapitalændringer i alt (egenkapitalforskydning) 1000 kr., 1170=25. EGENKAPITAL, ultimo, 1000 kr.]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- bedriftaars has 55 values in two tiers: aggregate categories (1–8: farm type × årsværk ranges like "Landbrug 1-3 årsværk") and specific production types (405–575: kvægbrug, svinebrug, gartneri subtypes, etc.). Never sum across bedriftaars — each represents an overlapping population.
- Unlike jord1 which covers all farms, jord2 covers only heltidsbedrifter (full-time farms with sufficient labor input). For organic full-time farms use bedriftaars='3'.
- Same regnskposter structure as jord1 (238 account line items). kvartil=1000 for average, never sum across kvartil or regnskposter.
- indhold values are per-farm averages. Use regnskposter='0' (antal bedrifter) to see the population size for each bedriftaars type.