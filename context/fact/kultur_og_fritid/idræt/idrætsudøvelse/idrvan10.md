table: fact.idrvan10
description: Børns idrætsudøvelse efter alder og køn, deltagelse og tid
measure: indhold (unit Pct.)
columns:
- alderk: values [100=I alt, D=Drenge, P=Piger, 0709=7-9 år, 1012=10-12 år, 1315=13-15 år]
- deltag1: values [3=Ja deltager, 4=Ja deltager, men ikke for tiden, 5=Nej, deltager ikke]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- deltag1 values are mutually exclusive and sum to ~100%.
- alderk mixes gender and age: 100=I alt, D=Drenge, P=Piger, then age bands. Don't sum gender + age rows.
- Survey data — not annual; data points at 2007, 2011, 2016, 2020, 2024.