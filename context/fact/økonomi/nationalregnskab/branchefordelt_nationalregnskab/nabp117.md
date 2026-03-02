table: fact.nabp117
description: 1-2.1.1 Produktion, BVT og indkomstdannelse (117-gruppering) efter transaktion, branche, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P1K=P.1 Produktion, P2D=P.2 Forbrug i produktionen, B1GD=B.1g Bruttoværditilvækst, BVT, D29X39D=D.29-D.39 Andre produktionskatter minus andre produktionssubsidier, B1GFD=B.1GF Bruttofaktorindkomst, BFI, D1D=D.1 Aflønning af ansatte, B2A3GD=B.2g+B.3g Bruttooverskud af produktion og blandet indkomst]
- branche: join dim.nr_branche on branche=kode [approx]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1966-01-01 to 2022-01-01
dim docs: /dim/nr_branche.md

notes:
- branche join: `JOIN dim.nr_branche d ON d.kode = substring(f.branche from 2) AND d.niveau = 5`. Strip V prefix — niveau-5 codes are 6-digit numeric. 117 sectors + V + VMEMO.
- transakt contains accounting aggregates — never sum across transakt. Filter to one (typically B1GD for GVA).
- nabp117 has fewer transakt types than the coarser tables (no B2A3ND, B1N2D).
- Data only runs to 2022 — use nabp69 or coarser tables for more recent years.