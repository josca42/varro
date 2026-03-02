table: fact.lons40
description: Løn efter branche (DB07), sektor, aflønningsform, lønmodtagergruppe, lønkomponenter, køn og tid
measure: indhold (unit Kr.)
columns:
- branche07: join dim.db on branche07=kode::text; levels [2]
- sektor: values [1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1016=Stat (inklusiv sociale kasser og fonde), 1018=Kommuner og regioner i alt, 1020=Regioner, 1025=Kommuner, 1046=Virksomheder og organisationer]
- afloen: values [TIFA=Time- og fastlønnede i alt, TIME=Timelønnede, FAST=Fastlønnede]
- longrp: values [LTOT=Lønmodtagergrupper i alt, LED=Ledere, VOK=Lønmodtagergrupper (eksklusiv unge og elever), MED=Lønmodtagere uden ledelsesansvar, UNG=Unge, 13-17 år, ELE=Elever]
- lonmal: values [FORINKL=FORTJENESTE PR. PRÆSTERET TIME, OVERB=Overtidstillæg pr. præsteret time, SYGDOM=Fraværsbetalinger pr. præsteret time, GENE=Genetillæg pr. præsteret time, GODE=Personalegoder pr. præsteret time ... NEDREST=Nedre kvartil, standardberegnet timefortjeneste, MEDIANST=Median, standardberegnet timefortjeneste, OVREST=Øvre kvartil, standardberegnet timefortjeneste, MDRSNIT=STANDARDBEREGNET MÅNEDSFORTJENESTE, ANTAL=Antal fuldtidsbeskæftigede i lønstatistikken]
- kon: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- tid: date range 2013-01-01 to 2024-01-01
dim docs: /dim/db.md
notes:
- WARNING: The documented dim.db join (branche07=kode::text) is WRONG and produces misleading labels. Numeric codes 1-10 in this table mean DST sector aggregates (e.g. "1"="Landbrug, skovbrug og fiskeri" = the whole agriculture sector), but dim.db code 1 = "Plante- og husdyravl" (a specific sub-group). Never join to dim.db for this table.
- branche07 uses a three-tier system: TOT=overall, single letters A-S=DB07 sections, compound letters CA/CB/JA/QB etc.=DB07 sub-sections, numbers 1-10=DST custom sector aggregates that parallel the letter codes. Use ColumnValues("lons40", "branche07") to see all 30 codes with correct labels.
- lonmal is a measurement-type selector with 25 values. ALWAYS filter to one lonmal value. FORINKL=total hourly earnings, ANTAL=headcount, STAND=standardised hourly pay, MDRSNIT=monthly pay.
- sektor has overlapping aggregates (same as lons30): always filter to one value. 1000=all, 1032=public, 1046=private.
- afloen=TIFA + longrp=LTOT gives overall totals. kon=MOK for combined sex.
- All 6 non-tid, non-indhold columns must be filtered to a single value when you only want one measure, or you need to GROUP BY them to avoid over-aggregation.
