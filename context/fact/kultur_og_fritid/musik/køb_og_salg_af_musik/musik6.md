table: fact.musik6
description: Autorer (komponister og sangskrivere) med nye registrerede musikværker efter køn, alder og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 9920=Under 20 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7099=70 år og derover]
- tid: date range 2021-01-01 to 2024-01-01

notes:
- Both kon and alder have total rows (kon='TOT', alder='TOT'). Summing all values of either column will double-count — always filter to specific values or to the total, not both.
- For overall count of authors: filter kon='TOT' AND alder='TOT'.
- For breakdown by gender only: filter alder='TOT' and group by kon IN ('1','2').
- For breakdown by age only: filter kon='TOT' and group by alder (excluding 'TOT').
- Short time series (2021–2024 only) — not suitable for long-term trend analysis.