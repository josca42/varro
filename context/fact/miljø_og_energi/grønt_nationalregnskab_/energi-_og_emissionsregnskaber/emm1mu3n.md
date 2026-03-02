table: fact.emm1mu3n
description: Direkte og indirekte luftemissioner efter branche, emissionstype, årsag, prisenhed og tid
measure: indhold (unit -)
columns:
- branche: join dim.nr_branche on branche=kode [approx]
- emtype8: values [1=Kuldioxid (CO2) inkl. fra afbrænding af biomasse, (1000 ton), 3=Kuldioxid (CO2) ekskl. fra afbrænding af biomasse, (1000 ton), 2=Kuldioxid (CO2) fra afbrænding af biomasse, (1000 ton), 4=Svovldioxid (SO2), (ton), 5=Nitrogenoxider (NOx), (ton), 6=Kulilte (CO), (ton), 7=Ammoniak (NH3), (ton), 8=Lattergas (N2O), (ton), 9=Metan (CH4), (ton), 10=Ikke-metanholdige flygtige organiske forbindelser (NMVOC), (ton), 11=Partikler < 10 µm (PM10), (ton), 12=Partikler < 2,5 µm (PM2,5), (ton), 13=Svovlhexafluorid (SF6), (tons CO2-ækvivalenter), 14=Perfluorcarboner (PFC), (tons CO2-ækvivalenter), 15=Hydrofluorcarboner (HFC), (tons CO2-ækvivalenter)]
- affaldsopr: values [ACPT=Husholdningernes forbrugsudgifter (Anvendelse), ACPA=A Fødevarer mv. - (Anvendelse), ACPB=B Drikkevarer og tobak mv. - (Anvendelse), ACPC=C Beklædning og fodtøj - (Anvendelse), ACPD=D Boligbenyttelse - (Anvendelse) ... ABI5150=Investering i ændring i dyrkede aktiver - (Anvendelse), ABI517P=Intellektuelle rettigheder - (Anvendelse), AL5200=Lagre - (Anvendelse), AV5300=Værdigenstande - (Anvendelse), AE6000=Eksport - (Anvendelse)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1990-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md

notes:
- branche joins dim.nr_branche using: REPLACE(REPLACE(f.branche, 'V', ''), '_', '-') = TRIM(d.kode). 'V' alone has no dim match.
- affaldsopr contains final demand categories (same ACP* structure as emm1mu2n.anvend1 and ene2mu3n.affaldsopr) — shows which final demand drives emissions in each sector.
- emtype8: 15 pollutants with mixed units — filter to one.
- prisenhed: selector (V=current, LAN=2020). Filter to one.
- No mult column — indhold unit varies by context. Ends at 2023 (emm1mu1n goes to 2024). Emissions equivalent of ene2mu3n. Use for branche × final-demand emission attribution.