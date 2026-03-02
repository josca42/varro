table: fact.nkbp10
description: 1-2.1.1 Produktion, BVT og indkomstdannelse (10a3-gruppering) efter transaktion, branche, prisenhed, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P1K=P.1 Produktion, P2D=P.2 Forbrug i produktionen, B1GD=B.1g Bruttoværditilvækst, BVT, D29X39D=D.29-D.39 Andre produktionskatter minus andre produktionssubsidier, B1GFD=B.1GF Bruttofaktorindkomst, BFI, D1D=D.1 Aflønning af ansatte, B2A3GD=B.2g+B.3g Bruttooverskud af produktion og blandet indkomst]
- branche: join dim.nr_branche on branche=kode [approx]
- prisenhed: values [V=Løbende priser, LKV=2020-priser, kædede værdier]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1990-01-01 to 2025-04-01
dim docs: /dim/nr_branche.md

notes:
- branche join: same V-prefix/underscore pattern as nabp10 — `JOIN dim.nr_branche d ON d.kode = replace(substring(f.branche from 2), '_', '-') AND d.niveau = 1`.
- Three selector columns must all be filtered: `transakt` (accounting aggregates, never sum), `prisenhed` (V or LKV — note LKV not LAN as in annual nabp10), and `saeson` (N/Y).
- prisenhed code for volume is LKV in this quarterly table, vs LAN in the annual nabp10.
- nkbp10 has fewer transakt types than nabp10 (no P51CD, B2A3ND, B1N2D).
- tid is quarterly (2024-01-01 = Q1, 2024-04-01 = Q2). Data runs 1990–present.
- For annual data, use nabp10. nkbp10 is the quarterly/seasonal companion.