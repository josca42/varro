table: fact.idrvan04
description: Idrætsaktive voksnes idrætsudøvelse efter køn og alder, tidsforbrug og tid
measure: indhold (unit Pct.)
columns:
- koal: values [100=I alt, 1=Mand, 2=Kvinde, 1619=16-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7099=70 år og derover]
- tidbrug: values [1111=Under 1 time, 2222=1 time - 1 time og 59 minutter, 3333=2 timer - 3 timer 59 minutes, 4444=4 timer - 5 timer og 59 minutter, 6666=6 timer og derover]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- Base population is sports-ACTIVE adults only (not all adults). Percentages show the distribution of time spent — tidbrug values together sum to ~100% for a given koal/tid.
- tidbrug has no total/aggregate value — it's a distribution of time-use buckets among active adults.
- koal mixes gender and age: 100=I alt, 1=Mand, 2=Kvinde, then age bands. Don't sum gender + age rows.
- Survey data — not annual; data points at 2007, 2011, 2016, 2020, 2024.