table: fact.lbesk03
description: Lønmodtagere (sæsonkorrigeret) efter branche (DB07 10- og 19-grp) og tid
measure: indhold (unit Antal)
columns:
- branchedb071038: join dim.db on branchedb071038=kode::text; levels [2, 3]
- tid: date range 2008-01-01 to 2025-08-01
dim docs: /dim/db.md

notes:
- WARNING: dim.db join is incorrect. branchedb071038 uses numeric codes 1–11 (matching dim.db_10 niveau 1, not dim.db) and letter codes A–S + X (19-gruppe, no dim table). Use dim.db_10 for the 10-gruppe numeric codes.
- branchedb071038 mixes two grouping schemes: numeric 1–11 (10-gruppe) and letter codes A–S + X (19-gruppe). TOT = alle brancher. Never aggregate across both.
- For 10-gruppe: WHERE branchedb071038 ~ '^[0-9]+$'. Join: JOIN dim.db_10 d ON f.branchedb071038 = d.kode::text AND d.niveau = 1.
- For 19-gruppe: WHERE branchedb071038 ~ '^[A-Z]' AND branchedb071038 != 'TOT'. Use ColumnValues("lbesk03", "branchedb071038") for labels. Letter codes are NOT in any dim table.
- lbesk03 = sæsonkorrigeret. Same structure as lbesk01 (ukorrigeret). No tal column.