table: fact.kv2kar1
description: Besøg på dansk kulturarv efter type af kulturarv, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- typkultarv: values [30570=Historiske bymiljøer, 30580=Historiske bygninger eller bygninger kendt for deres arkitektur, 30590=Landskabelige kulturmiljøer, 30600=Oldtidsgrave, 30610=Forsvarsværker eller voldsteder, 30620=Runesten eller helleristninger, 30630=Ruiner, 30640=Arkæologiske udgravninger, 30650=Anlæg fra 2. verdenskrig eller Den Kolde Krig, 30660=Mindesmærker for historiske begivenheder]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- indhold is percentage (Pct.) of respondents who visited each type of kulturarv. Categories are NOT mutually exclusive — a person can visit multiple types, so values sum to 156% across all typkultarv. Never sum across typkultarv; compare individual category percentages instead.
- kon: 10=total, 1=mænd, 2=kvinder. alder: TOT=total, plus 7 age bands. Filter to kon=10 and alder=TOT for overall rates.
- Single year only (2024) — no trend analysis possible.