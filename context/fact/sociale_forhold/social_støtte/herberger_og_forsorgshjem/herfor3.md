table: fact.herfor3
description: Ophold på herberger og forsorgshjem efter overnatning, alder, køn og tid
measure: indhold (unit Antal)
columns:
- overnat: values [TOT=I alt, 1=1 dag, 2=2-5 dage, 3=6-30 dage, 4=31-119 dage, 5=120-364 dage, 6=Hele året, 9=Uoplyst]
- alerams: values [TOT=Alder i alt, 1824=18-24 år, 2529=25-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover, 9999=Uoplyst alder]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- tid: date range 2021-01-01 to 2024-01-01

notes:
- This table counts STAYS (ophold), not people. A person with 3 stays is counted 3 times (once per stay). Always higher than herfor1/herfor2: 2024 total stays = 11,243 vs 7,346 persons.
- Both overnat and alerams have TOT rows that are proper aggregates (TOT = sum of individual categories). To get total stays: WHERE overnat='TOT' AND alerams='TOT' AND kon='TOT'.
- kon has TOT (=1+2). Filter appropriately to avoid double-counting.
- Use this table when the question is about number of stays/overnight-nights (e.g. "how many stays lasted over 120 days?"). Use herfor1/herfor2 when the question is about number of people.
- overnat='TOT' is available here (unlike herfor1 which has no overnat total) — so cross-tabulating stays by age without filtering overnat is straightforward: WHERE overnat='TOT'.