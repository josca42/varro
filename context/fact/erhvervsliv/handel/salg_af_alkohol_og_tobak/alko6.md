table: fact.alko6
description: Salg af alkohol og tobak efter type og tid
measure: indhold (unit -)
columns:
- type: values [0=Salg af pilsnerækvivalenter, i alt (1000 liter) (alkohol 4,6 vol.), 5=Salg af vin, i alt (1000 liter), 6=Salg af spiritus, i alt (1000 liter), 12=Salg af alkohol i alt, ren alkohol (1000 liter), 13=Salg af øl, ren alkohol (1000 liter), 14=Salg af vin, ren alkohol (1000 liter), 15=Salg af spiritus, ren alkohol, (1000 liter), 22=Salg af cigaretter (mio. stk), 23=Salg af cigarer og cigarillos (mio. stk), 24=Salg af røgtobak (tons)]
- tid: date range 1921-01-01 to 2024-01-01

notes:
- Each type value is a completely separate measure with its own unit — never sum across types. Units are mixed: 1000 liters (beer/wine/spirits/pure alcohol), million pieces (cigarettes type 22, cigars type 23), tons (smoking tobacco type 24).
- type 0, 5, 6 are beverage volumes; types 12, 13, 14, 15 are the same drinks expressed as pure alcohol equivalents. Don't mix these two perspectives in the same query.
- Not all types start in 1921. Beer/wine/spirits (0, 5, 6, 12) from 1921; tobacco (22, 23, 24) from 1923; pure alcohol breakdown by drink (13, 14, 15) only from 1955. Filter by type before comparing time ranges.
- Simple single-type query: SELECT tid, indhold FROM fact.alko6 WHERE type = 5 ORDER BY tid; (wine volumes over time)