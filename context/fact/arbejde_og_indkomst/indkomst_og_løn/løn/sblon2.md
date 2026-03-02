table: fact.sblon2
description: Standardberegnet lønindeks efter arbejdsfunktion, sektor, enhed og tid
measure: indhold (unit Indeks)
columns:
- arbfunk: values [TOT=TOT I alt, 0=0 Militært arbejde, 1=1 Ledelsesarbejde, 2=2 Arbejde, der forudsætter viden på højeste niveau inden for pågældende område, 3=3 Arbejde, der forudsætter viden på mellemniveau, 4=4 Almindeligt kontor- og kundeservicearbejde, 5=5 Service- og salgsarbejde, 6=6 Arbejde inden for landbrug, skovbrug og fiskeri ekskl. medhjælp, 7=7 Håndværkspræget arbejde, 8=8 Operatør- og monteringsarbejde samt transportarbejde, 9=9 Andet manuelt arbejde]
- sektor: values [1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1016=Stat (inklusiv sociale kasser og fonde), 1018=Kommuner og regioner i alt, 1020=Regioner, 1025=Kommuner, 1046=Virksomheder og organisationer]
- varia1: values [100=Indeks, 215=Ændring i forhold til samme kvartal året før (pct.)]
- tid: date range 2016-01-01 to 2025-04-01
notes:
- varia1 is a measurement-type selector: 100=index value, 215=year-on-year pct change. ALWAYS filter to one value — every arbfunk/sektor combination appears twice (once per measure type).
- sektor has overlapping aggregates: 1000=all, 1032=public, 1046=private, etc. Filter to one value.
- arbfunk has 11 values: TOT=all, 0=military, 1=management, 2=highest-knowledge, 3=mid-level, 4=clerical, 5=service/sales, 6=agriculture, 7=craft, 8=operators, 9=manual. These are top-level ISCO-08 major groups — no hierarchy overlap, can freely filter or group.
- Quarterly frequency (Q1 2016 to Q2 2025). Use for wage index by occupation type across sectors.
