table: fact.nrhp
description: 1-2.1.1 Produktion, BNP og indkomstdannelse efter område, transaktion, prisenhed og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- transakt: values [P1K=P.1 Produktion, P2D=P.2 Forbrug i produktionen, B1GD=B.1g Bruttoværditilvækst, BVT, D21X31D=D.21-D.31 Produktskatter minus produktsubsidier, B1GQD=B.1*g Bruttonationalprodukt, BNP, D29X39D=D.29-D.39 Andre produktionskatter minus andre produktionssubsidier, B1GFD=B.1GF Bruttofaktorindkomst, BFI, D1D=D.1 Aflønning af ansatte, B2A3GD=B.2g+B.3g Bruttooverskud af produktion og blandet indkomst]
- prisenhed: values [V_T=Løbende priser, (mio. kr.), V_C=Pr. indbygger, løbende priser, (1000 kr.), LRG_T=2020-priser, kædede værdier, (mio. kr.), LRG_C=Pr. indbygger, 2020-priser, kædede værdier, (1000 kr.)]
- tid: date range 1993-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts but codes 0 (hele landet) and 999 (ikke regionalfordelt) are NOT in the dim table. omrade=0 is the national total; omrade=999 is activity not allocated to a region; together regions + 999 = 0. Exclude both when doing regional breakdowns.
- omrade uses levels 1 (5 regioner: 81–85) and 2 (11 landsdele: 1–11). Filter WHERE d.niveau=1 for regions or d.niveau=2 for landsdele. Do not join without a niveau filter or you get both levels and double-count.
- prisenhed is a measurement selector — the same (omrade, transakt, tid) combination appears 4 times, once per price unit. Always filter to one prisenhed: V_T (løbende priser, mio. kr.) is the most common; LRG_T (2020-priser, kædede værdier) for volume comparisons; V_C/LRG_C for per-capita.
- transakt codes are distinct national accounts items in a hierarchical identity (e.g. B1GQD=BNP, B1GD=BVT, B1GFD=BFI). Do not sum across transakt — pick the specific transaction needed.
- Typical regional BNP query: JOIN dim.nuts d ON f.omrade=d.kode WHERE d.niveau=1 AND f.prisenhed='V_T' AND f.transakt='B1GQD'.
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade IN (0, 999).