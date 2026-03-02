table: fact.jord1
description: Resultatopgørelse for alle bedrifter (gennemsnit) efter bedriftstype region standardoutput, kvartilgruppe, regnskabsposter og tid
measure: indhold (unit Gns.)
columns:
- bedriftstand: values [0=Alle bedrifter, 1=Landbrug, 2=Konventionelt landbrug, 3=Økologisk landbrug, 4=Gartneri, 300=Hovedstaden (region), 302=Sjælland (region), 304=Syddanmark (region), 306=Fyn (landsdel), 308=Sydjylland (landsdel), 310=Midtjylland (region), 312=Østjylland (landsdel), 314=Vestjylland (landsdel), 316=Nordjylland (region), 318=Standardoutput 0-100.000 Euro, 320=Standardoutput 100.000-499.999 Euro, 322=Standardoutput 500.000-999.999 Euro, 324=Standardoutput 1.000.000+ Euro]
- kvartil: values [1000=Gennemsnit, alle, 1010=1. kvartilgruppe efter driftsresultat, 1015=2. kvartilgruppe efter driftsresultat, 1020=3. kvartilgruppe efter driftsresultat, 1025=4. kvartilgruppe efter driftsresultat]
- regnskposter: values [0=1. POPULATION, ANTAL BEDRIFTER, 5=2. STIKPRØVE, ANTAL BEDRIFTER, 10=3. JORDBRUGSAREAL, HA, PRIMO, 15=3.1. Selveje, ha, primo (Jordbrugsareal), 20=3.2. Forpagtning, ha, primo (jordbrugsareal) ... 1150=24.1.2. Løbende opsparing (egenkapitalforskydninger) 1.000 kr., 1155=24.2. Kapitalændringer på aktiver (egenkapital forskydninger) 1000 kr., 1160=24.3. Kapitalændringer på gæld (egenkapitalforskydninger) 1000 kr., 1165=24.4. Andre kapitalændringer i alt (egenkapitalforskydning) 1000 kr., 1170=25. EGENKAPITAL, ultimo, 1000 kr.]
- tid: date range 2008-01-01 to 2024-01-01
notes:
- bedriftstand multiplexes three classification schemes in one column: bedriftstype (0–4), region (300–316), and standardoutput size class (318–324). These are separate categorizations — for a given question, filter to ONE scheme (e.g., WHERE bedriftstand IN (0,1,2,3,4) for type breakdown, or WHERE bedriftstand IN (300,302,304,306,308,310,312,314,316) for regional).
- kvartil=1000 = gennemsnit for alle bedrifter (overall average). kvartil 1010–1025 are performance quartiles (4th = best driftsresultat). Filter to kvartil=1000 for a simple average.
- regnskposter has ~234 distinct accounting items with mixed units: count (antal bedrifter), area (ha), money (1000 kr.), percentage (pct.). Always filter to a specific regnskposter — indhold values are meaningless mixed together.
- indhold is a per-farm average (Gns.), not a sector total. Multiply by regnskposter=0 (antal bedrifter) to approximate sector totals.
- For key/ratios use jord6 instead (same bedriftstand/kvartil structure but regnskposter has financial ratios like soliditetsgrad, afkastningsgrad).
