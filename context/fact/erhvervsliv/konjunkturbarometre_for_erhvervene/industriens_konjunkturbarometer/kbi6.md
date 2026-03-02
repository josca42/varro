table: fact.kbi6
description: Konkurrencesituationen på eksportmarkederne i industrien efter branche (DB07), indikator, bedømmelse og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- indikator1: values [KSIEU=Udviklingen på markedet i EU de seneste tre måneder, KSUFEU=Udviklingen på markedet udenfor EU de seneste tre måneder]
- bedommelse: values [FORB=Forbedret, UÆN=Omtrent uændret, FORR=Forringet, NET=Nettotal]
- tid: date range 2005-01-01 to 2025-10-01
dim docs: /dim/db.md

notes:
- branche07 does NOT join dim.db — uses DB07 letter codes. Same hierarchy as kbi1. Use ColumnValues("kbi6", "branche07") for labels.
- indikator1 is a selector — EU vs non-EU export market. Always filter indikator1; never sum across it.
- bedommelse=NET = FORB − FORR. Positive = improving competitive position, negative = deteriorating. Example for C in 2024-Q1: EU NET=−8 (FORB=2, FORR=10), non-EU NET=−24 (FORB=1, FORR=25). Do not sum across bedommelse values.
- Sample: SELECT tid, indhold FROM fact.kbi6 WHERE branche07='C' AND indikator1='KSUFEU' AND bedommelse='NET' ORDER BY tid;