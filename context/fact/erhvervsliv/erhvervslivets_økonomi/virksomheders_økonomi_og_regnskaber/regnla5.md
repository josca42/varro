table: fact.regnla5
description: Nøgletal i procent for regnskabsstatistik for primære erhverv efter branche (DB07), regnskabsposter og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- regnskposter: values [XVTP=Værditilvækst (pct.), gennemsnit, XBA=Bruttoavance (pct.) , gennemsnit, XOG=Overskudsgrad (pct.) gennemsnit, XEF=Egenkapitalens forrentning (pct.) gennemsnit, XSO=Soliditetsgrad (pct.) gennemsnit]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/db.md
notes:
- Companion to regnla4: ratio indicators (Pct.) only — 5 regnskposter, all averages. Never sum across regnskposter values. Use to compare profitability/solvency across branches.
- branche07 same leading-zero mismatch as regnla4: join with LTRIM(f.branche07, '0') = d.kode::text. "A" and "01000" are aggregates not in dim.db.
- Use regnla4 for absolute figures (mio. kr.), regnla5 for ratios (%). Both cover 2008-2023.
