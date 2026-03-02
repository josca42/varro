table: fact.straf20
description: Anmeldte forbrydelser og sigtelser efter overtrædelsens art, anmeldte og sigtede og tid
measure: indhold (unit Antal)
columns:
- overtraed: join dim.overtraedtype on overtraed=kode::text [approx: Fact col is string, dim KODE is int64. Also has TOT placeholder.]; levels [1, 2, 3]
- anmsigt: values [ANM=Anmeldt, SIG=Sigtelser]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/overtraedtype.md

notes:
- anmsigt splits every row into two mutually exclusive categories: ANM (Anmeldt = reported crimes) and SIG (Sigtelser = charges filed). Always filter to one value to avoid double-counting. ANM gives the same crime counts as straf10; SIG adds the charge dimension.
- overtraed joins dim.overtraedtype via `f.overtraed = d.kode::text`. Niveaux 1, 2, 3 coexist — filter to a single niveau. overtraed='TOT' = grand total (not in dim).
- Only Straffelov and Særlov at niveau 1 — Færdselslov absent.
- To compare reported vs charged: query with both ANM and SIG and pivot on anmsigt rather than summing across it.
- Covers 1995–2024 (annual). This is the right table when you need both crime counts and charges in a single query.