table: fact.dnpuddk
description: Indenlandsk udlån fra pengeinstitutter efter instrument, datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid) og tid
measure: indhold (unit Mio. kr.)
columns:
- instrnat: values [AL00=Udlån i alt, AL10=- Anfordringstilgodehavender hos centralbanker, AL20=- Kassekreditter (revolverende lån) og overtræk, AL30=- Kredit på kreditkort, AL40=- Repoudlån, AL99=- Øvrige udlån]
- data: values [ULT=Ultimobalance (mio. kr.), VAL=Valutakursreguleringer (mio. kr.), NET=Nettotransaktioner (mio. kr.), KI=Indeks over nominelle beholdninger (indeks 201501=100)]
- indsek: values [1000=1000: Alle indenlandske sektorer, 1100=- 1100: Ikke-finansielle selskaber, 1200=- 1200: Finansielle selskaber, 12AA=-  - 12aa: Monetære finansielle institutioner (MFIer), 1210=-  -  - heraf 1210: Centralbanker, 1220=-  -  - heraf 1220: Kreditinstitutter, 1221=-  -  -  - heraf 1221: Pengeinstitutter, 1222=-  -  -  - heraf 1222: Realkreditinstitutter, 12BB=-  - 12bb: Andre finansielle institutioner ekskl. forsikringsselskaber og pensionskasser, 12CC=-  - 12cc: Forsikringsselskaber og pensionskasser, 1280=-  -  - 1280: Forsikringsselskaber, 1290=-  -  - 1290: Pensionskasser, 1300=- 1300: Offentlig forvaltning og service, 1400=- 1400: Husholdninger, 1410=-  - 1410: Husholdninger - personligt ejede virksomheder, 1430=-  - 1430: Husholdninger - lønmodtagere, pensionister mv., 1500=- 1500: Nonprofitinstitutioner rettet mod husholdninger]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- lobetid1: values [ALLE=Alle løbetider, M1A=Op til og med 1 år, S1A=Over 1 år]
- tid: date range 2013-09-01 to 2025-09-01
dim docs: /dim/valuta_iso.md

notes:
- data is a measurement-type selector: ULT=end-of-period stock (mio. kr.), NET=net transactions, VAL=fx revaluation, KI=index. Filter to data='ULT' for balance amounts.
- indsek is a hierarchy: 1000=alle indenlandske sektorer (total). Sub-codes (1100, 1200, 12AA, 1210, ..., 1400, 1410, 1430, 1500) are nested components. Pick one level; don't sum sub-sectors with their parent.
- instrnat: AL00=udlån i alt (total); AL10-AL99 are instrument sub-types summing to AL00.
- valuta: Z01=alle valutaer (typical), X00=foreign currencies only. Neither joins dim.valuta_iso; treat as inline aggregate codes.
- lobetid1: ALLE=all maturities (total); M1A and S1A are sub-ranges.
- For a simple domestic loan total: instrnat='AL00', data='ULT', indsek='1000', valuta='Z01', lobetid1='ALLE'.