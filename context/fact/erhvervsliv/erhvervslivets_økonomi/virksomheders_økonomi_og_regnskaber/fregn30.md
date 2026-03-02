table: fact.fregn30
description: Foreløbig regnskabsstatistik for private byerhverv efter branche, regnskabsposter, ejerform og tid
measure: indhold (unit -)
columns:
- erhverv: join dim.db on erhverv=kode::text; levels [2]
- regnskposter: values [ANTFIR=Firmaer (antal), XOM=Omsætning (mio. kr.), AARSV1=Ansatte (årsværk), XPO=Løn, pension mv. (mio. kr.), AARE=RESULTAT EFTER SELSKABSSKAT (mio. kr.), XVT=Værditilvækst (mio. kr.), PAST=AKTIVER I ALT = PASSIVER I ALT (mio. kr.), EGUL=Egenkapital (mio. kr.)]
- ejerform: values [TOT=I ALT, A=Aktie- og anpartsselskab mv., B=Enkeltmands- firma og I/S]
- tid: date range 2023-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- Foreløbige (preliminary) data for 2023 only — use regn30 for 2019-2022, fregn30 for the latest year.
- Smaller regnskposter set than regn30: only 8 key measures (same as fregn20). MUST filter regnskposter.
- ejerform: TOT=I alt, A=Aktie- og anpartsselskab mv., B=Enkeltmandsfirma og I/S. Filter WHERE ejerform='TOT' for totals. Never aggregate A+B+TOT together.
- erhverv same mixed letter+number codes. Use ColumnValues("fregn30", "erhverv").
