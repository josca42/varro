table: fact.ibib3
description: Udlån og lånere efter område, udlånssted, højest fuldførte uddannelse, kategori og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- udlanssted: values [9000=Samlet udlån, 9005=Folkebibliotekerne, 9010=eReolen]
- hfudd: values [TOT=I alt, H10=H10 Grundskole, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, 900=Ingen eller uoplyst]
- dyrkat: values [9015=Udlån, 9020=Lånere, 9025=Personer i befolkningen]
- tid: date range 2020-01-01 to 2025-04-01
dim docs: /dim/nuts.md
notes:
- Same structure as ibib1 but with hfudd (highest completed education) instead of kon. omrade at all 3 nuts levels + omrade=0.
- hfudd: TOT=I alt, H10–H70 (standard Danish education levels), 900=Ingen eller uoplyst. Filter to TOT to avoid double-counting.
- udlanssted and dyrkat must each be filtered — same rules as ibib1.
- ibib3 (to 2025) vs ibib3a (archive, to 2024).
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
