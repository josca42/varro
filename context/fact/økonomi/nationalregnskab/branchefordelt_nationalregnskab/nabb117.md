table: fact.nabb117
description: Beskæftigelse og timer (117-gruppering) efter socioøkonomisk status, branche og tid
measure: indhold (unit -)
columns:
- socio: values [EMPH_DC=Samlede præsterede timer (1000 timer), SALH_DC=Præsterede timer for lønmodtagere (1000 timer), EMPM_DC=Samlet antal beskæftigede (antal), SALM_DC=Lønmodtagere (antal)]
- branche: join dim.nr_branche on branche=kode [approx]
- tid: date range 1966-01-01 to 2022-01-01
dim docs: /dim/nr_branche.md

notes:
- branche join: `JOIN dim.nr_branche d ON d.kode = substring(f.branche from 2) AND d.niveau = 5`. Strip V prefix only — niveau-5 codes are 6-digit numeric. 117 sectors + V + VMEMO.
- socio is a measurement-type selector — filter to exactly one (EMPH_DC/SALH_DC for hours, EMPM_DC/SALM_DC for persons).
- Data only runs to 2022 — use nabb69 or coarser tables for more recent years.