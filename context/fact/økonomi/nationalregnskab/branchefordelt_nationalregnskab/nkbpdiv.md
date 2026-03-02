table: fact.nkbpdiv
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
- Like nabpdiv but quarterly. Contains extra branche codes TXB and TXMEMO (adjustment items, not in dim). For standard sector analysis, exclude these and VMEMO.
- Three selector columns: `transakt`, `prisenhed` (LKV not LAN for volume), `saeson` (N/Y). All must be filtered.
- tid is quarterly. Data runs 1990–present.