table: fact.bdf7
description: Medhjælpere i landbrug og gartneri efter areal, antal ansatte, bedriftstype og tid
measure: indhold (unit -)
columns:
- areal1: values [AIALT=I alt, A1=Under 10,0 ha, A19=10,0 - 19,9 ha, A29=20,0 - 29,9 ha, A49=30,0 - 49,9 ha, A62=50,0 - 74,9 ha, A100=75,0 - 99,9 ha, A210=100,0 - 199,9 ha, A220=200,0 ha og derover]
- ansatte: values [5000=Alle bedrifter, 5005=Ingen medhjælpere, 5010=1 medhjælper, 5015=2 medhjælpere, 5020=3 medhjælpere, 5025=4 medhjælpere, 5030=5 medhjælpere og derover]
- bedrift: values [700=Dyrket areal i alt, 702=Antal bedrifter i alt, 704=Antal medhjælpere, 706=Antal bedrifter med kvæg, 708=Antal kvæg på bedriften, 710=Antal bedrifter med svin, 712=Antal svin på bedriften]
- tid: date range 1982-01-01 to 2023-01-01

notes:
- Sister table to bdf6: same bedrift and ansatte columns but crosses by farm area (areal1) instead of region.
- bedrift encodes 7 completely different statistics — same as bdf6, always filter to exactly one: 700=Dyrket areal (ha), 702=Antal bedrifter, 704=Antal medhjælpere, 706=Antal bedrifter med kvæg, 708=Antal kvæg, 710=Antal bedrifter med svin, 712=Antal svin.
- areal1: AIALT = all farm sizes combined. ansatte: 5000 = all farm sizes.
- No regional breakdown — national only (by farm size). Use bdf307 for modern regional employment data.