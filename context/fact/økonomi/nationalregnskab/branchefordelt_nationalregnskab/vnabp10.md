table: fact.vnabp10
description: Versionstabel NABP10 Produktion, BVT og indkomstdannelse (10a3-gruppering) efter version, transaktion, branche, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- version: values [V2024_JUN=Juniversion 2021-2024, V2024_MAR=Martsversion 2024, V2024_FEB=Februarversion 2024, V2023_JUN=Juniversion 1966-2023 (Hovedrevision 2024), V2023_MAR=Martsversion 2023 ... V2014_JUN=Juniversion 2014, V2014_MAR=Martsversion 2014, V2014_FEB=Februarversion 2014, V2013_NOV=Novemberversion 2011-2013, V2013_SEP=Septemberversion 1966-2013 (Hovedrevision 2014)]
- transakt: values [P1K=P.1 Produktion, P2D=P.2 Forbrug i produktionen, B1GD=B.1g Bruttoværditilvækst, BVT, D29X39D=D.29-D.39 Andre produktionskatter minus andre produktionssubsidier, B1GFD=B.1GF Bruttofaktorindkomst, BFI, D1D=D.1 Aflønning af ansatte, B2A3GD=B.2g+B.3g Bruttooverskud af produktion og blandet indkomst, P51CD=P.51c Forbrug af fast realkapital, B2A3ND=B.2n+B.3n Nettooverskud af produktion og blandet indkomst, B1N2D=B.1n Nettoværditilvækst]
- erhverv: join dim.nr_branche on erhverv=kode [approx]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier, LPR=2010-priser, kædede værdier]
- tid: date range 1966-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- Column is named `erhverv` (not `branche`). Join: `JOIN dim.nr_branche d ON d.kode = replace(substring(f.erhverv from 2), '_', '-') AND d.niveau = 1` — same V-prefix/underscore pattern as nabp10.
- prisenhed includes LPR (2010-priser) in addition to V and LAN — an older base year present in earlier version releases.
- Use `version` to compare figures across release vintages. Filter to a single version for a consistent time series.
- transakt contains accounting aggregates — never sum across transakt.
- For current estimates without version history, use nabp10 instead.