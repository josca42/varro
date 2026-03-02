table: fact.kbi3
description: Produktionsbegrænsninger i industrien efter branche (DB07), årsag og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- aarsag: values [INGEN=Ingen begrænsninger, AMA=Mangel på arbejdskraft, UKA=Mangel på materialer og/eller udstyr, UEF=Mangel på efterspørgsel, FINBE=Finansielle begrænsninger, ANDÅS=Andre årsager]
- tid: date range 2005-01-01 to 2025-10-01
dim docs: /dim/db.md

notes:
- branche07 does NOT join dim.db — uses DB07 letter codes. Same hierarchy as kbi1. Use ColumnValues("kbi3", "branche07") for labels.
- CRITICAL: aarsag values are NOT mutually exclusive. A firm can cite multiple constraints at once. Values represent % of firms citing each reason — they can sum to well over 100%. Never sum across aarsag. Each row is an independent reading.
- INGEN (no constraints) is its own category, not the complement of the others. Even with INGEN=32%, constraint categories can be high (different firms). Example for C in 2024-Q1: AMA=8, UKA=18, UEF=38, FINBE=9, ANDÅS=12, INGEN=32 — total = 117%.
- Sample: SELECT tid, indhold FROM fact.kbi3 WHERE branche07='C' AND aarsag='UEF' ORDER BY tid;