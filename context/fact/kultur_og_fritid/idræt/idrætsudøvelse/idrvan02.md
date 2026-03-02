table: fact.idrvan02
description: Voksnes idrætsudøvelse efter køn og alder, deltagelse og tid
measure: indhold (unit Pct.)
columns:
- koal: values [100=I alt, 1=Mand, 2=Kvinde, 1619=16-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7099=70 år og derover]
- deltag1: values [3=Ja deltager, 4=Ja deltager, men ikke for tiden, 5=Nej, deltager ikke]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- deltag1 values are mutually exclusive and sum to ~100% (3=aktiv, 4=aktiv men ikke for tiden, 5=ikke aktiv). Safe to compare individual values.
- koal mixes gender and age in one column: 100=I alt, 1=Mand, 2=Kvinde, then age bands. Do not sum gender + age rows together — overlapping populations.
- Survey data — not annual; data points at 2007, 2011, 2016, 2020, 2024.