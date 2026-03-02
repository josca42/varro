table: fact.silc1b
description: Boligbyrde: Andel personer efter køn, alder, i hvor høj grad husstanden synes boligudgiften er en byrde og tid
measure: indhold (unit Pct.)
columns:
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 0019=Under 20 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7099=70 år og derover]
- svaerhed1: values [100=I alt, 115=En tung byrde, 120=Noget af en byrde, 125=Ikke noget problem]
- tid: date range 2004-01-01 to 2024-01-01
notes:
- Longest series for housing cost burden (2004–2024). Values are percentages only (Pct.) — no enhed selector.
- svaerhed1=100 is a dummy total row where indhold=100 always. Use svaerhed1 IN (115, 120, 125) for the actual distribution. Values 115+120+125 sum to 100%. To identify households under financial strain from housing: svaerhed1 IN (115, 120) — "some burden or heavy burden".
- koen: TOT, M=Mænd, K=Kvinder. alder: TOT + 7 age bands (0019 to 7099). For the overall national figure: WHERE koen='TOT' AND alder='TOT'.
- To avoid overcounting when aggregating, filter koen='TOT' OR alder='TOT' (not both non-total at once unless the table actually crosses them, which it does).
