table: fact.kv2mus5
description: Barrierer for museumsbesøg efter årsag, køn og tid
measure: indhold (unit Pct.)
columns:
- aarsag: values [30420=Det interesserer mig ikke, 30430=Det er for dyrt, 30440=Jeg har ikke tid, 30450=Jeg har ikke nogen at følges med, 30460=Det er for svært at komme dertil, 30470=Det er ikke børnevenligt, 30480=Jeg er mere et hjemmemenneske, 30490=Det er ikke handicapvenligt, 41800=Andre årsager]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- indhold is % of respondents who cite that barrier. aarsag values are independent — a person can have multiple barriers. Sums exceed 100%, so never aggregate across aarsag.
- No alder column (simpler than other kv2 tables). Filter kon=10 for national totals.
- Single year only (2024 survey).