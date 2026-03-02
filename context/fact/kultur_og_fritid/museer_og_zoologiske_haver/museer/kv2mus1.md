table: fact.kv2mus1
description: Besøg på museum efter museumskategori, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- museer: values [30000=Historisk museum, 30010=Kunstmuseum, 30020=Naturhistorisk museum]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- indhold is % of respondents who visited that museum type. museer values are independent — a person can visit multiple types. Sums exceed 100%, so never aggregate across museer.
- No "Alle museer" total in museer column. Each row is a specific museum type; they cannot be summed to a meaningful national museum-going rate.
- Filter kon=10 and alder='TOT' for national results. Single year only (2024 survey).