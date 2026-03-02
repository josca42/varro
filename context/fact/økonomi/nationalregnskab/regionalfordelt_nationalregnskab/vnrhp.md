table: fact.vnrhp
description: Versionstabel NRHP - Produktion, BNP og indkomstdannelse efter version, område, transaktion, prisenhed og tid
measure: indhold (unit -)
columns:
- version: values [V2024_JUN=Juniversion 2021-2024, V2023_JUN=Juniversion 1993-2023 (Hovedrevision 2024), V2022_SEP=Septemberversion 2020-2022, V2021_SEP=Septemberversion 2019-2021, V2020_SEP=Septemberversion 2018-2020, V2019_SEP=Septemberversion 2017-2019, V2018_NOV=Novemberversion 2016-2018, V2017_NOV=Novemberversion 2015-2017, V2017_MAR=Martsversion 2014-2017, V2016_NOV=Novemberversion 2014-2016, V2015_NOV=Novemberversion 2004-2015 (Datarevision 2016), V2014_NOV=Novemberversion 2012-2014, V2013_NOV=Novemberversion 2011-2013, V2013_SEP=Septemberversion 1966-2013 (Hovedrevision 2014)]
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- transakt: values [P1K=P.1 Produktion, P2D=P.2 Forbrug i produktionen, B1GD=B.1g Bruttoværditilvækst, BVT, D21X31D=D.21-D.31 Produktskatter minus produktsubsidier, B1GQD=B.1*g Bruttonationalprodukt, BNP, D29X39D=D.29-D.39 Andre produktionskatter minus andre produktionssubsidier, B1GFD=B.1GF Bruttofaktorindkomst, BFI, D1D=D.1 Aflønning af ansatte, B2A3GD=B.2g+B.3g Bruttooverskud af produktion og blandet indkomst]
- prisenhed: values [V_T=Løbende priser, (mio. kr.), V_C=Pr. indbygger, løbende priser, (1000 kr.), LRG_TO=2010-priser, kædede værdier, (mio. kr.), LRG_T=2020-priser, kædede værdier, (mio. kr.), LRG_CA=Pr. indbygger, 2010-priser, kædede værdier, (1000 kr.), LRG_C=Pr. indbygger, 2020-priser, kædede værdier, (1000 kr.)]
- tid: date range 1993-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- version is a critical filter — each version covers the full time series back to 1993, so all 14 versions heavily overlap. Querying without filtering version inflates all values by 14x. Always filter to one version: V2024_JUN for the latest official figures.
- omrade joins dim.nuts but codes 0 (hele landet) and 999 (ikke regionalfordelt) are NOT in the dim. Exclude both for regional analysis.
- prisenhed is a measurement selector (6 options including older 2010-priser chains for historical versions). Filter to one. Use V_T or LRG_T.
- Prefer nrhp for standard analysis. Use vnrhp only when you need to compare how a specific time period's figures changed between revisions (e.g. how the 2020 BNP estimate evolved across release versions).