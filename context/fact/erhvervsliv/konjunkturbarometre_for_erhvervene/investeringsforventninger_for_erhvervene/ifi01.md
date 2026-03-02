table: fact.ifi01
description: Industriens investeringsforventninger efter branche (DB07), bedømmelse og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- bedommelse: values [STØ=Stigende/forbedret, UÆN=Omtrent uændret, MIN=Faldende/forringet, NET=Nettotal]
- tid: date range 2010-01-01 to 2026-01-01

notes:
- branche07 does NOT join dim.db. Codes are DB07 section letters (B=Råstofindvinding, C=Industri, CA–CM=industri subsections) plus MIG branchegrupper (S1=Investeringsgodeindustri, S2=Mellemproduktindustri, S3=Varige forbrugsgoder, S4=Ikke-varige forbrugsgoder). Use ColumnValues("ifi01", "branche07") for the full list with labels.
- bedommelse: STØ, UÆN, MIN always sum to 100 for a given branche07/tid — they are exhaustive percentages. NET = STØ − MIN (nettotal, the expectation balance indicator). Never sum across bedommelse values. Filter to one value: use bedommelse='NET' for the net indicator, or bedommelse='STØ' etc. for individual sentiment shares.
- BC is the aggregate of B+C (Råstofindvinding og industri i alt). Filter to branche07='C' for total industri or specific CA–CM codes for subsectors. S1–S4 are cross-cutting MIG groups that overlap with C subsections — don't mix them with CA–CM in the same query.