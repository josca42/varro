table: fact.nkn3
description: Forbrug, disponibel indkomst og opsparing for husholdninger og NPISH, sæsonkorrigeret efter transaktion, prisenhed og tid
measure: indhold (unit -)
columns:
- transakt: values [P31=P.31 Udgifter til individuelt forbrug, P41=P.41 Faktisk individuelt forbrug, P3=P.3 Udgifter til forbrug (hele økonomien), B6G=B.6g Disponibel bruttoindkomst, B7G=B.7g Korrigeret disponibel bruttoindkomst, D8K=D.8 Korrektion for ændringer i pensionsrettigheder, B8G=B.8g Bruttoopsparing, P51C=P.51c Forbrug af fast realkapital, B6N=B.6n Disponibel nettoindkomst, B7N=B.7n Korrigeret disponibel nettoindkomst, B8N=B.8n Nettoopsparing]
- prisenhed: values [V_M=Løbende priser, (mia. kr.), RKV_M=2020-priser, kædede værdier, (mia. kr.), V_C=Pr. indbygger, løbende priser, (1000 kr.), RKV_C=Pr. indbygger, 2020-priser, kædede værdier (1000 kr.)]
- tid: date range 1999-01-01 to 2025-04-01

notes:
- prisenhed is a MEASUREMENT SELECTOR — always filter to one: V_M (løbende priser, mia. kr.), RKV_M (2020-priser kædede, mia. kr.), V_C (pr. indbygger løbende), RKV_C (pr. indbygger real). No growth rate variants.
- No saeson column — unlike nkn1/nkn2, this table contains only seasonally adjusted data by definition. Do not filter on saeson.
- Quarterly from 1999 (later start than nkn1/nkn2 which begin 1990). Shorter series than nan3 annual which starts 1995.
- Same 11 transakt codes as nan3 (husholdninger og NPISH: consumption, income, savings). Uses RKV_* prefix for real values (vs RAN_* in nan3).
- Sample query — husholdningernes bruttoopsparing, sæsonkorrigeret kvartal: SELECT tid, indhold FROM fact.nkn3 WHERE transakt='B8G' AND prisenhed='V_M' ORDER BY tid