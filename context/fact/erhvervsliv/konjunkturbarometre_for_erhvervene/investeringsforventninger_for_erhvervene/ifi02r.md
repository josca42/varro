table: fact.ifi02r
description: Industriens investeringsforventninger efter branche (DB07), opgørelse (målingstidspunkt), investeringstype, bedømmelse og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- opg: values [10=Foreløbige tal (Opgjort oktober året før), 25=Foreløbige tal 1. revision (Opgjort april samme år), 30=Foreløbige tal 2. revision (Opgjort oktober samme år), 45=Endelige tal (Opgjort april året efter)]
- invest: values [TOTAL=Samlet investeringer, MASK=Maskiner og udstyr, LAND=Land, bygninger og infrastruktur, IMMA=Immaterielle investeringer (forskning og udvikling/ software/intellektuelle rettigheder /efteruddannelse osv.)]
- bedommelse: values [STØ=Stigende/forbedret, UÆN=Omtrent uændret, MIN=Faldende/forringet, NET=Nettotal]
- tid: date range 2010-01-01 to 2026-01-01

notes:
- opg multiplies rows 4× per year. Always filter to one opg value. Use opg=45 for final figures, opg=10 for earliest preliminary estimates. Prefer ifi02 if you don't need to track revisions.
- branche07 does NOT join dim.db. Same letter-coded scheme as ifi01: B, C, CA–CM, S1–S4. Use ColumnValues("ifi02r", "branche07") for labels.
- invest: TOTAL is reported independently. Don't sum MASK+LAND+IMMA and expect to match TOTAL. Filter invest='TOTAL' for aggregate, or pick specific types for composition analysis.
- bedommelse: STØ+UÆN+MIN = 100 per branche07/invest/opg/tid; NET = STØ−MIN. Filter to one bedommelse per query.