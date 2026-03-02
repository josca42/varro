table: fact.vbbm
description: Versionstabel af BBM - Betalingsbalancen månedlig efter version, poster, indtægt/udgift, land, enhed, sæsonkorrigering og tid
measure: indhold (unit -)
columns:
- version: values [V2021M12=9. december 2021 (Januar 2021 til oktober 2021), V2022M01=10. januar 2022 (Januar 2021 til november 2021), V2022M02=8. februar 2022 (Januar 2021 til december 2021), V2022M03=11. marts 2022 (Januar 2021 til januar 2022), V2022M04=11. april 2022 (Januar 2021 til februar 2022) ... V2025M09_LIGHT=23. september 2025 (Januar 2023 til juli 2025), V2025M10=9. oktober 2025 (Januar 2025 til august 2025), V2025M11=10. november 2025 (Januar 2025 til september 2025), V2025M12=9. december 2025 (Januar 2025 til oktober 2025), V2026M01=9. januar 2026 (Januar 2025 til november 2025)]
- post: values [1=BETALINGSBALANCENS LØBENDE POSTER, 1.A=VARER OG TJENESTER, 1.A.A=VARER, 1.A.A.1.Z=VARER DER KRYDSER DANSK GRÆNSE, 1.A.A.1.Q=VARER DER IKKE KRYDSER DANSK GRÆNSE, 1.A.B=TJENESTER, 1.B=INDKOMST, 1.C=LØBENDE OVERFØRSLER, 2=Kapitaloverførsler mv., NF=Nettofordringserhvervelsen, 3=FINANSIELLE POSTER I ALT, 4.5=FEJL OG UDELADELSER]
- indudbop: values [K=Løbende indtægter, D=Løbende udgifter, N=Nettoindtægter]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [2]
- enhed: values [93=Millioner kroner, 100=Procentvis udvikling (måned), 101=Procentvis udvikling (3 måneder), 102=Procentvis udvikling (år)]
- saeson: values [1=Ikke sæsonkorrigeret, 2=Sæsonkorrigeret]
- tid: date range 2005-01-01 to 2025-08-01
dim docs: /dim/lande_uht_bb.md

notes:
- version: always filter to one version. MAX(version) = latest release. The table contains many overlapping versions (rolling monthly releases); without filtering, each fact row is repeated once per version.
- enhed is a critical measurement-type selector: 93=Mio. kr. (absolute), 100=% ændring måned, 101=% ændring 3 måneder, 102=% ændring år. All four repeat every combination — forgetting to filter enhed quadruples all sums. Always filter, e.g. WHERE enhed = 93 for monetary values.
- saeson doubles rows: 1=Ikke sæsonkorrigeret, 2=Sæsonkorrigeret. Always filter to one. For trend analysis use 2; for point-in-time values use 1.
- indudbop: N = K − D (netto = løbende indtægter minus løbende udgifter). Never sum all three. Filter to indudbop='N' for net balance or 'K'/'D' for income/expenditure separately.
- post is hierarchical — parent posts are sums of children. '1' = BETALINGSBALANCENS LØBENDE POSTER (sum of 1.A + 1.B + 1.C). Summing across all post values massively overcounts. Filter to a specific post or filter to leaf-level posts only.
- land: only 3 distinct values in this table: B6 (EU-27 uden GB), D6 (Extra EU-27), W1 (alle lande). W1 is not in dim.lande_uht_bb — it is the world total aggregate. For total Denmark figures use land='W1'. No country-level breakdown is available in vbbm.
- A minimal correct query: SELECT SUM(indhold) FROM fact.vbbm WHERE version=MAX(version) AND enhed=93 AND saeson=1 AND indudbop='N' AND post='1' AND land='W1' AND tid='2025-01-01'