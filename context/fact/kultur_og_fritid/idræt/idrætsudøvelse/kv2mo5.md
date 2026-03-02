table: fact.kv2mo5
description: Barrierer for forbrug af tilskuersport efter årsag, køn og tid
measure: indhold (unit Pct.)
columns:
- aarsag: values [41700=Det interesserer mig ikke, 41710=Det er for dyrt, 41720=Jeg har ikke tid, 41730=Jeg har ikke nogen at følges med, 41740=Det er for svært at komme dertil, 41755=Det er ikke børnevenligt, 41760=Det er ikke handicapvenligt, 41770=Jeg er mere et hjemmemenneske, 41790=Jeg vil hellere følge livesport i radio, tv, på internettet eller sociale medier, 41800=Andre årsager]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- aarsag values are NOT mutually exclusive — respondents can cite multiple barriers. Values sum to ~140% for kon=10. Each row = "X% of non-spectators cite this barrier".
- Base population = people who do NOT consume tilskuersport. Not the general population.
- aarsag differs from kv2mo4: includes spectator-specific barriers (41755=ikke børnevenligt, 41770=hjemmemenneske, 41790=vil hellere følge via media). kode 41750 (ingen plads derhjemme) from kv2mo4 is absent here.
- Single time point (2024 only).