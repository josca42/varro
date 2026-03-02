table: fact.kv2mo4
description: Barrierer for forbrug af sport og motion efter årsag, køn og tid
measure: indhold (unit Pct.)
columns:
- aarsag: values [41700=Det interesserer mig ikke, 41710=Det er for dyrt, 41720=Jeg har ikke tid, 41730=Jeg har ikke nogen at følges med, 41740=Det er for svært at komme dertil, 41750=Jeg har ikke plads eller mulighed derhjemme, 41760=Det er ikke handicapvenligt, 41780=Har vanskeligt ved det pga. mit helbred, fysik eller skader, 41800=Andre årsager]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- aarsag values are NOT mutually exclusive — respondents can cite multiple barriers. Values sum to ~143% for kon=10. Each row = "X% of non-participants cite this barrier".
- Base population = people who do NOT consume sport/motion. Not the general population.
- Single time point (2024 only). No alder dimension in this table — compare with kv2mo5 for spectator sport barriers.