table: fact.ff1
description: Ferierejser til udlandet efter destination, varighed og tid
measure: indhold (unit Pct.)
columns:
- destina: values [BELU=Belgien, BUL=Bulgarien, CYP=Cypern, EST=Estland, FIN=Finland ... THA=Thailand, SØA=Asien uden Kina, Japan, Sydkorea, Indien og Thailand, AUS=Australien, OCEX=Oceanien uden Australien, ANDRE=Uoplyst land]
- kmdr: values [1=Mindre end fire overnatninger, 2=Mindst fire overnatninger]
- tid: date range 2001-01-01 to 2024-01-01

notes:
- indhold is percentage share of holiday trips abroad by destination. Values sum to ~100 across destina for a fixed kmdr+tid. Never sum indhold across destinations — they're already shares.
- kmdr splits trips into two non-overlapping groups (short <4 nights vs long ≥4 nights). Always filter to one kmdr value, or aggregate separately and present both, to avoid double-counting.
- No aggregate destina code (no IALT/TOT). The 50 codes are all individual countries/regions. Coverage expands over time: only 10-17 destinations in 2001-2006, growing to 45-47 by 2023-2024. Comparing a specific country's share across years is valid, but the "long tail" of small destinations is only captured in recent years.
- To get shares for a single year: SELECT destina, indhold FROM fact.ff1 WHERE kmdr=2 AND tid='2024-01-01' ORDER BY indhold DESC.
- This table covers udlandet only — for domestic holiday trips use ff2 (destina='DAN').