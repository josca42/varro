table: fact.nabp10
description: 1-2.1.1 Produktion, BVT og indkomstdannelse (10a3-gruppering) efter transaktion, branche, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [P1K=P.1 Produktion, P2D=P.2 Forbrug i produktionen, B1GD=B.1g Bruttoværditilvækst, BVT, D29X39D=D.29-D.39 Andre produktionskatter minus andre produktionssubsidier, B1GFD=B.1GF Bruttofaktorindkomst, BFI, D1D=D.1 Aflønning af ansatte, B2A3GD=B.2g+B.3g Bruttooverskud af produktion og blandet indkomst, P51CD=P.51c Forbrug af fast realkapital, B2A3ND=B.2n+B.3n Nettooverskud af produktion og blandet indkomst, B1N2D=B.1n Nettoværditilvækst]
- branche: join dim.nr_branche on branche=kode [approx]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1966-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- branche join: same V-prefix/underscore pattern — `JOIN dim.nr_branche d ON d.kode = replace(substring(f.branche from 2), '_', '-') AND d.niveau = 1`. 13 niveau-1 sectors + V + VMEMO.
- transakt contains accounting aggregates that are identities of each other — never sum across transakt. B1GD (GVA) is the most commonly needed. Key identity: P1K − P2D = B1GD; B1GD − D29X39D = B1GFD; D1D + B2A3GD = B1GFD.
- prisenhed must be filtered (V=current prices, LAN=2020 chain-linked). B1GFD, B2A3GD, B2A3ND, D1D, D29X39D are only available in V (current prices).
- Sample — GVA by sector in 2023 (current prices): `SELECT d.titel, f.indhold FROM fact.nabp10 f JOIN dim.nr_branche d ON d.kode = replace(substring(f.branche from 2), '_', '-') AND d.niveau = 1 WHERE f.transakt = 'B1GD' AND f.prisenhed = 'V' AND f.tid = '2023-01-01' AND f.branche NOT IN ('V','VMEMO') ORDER BY f.indhold DESC;`