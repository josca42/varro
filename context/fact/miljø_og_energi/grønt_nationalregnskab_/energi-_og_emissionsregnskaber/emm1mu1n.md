table: fact.emm1mu1n
description: Direkte og indirekte luftemissioner efter branche, emissionstype, multiplikator, prisenhed og tid
measure: indhold (unit -)
columns:
- branche: join dim.nr_branche on branche=kode [approx]
- emtype8: values [1=Kuldioxid (CO2) inkl. fra afbrænding af biomasse, (1000 ton), 3=Kuldioxid (CO2) ekskl. fra afbrænding af biomasse, (1000 ton), 2=Kuldioxid (CO2) fra afbrænding af biomasse, (1000 ton), 4=Svovldioxid (SO2), (ton), 5=Nitrogenoxider (NOx), (ton), 6=Kulilte (CO), (ton), 7=Ammoniak (NH3), (ton), 8=Lattergas (N2O), (ton), 9=Metan (CH4), (ton), 10=Ikke-metanholdige flygtige organiske forbindelser (NMVOC), (ton), 11=Partikler < 10 µm (PM10), (ton), 12=Partikler < 2,5 µm (PM2,5), (ton), 13=Svovlhexafluorid (SF6), (tons CO2-ækvivalenter), 14=Perfluorcarboner (PFC), (tons CO2-ækvivalenter), 15=Hydrofluorcarboner (HFC), (tons CO2-ækvivalenter)]
- mult: values [EMMDIR=Direkte luftemissioner, EMMINT=Direkte krav til luftemissioner (emissionsintensitet), (vægtenhed pr. mio. kr.), EMMMUL=Direkte og indirekte krav til luftemissioner (multiplikator), (vægtenhed pr. mio. kr.)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1990-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- branche joins dim.nr_branche using: REPLACE(REPLACE(f.branche, 'V', ''), '_', '-') = TRIM(d.kode). 'V' alone (total of all sectors) has no dim match.
- emtype8 encodes pollutant + unit (same 15-code scheme as mru1). Units differ across emtype8 — filter to one when aggregating.
- mult is a measurement-type selector — each branche × emtype8 × prisenhed appears 3×: EMMDIR=direct emissions (in weight unit), EMMINT=emission intensity (weight/mio.kr.), EMMMUL=multiplier incl. indirect (weight/mio.kr.). Never SUM across mult.
- prisenhed: filter to one (V=current prices, LAN=2020). Same note as ene2mu1n: for absolute emissions (EMMDIR) prisenhed only affects denominator in intensity/multiplier measures.
- Emissions equivalent of ene2mu1n. Use ColumnValues("nr_branche", "titel", for_table="emm1mu1n") to see branches.