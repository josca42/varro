table: fact.nabb69
description: Beskæftigelse og timer (69-gruppering) efter socioøkonomisk status, branche og tid
measure: indhold (unit -)
columns:
- socio: values [EMPH_DC=Samlede præsterede timer (1000 timer), SALH_DC=Præsterede timer for lønmodtagere (1000 timer), EMPM_DC=Samlet antal beskæftigede (antal), SALM_DC=Lønmodtagere (antal)]
- branche: join dim.nr_branche on branche=kode [approx]
- tid: date range 1966-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- branche join: `JOIN dim.nr_branche d ON d.kode = substring(f.branche from 2) AND d.niveau = 4`. Strip V prefix only — niveau-4 codes are 5-digit numeric (e.g. V01000→01000). 69 sectors + V + VMEMO.
- socio is a measurement-type selector — filter to exactly one (EMPH_DC/SALH_DC for hours, EMPM_DC/SALM_DC for persons).
- VMEMO is not in dim and should be excluded when aggregating.