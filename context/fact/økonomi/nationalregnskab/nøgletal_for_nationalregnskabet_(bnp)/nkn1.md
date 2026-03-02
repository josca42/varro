table: fact.nkn1
description: Forsyningsbalance, Bruttonationalprodukt (BNP), beskæftigelse mv. efter transaktion, prisenhed, sæsonkorrigering og tid
measure: indhold (unit -)
columns:
- transakt: values [B1GQK=B.1*g Bruttonationalprodukt, BNP, P7K=P.7 Import af varer og tjenester, P71K=P.71 Import af varer, P72K=P.72 Import af tjenester, TFSPR=Forsyning i alt ... P53D=P.53 Anskaffelser minus afhændelser af værdigenstande, TFUPRXP6=Endelig indenlandsk anvendelse, TFUPR=Endelig anvendelse i alt, EMPH_DC=Samlede præsterede timer (mio. timer), EMPM_DC=Samlet antal beskæftigede (1000 personer)]
- prisenhed: values [V_M=Løbende priser, (mia. kr.), L_V=Realvækst i forhold til foregående periode (pct.), V_C=Pr. indbygger, løbende priser, (1000 kr.), LKV_M=2020-priser, kædede værdier, (mia. kr.), L_VB=Bidrag til realvækst i BNP, (procentpoint), LKV_C=Pr. indbygger, 2020-priser, kædede værdier, (1000 kr.)]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1990-01-01 to 2025-04-01

notes:
- TWO measurement selectors — both prisenhed and saeson must be filtered. Every (transakt, prisenhed) pair exists in both saeson='Y' (sæsonkorrigeret) and saeson='N' (ikke sæsonkorrigeret). Omitting either filter silently doubles rows.
- prisenhed values: V_M (løbende priser, mia. kr.), LKV_M (2020-priser kædede, mia. kr.), V_C (pr. indbygger løbende), LKV_C (pr. indbygger 2020-priser), L_V (realvækst %), L_VB (bidrag til vækst pp). Note: uses LKV_* prefix where nan1 uses LAN_* for the same 2020-chained series.
- EMPH_DC and EMPM_DC only support prisenhed IN ('V_M','L_V') — same constraint as nan1.
- Quarterly (tid='YYYY-01-01'=Q1, 'YYYY-04-01'=Q2, 'YYYY-07-01'=Q3, 'YYYY-10-01'=Q4). Starts 1990, whereas nan1 starts 1966.
- Sample query — BNP realvækst kvartal for kvartal, sæsonkorrigeret: SELECT tid, indhold FROM fact.nkn1 WHERE transakt='B1GQK' AND prisenhed='L_V' AND saeson='Y' ORDER BY tid