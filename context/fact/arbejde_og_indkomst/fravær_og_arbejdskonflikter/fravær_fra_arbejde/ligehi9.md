table: fact.ligehi9
description: Ligestillingsindikator for fraværsdagsværk ved egen sygdom (gennemsnitlig) efter indikator, sektor, arbejdsfunktion, familietype og tid
measure: indhold (unit Antal)
columns:
- indikator: values [LAV1=Mænd (fraværsdagsværk pr. fuldtidsansat), LAV2=Kvinder (fraværsdagsværk pr. fuldtidsansat), LAV3=Forskel mellem mænd og kvinder (fraværsdagsværk pr. fuldtidsansat)]
- sektor: values [1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1016=Stat (inklusiv sociale kasser og fonde), 1018=Kommuner og regioner i alt, 1020=Regioner, 1025=Kommuner, 1046=Virksomheder og organisationer]
- arbfunk: join dim.disco on arbfunk=kode::text [approx]; levels [1, 2]
- famtyp: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, EMHB=Enlige med hjemmeboende børn, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, PMHB=Par med hjemmeboende børn]
- tid: date range 2013-01-01 to 2023-01-01
dim docs: /dim/disco.md
notes:
- indikator is a gender-comparison selector with 3 values: LAV1=Mænd, LAV2=Kvinder, LAV3=Forskel (difference). Filter to one value. Do NOT sum across indikator.
- indhold is average fraværsdagsværk pr. fuldtidsansat for own sickness — a rate, not a count.
- arbfunk joins dim.disco at niveau 1 and niveau 2. 'TOT'=I alt does not join. Do not mix niveaus in the same query.
- famtyp = family type (TOT, pairs with/without children, singles with/without children). TOT=I alt. Note that F1 (med hjemmeboende børn) includes both E1 (enlige) and P1 (par) subsets — filter carefully to avoid double-counting.
- sektor does NOT include '1047'/'1048' sub-types.
