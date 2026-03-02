table: fact.dnpin
description: Indlån i pengeinstitutter i alt efter instrument, datatype, sektor i ind- og udland, land, valuta og tid
measure: indhold (unit Mio. kr.)
columns:
- instrnat: values [PL00=Indlån i alt, PL60=- heraf repoindlån]
- data: values [ULT=Ultimobalance (mio. kr.), VAL=Valutakursreguleringer (mio. kr.), NET=Nettotransaktioner (mio. kr.), KI=Indeks over nominelle beholdninger (indeks 201501=100)]
- sektor2: values [1000=X000: Alle sektorer i ind- og udland, 1100=- X100: Ikke-finansielle selskaber, 1200=- X200: Finansielle selskaber, 12AA=-  - X2aa: Monetære finansielle institutioner (MFIer), 1210=-  -  - heraf X210: Centralbanker, 1220=-  -  - heraf X220: Kreditinstitutter, 1221=-  -  -  - heraf X221: Pengeinstitutter, 1222=-  -  -  - heraf X222: Realkreditinstitutter, 12BB=-  - X2bb: Andre finansielle institutioner ekskl. forsikringsselskaber og pensionskasser, 12CC=-  - X2cc: Forsikringsselskaber og pensionskasser, 1280=-  -  - X280: Forsikringsselskaber, 1290=-  -  - X290: Pensionskasser, 1300=- X300: Offentlig forvaltning og service, 1400=- X400: Husholdninger, 1410=- - X410: Husholdninger - personligt ejede virksomheder, 1430=- - X430: Husholdninger - lønmodtagere, pensionister mv., 1500=- X500: Nonprofitinstitutioner rettet mod husholdninger]
- land: join dim.lande_uhv on land=kode [approx]; levels [4]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- tid: date range 2003-01-01 to 2025-09-01
dim docs: /dim/lande_uhv.md, /dim/valuta_iso.md

notes:
- data is a measurement-type selector: ULT=end-of-period stock (mio. kr.), NET=net transactions, VAL=fx revaluation, KI=index (201501=100). Always filter to one value; typically data='ULT' for balance amounts.
- sektor2 is a hierarchy: 1000=alle sektorer total. All other codes are sub-components. Filter to a single non-overlapping level to avoid double-counting.
- valuta: Z01=alle valutaer (most queries want this). Z01 and X00 (foreign currencies total) do not join to dim.valuta_iso — that's fine, they're aggregate codes. For specific currencies (DKK, EUR, USD, ...) the dim join works.
- land: A1=hele verden, DK=Danmark, X0=udland i alt, E0/E9=EU/EEA aggregates. These 5 aggregate codes do not match dim.lande_uhv. Named countries (CH, DE, ES, FR, GB, NL, NO, SE, US) join at niveau=4. Use ColumnValues("lande_uhv", "titel", for_table="dnpin") to see the 14 available countries+aggregates.
- instrnat: PL00=indlån i alt (total). PL60 (repoindlån) is a sub-component. Filter to PL00 unless you specifically want repo deposits.
- To get a single total: instrnat='PL00', data='ULT', sektor2='1000', valuta='Z01', land='A1'.