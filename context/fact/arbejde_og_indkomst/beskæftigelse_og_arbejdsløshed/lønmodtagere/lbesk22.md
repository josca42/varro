table: fact.lbesk22
description: Lønmodtagere (sæsonkorrigeret) efter enhed, branche (DB07 10- og 19-grp) og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- branchedb071038: join dim.db on branchedb071038=kode::text; levels [2, 3]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/db.md
notes:
- Sæsonkorrigeret version of lbesk20. Same structure — see lbesk20 notes.
- ALWAYS filter tal to one value (1010 or 1020). dim.db join is incorrect — use dim.db_10 for 10-gruppe numeric codes.
- branchedb071038 mixes two schemes: numeric 1–11 (10-gruppe) and letters A–S + X (19-gruppe, inline only). Filter to one scheme.
