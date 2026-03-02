table: fact.fregn20
description: Foreløbig regnskabsstatistik for private byerhverv efter branche, regnskabsposter, størrelse og tid
measure: indhold (unit -)
columns:
- erhverv: join dim.db on erhverv=kode::text; levels [2]
- regnskposter: values [ANTFIR=Firmaer (antal), XOM=Omsætning (mio. kr.), AARSV1=Ansatte (årsværk), XPO=Løn, pension mv. (mio. kr.), AARE=RESULTAT EFTER SELSKABSSKAT (mio. kr.), XVT=Værditilvækst (mio. kr.), PAST=AKTIVER I ALT = PASSIVER I ALT (mio. kr.), EGUL=Egenkapital (mio. kr.)]
- storrelse: values [TOT=I alt, 0-9=0-9 ansatte, 10-19=10-19 ansatte, 20-99=20-99 ansatte, 100OV=100 ansatte og derover]
- tid: date range 2023-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- Foreløbige (preliminary) data for 2023 only — use regn20 for 2019-2022, fregn20 for the latest year.
- Smaller regnskposter set than regn20: only 8 key measures (ANTFIR, XOM, AARSV1, XPO, AARE, XVT, PAST, EGUL). MUST filter regnskposter.
- storrelse same as regn20 (TOT, 0-9, 10-19, 20-99, 100OV). Filter WHERE storrelse='TOT' for totals.
- erhverv same mixed letter+number codes. Use ColumnValues("fregn20", "erhverv").
