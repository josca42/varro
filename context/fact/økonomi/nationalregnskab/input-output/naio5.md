table: fact.naio5
description: Beskæftigelse og timer efter socioøkonomisk status, branche og tid
measure: indhold (unit -)
columns:
- socio: values [EMPH_DC=Samlede præsterede timer (1000 timer), SALH_DC=Præsterede timer for lønmodtagere (1000 timer), SELFH_DC=Præsterede timer for selvstændige (1000 timer), EMPM_DC=Samlet antal beskæftigede (antal), SALM_DC=Lønmodtagere (antal), SELFM_DC=Selvstændige (antal), EMPEM_DC=Samlet antal beskæftigede ekskl. orlov mv. (antal), SALEM_DC=Lønmodtagere ekskl. orlov mv. (antal), SELFEM_DC=Selvstændige ekskl. orlov mv. (antal)]
- branche: join dim.nr_branche on branche=kode [approx]
- tid: date range 1966-01-01 to 2022-01-01
dim docs: /dim/nr_branche.md

notes:
- **socio is a measurement selector** — 9 values covering different population scopes (total / lønmodtagere / selvstændige) and different metrics (præsterede timer in 1000 timer vs antal beskæftigede vs ekskl. orlov). These are NOT additive. Always filter to exactly one socio value. For total employment: `EMPM_DC` (antal). For total hours: `EMPH_DC`.
- **branche uses V-prefix**. The documented join `f.branche=d.kode` does NOT work. Use `SUBSTRING(f.branche, 2) = d.kode` to join dim.nr_branche. `V` alone = total, `VA`-`VU` = niveau 1–2, `VCA` etc = niveau 3, `V01000` = niveau 4 (5-digit), `V010000` = niveau 5 (6-digit).
- Filter `d.niveau` in the join to avoid summing across hierarchy levels. E.g. `WHERE d.niveau = 4` for the 69-group breakdown.
- naio5 goes to the detailed 6-digit level (niveau 5 + sub-codes). Use naio5f if the 69-groupering is sufficient.