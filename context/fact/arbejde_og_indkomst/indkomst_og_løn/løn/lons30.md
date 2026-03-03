table: fact.lons30
description: Løn efter område, sektor, aflønningsform, lønmodtagergruppe, lønkomponenter, køn og tid
measure: indhold (unit Kr.)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- sektor: values [1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1016=Stat (inklusiv sociale kasser og fonde), 1018=Kommuner og regioner i alt, 1020=Regioner, 1025=Kommuner, 1046=Virksomheder og organisationer]
- afloen: values [TIFA=Time- og fastlønnede i alt, TIME=Timelønnede, FAST=Fastlønnede]
- longrp: values [LTOT=Lønmodtagergrupper i alt, LED=Ledere, VOK=Lønmodtagergrupper (eksklusiv unge og elever), MED=Lønmodtagere uden ledelsesansvar, UNG=Unge, 13-17 år, ELE=Elever]
- lonmal: values [FORINKL=FORTJENESTE PR. PRÆSTERET TIME, OVERB=Overtidstillæg pr. præsteret time, SYGDOM=Fraværsbetalinger pr. præsteret time, GENE=Genetillæg pr. præsteret time, GODE=Personalegoder pr. præsteret time ... NEDREST=Nedre kvartil, standardberegnet timefortjeneste, MEDIANST=Median, standardberegnet timefortjeneste, OVREST=Øvre kvartil, standardberegnet timefortjeneste, MDRSNIT=STANDARDBEREGNET MÅNEDSFORTJENESTE, ANTAL=Antal fuldtidsbeskæftigede i lønstatistikken]
- kon: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- tid: date range 2013-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- lonmal is a measurement-type selector with 25 values. ALWAYS filter to one lonmal value or every row is counted 25 times. Key values: FORINKL=total hourly earnings (most used), ANTAL=headcount (not a wage — completely different unit), STAND=standardised hourly pay, MDRSNIT=standardised monthly pay, MEDIAN/NEDRE/OVRE=percentiles (cannot be summed).
- sektor has overlapping aggregates: 1000=all, 1032=public (=1016+1018), 1016=state, 1018=kommuner+regioner (=1020+1025), 1046=private. Always filter to one sektor value.
- omrade joins dim.nuts at niveau 1 (5 regions: 81-85). Code "0" is the national total — not in dim.nuts, filter with WHERE omrade <> '0' or handle separately.
- afloen and longrp are independent selectors without overlapping aggregates — TIFA includes both TIME and FAST, LTOT includes all longrp groups. Filter to TIFA+LTOT for overall figures.
- Sample query: WHERE lonmal='FORINKL' AND sektor='1000' AND afloen='TIFA' AND longrp='LTOT' AND kon='MOK' to get all-sector, all-group, combined-sex total hourly earnings per region/year.
- Map: /geo/regioner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
