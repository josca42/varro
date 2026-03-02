table: fact.mro2
description: Overgangstabel for drivhusgasser efter overgangsposter, emissionstype og tid
measure: indhold (unit 1.000 ton)
columns:
- overpost: values [DSTTOTAL=Emissioner fra dansk økonomi (Grønt nationalregnskab) (1), BUNKSUM=Emissioner i udlandet (international transport) (2)=(2.1)+(2.2)+(2.3), BUNKSKIB=Emissioner fra dansk opererede skibe i udlandet (2.1), BUNKFLY=Emissioner fra dansk opererede fly i udlandet (2.2), BUNKLAND=Emissioner fra dansk opererede køretøjer i udlandet (2.3), ANTRANS=Andre forskelle i emissioner fra transport og grænsehandel (3), DKTOTAL=Emissioner fra dansk territorium (UNFCCC/UNECE-opgørelsen) (4=(1)÷(2)÷(3)), LULUCF=Arealanvendelse og skovbrug (LULUCF) (5), TOTLULU=Emissioner fra dansk territorium inklusive LULUCF (6=(4)+(5))]
- emtype8: values [GHGEXBIO=Drivhusgasser i alt, ekskl. CO2 fra afbrænding af biomasse, GHGBIO=Drivhusgasser i alt, inkl. CO2 fra afbrænding af biomasse, CO2UBIO=Kuldioxid (CO2), ekskl. fra afbrænding af biomasse, CO2BIO=Kuldioxid (CO2) fra afbrænding af biomasse, N2O=Lattergas (N2O), CH4=Metan (CH4), FGAS=Fluorerede gasser (SF6, PFC, HFC)]
- tid: date range 1990-01-01 to 2023-01-01

notes:
- Same bridge structure as mro1 (national accounts ↔ territorial UNFCCC). overpost arithmetic: DKTOTAL = DSTTOTAL - BUNKSUM - ANTRANS; TOTLULU = DKTOTAL + LULUCF. Never sum all overpost values.
- emtype8 here uses GHG-specific codes (GHGEXBIO, GHGBIO, CO2UBIO, CO2BIO, N2O, CH4, FGAS) all in 1.000 ton CO2-equivalents — consistent units, so summing is meaningful within a single overpost value.
- GHGEXBIO = CO2UBIO + N2O + CH4 + FGAS (excludes biomass CO2). GHGBIO = GHGEXBIO + CO2BIO.
- mro2 = GHG-only version of mro1. For territorial vs. economy-principle comparisons on GHGs, this is the table to use.