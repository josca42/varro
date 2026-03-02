table: fact.regn10a
description: Nøgletal i procent for regnskabsstatistik for private byerhverv efter branche, regnskabsposter og tid
measure: indhold (unit Pct.)
columns:
- erhverv: join dim.nr_branche on erhverv::text=kode [approx]; levels [4]
- regnskposter: values [XVTP=Værditilvækst (pct.), gennemsnit, XBA=Bruttoavance (pct.) , gennemsnit, XOGS=Overskudsgrad (pct.), gennemsnit A/S, Aps, Amba, mv., XEFS=Egenkapitalens forrentning (pct.), gennemsnit A/S, Aps, Amba, mv., XSOS=Soliditetsgrad (pct.), gennemsnit A/S, Aps, Amba, mv., XOGP=Overskudsgrad (pct.), gennemsnit Enkeltmandsfirmaer og I/S, XEFP=Egenkapitalens forrentning (pct.), gennemsnit Enkeltmandsfirmaer og I/S, XSOP=Soliditetsgrad (pct.), gennemsnit Enkeltmandsfirmaer og I/S, XVTM=Værditilvækst (pct.), median, XBAM=Bruttoavance (pct.), median, XOGMS=Overskudsgrad (pct.), median A/S, Aps, Amba, mv., XEFMS=Egenkapitalens forrentning (pct.), median A/S, Aps, Amba, mv., XSOMS=Soliditetsgrad (pct.), median A/S, Aps, Amba, mv., XOGMP=Overskudsgrad (pct.), median Enkeltmandsfirmaer og I/S, XEFMP=Egenkapitalens forrentning (pct.), median Enkeltmandsfirmaer og I/S, XSOMP=Soliditetsgrad (pct.), median Enkeltmandsfirmaer og I/S]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md
notes:
- Companion to regn10: ratio indicators (Pct.) only — 15 regnskposter. Unlike regn50a (which only has averages for A/S), regn10a provides both gennemsnit and median, and splits metrics by legal form (S-suffix=A/S+ApS, P-suffix=Enkeltmandsfirmaer+I/S). Never sum across regnskposter.
- erhverv same 101-code structure as regn10. Use ColumnValues("regn10a", "erhverv"). No dim.nr_branche join.
- Use regn10a when you need median ratios or want to compare corporate vs. personal-firm performance at fine branch level. Use regn50a for broad sector overview.
