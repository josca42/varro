table: fact.dnmin
description: Indlån i den konsoliderede MFI-sektor i alt ekskl. Nationalbanken efter instrument, datatype, sektor, valuta og tid
measure: indhold (unit Mio. kr.)
columns:
- instrnat: values [PL00=Indlån i alt, PL10=Transferable indlån (anfordring), PL20=Dag til dag-indskud, PL30=Elektroniske penge, PL40=Tidsindskud, PL50=Indlån med opsigelse, PL60=Repoindlån]
- data: values [ULT=Ultimobalance (mio. kr.), VAL=Valutakursreguleringer (mio. kr.), NET=Nettotransaktioner (mio. kr.), REK=Reklassifikationer (mio. kr.), KI=Indeks over nominelle beholdninger (indeks 201501=100)]
- sektornat: join dim.esr_sekt on sektornat=kode [approx]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- tid: date range 2003-01-01 to 2025-09-01
dim docs: /dim/esr_sekt.md, /dim/valuta_iso.md

notes:
- data is a measurement-type selector: ULT=end-of-period stock (mio. kr.), NET=net transactions, VAL=fx revaluation, REK=reclassifications, KI=index. Filter to data='ULT' for balance amounts.
- sektornat uses compound sector+country codes like '10XXDK' (all domestic sectors), '1100DK' (domestic non-financial corps), '10XXA1' (all sectors worldwide), '1000X0' (all foreign sectors). These do NOT join to dim.esr_sekt (0% match); the dim link in this doc is incorrect. Treat sektornat as inline values.
- instrnat: PL00=indlån i alt (total); PL10-PL60 are instrument sub-types that sum to PL00.
- valuta: Z01=alle valutaer (typical), X00=foreign currencies total. Neither joins dim.valuta_iso; treat as inline aggregate codes.
- For a simple total MFI deposit: instrnat='PL00', data='ULT', sektornat='10XXDK' (domestic) or '10XXA1' (all), valuta='Z01'.