table: fact.ifi02
description: Industriens investeringsforventninger efter branche (DB07), investeringstype, bedømmelse og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- invest: values [TOTAL=Samlet investeringer, MASK=Maskiner og udstyr, LAND=Land, bygninger og infrastruktur, IMMA=Immaterielle investeringer (forskning og udvikling/ software/intellektuelle rettigheder /efteruddannelse osv.)]
- bedommelse: values [STØ=Stigende/forbedret, UÆN=Omtrent uændret, MIN=Faldende/forringet, NET=Nettotal]
- tid: date range 2010-01-01 to 2025-01-01

notes:
- branche07 does NOT join dim.db. Same letter-coded scheme as ifi01: B, C, CA–CM, S1–S4. Use ColumnValues("ifi02", "branche07") for labels.
- invest: TOTAL=overall investment, MASK=machinery, LAND=land/buildings, IMMA=intangibles. TOTAL is reported independently (not derived from MASK+LAND+IMMA in the fact table). Filter to invest='TOTAL' for an aggregate view; use specific types to compare investment composition. Don't sum across invest values — TOTAL already represents the aggregate.
- bedommelse: STØ+UÆN+MIN = 100 per branche07/invest/tid; NET = STØ−MIN. Filter to one bedommelse per query. Use bedommelse='NET' for the net expectation indicator.
- This is the non-revision version (no opg column); all data are final. For revision tracking use ifi02r.