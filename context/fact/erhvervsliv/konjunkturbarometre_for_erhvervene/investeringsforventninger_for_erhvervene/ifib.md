table: fact.ifib
description: Industriens investeringsforventninger efter branche (DB07), påvirkende forhold og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- paafor: values [EFTERSP=Udviklingen i efterspørgsel, FINANS=Adgang til finansielle ressourcer eller forventet profit, TEKNISK=Tekniske forhold fx teknologiske udvikling, uddannelse og myndighedskrav, ANDRE=Andre forhold fx beskatningsregler mv.]
- tid: date range 2010-01-01 to 2026-01-01

notes:
- branche07 does NOT join dim.db. Same letter-coded scheme as ifi01: B, C, CA–CM, S1–S4. Use ColumnValues("ifib", "branche07") for labels.
- paafor (påvirkende forhold) values are NOT mutually exclusive — each is the percentage of companies citing that factor as influencing investment plans. Values sum well above 100 for a given branche07/tid (e.g. EFTERSP=55, FINANS=30, TEKNISK=37, ANDRE=10 for C in 2024). Never sum across paafor. Query each factor independently or show them side by side.