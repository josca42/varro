table: fact.nan1
description: Forsyningsbalance, bruttonationalprodukt (BNP),økonomisk vækst, beskæftigelse mv. efter transaktion, prisenhed og tid
measure: indhold (unit -)
columns:
- transakt: values [B1GQK=B.1*g Bruttonationalprodukt, BNP, P7K=P.7 Import af varer og tjenester, P71K=P.71 Import af varer, P72K=P.72 Import af tjenester, TFSPR=Forsyning i alt ... P53D=P.53 Anskaffelser minus afhændelser af værdigenstande, TFUPRXP6=Endelig indenlandsk anvendelse, TFUPR=Endelig anvendelse i alt, EMPH_DC=Samlede præsterede timer (mio. timer), EMPM_DC=Samlet antal beskæftigede (1000 personer)]
- prisenhed: values [V_M=Løbende priser, (mia. kr.), LAN_M=2020-priser, kædede værdier, (mia. kr.), L_V=Realvækst i forhold til foregående periode (pct.), V_C=Pr. indbygger, løbende priser, (1000 kr.), L_VB=Bidrag til realvækst i BNP, (procentpoint), LAN_C=Pr. indbygger, 2020-priser, kædede værdier, (1000 kr.)]
- tid: date range 1966-01-01 to 2024-01-01

notes:
- prisenhed is a MEASUREMENT SELECTOR — every transakt appears 2–6 times with different prisenhed values. Always filter to exactly one: V_M (løbende priser, mia. kr.), LAN_M (2020-priser kædede værdier, mia. kr.), V_C (løbende priser pr. indbygger, 1000 kr.), LAN_C (2020-priser pr. indbygger), L_V (realvækst %, foregående periode), L_VB (bidrag til BNP-vækst, procentpoint). Failing to filter silently multiplies rows.
- EMPH_DC (præsterede timer) and EMPM_DC (antal beskæftigede) only support prisenhed IN ('V_M','L_V') — no chained price or per-capita variants exist for these.
- L_V and L_VB are percentage/rate measures — never sum across transakt values. V_M and LAN_M are in mia. kr. and can be summed where economically meaningful.
- 31 distinct transakt codes covering supply (import), use (exports, consumption, investment), and BNP. Use ColumnValues("nan1", "transakt") to browse all codes with labels.
- Sample query — BNP i løbende priser over tid: SELECT tid, indhold FROM fact.nan1 WHERE transakt='B1GQK' AND prisenhed='V_M' ORDER BY tid