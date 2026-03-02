table: fact.vnkn1
description: Versionstabel NKN1 - Forsyningsbalance (kvartaler) efter version, transaktion, prisenhed, sæsonkorrigering og tid
measure: indhold (unit -)
columns:
- version: values [V2025Q2R=2025K2, Revideret, V2025Q2F=2025K2, V2025Q1R=2025K1, Revideret, V2025Q1F=2025K1, V2024Q4R=2024K4, Revideret ... V2020Q3F=2020K3, V2020Q2R=2020K2 Revideret, V2020Q2F=2020K2, V2020Q1R=2020K1 Revideret, V2020Q1F=2020K1]
- transakt: values [B1GQK=B.1*g Bruttonationalprodukt, BNP, P7K=P.7 Import af varer og tjenester, P71K=P.71 Import af varer, P72K=P.72 Import af tjenester, TFSPR=Forsyning i alt ... P53D=P.53 Anskaffelser minus afhændelser af værdigenstande, TFUPRXP6=Endelig indenlandsk anvendelse, TFUPR=Endelig anvendelse i alt, EMPH_DC=Samlede præsterede timer (mio. timer), EMPM_DC=Samlet antal beskæftigede (1000 personer)]
- prisenhed: values [V_M=Løbende priser, (mia. kr.), L_V=Realvækst i forhold til foregående periode (pct.), V_C=Pr. indbygger, løbende priser, (1000 kr.), LPR_C=Pr. indbygger, 2010-priser, kædede værdier, (1000 kr.), LKV_M=2020-priser, kædede værdier, (mia. kr.), LPR_M=2010-priser, kædede værdier, (mia. kr.), L_VB=Bidrag til realvækst i BNP, (procentpoint), LKV_C=Pr. indbygger, 2020-priser, kædede værdier, (1000 kr.)]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1990-01-01 to 2025-04-01

notes:
- VERSION HISTORY TABLE — quarterly counterpart of vnan1. 44 versions tracking each publication of nkn1. Must filter to a single version.
- Version naming: V2025Q2F = 2025K2 first estimate (F=first), V2025Q2R = 2025K2 revised (R=revideret). F versions are the flash estimates; R versions are the subsequent revisions.
- prisenhed includes legacy LPR_M and LPR_C (2010-priser) from older versions — same caution as vnan1.
- Same three selectors as nkn1: prisenhed, saeson, and now version — all three must be filtered to avoid multiplicative overcounting.
- Sample query — compare first vs revised BNP for a quarter: SELECT a.tid, a.indhold AS first_est, b.indhold AS revised FROM fact.vnkn1 a JOIN fact.vnkn1 b USING (transakt, prisenhed, saeson, tid) WHERE a.version='V2024Q4F' AND b.version='V2024Q4R' AND a.transakt='B1GQK' AND a.prisenhed='V_M' AND a.saeson='N' ORDER BY a.tid