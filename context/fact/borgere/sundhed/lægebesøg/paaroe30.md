table: fact.paaroe30
description: Befolkningens kontakt til praktiserende læge (0-17 år) efter relation, nøgletal, alder, køn og tid
measure: indhold (unit -)
columns:
- parorendeforhold: values [PR710=Bor sammen med en forælder, PR720=Bor sammen med to forældre]
- bnogle: values [1000=Kontakter (gennemsnitligt antal pr. person), 1010=Personer med kontakt (pct.)]
- alerams: values [9817=0-17 år i alt, 09=0-9 år, 10-17=10-17 år]
- koen: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- tid: date range 2021-01-01 to 2024-01-01
notes:
- For children 0-17 years. parorendeforhold has only two categories (single parent vs two parents) — not a total row. These categories do not cover all children (excludes those not living with any parent).
- bnogle is a measurement selector (1000=avg contacts per person, 1010=% with contact). Never aggregate across bnogle values.
- koen uses 10=køn i alt, 1=mænd, 2=kvinder (not TOT/M/K like most tables in this subject).
- alerams: 9817=0-17 total, 09=0-9, 10-17=10-17. Note unusual total code 9817.
- No regional breakdown. Only from 2021.
