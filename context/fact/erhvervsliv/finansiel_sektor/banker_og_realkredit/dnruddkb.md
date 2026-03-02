table: fact.dnruddkb
description: Indenlandsk realkreditudlån fra realkreditinstitutter efter datatype, valuta, branche og tid
measure: indhold (unit -)
columns:
- datat: values [ULT=Ultimobalance - markedsværdi (mio. kr.), VAL=Valutakursreguleringer (mio. kr.), NET=Nettotransaktioner (mio. kr.), KI=Indeks over nominelle beholdninger (indeks 201501=100)]
- valuta: values [Z01=Alle valutaer, DKK=DKK, X00=Udenlandsk valuta i alt]
- branche: join dim.db on branche=kode::text [approx]
- tid: date range 2014-06-01 to 2025-09-01
dim docs: /dim/db.md

notes:
- datat is a measurement-type selector (note: column is named 'datat', not 'data'): ULT=end-of-period stock as market value (mio. kr.), NET=net transactions, VAL=fx revaluation, KI=index. Filter to datat='ULT' for balance amounts.
- branche uses NACE section-level letter+ZZ codes: ALLE=all sectors total, AZZ=Landbrug, BZZ=Råstofindvinding, CZZ=Fremstilling, DZZ=Energi, EZZ=Vandforsyning, FZZ=Byggeri, GZZ=Handel, HZZ=Transport, IZZ=Overnatning, JZZ=Information, KZZ=Finansiering, LZZ=Ejendomme, MZZ=Rådgivning, NZZ=Service, OZZ=Off.forvaltning, PZZ=Uddannelse, QZZ=Sundhed, RZZ=Kultur, SZZ=Andre service, TZZ=Privathusholdninger m. ansat, YZZ=Lønmodtagere/pensionister.
- branche does NOT join to dim.db (type mismatch: text ZZ-codes vs integer DB07 codes). The dim link in this doc is incorrect; treat branche as inline values.
- Note: no 'UZZ' (Int.org) code in this table (unlike dnpuddkb/dnpindkb).
- valuta: Z01=alle valutaer (typical), DKK, X00=foreign currencies total. All are inline; Z01 gives the overall total.
- To get total mortgage lending by sector: datat='ULT', valuta='Z01', branche='ALLE'.