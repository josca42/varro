table: fact.ligehi8
description: Ligestillingsindikator for fraværsdagsværk ved egen sygdom (gennemsnitlig) efter indikator, sektor, arbejdsfunktion, alder og tid
measure: indhold (unit Antal)
columns:
- indikator: values [LAV1=Mænd (fraværsdagsværk pr. fuldtidsansat), LAV2=Kvinder (fraværsdagsværk pr. fuldtidsansat), LAV3=Forskel mellem mænd og kvinder (fraværsdagsværk pr. fuldtidsansat)]
- sektor: values [1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1016=Stat (inklusiv sociale kasser og fonde), 1018=Kommuner og regioner i alt, 1020=Regioner, 1025=Kommuner, 1046=Virksomheder og organisationer]
- arbfunk: join dim.disco on arbfunk=kode::text [approx]; levels [1, 2]
- alder: values [TOT=Alder i alt, 1819=18-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- tid: date range 2013-01-01 to 2023-01-01
dim docs: /dim/disco.md
notes:
- indikator is a gender-comparison selector with 3 values: LAV1=Mænd, LAV2=Kvinder, LAV3=Forskel (difference). Filter to one value. Do NOT sum across indikator.
- indhold is average fraværsdagsværk pr. fuldtidsansat for own sickness — a rate, not a count.
- arbfunk joins dim.disco at niveau 1 (single-digit) and niveau 2 (two-digit). 'TOT'=I alt does not join. Mixing niveaus causes double-counting — filter to one niveau.
- alder uses coarser age groups than fra024 (6 groups: 18-19, 20-29, 30-39, 40-49, 50-59, 60+) plus TOT.
- sektor does NOT include '1047'/'1048' sub-types.
