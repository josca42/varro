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
- bnogle is a measurement selector that doubles every row: 1000 = average contacts per person (e.g. 3.6), 1010 = share of persons with any contact in pct (e.g. 78.6). Always filter to one. These are different measures of the same population and must never be summed or averaged together.
- parorendeforhold has only 2 values: PR710 (lives with 1 parent) and PR720 (lives with 2 parents). No total-across-family-type code — these are mutually exclusive and can be summed for a combined count.
- koen has 10 (i alt), 1 (mænd), 2 (kvinder). Filter to 10 for gender-total.
- alerams has 9817 (0–17 i alt), 09 (0–9 år), 10-17 (10–17 år). The two sub-groups sum to the total. Filter to one level.
- For 0–17 year olds living with parents only (no grandparent dimension in this table). Use paaroe02 if you want grandparent counts.