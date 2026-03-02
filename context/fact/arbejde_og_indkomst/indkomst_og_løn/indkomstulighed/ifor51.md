table: fact.ifor51
description: Relativ fattigdom efter alder, enhed, varighed og tid
measure: indhold (unit -)
columns:
- alder: values [TOT=Alder i alt, 0017=Under 18 år, 0004=0-4 år, 0509=5-9 år, 1014=10-14 år, 1519=15-19 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6064=60-64 år, 6569=65-69 år, 7074=70-74 år, 7579=75-79 år, 8084=80-84 år, 8599=85 år og derover]
- enhed: values [ANT=Personer (antal), AND=Pct. af befolkningen]
- kmdr: values [1AAR=1 år, 2AAR=2 år i træk, 3AAR=3 år i træk, 4AAR=4 år i træk]
- tid: date range 2015-01-01 to 2023-01-01
notes:
- enhed is a measurement selector: ANT=antal (count of persons) and AND=pct. af befolkningen. Every row exists in both units. Always filter to one: WHERE enhed = 'ANT' or WHERE enhed = 'AND'. Forgetting this doubles all values.
- kmdr (varighed) indicates consecutive years in poverty: 1AAR=at least 1 year, 2AAR=at least 2 consecutive years, 3AAR=3 consecutive years, 4AAR=4 consecutive years. These are nested — everyone in 4AAR is also in 3AAR, 2AAR, and 1AAR. Do NOT sum across kmdr values. Filter to one duration depending on the question.
- alder includes TOT (all ages), a broad 0017 band (under 18), and 19 individual 5-year age bands (0004 through 8599). TOT is the aggregate of all individual bands. Do not mix TOT with individual bands. Note the coding: 0017, 0004, 0509, etc.
- No municipality breakdown — national-level only. For municipality breakdown see laby07 (kommunegrupper).
- This is the only table with multi-year poverty duration (kmdr). Use it when the question is about persistent poverty.
