table: fact.naio5f
description: Beskæftigelse og timer (69-gruppering) efter socioøkonomisk status, branche og tid
measure: indhold (unit -)
columns:
- socio: values [EMPH_DC=Samlede præsterede timer (1000 timer), SALH_DC=Præsterede timer for lønmodtagere (1000 timer), SELFH_DC=Præsterede timer for selvstændige (1000 timer), EMPM_DC=Samlet antal beskæftigede (antal), SALM_DC=Lønmodtagere (antal), SELFM_DC=Selvstændige (antal), EMPEM_DC=Samlet antal beskæftigede ekskl. orlov mv. (antal), SALEM_DC=Lønmodtagere ekskl. orlov mv. (antal), SELFEM_DC=Selvstændige ekskl. orlov mv. (antal)]
- branche: join dim.nr_branche on branche=kode [approx]
- tid: date range 1966-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- Same as naio5 but limited to the 69-groupering (niveau 4, 5-digit codes). Covers to 2024 vs 2022.
- **socio must be filtered to one value**. Same 9 measurement selectors as naio5. See naio5 notes.
- `branche` uses V-prefix; join via `SUBSTRING(f.branche, 2) = d.kode` and filter `d.niveau = 4` for the 69-group level.