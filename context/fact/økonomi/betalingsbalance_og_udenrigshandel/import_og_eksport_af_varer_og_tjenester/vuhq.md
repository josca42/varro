table: fact.vuhq
description: Versionstabel af UHQ - Udenrigshandel kvartalsvis efter version, poster, im- og eksport, land, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- version: values [V2021M12=9. december 2021 (Januar 2021 til oktober 2021), V2022M01=10. januar 2022 (Januar 2021 til november 2021), V2022M02=8. februar 2022 (Januar 2021 til december 2021), V2022M03=11. marts 2022 (Januar 2021 til januar 2022), V2022M04=11. april 2022 (Januar 2021 til februar 2022) ... V2025M09=8. september 2025 (Januar 2025 til juli 2025), V2025M10=9. oktober 2025 (Januar 2025 til august 2025), V2025M11=10. november 2025 (Januar 2025 til september 2025), V2025M12=9. december 2025 (Januar 2025 til oktober 2025), V2026M01=9. januar 2026 (Januar 2025 til november 2025)]
- post: values [1.A=VARER OG TJENESTER, 1.A.A=VARER, 1.A.A.1.Z=VARER DER KRYDSER DANSK GRÆNSE, 1.A.A.1.0-4X2-3=Næringsmidler, drikkevarer, tobak mv., 1.A.A.1.2=Råstoffer, ikke spiselige, undt. brændsel ... 1.A.B.8=Royalties og licenser, 1.A.B.9=Telekommunikation, computer- og informationstjenester, 1.A.B.10=Andre forretningstjenester, 1.A.B.11=Audiovisuelle tjenester samt tjenester ifm. uddannelse, sundhed, kultur og rekreation, 1.A.B.12=Offentlige tjenester]
- indud: values [1=Import, 2=Eksport]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [2, 3, 4]
- saeson: values [1=Ikke sæsonkorrigeret, 2=Sæsonkorrigeret]
- tid: date range 2010-01-01 to 2025-07-01
dim docs: /dim/lande_uht_bb.md

notes:
- This is a revision-tracking table. It holds 50 versions (monthly publication releases from Dec 2021 to Jan 2026), each covering a different time window. Use this table only when comparing how estimates changed across publication vintages — not for current trade data (use uhq instead).
- version codes are in the form V{year}M{month} (e.g. V2024M03 = the March 2024 publication). Each version covers a rolling window of quarters; the version column description text states the covered period. Always filter to a single version when analysing a specific publication's data.
- Same post hierarchy as uhq — filter to a single post level to avoid double-counting.
- land: 80% of codes match dim.lande_uht_bb. Unmatched: W1 (Verden/world total), I9/J8/J9/P4/P7 (service-only aggregate regions, 1.A.B.* posts only). More unmatched codes than uhq due to additional groupings present in certain version vintages.
- saeson must be filtered — same gotcha as uhq.
- Typical use: `WHERE version = 'V2024M09' AND saeson = 1 AND post = '1.A'` to get a specific quarterly publication snapshot.