table: fact.kv2fs4
description: Barrierer for brug af biografer efter årsag, køn og tid
measure: indhold (unit Pct.)
columns:
- aarsag: values [30420=Det interesserer mig ikke, 30430=Det er for dyrt, 30440=Jeg har ikke tid, 30450=Jeg har ikke nogen at følges med, 30460=Det er for svært at komme dertil, 30470=Det er ikke børnevenligt, 30480=Jeg er mere et hjemmemenneske, 30490=Det er ikke handicapvenligt, 41800=Andre årsager]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey data, single year (2024 only). Values are percentages of respondents who cited each barrier.
- aarsag values are NOT mutually exclusive — a person can cite multiple barriers to cinema attendance. Do not sum across aarsag.
- kon=10 is total. No age breakdown in this table (unlike kv2fs1–3).