table: fact.lbesk20
description: Lønmodtagere efter enhed, branche (DB07 10- og 19-grp) og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- branchedb071038: join dim.db on branchedb071038=kode::text; levels [2, 3]
- tid: date range 2008-01-01 to 2025-04-01
dim docs: /dim/db.md
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- WARNING: dim.db join is incorrect. branchedb071038 mixes two grouping schemes in one column: numeric 1–11 (10-gruppe, matches dim.db_10 niveau 1) and letter codes A–S + X (19-gruppe NACE afsnit, not in any dim table). TOT = alle brancher. Filter to one scheme to avoid overlap.
- For 10-gruppe: WHERE branchedb071038 ~ '^[0-9]+$'. Join: JOIN dim.db_10 d ON f.branchedb071038 = d.kode::text AND d.niveau = 1.
- For 19-gruppe: WHERE branchedb071038 ~ '^[A-Z]' AND branchedb071038 != 'TOT'. Use ColumnValues("lbesk20", "branchedb071038") for labels. Letter codes are NOT in any dim table.
- lbesk20 = ukorrigeret; lbesk22 = sæsonkorrigeret (identical structure).
