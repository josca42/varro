table: fact.vbbq
description: Versionstabel af BBQ - Betalingsbalancen kvartalsvis efter version, poster, indtægt/udgift, land og tid
measure: indhold (unit Mio. kr.)
columns:
- version: values [V2021M12=9. december 2021 (Januar 2021 til oktober 2021), V2022M01=10. januar 2022 (Januar 2021 til november 2021), V2022M02=8. februar 2022 (Januar 2021 til december 2021), V2022M03=11. marts 2022 (Januar 2021 til januar 2022), V2022M04=11. april 2022 (Januar 2021 til februar 2022) ... V2025M09_LIGHT=23. september 2025 (Januar 2023 til juli 2025), V2025M10=9. oktober 2025 (Januar 2025 til august 2025), V2025M11=10. november 2025 (Januar 2025 til september 2025), V2025M12=9. december 2025 (Januar 2025 til oktober 2025), V2026M01=9. januar 2026 (Januar 2025 til november 2025)]
- post: values [1=BETALINGSBALANCENS LØBENDE POSTER, 1.A=VARER OG TJENESTER, 1.A.A=VARER, 1.A.A.1.Z=VARER DER KRYDSER DANSK GRÆNSE, 1.A.A.1.Q=VARER DER IKKE KRYDSER DANSK GRÆNSE ... 1.C.0.6=Løbende overførsler, andre overførsler, 2=Kapitaloverførsler mv., NF=Nettofordringserhvervelsen, 3=FINANSIELLE POSTER I ALT, 4.5=FEJL OG UDELADELSER]
- indudbop: values [K=Løbende indtægter, D=Løbende udgifter, N=Nettoindtægter]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [2, 3, 4]
- tid: date range 2005-01-01 to 2025-07-01
dim docs: /dim/lande_uht_bb.md

notes:
- version: always filter to one version. Use MAX(version) for current data. Without filtering, rows are repeated once per version. The version table is useful for revision analysis — comparing how an estimate evolved across monthly releases.
- land spans niveau 2, 3, and 4 (wider range than bbq). Filter WHERE d.niveau = 4 for country detail to avoid double-counting hierarchy levels. Unmatched land codes: I9, J8, J9, P4, P7, W1 — these are aggregate groupings not in the dim hierarchy.
- post is hierarchical — same structure as bbq. Filter to a single post code.
- indudbop: N = K − D. Filter to one value.
- Use ColumnValues("lande_uht_bb", "titel", for_table="vbbq") to see the matched land codes available.