table: fact.kv2kar4
description: Barrierer for besøg på dansk kulturarv efter årsag, køn og tid
measure: indhold (unit Pct.)
columns:
- aarsag: values [30420=Det interesserer mig ikke, 30430=Det er for dyrt, 30440=Jeg har ikke tid, 30450=Jeg har ikke nogen at følges med, 30460=Det er for svært at komme dertil, 30470=Det er ikke børnevenligt, 30480=Jeg er mere et hjemmemenneske, 30490=Det er ikke handicapvenligt, 41800=Andre årsager]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- indhold is percentage (Pct.) of non-visitors citing each barrier. Categories are NOT mutually exclusive — sums to 113% across all aarsag. Compare individual barrier rates, never sum.
- Top barriers (for kon=10): "Det interesserer mig ikke" (40%), "Jeg har ikke tid" (18%), "Andre årsager" (16%), "Jeg er mere et hjemmemenneske" (14%).
- No alder column — only kon breakdown. Single year only (2024).