table: fact.vnabb10
description: Versionstabel NABB10 Beskæftigelse og timer (10a3-gruppering) efter version, socioøkonomisk status, branche og tid
measure: indhold (unit -)
columns:
- version: values [V2024_JUN=Juniversion 2021-2024, V2024_MAR=Martsversion 2024, V2024_FEB=Februarversion 2024, V2023_JUN=Juniversion 1966-2023 (Hovedrevision 2024), V2023_MAR=Martsversion 2023 ... V2014_JUN=Juniversion 2014, V2014_MAR=Martsversion 2014, V2014_FEB=Februarversion 2014, V2013_NOV=Novemberversion 2011-2013, V2013_SEP=Septemberversion 1966-2013 (Hovedrevision 2014)]
- socio: values [EMPH_DC=Samlede præsterede timer (1000 timer), SALH_DC=Præsterede timer for lønmodtagere (1000 timer), EMPM_DC=Samlet antal beskæftigede (antal), SALM_DC=Lønmodtagere (antal)]
- erhverv: join dim.nr_branche on erhverv=kode [approx]
- tid: date range 1966-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- Column is named `erhverv` (not `branche`). Join: `JOIN dim.nr_branche d ON d.kode = replace(substring(f.erhverv from 2), '_', '-') AND d.niveau = 1` — same V-prefix/underscore pattern as nabb10.
- Use `version` to compare figures across release vintages. Each version code encodes the release month and year (e.g. V2024_JUN = June 2024 release). Filter to a single version for a consistent time series.
- socio is a measurement-type selector — filter to exactly one.
- For current estimates without version history, use nabb10 instead.