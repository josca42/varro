table: fact.fod11
description: Gennemsnitsalder for fødende kvinder og nybagte fædre efter alder og tid
measure: indhold (unit -)
columns:
- alder: values [610=Gennemsnitsalder for førstegangsfødende kvinder, 611=Gennemsnitsalder for samtlige fødende kvinder, 617=Gennemsnitsalder for førstegangs fædre, 612=Gennemsnitsalder for fædre til nyfødte]
- tid: date range 1901-01-01 to 2024-01-01
notes:
- indhold is an average age in years — NEVER sum across alder values. Each alder code is an independent metric: 610=first-time mothers, 611=all mothers, 617=first-time fathers, 612=all fathers. Always filter to exactly one alder per query.
- Longest series for average parental age: back to 1901. For regional breakdown of the same metrics, use fod111.
