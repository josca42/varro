table: fact.vbbuhv
description: Versionstabel af BBUHV - Overgangstabel for varer mellem udenrigshandel og betalingsbalance efter version, poster, indtægt/udgift, land og tid
measure: indhold (unit Mio. kr.)
columns:
- version: values [V2018M10=9. oktober 2018 (Januar 2015 til august 2018), V2018M11=9. november 2018 (Januar 2018 til september 2018), V2018M12=10. december 2018 (Januar 2018 til oktober 2018), V2019M01=9. januar 2019 (Januar 2018 til november 2018), V2019M02=8. februar 2019 (Januar 2018 til december 2018) ... V2025M09=8. september 2025 (Januar 2025 til juli 2025), V2025M10=9. oktober 2025 (Januar 2025 til august 2025), V2025M11=10. november 2025 (Januar 2025 til september 2025), V2025M12=9. december 2025 (Januar 2025 til oktober 2025), V2026M01=9. januar 2026 (Januar 2025 til november 2025)]
- post: values [1.A.A.1.I=GENERALHANDEL (UHV), 1.A.A.1.II=Bunkring og proviantering, 1.A.A.1.III=Varer købt eller solgt i udlandet i forb. med forarbejdning i udlandet, 1.A.A.1.IV=Øvrige korrektioner, 1.A.A.1.IV.1.A=Øvrige korrektioner, varer der krydser grænsen i forbindelse med forarbejdning i Danmark, 1.A.A.1.IV.1.B=Øvrige korrektioner, varer der krydser grænsen i forbindelse med forarbejdning i udlandet, 1.A.A.1.IV.2=Øvrige korrektioner, returvarer, 1.A.A.1.IV.3=Øvrige korrektioner, varer der krydser grænsen i forbindelse med bygge og anlægsprojekter, 1.A.A.1.IV.4=Øvrige korrektioner, fragt på import (CIFFOB), 1.A.A.1.IV.5=Øvrige korrektioner, andre varer, 1.A.A.2=Merchanting, 1.A.A.3=Ikke monetært guld, 1.A.A=LØBENDE POSTER, VARER (FOB)]
- indudbop: values [K=Løbende indtægter, D=Løbende udgifter]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [2]
- tid: date range 2005-01-01 to 2025-08-01
dim docs: /dim/lande_uht_bb.md

notes:
- version: always filter to one version (use MAX(version) for current data). Version table covering the same reconciliation series as bbuhv — useful for tracking revisions to the CIF→FOB goods adjustment.
- land: only B6 (EU-27), D6 (Extra EU-27), W1 (world total). In older versions, codes B5 and D5 appear — these are outdated EU/non-EU region codes from earlier vintages. Filtering to MAX(version) avoids these old codes.
- post: same 13 correction line items as bbuhv — not a hierarchy, not summable across all posts.
- indudbop: only K and D (no N).
- Same query patterns as bbuhv, with the addition of a WHERE version = (SELECT MAX(version) FROM fact.vbbuhv) filter.