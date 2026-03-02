table: fact.kv2lit4
description: Barrierer for forbrug af litteratur efter årsag, køn og tid
measure: indhold (unit Pct.)
columns:
- aarsag: values [40640=Det interesserer mig ikke, 40650=Jeg har ikke tid, 40660=Det er svært at finde ud af, hvad jeg skal læse eller lytte til, 40670=Sproglige eller læsemæssige udfordringer, 40680=Jeg kan ikke koncentrere mig om at læse eller lytte til bøger, 41800=Andre årsager]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey data (2024 only). indhold is a percentage (Pct.) of non-readers citing each barrier.
- aarsag values are NON-mutually exclusive — a person can cite multiple barriers. The 6 values sum to >130%. Never sum across aarsag values; each is an independent rate.
- kon=10 ("Køn i alt") is the total. Filter to one kon value.
- No alder dimension — only gender breakdown available.
- Single time point (2024). No trend analysis possible.