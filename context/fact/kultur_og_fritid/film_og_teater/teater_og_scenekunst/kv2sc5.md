table: fact.kv2sc5
description: Barrierer for forbrug af scenekunst efter årsag, køn og tid
measure: indhold (unit Pct.)
columns:
- aarsag: values [30420=Det interesserer mig ikke, 30430=Det er for dyrt, 30440=Jeg har ikke tid, 30450=Jeg har ikke nogen at følges med, 30460=Det er for svært at komme dertil, 30470=Det er ikke børnevenligt, 30480=Jeg er mere et hjemmemenneske, 30490=Det er ikke handicapvenligt, 41800=Andre årsager]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- All values are survey percentages from Kulturvaneundersøgelsen 2024. Single snapshot. Covers non-consumers (those who did not consume scenekunst).
- aarsag (barrier/reason) values are NOT mutually exclusive — respondents can cite multiple reasons. The 9 aarsag values for kon=10 sum to 133%. Never sum across aarsag.
- kon: 10=Køn i alt, 1=Mænd, 2=Kvinder. Filter to one. No alder breakdown in this table (unlike kv2sc1–4).
- Each value reads as "X% of non-consumers cited [reason] as a barrier".