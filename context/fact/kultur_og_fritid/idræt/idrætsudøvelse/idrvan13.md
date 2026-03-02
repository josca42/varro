table: fact.idrvan13
description: Børns idrætsudøvelse efter alder og køn, organisering og tid
measure: indhold (unit Pct.)
columns:
- alderk: values [100=I alt, D=Drenge, P=Piger, 0709=7-9 år, 1012=10-12 år, 1315=13-15 år]
- organ1: values [FOR=Forening, PRI=Privat, SFO=SFO/FRITIDSKLUB, EGN=På egen hånd, FAE=Andet træningsfællesskab (internet mv.) (2020), ANS=Anden sammenhæng]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- organ1 values are NOT mutually exclusive — children exercise in multiple contexts. Values sum to ~205% for alderk=100. Each row = "X% of children exercise in this context".
- Children's organ1 includes SFO/Fritidsklub instead of adults' Aftenskole. FAE (internet-fællesskab) added in 2020.
- alderk mixes gender and age: 100=I alt, D=Drenge, P=Piger, then age bands. Don't sum gender + age rows.
- Survey data — not annual; data points at 2007, 2011, 2016, 2020, 2024.