table: fact.straf24
description: Anmeldte forbrydelser pr. 100.000 indbyggere efter overtrædelsens art og tid
measure: indhold (unit Antal)
columns:
- overtraed: join dim.overtraedtype on overtraed=kode::text [approx: Fact col is string, dim KODE is int64. Also has TOT placeholder.]; levels [1, 2, 3]
- tid: date range 2018-01-01 to 2024-01-01
dim docs: /dim/overtraedtype.md

notes:
- indhold is crimes per 100,000 inhabitants — a rate, not a count. Do NOT sum across rows; use as-is for comparisons.
- overtraed joins dim.overtraedtype via `f.overtraed = d.kode::text`. Niveaux 1, 2, 3 coexist — filter to a single niveau to avoid mixing aggregate and detail rates. overtraed='TOT' = overall rate (not in dim).
- Only Straffelov and Særlov at niveau 1 — Færdselslov absent.
- Covers 2018–2024 only — much shorter than straf10/straf20. Use for rate-based comparisons; use straf10 for count-based or historical analysis.
- No regional breakdown — national rates only. There is no regional equivalent of this table in this subject.