table: fact.lons11
description: Løn efter uddannelse, sektor, aflønningsform, lønmodtagergruppe, lønkomponenter, køn og tid
measure: indhold (unit Kr.)
columns:
- uddannelse: values [TOT=I alt, H10=H10 Grundskole, H1001=H1001 Ingen uddannelse, H1010=H1010 Grundskole til og med 6. klasse, H1020=H1020 Grundskole 7.-9. klasse ... H8080=H8080 Jordbrug, natur og miljø, Ph.d., H8090=H8090 Sundhedsvidenskab, Ph.d., H8097=H8097 Videregående uddannelser uden nærmere angivelse, Ph.d., H90=H90 Uoplyst mv., H9099=H9099 Uoplyst mv.]
- sektor: values [1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1016=Stat (inklusiv sociale kasser og fonde), 1018=Kommuner og regioner i alt, 1020=Regioner, 1025=Kommuner, 1046=Virksomheder og organisationer]
- afloen: values [TIFA=Time- og fastlønnede i alt, TIME=Timelønnede, FAST=Fastlønnede]
- longrp: values [LTOT=Lønmodtagergrupper i alt, LED=Ledere, VOK=Lønmodtagergrupper (eksklusiv unge og elever), MED=Lønmodtagere uden ledelsesansvar, UNG=Unge, 13-17 år, ELE=Elever]
- lonmal: values [FORINKL=FORTJENESTE PR. PRÆSTERET TIME, OVERB=Overtidstillæg pr. præsteret time, SYGDOM=Fraværsbetalinger pr. præsteret time, GENE=Genetillæg pr. præsteret time, GODE=Personalegoder pr. præsteret time ... NEDREST=Nedre kvartil, standardberegnet timefortjeneste, MEDIANST=Median, standardberegnet timefortjeneste, OVREST=Øvre kvartil, standardberegnet timefortjeneste, MDRSNIT=STANDARDBEREGNET MÅNEDSFORTJENESTE, ANTAL=Antal fuldtidsbeskæftigede i lønstatistikken]
- kon: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- tid: date range 2015-01-01 to 2024-01-01
notes:
- uddannelse has 89 values with two hierarchy levels: 3-char codes (H10, H20, ..., H90) = 10 major education groups, 5-char codes (H1001, H1010, ...) = ~80 detailed education types. TOT=overall. Mixing levels in a GROUP BY will double-count. Filter to one level: e.g. WHERE length(uddannelse)=3 for broad groups, or length(uddannelse)=5 for detail. Or filter to a single code.
- lonmal is a measurement-type selector with 25 values. ALWAYS filter to one value (FORINKL for total hourly earnings, ANTAL for headcount, MDRSNIT for monthly pay).
- sektor has overlapping aggregates: 1000=all, 1032=public, 1046=private, etc. Filter to one value.
- afloen=TIFA + longrp=LTOT + kon=MOK for overall totals.
- Only from 2015. Use ColumnValues("lons11", "uddannelse") to browse all codes with labels.
