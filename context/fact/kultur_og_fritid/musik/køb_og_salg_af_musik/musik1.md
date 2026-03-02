table: fact.musik1
description: Salg af indspillet musik efter nationalitet, distributionsform og tid
measure: indhold (unit Mio. kr.)
columns:
- nation2: values [TOT=I alt, 1=Dansk, 2=Udenlandsk]
- distrib: values [3=Fysiske medier, 4=Streaming, 5=Downloads, 50=Andre digitale produkter (2023-)]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- nation2=TOT is the sum of 1 (Dansk) and 2 (Udenlandsk). Filter nation2 IN ('1','2') for a nationality breakdown, or use 'TOT' for the overall total — never sum all three.
- distrib code 50 (Andre digitale produkter) only exists for nation2='TOT' and only from 2023. For long time series use distrib IN (3,4,5).
- distrib categories (3=Fysiske medier, 4=Streaming, 5=Downloads) are mutually exclusive — safe to sum across them. No distrib total row exists, so summing all is fine.