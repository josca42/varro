table: fact.veuhel10
description: Personer der har fuldført en hel voksenuddannelse efter uddannelse, alder, køn, herkomst, tidsangivelse og tid
measure: indhold (unit Antal)
columns:
- uddannelse: values [TOT=I alt, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU]
- alder: values [0000=Alder i alt, 9920=Under 20 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6099=60 år og derover]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- herkams: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- tidspunkter: values [22=Skoleår, 11=Kalenderår]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- tidspunkter is a measurement selector — every row exists twice (skoleår and kalenderår). Always filter to one: tidspunkter='11' for kalenderår or tidspunkter='22' for skoleår. For multi-year programs (H40 KVU, H50 MVU, H60 BACH, H70 LVU) the two counts differ meaningfully; for H20 (gymnasiale) they are identical.
- alder total code is '0' (not '0000' — note the difference from veu20). Filter alder='0' for all ages.
- herkams categories (5=dansk oprindelse, 4=indvandrere, 3=efterkommere, 0=uoplyst) plus TOT. These are mutually exclusive; summing 5+4+3+0 ≈ TOT.
- uddannelse has only top-level codes (H20–H70) plus TOT. No sub-levels — no overcounting risk within uddannelse.