table: fact.vogrg
description: Værdien af olie og naturgas efter balanceposter og tid
measure: indhold (unit -)
columns:
- balpost: values [90=Primobeholdning (1) mio kr., 92=Indvinding (2) mio kr., 94=Nye fund og anden økonomisk opståen (+)/forsvinden (-) (3) mio. kr., 96=Omvurdering (4) mio. kr., 98=Ultimobeholdning (5)=(1)-(2)+(3)+(4) mio. kr., 99=Værdien af ultimobeholdningen i pct. af BNP]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- Never sum across all balpost codes: 90/92/94/96/98 are mio. kr., but 99 is a percentage (pct. af BNP) — a different unit. These are balance sheet rows, not additive categories.
- The accounting identity is: 98 = 90 - 92 + 94 + 96 (ultimo = primo - extraction + new finds ± revaluation). Summing all rows gives nonsense.
- balpost 99 (pct. af BNP) only has non-zero values for 1990–approx 2013; later years are zero as Danish oil/gas reserves were depleted. For long-run trend use 90 or 98.
- Recent years (approx 2015+) show all values at zero — Danish oil/gas reserves are essentially exhausted. Historical peak is in the 1990s–2000s.