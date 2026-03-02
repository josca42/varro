table: fact.lons50
description: Løn efter alder, sektor, aflønningsform, lønmodtagergruppe, lønkomponenter, køn og tid
measure: indhold (unit Kr.)
columns:
- alder1: values [TOT=Alder i alt, -19=Under 20 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-=60 år og derover]
- sektor: values [1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1016=Stat (inklusiv sociale kasser og fonde), 1018=Kommuner og regioner i alt, 1020=Regioner, 1025=Kommuner, 1046=Virksomheder og organisationer]
- afloen: values [TIFA=Time- og fastlønnede i alt, TIME=Timelønnede, FAST=Fastlønnede]
- longrp: values [LTOT=Lønmodtagergrupper i alt, LED=Ledere, VOK=Lønmodtagergrupper (eksklusiv unge og elever), MED=Lønmodtagere uden ledelsesansvar, UNG=Unge, 13-17 år, ELE=Elever]
- lonmal: values [FORINKL=FORTJENESTE PR. PRÆSTERET TIME, OVERB=Overtidstillæg pr. præsteret time, SYGDOM=Fraværsbetalinger pr. præsteret time, GENE=Genetillæg pr. præsteret time, GODE=Personalegoder pr. præsteret time ... NEDREST=Nedre kvartil, standardberegnet timefortjeneste, MEDIANST=Median, standardberegnet timefortjeneste, OVREST=Øvre kvartil, standardberegnet timefortjeneste, MDRSNIT=STANDARDBEREGNET MÅNEDSFORTJENESTE, ANTAL=Antal fuldtidsbeskæftigede i lønstatistikken]
- kon: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- tid: date range 2013-01-01 to 2024-01-01
notes:
- lonmal is a measurement-type selector with 25 values. ALWAYS filter to one lonmal value. Same values as lons30/lons40: FORINKL=total hourly earnings (most used), ANTAL=headcount, STAND=standardised hourly pay, MDRSNIT=monthly pay, MEDIAN/NEDRE/OVRE=percentiles.
- sektor has overlapping aggregates: 1000=all, 1032=public (1016+1018), 1016=state, 1018=municipalities+regions (1020+1025), 1046=private. Filter to one value.
- alder1 is a flat age-band column (no hierarchical overlap): TOT=all ages, then 10-year bands (-19, 20-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-). Filter alder1='TOT' for all ages.
- afloen=TIFA + longrp=LTOT + kon=MOK for overall totals.
