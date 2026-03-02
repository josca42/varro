table: fact.regn20
description: Regnskabsstatistik for private byerhverv efter branche, regnskabsposter, størrelse og tid
measure: indhold (unit -)
columns:
- erhverv: join dim.db on erhverv=kode::text [approx]; levels [2]
- regnskposter: values [ANTFIR=Firmaer (antal), XOM=Omsætning (mio. kr.), BESK=Antal beskæftigede (i årsværk), AARSV=Heraf: ansatte (i årsværk), ADR=Andre driftsindtægter (mio. kr.) ... XINT=INVESTERINGER, NETTO (mio. kr.), XOB=Driftsindtægter pr. beskæftiget (1000 kr.), gennemsnit, XLA=Løn pr. ansat (1000 kr.), gennemsnit, XOBM=Driftsindtægter pr. beskæftiget (1000 kr.), median, XLAM=Løn pr. ansat (1000 kr.), median]
- storrelse: values [TOT=I alt, 0-9=0-9 ansatte, 10-19=10-19 ansatte, 20-99=20-99 ansatte, 100OV=100 ansatte og derover]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- Adds storrelse dimension to regn50's structure: TOT=I alt, 0-9, 10-19, 20-99, 100OV. Filter WHERE storrelse='TOT' to get totals across all sizes; filter to a specific size band to compare small vs. large firms.
- regnskposter is a measure-selector: MUST filter to one value. Use ColumnValues("regn20", "regnskposter").
- erhverv same mixed letter+number codes as regn50 (no dim.db join for letter codes). Use ColumnValues("regn20", "erhverv") for the 16 options.
- To avoid overcounting: always filter both regnskposter AND storrelse. Forgetting storrelse gives you 5× too many rows (one per size class including TOT).
