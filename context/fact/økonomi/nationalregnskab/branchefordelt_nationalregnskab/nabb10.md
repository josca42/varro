table: fact.nabb10
description: Beskæftigelse og timer (10a3-gruppering) efter socioøkonomisk status, branche og tid
measure: indhold (unit -)
columns:
- socio: values [EMPH_DC=Samlede præsterede timer (1000 timer), SALH_DC=Præsterede timer for lønmodtagere (1000 timer), EMPM_DC=Samlet antal beskæftigede (antal), SALM_DC=Lønmodtagere (antal)]
- branche: join dim.nr_branche on branche=kode [approx]
- tid: date range 1966-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- branche join requires stripping the V prefix AND converting underscores to hyphens: `JOIN dim.nr_branche d ON d.kode = replace(substring(f.branche from 2), '_', '-') AND d.niveau = 1`. Direct join (branche=kode) gives 0% match. The 13 niveau-1 codes map VA→A, VB→B, ..., VD_E→D-E, VG_I→G-I, VM_N→M-N, VO_Q→O-Q, VR_S→R-S.
- V is the economy-wide total; VMEMO is a separate memo aggregate (not in dim, much smaller than V). Exclude both when summing across sectors to avoid double-counting.
- socio is a measurement-type selector — all 4 values are repeated for every branche×tid. Always filter to exactly one: EMPH_DC (total hours, 1000 timer), SALH_DC (employee hours, 1000 timer), EMPM_DC (total employed, antal), SALM_DC (employees, antal). The unit of indhold changes with the choice.
- Sample — employment by sector in 2023: `SELECT d.titel, f.indhold FROM fact.nabb10 f JOIN dim.nr_branche d ON d.kode = replace(substring(f.branche from 2), '_', '-') AND d.niveau = 1 WHERE f.socio = 'EMPM_DC' AND f.tid = '2023-01-01' AND f.branche NOT IN ('V','VMEMO') ORDER BY f.indhold DESC;`