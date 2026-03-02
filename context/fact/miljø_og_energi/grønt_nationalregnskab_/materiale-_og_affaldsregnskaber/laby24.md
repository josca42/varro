table: fact.laby24
description: Husholdningsaffald efter kommunegruppe, behandlingsform, affaldsfraktion og tid
measure: indhold (unit Ton)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1, 2]
- behandling: values [TOT=I alt, GENANV=Genanvendelse, inkl. anden endelig materialenyttiggørelse, FORBRND=Forbrænding, DEPOT=Deponering]
- afffrak: values [TOTHHAFFALD=HUSHOLDNINGSAFFALD I ALT, A=DAGRENOVATION OG LIGNENDE, B=ORGANISK AFFALD, INKL. HAVEAFFALD, C=FORBRÆNDINGSEGNET AFFALD, D=PAPIR OG PAP, I=MADAFFALD, F=GLAS, INKL EMBALLAGE, G=JERN OG METAL, INKL EMBALLAGE, H=PLAST OG DÆK, J=ELEKTRONIK, BATTERIER, MV., X=ØVRIGT AFFALD]
- tid: date range 2013-01-01 to 2022-01-01
dim docs: /dim/kommunegrupper.md
notes:
- komgrp joins dim.kommunegrupper (99% match). Use: JOIN dim.kommunegrupper d ON f.komgrp = d.kode.
- komgrp=0 is an aggregate total not present in the dim table — handle separately or exclude when joining.
- niveau 1 = 5 kommunegrupper (Hovedstads-, Storby-, Provinsby-, Oplands-, Landkommuner), kode 1–5. niveau 2 = 99 individual municipalities. Filter WHERE d.niveau=1 for group-level analysis, niveau=2 for municipality-level.
- behandling has TOT + GENANV/FORBRND/DEPOT — filter to one to avoid double-counting.
- afffrak covers household waste fractions only (TOTHHAFFALD + 10 categories A–X). Not the full fraction list from the affald tables.
- Use laby25 for per-capita kg and recycling rate (%) by kommunegruppe.
- Map: context/geo/kommuner.parquet — filter dim.kommunegrupper to niveau=2, then merge on komgrp=dim_kode. Exclude komgrp=0.
