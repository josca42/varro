table: fact.dnmud
description: Udlån fra den konsoliderede MFI-sektor i alt ekskl. Nationalbanken efter datatype, sektor, valuta og tid
measure: indhold (unit Mio. kr.)
columns:
- data: values [ULT=Ultimobalance (mio. kr.), VAL=Valutakursreguleringer (mio. kr.), BORS=Børskursreguleringer (mio. kr.), NET=Nettotransaktioner (mio. kr.), REK=Reklassifikationer (mio. kr.), TAB=Tab på udlån (mio. kr.), KI=Indeks over nominelle beholdninger (indeks 201501=100)]
- sektornat: values [10XXA1=Alle sektorer, 10XXDK=1000: Alle indenlandske sektorer, 1100DK=- 1100: Ikke-finansielle selskaber, 12XXDK=- 1200: Finansielle selskaber, 12BBDK=-  - 12bb: Andre finansielle institutioner ekskl. forsikringsselskaber og pensionskasser, 12CCDK=-  - 12cc: Forsikringsselskaber og pensionskasser, 1280DK=-  -  - 1280: Forsikringsselskaber, 1290DK=-  -  - 1290: Pensionskasser, 1300DK=- 1300: Offentlig forvaltning og service, 1400DK=- 1400: Husholdninger, 1410DK=-  - 1410: Husholdninger - personligt ejede virksomheder, 1430DK=-  - 1430: Husholdninger - lønmodtagere, pensionister mv., 1500DK=- 1500: Nonprofitinstitutioner rettet mod husholdninger, 1000X0=2000: Alle udenlandske sektorer]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- tid: date range 2003-01-01 to 2025-09-01
dim docs: /dim/valuta_iso.md

notes:
- data is a measurement-type selector: ULT=end-of-period stock (mio. kr.), NET=net transactions, VAL=fx revaluation, BORS=equity revaluation, REK=reclassifications, TAB=loan losses, KI=index. Filter to data='ULT' for balance amounts.
- sektornat uses inline compound sector+country codes: 10XXA1=alle sektorer worldwide, 10XXDK=alle indenlandske, 1000X0=alle udenlandske. Sub-sectors (1100DK, 12XXDK, ..., 1400DK, ...) are nested within 10XXDK. Don't sum sub-sectors with their parent.
- valuta: Z01=alle valutaer (typical), X00=foreign currencies total. These don't join to dim.valuta_iso; treat as inline aggregate codes.
- No instrnat column — this is total loans only. For instrument breakdown use dnpuddk (banks) or dnruddkb (mortgage banks).
- For domestic MFI lending total: data='ULT', sektornat='10XXDK', valuta='Z01'.