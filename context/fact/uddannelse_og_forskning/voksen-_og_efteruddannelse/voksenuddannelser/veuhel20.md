table: fact.veuhel20
description: Personer der har fuldført en hel voksenuddannelse efter uddannelse, køn, højest fuldførte uddannelse, tidsangivelse og tid
measure: indhold (unit Antal)
columns:
- uddannelse: values [TOT=I alt, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- hfudd: values [TOT=I alt, H10=H10 Grundskole, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H90=H90 Uoplyst mv.]
- tidspunkter: values [22=Skoleår, 11=Kalenderår]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- tidspunkter is a measurement selector — every row exists twice. Always filter to one value. For multi-year programs (H40, H50, H60, H70) skoleår and kalenderår counts differ materially; for H20 they are the same.
- hfudd is the prior highest completed education (background variable), using the same H-codes as uddannelse. Useful for cross-tabulating what people completed (uddannelse) against what they already had (hfudd). TOT covers all prior education levels.
- uddannelse and hfudd both have only top-level codes — no sub-level overcounting risk.
- No alder or herkomst breakdown (unlike veuhel10). Use veuhel10 if you need age or herkomst; use veuhel20 if you need prior education level.