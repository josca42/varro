table: fact.fstrib3a
description: Filmstribens udlån og lånere efter kommune, højest fuldførte uddannelse, kategori og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [1, 2, 3]
- hfudd2: values [TOT=I alt, H10=H10 Grundskole, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, 900=Ingen eller uoplyst]
- misbrug2: values [9015=Udlån, 9020=Lånere, 9025=Personer i befolkningen]
- tid: date range 2024-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Archive version of fstrib3 (Filmstriben, education breakdown) — only 2024. See fstrib3.md for full notes.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on kommunedk=dim_kode. Exclude kommunedk=0.
