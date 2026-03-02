table: fact.ligefi9
description: Ligestillingsindikator for fraværsdagsværk ved barns sygdom (gennemsnitlig) efter indikator, sektor, branche og tid
measure: indhold (unit Antal)
columns:
- indikator: values [LAV1=Mænd (fraværsdagsværk pr. fuldtidsansat), LAV2=Kvinder (fraværsdagsværk pr. fuldtidsansat), LAV3=Forskel mellem mænd og kvinder (fraværsdagsværk pr. fuldtidsansat)]
- sektor: values [1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1016=Stat (inklusiv sociale kasser og fonde), 1018=Kommuner og regioner i alt, 1020=Regioner, 1025=Kommuner, 1046=Virksomheder og organisationer]
- branche: join dim.db on branche=kode::text [approx]; levels [2]
- tid: date range 2013-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- indikator is a gender-comparison selector with 3 values: LAV1=Mænd, LAV2=Kvinder, LAV3=Forskel (difference). Filter to one value. Do NOT sum across indikator.
- indhold is average fraværsdagsværk pr. fuldtidsansat for child sickness — a rate, not a count.
- branche uses numeric codes (1-10) matching dim.db_10 niveau 1 (Landbrug, Industri, Bygge og anlæg, etc.) plus TOT. The fact doc says dim.db join at niveau 2, but that is incorrect — the codes map to dim.db_10 niveau 1. Codes '4'=Handel og transport and 'TOT' are not in dim.db. Use ColumnValues("ligefi9", "branche") for the 10 industry group labels.
- sektor does NOT include '1047'/'1048' sub-types of virksomheder.
