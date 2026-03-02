table: fact.nkbb10
description: Beskæftigelse og timer (10a3-gruppering) efter socioøkonomisk status, branche, sæsonkorrigering og tid
measure: indhold (unit -)
columns:
- socio: values [EMPH_DC=Samlede præsterede timer (1000 timer), SALH_DC=Præsterede timer for lønmodtagere (1000 timer), EMPM_DC=Samlet antal beskæftigede (antal), SALM_DC=Lønmodtagere (antal)]
- branche: join dim.nr_branche on branche=kode [approx]
- saeson: values [N=Ikke sæsonkorrigeret, Y=Sæsonkorrigeret]
- tid: date range 1990-01-01 to 2025-04-01
dim docs: /dim/nr_branche.md

notes:
- branche join: same V-prefix/underscore pattern as nabb10 — `JOIN dim.nr_branche d ON d.kode = replace(substring(f.branche from 2), '_', '-') AND d.niveau = 1`.
- Two selector columns must both be filtered: `socio` (measurement type) AND `saeson` (N=unadjusted, Y=seasonally adjusted). Forgetting either silently doubles the result.
- tid is quarterly (2024-01-01 = Q1 2024, 2024-04-01 = Q2 2024). Data runs 1990–present.
- For annual totals, use nabb10. nkbb10 is the quarterly/seasonal companion.