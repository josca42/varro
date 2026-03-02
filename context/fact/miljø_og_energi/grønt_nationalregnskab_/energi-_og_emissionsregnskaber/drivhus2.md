table: fact.drivhus2
description: Drivhusgasregnskab (i CO2-ækvivalenter) efter branche, emissionstype, opgørelsesprincip og tid
measure: indhold (unit 1.000 ton)
columns:
- branche: join dim.nr_branche on branche=kode [approx]
- emtype8: values [GHGEXBIO=Drivhusgasser i alt, ekskl. CO2 fra afbrænding af biomasse, GHGBIO=Drivhusgasser i alt, inkl. CO2 fra afbrænding af biomasse, CO2UBIO=Kuldioxid (CO2), ekskl. fra afbrænding af biomasse, CO2BIO=Kuldioxid (CO2) fra afbrænding af biomasse, N2O=Lattergas (N2O), CH4=Metan (CH4), FGAS=Fluorerede gasser (SF6, PFC, HFC)]
- opprincip: values [DIR=Direkte emissioner, FORDEL=Fordeling af emissioner fra el og fjernvarme, BRUTTO=Samlede emissioner]
- tid: date range 1990-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- branche: same join as drivhus — REPLACE(REPLACE(f.branche, 'V', ''), '_', '-') = TRIM(d.kode). Special codes not in dim: MTOT, MHUSHOLD. NEEL (net electricity) is a correction term with negative values, used in the FORDEL allocation.
- opprincip is a critical selector — every branche × emtype8 combination appears 3×. Always filter to one: DIR=direct emissions only, FORDEL=allocated el/fjernvarme share, BRUTTO=DIR+FORDEL (total allocated). Never sum across opprincip.
- emtype8: GHG codes in 1.000 ton CO2-equivalents, same as drivhus.
- Use drivhus (without opprincip) for simpler queries. Use drivhus2 when you need to compare direct vs. allocated emissions (e.g. a sector's Scope 1 vs. Scope 2).
- Use ColumnValues("nr_branche", "titel", for_table="drivhus2") to see available branches.