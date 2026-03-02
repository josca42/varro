table: fact.regn30
description: Regnskabsstatistik for private byerhverv i mio. kr. efter branche, regnskabsposter, ejerform og tid
measure: indhold (unit -)
columns:
- erhverv: join dim.db on erhverv=kode::text [approx]; levels [2]
- regnskposter: values [ANTFIR=Firmaer (antal), XOM=Omsætning (mio. kr.), BESK=Antal beskæftigede (i årsværk), AARSV=Heraf: ansatte (i årsværk), ADR=Andre driftsindtægter (mio. kr.) ... XINT=INVESTERINGER, NETTO (mio. kr.), XOB=Driftsindtægter pr. beskæftiget (1000 kr.), gennemsnit, XLA=Løn pr. ansat (1000 kr.), gennemsnit, XOBM=Driftsindtægter pr. beskæftiget (1000 kr.), median, XLAM=Løn pr. ansat (1000 kr.), median]
- ejerform: values [TOT=I ALT, A=Aktie- og anpartsselskab mv., B=Enkeltmands- firma og I/S]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- Adds ejerform dimension to regn50's structure: TOT=I alt, A=Aktie- og anpartsselskab mv., B=Enkeltmandsfirma og I/S. Filter WHERE ejerform='TOT' for totals; filter A or B to compare legal forms.
- regnskposter is a measure-selector: MUST filter to one value. Use ColumnValues("regn30", "regnskposter").
- erhverv same mixed letter+number codes as regn50. Use ColumnValues("regn30", "erhverv").
- To avoid overcounting: always filter both regnskposter AND ejerform. Forgetting ejerform gives you 3× too many rows.
