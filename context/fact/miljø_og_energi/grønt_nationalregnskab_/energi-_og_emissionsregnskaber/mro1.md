table: fact.mro1
description: Overgangstabel efter overgangsposter, emissionstype og tid
measure: indhold (unit -)
columns:
- overpost: values [DSTTOTAL=Emissioner fra dansk økonomi (Grønt nationalregnskab) (1), BUNKSUM=Emissioner i udlandet (international transport) (2)=(2.1)+(2.2)+(2.3), BUNKSKIB=Emissioner fra dansk opererede skibe i udlandet (2.1), BUNKFLY=Emissioner fra dansk opererede fly i udlandet (2.2), BUNKLAND=Emissioner fra dansk opererede køretøjer i udlandet (2.3), ANTRANS=Andre forskelle i emissioner fra transport og grænsehandel (3), DKTOTAL=Emissioner fra dansk territorium (UNFCCC/UNECE-opgørelsen) (4=(1)÷(2)÷(3)), LULUCF=Arealanvendelse og skovbrug (LULUCF) (5), TOTLULU=Emissioner fra dansk territorium inklusive LULUCF (6=(4)+(5))]
- emtype8: values [1=Kuldioxid (CO2) inkl. fra afbrænding af biomasse, (1000 ton), 3=Kuldioxid (CO2) ekskl. fra afbrænding af biomasse, (1000 ton), 2=Kuldioxid (CO2) fra afbrænding af biomasse, (1000 ton), 4=Svovldioxid (SO2), (ton), 5=Nitrogenoxider (NOx), (ton), 6=Kulilte (CO), (ton), 7=Ammoniak (NH3), (ton), 8=Lattergas (N2O), (ton), 9=Metan (CH4), (ton), 10=Ikke-metanholdige flygtige organiske forbindelser (NMVOC), (ton), 11=Partikler < 10 µm (PM10), (ton), 12=Partikler < 2,5 µm (PM2,5), (ton)]
- tid: date range 1990-01-01 to 2023-01-01

notes:
- This is a bridge table between the national accounts emissions framework (green national accounts, Danish economy principle) and the territorial UNFCCC/UNECE principle. The overpost column encodes the reconciliation items: DSTTOTAL=national accounts total, DKTOTAL=territorial total, with bunker fuel corrections in between.
- Arithmetic: DKTOTAL (4) = DSTTOTAL (1) minus BUNKSUM (2) minus ANTRANS (3). TOTLULU (6) = DKTOTAL (4) + LULUCF (5). Never sum all overpost values.
- emtype8 encodes pollutant + unit (same as mru1). Units differ across emtype8 — filter to one.
- Use mro2 for greenhouse gases only (in CO2-equivalents, consistent units). Use mro1 for the full range of pollutants.