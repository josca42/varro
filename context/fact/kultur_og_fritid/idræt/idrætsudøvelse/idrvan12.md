table: fact.idrvan12
description: Idrætsaktive børns idrætsudøvelse efter alder og køn, tidsforbrug og tid
measure: indhold (unit Pct.)
columns:
- alderk: values [100=I alt, D=Drenge, P=Piger, 0709=7-9 år, 1012=10-12 år, 1315=13-15 år]
- tidbrug: values [1111=Under 1 time, 2222=1 time - 1 time og 59 minutter, 3333=2 timer - 3 timer 59 minutes, 4444=4 timer - 5 timer og 59 minutter, 6666=6 timer og derover]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- Base population is sports-ACTIVE children only. tidbrug values together sum to ~100% — they are a time distribution.
- tidbrug has no total/aggregate bucket — all 5 values partition active children by weekly time spent.
- alderk mixes gender and age: 100=I alt, D=Drenge, P=Piger, then age bands. Don't sum gender + age rows.
- Survey data — not annual; data points at 2007, 2011, 2016, 2020, 2024.