<fact tables>
<table>
id: forv1
description: Forbrugerforventninger (nettotal) efter indikator og tid
columns: indikator, tid (time), indhold (unit -)
tid range: 1974-10-01 to 2025-10-01
</table>
<table>
id: forv2
description: Planer om større investeringer efter indikator og tid
columns: indikator, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2025-10-01
</table>
</fact tables>

notes:
- forv1 = monthly consumer confidence (13 indicators, back to 1974). forv2 = quarterly investment plans (3 indicators, back to 1990). Neither has geographic or demographic breakdown — both are national aggregates only.
- For the headline confidence index, use forv1 with indikator='F1' (Forbrugertillidsindikatoren).
- For long historical series of sentiment, prefer forv1 (monthly since 1974). For purchase-intent questions (car/housing/renovation), forv2 is the only option.
- All indhold values are net balance scores (can be negative). Never sum across indicators — always filter to one indikator at a time.