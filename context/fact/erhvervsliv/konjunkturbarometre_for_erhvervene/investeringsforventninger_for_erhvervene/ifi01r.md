table: fact.ifi01r
description: Industriens investeringsforventninger efter branche (DB07), opgørelse (målingstidspunkt), bedømmelse og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- opg: values [10=Foreløbige tal (Opgjort oktober året før), 25=Foreløbige tal 1. revision (Opgjort april samme år), 30=Foreløbige tal 2. revision (Opgjort oktober samme år), 45=Endelige tal (Opgjort april året efter)]
- bedommelse: values [STØ=Stigende/forbedret, UÆN=Omtrent uændret, MIN=Faldende/forringet, NET=Nettotal]
- tid: date range 2010-01-01 to 2026-01-01

notes:
- This is the revision table. The opg column multiplies every row 4× — each calendar year appears up to 4 times (opg 10=Foreløbige oktober året før, 25=1. revision april, 30=2. revision oktober, 45=Endelige tal april året efter). Always filter to one opg value to avoid inflated counts. Use opg=45 for final figures; opg=10 for earliest preliminary estimates.
- branche07 does NOT join dim.db. Same letter-coded scheme as ifi01: B, C, CA–CM, S1–S4. Use ColumnValues("ifi01r", "branche07") for labels.
- bedommelse: STØ+UÆN+MIN = 100; NET = STØ−MIN. Never sum across bedommelse. Prefer ifi01 (without opg) if you only need final/current data — ifi01r adds the revision dimension for tracking estimate revisions over time.