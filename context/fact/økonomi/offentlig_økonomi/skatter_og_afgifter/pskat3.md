table: fact.pskat3
description: Skattepligtige personer efter skattetype og tid
measure: indhold (unit 1.000 personer)
columns:
- skatter: values [1=Bundskat, 2=Mellemskat, 3=Topskat, 12=Udligningsskat, 4=Sundhedsbidrag, 5=Amtsskat (-2006), 6=Kommuneskat, 7=Kirkeskat, 8=Aktieskat, 9=Virksomhedsskat, 13=Forskerskat, 14=Grundskyld, 10=Ejendomsværdiskat, 11=Skattepligtige i alt]
- tid: date range 1994-01-01 to 2023-01-01

notes:
- skatter codes are NOT mutually exclusive. The same person can pay bundskat, kommuneskat, kirkeskat, etc. simultaneously. In 2023: skatter=11 (total) = 5446 (1.000 persons), but sum of individual skatter types = 16679. Never sum across skatter values.
- skatter=11 (Skattepligtige i alt) is the total count of taxpayers. Individual codes count persons paying that specific tax. Use a single WHERE skatter='X' filter per query.
- Historical note: skatter=5 (Amtsskat) ends in 2006 when amt-kommuner were abolished. skatter=2 (Mellemskat) was abolished in 2010.
