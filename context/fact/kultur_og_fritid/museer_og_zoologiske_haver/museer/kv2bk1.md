table: fact.kv2bk1
description: Forbrug af billedkunst efter udstillingssted, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- udstil: values [30100=Galleri, 30110=Museum eller kunstudstilling, 30120=Kunsthaller eller kunstcentre, 30130=I det offentlige rum, 30140=I tv, 30150=På internettet, hjemmesider, apps eller sociale medier, 30160=Bøger eller magasiner, 42280=Andre steder]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- indhold is % of respondents who consumed visual art at that venue type. udstil values are independent — a person can consume art in multiple venues. Sums exceed 100%, so never aggregate across udstil.
- Filter kon=10 and alder='TOT' for national results. Single year only (2024 survey).