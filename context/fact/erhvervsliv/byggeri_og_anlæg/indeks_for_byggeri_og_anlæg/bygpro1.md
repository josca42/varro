table: fact.bygpro1
description: Produktionsindeks for bygge- og anlægssektoren efter branche og tid
measure: indhold (unit Indeks)
columns:
- branche: join dim.db on branche=kode::text [approx]
- tid: date range 2008-01-01 to 2025-08-01
dim docs: /dim/db.md

notes:
- Monthly frequency (all 12 months). The only monthly table in this subject and the most current (through 2025-08-01). No measurement selector column — `indhold` is always the index level.
- `branche` uses non-standard codes that DO NOT join to dim.db: `F41`, `F42`, `F43` use a letter-prefixed NACE coding, and `20100` is a proprietary aggregate code not in any dim table. Do not attempt the documented dim join.
- Interpret branche codes directly: `20100`=Bygge- og anlæg i alt (total sector), `F41`=Opførelse af bygninger, `F42`=Anlægsarbejder, `F43`=Bygge- og anlægsvirksomhed, som kræver specialisering. These correspond to DB07 sections 41/42/43 in meaning but not in code format.
- `20100` is the overall sector aggregate — do not sum F41+F42+F43; use `branche = '20100'` for the total.