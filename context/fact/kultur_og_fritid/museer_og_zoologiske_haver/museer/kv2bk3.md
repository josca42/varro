table: fact.kv2bk3
description: Forbrug af billedkunst efter billedkunstens placering, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- bilkunstplacering: values [30390=I lokalområdet (din by eller din omegn), 30400=I Danmark uden for lokalområdet, 30410=I udlandet]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- indhold is % of respondents who consumed visual art at that geographic location. bilkunstplacering values are independent — a person can consume art locally and abroad. Sums can exceed 100%, so never aggregate across bilkunstplacering.
- Filter kon=10 and alder='TOT' for national results. Single year only (2024 survey).