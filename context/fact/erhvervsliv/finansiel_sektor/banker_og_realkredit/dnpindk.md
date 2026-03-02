table: fact.dnpindk
description: Indenlandsk indlån i pengeinstitutter efter instrument, datatype, indenlandsk sektor, valuta, løbetid (oprindelig løbetid) og tid
measure: indhold (unit -)
columns:
- instrnat: values [PL00=Indlån i alt, PL10=Transferable indlån (anfordring), PL20=Dag til dag-indskud, PL30=Elektroniske penge, PL40=Tidsindskud, PL50=Indlån med opsigelse, PL60=Repoindlån]
- data: values [ULT=Ultimobalance (mio. kr.), VAL=Valutakursreguleringer (mio. kr.), NET=Nettotransaktioner (mio. kr.), KI=Indeks over nominelle beholdninger (indeks 201501=100)]
- indsek: values [1000.0=1000: Alle indenlandske sektorer, 1100.0=- 1100: Ikke-finansielle selskaber, 1200.0=- 1200: Finansielle selskaber, 1300.0=- 1300: Offentlig forvaltning og service, 1400.0=- 1400: Husholdninger, 1410.0=-  - 1410: Husholdninger - personligt ejede virksomheder, 1430.0=-  - 1430: Husholdninger - lønmodtagere, pensionister mv., 1500.0=- 1500: Nonprofitinstitutioner rettet mod husholdninger]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- lobetid1: values [ALLE=Alle løbetider, M1A=Op til og med 1 år, 3M=- Op til og med 3 mdr., 1A=- Over 3 mdr. og op til og med 1 år, S1A=Over 1 år, 2A=- Over 1 år og op til og med 2 år, S2A=- Over 2 år, 5A=- - Over 2 år og op til og med 5 år, S5A=- - Over 5 år]
- tid: date range 2003-01-01 to 2025-09-01
dim docs: /dim/valuta_iso.md

notes:
- data is a measurement-type selector: ULT=end-of-period stock (mio. kr.), NET=net transactions, VAL=fx revaluation, KI=index. Filter to one; use data='ULT' for balance amounts.
- indsek is a hierarchy: 1000.0=alle indenlandske sektorer (total). Sub-sectors (1100, 1200, 1300, 1400, 1410, 1430, 1500) are components. Filter to indsek='1000.0' for the national total or a single sub-sector.
- valuta: Z01=alle valutaer (typical), X00=foreign currencies only. These two don't join to dim.valuta_iso; treat as inline aggregate codes.
- lobetid1 hierarchy: ALLE=all maturities total. Other codes (M1A, 3M, 1A, S1A, etc.) are sub-ranges that sum to ALLE.
- instrnat: PL00=indlån i alt (total); all other PL codes are instrument sub-types summing to PL00.
- For a simple domestic deposit total: instrnat='PL00', data='ULT', indsek='1000.0', valuta='Z01', lobetid1='ALLE'.