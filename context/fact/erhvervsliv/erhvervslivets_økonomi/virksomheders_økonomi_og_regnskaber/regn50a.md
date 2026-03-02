table: fact.regn50a
description: Nøgletal i procent for regnskabsstatistik for private byerhverv efter branche, regnskabsposter og tid
measure: indhold (unit Pct.)
columns:
- erhverv: join dim.db on erhverv=kode::text [approx]; levels [2]
- regnskposter: values [XVTP=Værditilvækst (pct.), gennemsnit, XBA=Bruttoavance (pct.) , gennemsnit, XOGS=Overskudsgrad (pct.), gennemsnit A/S, Aps, Amba, mv., XEFS=Egenkapitalens forrentning (pct.), gennemsnit A/S, Aps, Amba, mv., XSO=Soliditetsgrad (pct.) gennemsnit]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- Companion to regn50: ratio indicators (Pct.) only — 5 regnskposter, all averages (A/S+ApS focused). Never sum across regnskposter.
- erhverv same mixed-code structure as regn50 (letters + 45/46/47/95 + TOTR). No dim.db join for letter codes. Use ColumnValues("regn50a", "erhverv").
- XOG/XEF/XSO use suffix "S" here (vs regn30a which has both S and P variants for A/S vs enkeltmandsfirma). Use regn30a if you need to compare by legal form.
