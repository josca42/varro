table: fact.ligefi8
description: Ligestillingsindikator for fraværsdagsværk ved barns sygdom (gennemsnitlig) efter indikator, sektor, indkomst og tid
measure: indhold (unit Antal)
columns:
- indikator: values [LAV1=Mænd (fraværsdagsværk pr. fuldtidsansat), LAV2=Kvinder (fraværsdagsværk pr. fuldtidsansat), LAV3=Forskel mellem mænd og kvinder (fraværsdagsværk pr. fuldtidsansat)]
- sektor: values [1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1016=Stat (inklusiv sociale kasser og fonde), 1018=Kommuner og regioner i alt, 1020=Regioner, 1025=Kommuner, 1046=Virksomheder og organisationer]
- indkom: values [TOT=I alt, 1000=Under   -  99.999 kr., 1001=100.000 - 149.999 kr., 1002=149.000 - 199.999 kr., 1003=200.000 - 249.999 kr. ... 1015=800.000 - 849.999 kr., 1016=850.000 - 899.999 kr., 1017=900.000 - 949.999 kr., 1018=950.000 - 999.999 kr., 1019=1.000.000 og derover]
- tid: date range 2013-01-01 to 2023-01-01
notes:
- indikator is a gender-comparison selector with 3 values: LAV1=Mænd, LAV2=Kvinder, LAV3=Forskel (difference). Each row exists once per indikator — filter to one value. Do NOT sum across indikator values.
- indhold is the average fraværsdagsværk pr. fuldtidsansat for child sickness — already a per-person rate, not a count.
- indkom = income brackets (TOT=I alt plus ~20 income groups from <100k to 1M+). Use ColumnValues("ligefi8", "indkom") for exact labels.
- sektor does NOT include '1047'/'1048' sub-types of virksomheder — simpler than the fra0XX sektor list.
- No dim joins in this table.
