table: fact.emm1mu2n
description: Direkte og indirekte luftemissioner efter anvendelse, emissionstype, multiplikator, prisenhed og tid
measure: indhold (unit -)
columns:
- anvend1: values [ACPT=Husholdningernes forbrugsudgifter (Anvendelse), ACPA=A Fødevarer mv. - (Anvendelse), ACPB=B Drikkevarer og tobak mv. - (Anvendelse), ACPC=C Beklædning og fodtøj - (Anvendelse), ACPD=D Boligbenyttelse - (Anvendelse) ... ABI5150=Investering i ændring i dyrkede aktiver - (Anvendelse), ABI517P=Intellektuelle rettigheder - (Anvendelse), AL5200=Lagre - (Anvendelse), AV5300=Værdigenstande - (Anvendelse), AE6000=Eksport - (Anvendelse)]
- emtype8: values [1=Kuldioxid (CO2) inkl. fra afbrænding af biomasse, (1000 ton), 3=Kuldioxid (CO2) ekskl. fra afbrænding af biomasse, (1000 ton), 2=Kuldioxid (CO2) fra afbrænding af biomasse, (1000 ton), 4=Svovldioxid (SO2), (ton), 5=Nitrogenoxider (NOx), (ton), 6=Kulilte (CO), (ton), 7=Ammoniak (NH3), (ton), 8=Lattergas (N2O), (ton), 9=Metan (CH4), (ton), 10=Ikke-metanholdige flygtige organiske forbindelser (NMVOC), (ton), 11=Partikler < 10 µm (PM10), (ton), 12=Partikler < 2,5 µm (PM2,5), (ton), 13=Svovlhexafluorid (SF6), (tons CO2-ækvivalenter), 14=Perfluorcarboner (PFC), (tons CO2-ækvivalenter), 15=Hydrofluorcarboner (HFC), (tons CO2-ækvivalenter)]
- mult: values [EMMDIREA=Direkte luftemissioner efter endelig anvendelse, EMMINTEA=Direkte og indirekte luftemissioner efter endelig anvendelse, EMMMULEA=Direkte og indirekte luftemissioner efter endelig anvendelse (multiplikator), (vægtenhed pr. mio. kr.)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- anvend1 is final demand by use category (same ACP* structure as ene2mu2n). ACPT=total household consumption; ACP* sub-codes are COICOP categories — don't mix with ACPT.
- emtype8: 15 pollutants with embedded units in labels. Filter to one emtype8 — units are incompatible across codes.
- mult is a measurement-type selector — every anvend1 × emtype8 × prisenhed appears 3×: EMMDIREA=direct emissions (weight), EMMINTEA=direct+indirect (weight), EMMMULEA=multiplier (weight/mio.kr.). Never SUM across mult.
- prisenhed: filter to one.
- No dim join — anvend1 is inline-coded. Emissions equivalent of ene2mu2n.