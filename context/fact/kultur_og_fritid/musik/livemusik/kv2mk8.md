table: fact.kv2mk8
description: Barrierer for forbrug af koncerter og musikfestivaler efter årsag, køn og tid
measure: indhold (unit Pct.)
columns:
- aarsag: values [30420=Det interesserer mig ikke, 30430=Det er for dyrt, 30440=Jeg har ikke tid, 30450=Jeg har ikke nogen at følges med, 30460=Det er for svært at komme dertil, 30470=Det er ikke børnevenligt, 30480=Jeg er mere et hjemmemenneske, 30490=Det er ikke handicapvenligt, 41800=Andre årsager]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey percentages (single year 2024). aarsag (barrier reasons) are NOT mutually exclusive — a person can cite multiple barriers. Values sum to ~158% (e.g. "not interested" 30%, "too expensive" 30%, "no time" 17%, ...). Never sum across aarsag.
- Each row answers: "what % of non-concert-goers cite this reason as a barrier?"
- kon='10' gives totals across gender.