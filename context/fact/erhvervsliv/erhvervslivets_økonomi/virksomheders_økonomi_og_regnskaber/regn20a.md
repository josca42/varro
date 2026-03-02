table: fact.regn20a
description: Nøgletal i procent for regnskabsstatistik for private byerhverv efter branche, regnskabsposter, størrelse og tid
measure: indhold (unit Pct.)
columns:
- erhverv: join dim.db on erhverv=kode::text [approx]; levels [2]
- regnskposter: values [XVTP=Værditilvækst (pct.), gennemsnit, XBA=Bruttoavance (pct.) , gennemsnit, XOGS=Overskudsgrad (pct.), gennemsnit A/S, Aps, Amba, mv., XEFS=Egenkapitalens forrentning (pct.), gennemsnit A/S, Aps, Amba, mv., XSOS=Soliditetsgrad (pct.), gennemsnit A/S, Aps, Amba, mv., XOGP=Overskudsgrad (pct.), gennemsnit Enkeltmandsfirmaer og I/S, XEFP=Egenkapitalens forrentning (pct.), gennemsnit Enkeltmandsfirmaer og I/S, XSOP=Soliditetsgrad (pct.), gennemsnit Enkeltmandsfirmaer og I/S, XVTM=Værditilvækst (pct.), median, XBAM=Bruttoavance (pct.), median, XOGMS=Overskudsgrad (pct.), median A/S, Aps, Amba, mv., XEFMS=Egenkapitalens forrentning (pct.), median A/S, Aps, Amba, mv., XSOMS=Soliditetsgrad (pct.), median A/S, Aps, Amba, mv., XOGMP=Overskudsgrad (pct.), median Enkeltmandsfirmaer og I/S, XEFMP=Egenkapitalens forrentning (pct.), median Enkeltmandsfirmaer og I/S, XSOMP=Soliditetsgrad (pct.), median Enkeltmandsfirmaer og I/S]
- storrelse: values [TOT=I alt, 0-9=0-9 ansatte, 10-19=10-19 ansatte, 20-99=20-99 ansatte, 100OV=100 ansatte og derover]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- Companion to regn20: ratio indicators (Pct.) with size breakdown. 15 regnskposter (same as regn10a: gennemsnit+median, S and P suffixes by legal form). Never sum across regnskposter.
- Always filter both regnskposter and storrelse. Use ColumnValues("regn20a", "regnskposter") and ColumnValues("regn20a", "erhverv").
- Use when you need to compare profitability by company size AND legal form simultaneously.
