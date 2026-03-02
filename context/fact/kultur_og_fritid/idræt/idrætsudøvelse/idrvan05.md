table: fact.idrvan05
description: Voksnes idrætsudøvelse efter køn og alder, organisering og tid
measure: indhold (unit Pct.)
columns:
- koal: values [100=I alt, 1=Mand, 2=Kvinde, 1619=16-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7099=70 år og derover]
- organ1: values [FOR=Forening, PRI=Privat, FIR=Arbejde/uddannelse, SEL=Selvorganiseret, AFT=Aftenskole, FAE=Andet træningsfællesskab (internet mv.) (2020), ANS=Anden sammenhæng]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- organ1 values are NOT mutually exclusive — one person can exercise in multiple contexts. Values sum to ~163% for koal=100. Never sum across organ1; each row is "X% of adults exercise in this context".
- FAE (Andet træningsfællesskab internet mv.) was added in 2020 — not available in earlier survey rounds.
- koal mixes gender and age: 100=I alt, 1=Mand, 2=Kvinde, then age bands. Don't sum gender + age rows.
- Survey data — not annual; data points at 2007, 2011, 2016, 2020, 2024.