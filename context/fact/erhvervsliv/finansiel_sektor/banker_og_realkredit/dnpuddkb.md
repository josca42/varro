table: fact.dnpuddkb
description: Indenlandsk udlån fra pengeinstitutter efter datatype, valuta, branche og tid
measure: indhold (unit Mio. kr.)
columns:
- data: values [ULT=Ultimobalance (mio. kr.), VAL=Valutakursreguleringer (mio. kr.), NET=Nettotransaktioner (mio. kr.), KI=Indeks over nominelle beholdninger (indeks 201501=100)]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- branche: join dim.db on branche=kode::text [approx]
- tid: date range 2013-09-01 to 2025-09-01
dim docs: /dim/db.md, /dim/valuta_iso.md

notes:
- data is a measurement-type selector: ULT=end-of-period stock (mio. kr.), NET=net transactions, VAL=fx revaluation, KI=index. Filter to data='ULT' for balance amounts.
- branche uses NACE section-level letter+ZZ codes: ALLE=all sectors total, AZZ=Landbrug, BZZ=Råstofindvinding, CZZ=Fremstilling, DZZ=Energi, EZZ=Vandforsyning, FZZ=Byggeri, GZZ=Handel, HZZ=Transport, IZZ=Overnatning, JZZ=Information, KZZ=Finansiering, LZZ=Ejendomme, MZZ=Rådgivning, NZZ=Service, OZZ=Off.forvaltning, PZZ=Uddannelse, QZZ=Sundhed, RZZ=Kultur, SZZ=Andre service, TZZ=Privathusholdninger m. ansat, UZZ=Int.org, YZZ=Lønmodtagere/pensionister.
- branche does NOT join to dim.db (type mismatch: text ZZ-codes vs integer DB07 codes). The dim link in this doc is incorrect; treat branche as inline values.
- valuta: Z01=alle valutaer (typical), X00=foreign currencies only, DKK=DKK. Z01 and X00 don't join to dim.valuta_iso; treat as inline aggregate codes.
- For total domestic loan by sector: data='ULT', valuta='Z01', branche='ALLE'.