table: fact.vnan1
description: Versionstabel NAN1 - Forsyningsbalance (år) efter version, transaktion, prisenhed og tid
measure: indhold (unit -)
columns:
- version: values [V2024_JUN=Juniversion 2021-2024, V2024_MAR=Martsversion 2024, V2024_FEB=Februarversion 2024, V2023_JUN=Juniversion 1966-2023 (Hovedrevision 2024), V2023_MAR=Martsversion 2023 ... V2014_JUN=Juniversion 2014, V2014_MAR=Martsversion 2014, V2014_FEB=Februarversion 2014, V2013_NOV=Novemberversion 2011-2013, V2013_SEP=Septemberversion 1966-2013 (Hovedrevision 2014)]
- transakt: values [B1GQK=B.1*g Bruttonationalprodukt, BNP, P7K=P.7 Import af varer og tjenester, P71K=P.71 Import af varer, P72K=P.72 Import af tjenester, TFSPR=Forsyning i alt ... P53D=P.53 Anskaffelser minus afhændelser af værdigenstande, TFUPRXP6=Endelig indenlandsk anvendelse, TFUPR=Endelig anvendelse i alt, EMPH_DC=Samlede præsterede timer (mio. timer), EMPM_DC=Samlet antal beskæftigede (1000 personer)]
- prisenhed: values [V_M=Løbende priser, (mia. kr.), LAN_M=2020-priser, kædede værdier, (mia. kr.), L_V=Realvækst i forhold til foregående periode (pct.), V_C=Pr. indbygger, løbende priser, (1000 kr.), LPR_C=Pr. indbygger, 2010-priser, kædede værdier, (1000 kr.), LPR_M=2010-priser, kædede værdier, (mia. kr.), L_VB=Bidrag til realvækst i BNP, (procentpoint), LAN_C=Pr. indbygger, 2020-priser, kædede værdier, (1000 kr.)]
- tid: date range 1966-01-01 to 2024-01-01

notes:
- VERSION HISTORY TABLE — same data as nan1 but with an additional version dimension tracking each published vintage. 42 versions from 2013 to 2024. Must filter to a single version or rows multiply 42x.
- Use latest version for current data (V2024_JUN = Juniversion 2021-2024, covering full 1966-2024 range). For revision analysis, compare two versions with a self-join.
- prisenhed here includes legacy codes LPR_M and LPR_C (2010-priser kædede værdier) not present in nan1 — these appear in older versions pre-dating the base year shift to 2020. When filtering for current analysis, use prisenhed IN ('V_M','LAN_M','V_C','LAN_C','L_V','L_VB').
- Same transakt codes and prisenhed measurement-selector caution as nan1.
- Sample query — BNP revision: compare two versions: SELECT a.tid, a.indhold AS v2023, b.indhold AS v2024 FROM fact.vnan1 a JOIN fact.vnan1 b USING (transakt, prisenhed, tid) WHERE a.version='V2023_JUN' AND b.version='V2024_JUN' AND a.transakt='B1GQK' AND a.prisenhed='V_M' ORDER BY a.tid