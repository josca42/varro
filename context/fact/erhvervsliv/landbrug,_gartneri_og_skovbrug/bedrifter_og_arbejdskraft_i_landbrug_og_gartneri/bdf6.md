table: fact.bdf6
description: Medhjælpere i landbrug og gartneri efter område, antal ansatte, bedriftstype og tid
measure: indhold (unit Antal)
columns:
- omrade: values [000=Hele landet, 002=Øst for Storebælt, 1580=Fyn, L3=Jylland]
- ansatte: values [5000=Alle bedrifter, 5005=Ingen medhjælpere, 5010=1 medhjælper, 5015=2 medhjælpere, 5020=3 medhjælpere, 5025=4 medhjælpere, 5030=5 medhjælpere og derover]
- bedrift: values [700=Dyrket areal i alt, 702=Antal bedrifter i alt, 704=Antal medhjælpere, 706=Antal bedrifter med kvæg, 708=Antal kvæg på bedriften, 710=Antal bedrifter med svin, 712=Antal svin på bedriften]
- tid: date range 1982-01-01 to 2023-01-01

notes:
- omrade has 4 coarse standalone codes: 000=Hele landet, 002=Øst for Storebælt, 1580=Fyn, L3=Jylland. No dim join. Very limited geography; use bdf307 for modern NUTS-based regional data.
- bedrift encodes 7 completely different statistics in one column — never aggregate across bedrift values: 700=Dyrket areal (ha), 702=Antal bedrifter, 704=Antal medhjælpere, 706=Antal bedrifter med kvæg, 708=Antal kvæg, 710=Antal bedrifter med svin, 712=Antal svin. Filter to one bedrift per query.
- ansatte: 5000=Alle bedrifter is the total across all employer-size brackets.
- For total hired workers nationally: WHERE omrade='000' AND ansatte=5000 AND bedrift=704.