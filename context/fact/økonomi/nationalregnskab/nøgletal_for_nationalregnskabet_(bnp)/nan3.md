table: fact.nan3
description: Forbrug, disponibel indkomst og opsparing for husholdninger og NPISH efter transaktion, prisenhed og tid
measure: indhold (unit -)
columns:
- transakt: values [P31=P.31 Udgifter til individuelt forbrug, P41=P.41 Faktisk individuelt forbrug, P3=P.3 Udgifter til forbrug (hele økonomien), B6G=B.6g Disponibel bruttoindkomst, B7G=B.7g Korrigeret disponibel bruttoindkomst, D8K=D.8 Korrektion for ændringer i pensionsrettigheder, B8G=B.8g Bruttoopsparing, P51C=P.51c Forbrug af fast realkapital, B6N=B.6n Disponibel nettoindkomst, B7N=B.7n Korrigeret disponibel nettoindkomst, B8N=B.8n Nettoopsparing]
- prisenhed: values [V_M=Løbende priser, (mia. kr.), RAN_M=2020-priser, kædede værdier, (mia. kr.), V_C=Pr. indbygger, løbende priser, (1000 kr.), RAN_C=Pr. indbygger, 2020-priser, kædede værdier (1000 kr.)]
- tid: date range 1995-01-01 to 2024-01-01

notes:
- prisenhed is a MEASUREMENT SELECTOR — always filter to one: V_M (løbende priser, mia. kr.), RAN_M (2020-priser, mia. kr.), V_C (løbende priser pr. indbygger, 1000 kr.), RAN_C (2020-priser pr. indbygger). No growth rate variants.
- B8N (nettoopsparing) only appears with prisenhed IN ('V_C','V_M') — no real price version.
- 11 transakt codes for husholdninger og NPISH only (not the whole economy except P3). Covers consumption (P31, P41), income (B6G, B7G), savings (B8G, B8N), and pension correction (D8K).
- Shorter series than nan1/nan2 — starts 1995. For pre-1995 household data, check samlet nationalregnskab tables.
- Sample query — husholdningernes disponible bruttoindkomst: SELECT tid, indhold FROM fact.nan3 WHERE transakt='B6G' AND prisenhed='V_M' ORDER BY tid