table: fact.drivhus
description: Drivhusgasregnskab (i CO2-ækvivalenter) efter branche, emissionstype og tid
measure: indhold (unit 1.000 ton)
columns:
- branche: join dim.nr_branche on branche=kode [approx]
- emtype8: values [GHGEXBIO=Drivhusgasser i alt, ekskl. CO2 fra afbrænding af biomasse, GHGBIO=Drivhusgasser i alt, inkl. CO2 fra afbrænding af biomasse, CO2UBIO=Kuldioxid (CO2), ekskl. fra afbrænding af biomasse, CO2BIO=Kuldioxid (CO2) fra afbrænding af biomasse, N2O=Lattergas (N2O), CH4=Metan (CH4), FGAS=Fluorerede gasser (SF6, PFC, HFC)]
- tid: date range 1990-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- branche joins dim.nr_branche using: REPLACE(REPLACE(f.branche, 'V', ''), '_', '-') = TRIM(d.kode). Strip V prefix, replace underscore with hyphen (e.g. VD_E → D-E), and TRIM dim kode (some have trailing spaces). Special aggregate codes not in dim: MTOT (total), MHUSHOLD (households), BUNK (international bunkers).
- emtype8 uses GHG codes in 1.000 ton CO2-equivalents (consistent units — summing across emtype8 is valid within a branche). GHGEXBIO is the standard total (excl. biomass CO2); GHGBIO includes biomass CO2.
- Multiple branche hierarchy levels coexist (niveau 1–5 plus special codes). Use niveau=1 for top-level sectors (13 categories) or filter by nr_branche.niveau to pick a consistent level.
- Use drivhus2 instead if you need to split by accounting principle (direct vs. allocated el/fjernvarme emissions).
- Use ColumnValues("nr_branche", "titel", for_table="drivhus") to see available branches.