table: fact.nak1
description: Nøgletal for akvakultur efter anlægstype, regnskabsposter og tid
measure: indhold (unit -)
columns:
- anlaeg: values [0=Alle anlæg, 6=Traditionelle dambrug, 11=Anlæg med lav recirkulation , 12=Anlæg med middelhøj recirkulation, 13=Anlæg med høj recirkulation , 25=Havbrug, 36=Muslinge- og østersanlæg]
- regnskposter: values [H115=H.3 Ejeraflønning (beregnet), 1000 kr., P200=P.2 Overskudsgrad, pct., P300=P.3 Afkastningsgrad, pct., P400=P.4 Soliditetsgrad, pct.]
- tid: date range 2017-01-01 to 2023-01-01

notes:
- regnskposter contains exactly 4 independent key figures with mixed units — do not sum across them: H115 (owner compensation, 1000 kr), P200 (profit margin, pct), P300 (return on assets, pct), P400 (equity ratio, pct). Always filter to the specific metric you need.
- No measurement selector column — unlike akregn1, there is no enhed here. Each anlaeg×regnskposter×tid combination has exactly one row.
- anlaeg=0 is Alle anlæg. The other 6 values are individual facility types. Do not mix anlaeg=0 with subtypes in an aggregation.
- This table is best for financial health/performance ratios. For absolute financial figures (revenue, costs, assets), use akregn1 instead.