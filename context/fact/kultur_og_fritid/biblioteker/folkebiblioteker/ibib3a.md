table: fact.ibib3a
description: Udlån og lånere efter område, udlånssted, højest fuldførte uddannelse, kategori og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- udlanssted: values [9000=Samlet udlån, 9005=Folkebibliotekerne, 9010=eReolen]
- hfudd: values [TOT=I alt, H10=H10 Grundskole, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, 900=Ingen eller uoplyst]
- dyrkat: values [9015=Udlån, 9020=Lånere, 9025=Personer i befolkningen]
- tid: date range 2020-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Archive version of ibib3 (education breakdown) — only to 2024. See ibib3.md for full notes.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
