table: fact.mru1
description: Emissionsregnskab efter branche, emissionstype og tid
measure: indhold (unit -)
columns:
- branche: values [MTOT=I alt, MHUSHOLD=Husholdninger, MV=Brancher i alt, VA=A Landbrug, skovbrug og fiskeri, V01000=01000 Landbrug og gartneri ... V96000=96000 Frisører, vaskerier og andre serviceydelser, V960000=960000 Frisører, vaskerier og andre serviceydelser, VSB=SB Private husholdninger med ansat medhjælp, V97000=97000 Private husholdninger med ansat medhjælp, V970000=970000 Private husholdninger med ansat medhjælp]
- emtype8: values [1=Kuldioxid (CO2) inkl. fra afbrænding af biomasse, (1000 ton), 3=Kuldioxid (CO2) ekskl. fra afbrænding af biomasse, (1000 ton), 2=Kuldioxid (CO2) fra afbrænding af biomasse, (1000 ton), 4=Svovldioxid (SO2), (ton), 5=Nitrogenoxider (NOx), (ton), 6=Kulilte (CO), (ton), 7=Ammoniak (NH3), (ton), 8=Lattergas (N2O), (ton), 9=Metan (CH4), (ton), 10=Ikke-metanholdige flygtige organiske forbindelser (NMVOC), (ton), 11=Partikler < 10 µm (PM10), (ton), 12=Partikler < 2,5 µm (PM2,5), (ton), 13=Svovlhexafluorid (SF6), (tons CO2-ækvivalenter), 14=Perfluorcarboner (PFC), (tons CO2-ækvivalenter), 15=Hydrofluorcarboner (HFC), (tons CO2-ækvivalenter)]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- emtype8 encodes both the pollutant and its unit in the label (CO2 in 1000 ton, SO2/NOx/NH3 in ton, SF6/PFC/HFC in ton CO2-equivalents). Units are incompatible across emtype8 codes — always filter to one emtype8 when aggregating.
- CO2 relationship: emtype8=1 (CO2 incl. biomass) = emtype8=2 (CO2 from biomass) + emtype8=3 (CO2 excl. biomass). Use emtype8=3 for the standard national accounts CO2 figure.
- branche: V-prefix convention. MTOT=total, MHUSHOLD=households, MV=all sectors. V-prefixed codes span multiple NACE hierarchy levels — filter to one to avoid double-counting.
- Broadest emissions table (15 pollutants including GHGs, acidification, particles). For greenhouse gases in CO2-equivalents only, use drivhus or drivhus2.