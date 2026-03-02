table: fact.vnrbp10
description: Versionstabel NRBP10 - Produktion, BVT og indkomstdannelse (10a3-gruppering) efter version, område, transaktion, branche, prisenhed og tid
measure: indhold (unit -)
columns:
- version: values [V2024_JUN=Juniversion 2021-2024, V2023_JUN=Juniversion 1993-2023 (Hovedrevision 2024), V2022_SEP=Septemberversion 2020-2022, V2021_SEP=Septemberversion 2019-2021, V2020_SEP=Septemberversion 2018-2020, V2019_SEP=Septemberversion 2017-2019, V2018_NOV=Novemberversion 2016-2018, V2017_NOV=Novemberversion 2015-2017, V2017_MAR=Martsversion 2014-2017, V2016_NOV=Novemberversion 2014-2016, V2015_NOV=Novemberversion 2004-2015 (Datarevision 2016), V2014_NOV=Novemberversion 2012-2014, V2013_NOV=Novemberversion 2011-2013, V2013_SEP=Septemberversion 1966-2013 (Hovedrevision 2014)]
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- transakt: values [P1K=P.1 Produktion, P2D=P.2 Forbrug i produktionen, B1GD=B.1g Bruttoværditilvækst, BVT, D29X39D=D.29-D.39 Andre produktionskatter minus andre produktionssubsidier, B1GFD=B.1GF Bruttofaktorindkomst, BFI, D1D=D.1 Aflønning af ansatte, B2A3GD=B.2g+B.3g Bruttooverskud af produktion og blandet indkomst]
- branche: join dim.nr_branche on branche=kode [approx]
- prisenhed: values [V_T=Løbende priser, (mio. kr.), V_C=Pr. indbygger, løbende priser, (1000 kr.), LRG_TO=2010-priser, kædede værdier, (mio. kr.), LRG_T=2020-priser, kædede værdier, (mio. kr.), LRG_CA=Pr. indbygger, 2010-priser, kædede værdier, (1000 kr.), LRG_C=Pr. indbygger, 2020-priser, kædede værdier, (1000 kr.)]
- tid: date range 1993-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md, /dim/nuts.md

notes:
- version is a critical filter — all 14 versions cover the full time series back to 1993. Always filter to one version: V2024_JUN. Omitting this inflates values by 14x.
- branche joins dim.nr_branche (approx match). Unlike nrbp10 which has inline branche codes (V, VA, etc.), vnrbp10 uses a dim join — check dim.nr_branche for available codes.
- omrade joins dim.nuts but codes 0 and 999 are not in the dim. Exclude for regional analysis. Levels 1 (regioner) and 2 (landsdele).
- prisenhed is a measurement selector (6 options, including older 2010-priser chains). Filter to one: V_T or LRG_T.
- transakt codes are distinct national accounts items. Do not sum across transakt.
- Prefer nrbp10 for standard analysis. Use vnrbp10 only for vintage comparison across revisions.