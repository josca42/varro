table: fact.kv2for1
description: Besøg i forlystelsespark, zoologisk have m.m. efter sted, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- sted: values [30510=Har besøgt forlystelses- eller temapark, 30520=Har besøgt zoologisk have eller dyrepark, 30530=Har besøgt sommerland, 30540=Har besøgt oplevelsescentre, 30550=Har været i cirkus, 30560=Har besøgt akvarie]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- indhold is a percentage (Pct.) — the share of the population who visited that type of attraction in the past year. Never sum across sted values; a person can visit multiple attraction types (the categories are not mutually exclusive).
- sted values relevant to this subject: 30520=zoologisk have/dyrepark, 30560=akvarie. The table also covers forlystelsespark (30510), sommerland (30530), oplevelsescentre (30540), cirkus (30550).
- kon=10 is the total (both genders); kon=1 men, kon=2 women. alder=TOT is the total. Filter to kon=10 AND alder=TOT for a single overall percentage. Forgetting either inflates results.
- Only a single time point (2024). No trend analysis possible with this table.
- Typical query: SELECT sted, indhold FROM fact.kv2for1 WHERE kon=10 AND alder='TOT' ORDER BY sted — share of Danes visiting each attraction type overall.