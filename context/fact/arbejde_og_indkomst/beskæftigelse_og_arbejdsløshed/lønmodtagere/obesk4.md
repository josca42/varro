table: fact.obesk4
description: Offentligt fuldtidsbeskæftigede lønmodtagere (sæsonkorrigeret) efter formålsopdeling (COFOG) og tid
measure: indhold (unit Antal)
columns:
- cofog: join dim.cofog on cofog=kode::text; levels [1]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/cofog.md
notes:
- Sæsonkorrigeret version of obesk1. Same structure — see obesk1 notes.
- cofog joins dim.cofog correctly at niveau 1 (codes 1–10). Filter out TOT1 and 99 in the JOIN.
- Use for seasonal trend analysis of public employment by COFOG purpose category.
