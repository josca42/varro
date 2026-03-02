table: fact.pskat2
description: Indkomster og fradrag ved slutligningen efter type og tid
measure: indhold (unit Mio. kr.)
columns:
- type: values [1=1. Personlig indkomst, 11=1.1 A-indkomst, 12=1.2 Overskud af egen virksomhed, 13=1.3 Udenlandsk indkomst, 14=1.4 Indkomst som medarbejdende ægtefælle ... 5=5. Skattepligtig indkomst (1+2-3+4), 6=6. Aktieindkomst (ud over bundgrænsebeløb), 7=7. Beregningsfradrag, 8=8. Udskrivningsgrundlag (5-7), 9=9. Antal skattepligtige personer (1 000 personer)]
- tid: date range 1994-01-01 to 2023-01-01

notes:
- type is a two-level hierarchy: single-digit codes (1–4) are top-level totals; two-digit codes (11–18, 21–27, 31–39) are sub-items. type=1 (Personlig indkomst) = sum of 11+12+...+18 (verified). Filter to one level to avoid double-counting.
- Types 5–8 are derived aggregates (skattepligtig indkomst, aktieindkomst, beregningsfradrag, udskrivningsgrundlag) — not simple sums of the other types. Type 9 is in 1.000 persons, not Mio. kr.
- Use ColumnValues("pskat2","type") to browse all 33 type codes with labels.
