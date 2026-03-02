table: fact.mpk30
description: Forbrugerkredit, ultimo kvartalet efter type og tid
measure: indhold (unit Mio. kr.)
columns:
- type: values [2482=0 - Den totale forbrugerkredit, 2481=1 - Bankernes forbrugerkredit i alt, 2480=2 - Forbrugerkreditselskaber i alt, 2442=2.1 - Blankolån, 2445=2.2 - Andre lån, 2441=2.2.1 - Heraf: Benzinselskaber, 2440=2.3 - Saldo på købekort og kontokort, 2443=2.4 - Kredit mod sikkerhed]
- tid: date range 2018-01-01 to 2025-04-01

notes:
- type encodes a hierarchy — do NOT sum across all type values. The hierarchy is: 2482 (total) = 2481 (banker) + 2480 (forbrugerkreditselskaber). Under 2480: 2442 (blankolån) + 2445 (andre lån) + 2440 (købekort/kontokort) + 2443 (kredit mod sikkerhed).
- Two sub-categories were discontinued after 2018: type 2440 (Saldo på købekort og kontokort) and 2443 (Kredit mod sikkerhed) only have 4 quarters (2018 Q1–Q4). type 2445 (Andre lån) starts from 2019 Q1. For trend analysis from 2018, stick to the aggregate types (2480, 2481, 2482).
- For total consumer credit over time: WHERE type = '2482'. For bank vs. non-bank split: filter to 2481 and 2480. Do not filter to all 8 types and sum — that will count the total multiple times.
- indhold is in Mio. kr. (millions DKK), quarterly (ultimo kvartalet = end-of-quarter balance).