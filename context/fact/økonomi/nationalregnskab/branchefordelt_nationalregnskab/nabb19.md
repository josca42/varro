table: fact.nabb19
description: Beskæftigelse og timer (19a2-gruppering) efter socioøkonomisk status, branche og tid
measure: indhold (unit -)
columns:
- socio: values [EMPH_DC=Samlede præsterede timer (1000 timer), SALH_DC=Præsterede timer for lønmodtagere (1000 timer), EMPM_DC=Samlet antal beskæftigede (antal), SALM_DC=Lønmodtagere (antal)]
- erhverv: join dim.nr_branche on erhverv=kode [approx]
- tid: date range 1966-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- Column is named `erhverv` (not `branche`). Join: `JOIN dim.nr_branche d ON d.kode = substring(f.erhverv from 2) AND d.niveau = 2`. Strip V prefix only — niveau-2 codes have no hyphens so no replace needed. 21 sectors + V (total) + VMEMO.
- socio is a measurement-type selector — filter to exactly one: EMPH_DC (total hours), SALH_DC (employee hours), EMPM_DC (total employed), SALM_DC (employees).
- VMEMO is not in dim.nr_branche. Exclude it (and V) when summing across sectors.