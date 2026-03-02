table: fact.jb2
description: Jordbrugets afskrivninger og nettoinvesteringer efter investeringstype og tid
measure: indhold (unit Mio. kr.)
columns:
- invest: values [3000=Bruttoinvesteringer i alt, 3005=Afskrivninger i alt, 3010=Nettoinvesteringer i alt, 3105=Bruttoinvesteringer, driftsbygninger, 3110=Afskrivninger, driftsbygninger, 3115=Nettoinvesteringer, driftsbygninger, 3205=Bruttoinvesteringer, maskiner og inventar, 3210=Afskrivninger, maskiner og inventar, 3215=Nettoinvesteringer, maskiner og inventar, 3305=Bruttoinvesteringer, plantager og grundforbedringer, 3310=Afskrivninger, plantager og grundforbedringer, 3315=Nettoinvesteringer, plantager og grundforbedringer]
- tid: date range 2005-01-01 to 2024-01-01
notes:
- invest codes mix three distinct metrics for each asset type: bruttoinvesteringer, afskrivninger, nettoinvesteringer. These are not summable together — filter to the specific metric you need (e.g., codes ending in 05, 10, or 15).
- Aggregate row: 3000=Bruttoinvesteringer i alt, 3005=Afskrivninger i alt, 3010=Nettoinvesteringer i alt. Nettoinvesteringer = Brutto − Afskrivninger.
