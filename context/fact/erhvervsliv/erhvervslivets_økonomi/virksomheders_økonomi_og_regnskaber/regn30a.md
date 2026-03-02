table: fact.regn30a
description: Nøgletal i procent for regnskabsstatistik for private byerhverv efter branche, regnskabsposter, ejerform og tid
measure: indhold (unit Pct.)
columns:
- erhverv: join dim.db on erhverv=kode::text [approx]; levels [2]
- regnskposter: values [XVTP=Værditilvækst (pct.), gennemsnit, XBA=Bruttoavance (pct.) , gennemsnit, XOG=Overskudsgrad (pct.) gennemsnit, XEF=Egenkapitalens forrentning (pct.) gennemsnit, XVTM=Værditilvækst (pct.), median, XBAM=Bruttoavance (pct.), median, XSO=Soliditetsgrad (pct.) gennemsnit, XOGM=Overskudsgrad (pct.)  median, XEFM=Egenkapitalens forrentning (pct.)  median, XSOM=Soliditetsgrad (pct.)  median]
- ejerform: values [TOT=I ALT, A=Aktie- og anpartsselskab mv., B=Enkeltmands- firma og I/S]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- Companion to regn30: ratio indicators (Pct.) with ejerform breakdown. 10 regnskposter (gennemsnit + median for Værditilvækst, Bruttoavance, Overskudsgrad, Egenkapitalens forrentning, Soliditetsgrad). Never sum across regnskposter.
- Note: compared to regn50a and regn20a, regn30a does NOT split metrics by S/P suffix — the same XOG/XEF/XSO codes apply to all firms. To compare A/S vs enkeltmandsfirma, filter ejerform instead.
- Always filter both regnskposter and ejerform. Use ColumnValues("regn30a", "erhverv").
