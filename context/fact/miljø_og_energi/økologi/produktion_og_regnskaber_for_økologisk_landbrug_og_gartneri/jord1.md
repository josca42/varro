table: fact.jord1
description: Resultatopgørelse for alle bedrifter (gennemsnit) efter bedriftstype region standardoutput, kvartilgruppe, regnskabsposter og tid
measure: indhold (unit Gns.)
columns:
- bedriftstand: values [0=Alle bedrifter, 1=Landbrug, 2=Konventionelt landbrug, 3=Økologisk landbrug, 4=Gartneri, 300=Hovedstaden (region), 302=Sjælland (region), 304=Syddanmark (region), 306=Fyn (landsdel), 308=Sydjylland (landsdel), 310=Midtjylland (region), 312=Østjylland (landsdel), 314=Vestjylland (landsdel), 316=Nordjylland (region), 318=Standardoutput 0-100.000 Euro, 320=Standardoutput 100.000-499.999 Euro, 322=Standardoutput 500.000-999.999 Euro, 324=Standardoutput 1.000.000+ Euro]
- kvartil: values [1000=Gennemsnit, alle, 1010=1. kvartilgruppe efter driftsresultat, 1015=2. kvartilgruppe efter driftsresultat, 1020=3. kvartilgruppe efter driftsresultat, 1025=4. kvartilgruppe efter driftsresultat]
- regnskposter: values [0=1. POPULATION, ANTAL BEDRIFTER, 5=2. STIKPRØVE, ANTAL BEDRIFTER, 10=3. JORDBRUGSAREAL, HA, PRIMO, 15=3.1. Selveje, ha, primo (Jordbrugsareal), 20=3.2. Forpagtning, ha, primo (jordbrugsareal) ... 1150=24.1.2. Løbende opsparing (egenkapitalforskydninger) 1.000 kr., 1155=24.2. Kapitalændringer på aktiver (egenkapital forskydninger) 1000 kr., 1160=24.3. Kapitalændringer på gæld (egenkapitalforskydninger) 1000 kr., 1165=24.4. Andre kapitalændringer i alt (egenkapitalforskydning) 1000 kr., 1170=25. EGENKAPITAL, ultimo, 1000 kr.]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- bedriftstand is a combined dimension that mixes mutually exclusive categories: farm types (0–4), regions (300–316), and standardoutput size groups (318–324). Never sum across all bedriftstand values — pick one category group. Use bedriftstand=0 for all farms, or bedriftstand=3 for organic farming specifically.
- regnskposter is the account line item selector (238 distinct items) — indhold is the average value for that account item. Never sum across regnskposter. Each item represents a different financial metric with its own unit (ha, antal, 1000 kr.).
- kvartil=1000 ("Gennemsnit, alle") is the population average. kvartil 1010–1025 are quartile groups ranked by driftsresultat. Always filter to one kvartil.
- indhold values are per-farm averages (Gns.), not totals. Multiply by regnskposter=0 (antal bedrifter) to get aggregate population estimates, but note that is approximate (stikprøve-based).
- Typical pattern for organic farming income statement: WHERE bedriftstand='3' AND kvartil='1000' AND tid='2024-01-01', then use regnskposter to select account items.