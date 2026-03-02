table: fact.vandrg1
description: Indvinding af vand (Fysiske vandregnskab) efter branche, vandtype og tid
measure: indhold (unit 1.000 m3)
columns:
- erhverv: join dim.nr_branche on REPLACE(erhverv, 'V', '')=kode::text [approx: Strip V prefix from fact values to match dimension KODE]
- vandtyp: values [TOTVAND=Vand i alt, GVAND=Grundvand, OVAND=Overfladevand]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md

notes:
- erhverv joins dim.nr_branche but requires: REPLACE(REPLACE(f.erhverv, 'V', ''), '_', '-') = TRIM(d.kode). Three transforms needed: (1) strip V prefix (V010000→010000), (2) replace underscore with hyphen for group codes (D_E→D-E, G_I→G-I, etc.), (3) TRIM trailing space from dim.kode (6-digit codes stored as VARCHAR(7) with trailing space).
- ETOT (total all industries) is not in dim.nr_branche — use WHERE f.erhverv='ETOT' for national total without joining the dim.
- 5 hierarchy levels in dim.nr_branche (niveau 1=sector groups, 2=sectors, 3=subsectors, 4=branch, 5=sub-branch). All levels are present simultaneously — filter by d.niveau to pick granularity and avoid double-counting across levels.
- vandtyp is hierarchical: TOTVAND = GVAND + OVAND. Filter to one value.
- Use ColumnValues("nr_branche", "titel", for_table="vandrg1") to browse available industries.
