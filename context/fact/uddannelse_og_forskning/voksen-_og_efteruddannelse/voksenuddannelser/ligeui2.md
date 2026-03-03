table: fact.ligeui2
description: Ligestillingsindikator for kursusdeltagelse ved voksen og efteruddannelse efter uddannelsesområde, indikator, alder, bopælsområde, enhed, tidsangivelse og tid
measure: indhold (unit -)
columns:
- fuddomr: values [TOT=I alt, H10=H10 Grundskole, H15=H15 Forberedende uddannelser, H20=H20 Gymnasiale uddannelser, H25=H25 Danskundervisning ved sprogcentre, H30=H30 Erhvervsfaglige uddannelser, H35=H35 Adgangsgivende uddannelsesforløb, H39=H39 Arbejdsmarkedsuddannelser, AMU, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser]
- indikator1: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- alder: values [0000=Alder i alt, 25UN=Under 25 år, 2539=25-39 år, 4059=40-59 år, 6099=60 år og derover]
- bopomr: join dim.nuts on bopomr=kode; levels [1, 2, 3]
- overnat1: values [11=Kursister, 13=Årselever]
- tidspunkter: values [22=Skoleår, 11=Kalenderår]
- tid: date range 2005-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- indikator1 is a measurement type selector, not a category to sum across. LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel (procentpoint). Always filter to one indicator. Summing LA1+LA2+LA3 is meaningless.
- overnat1 and tidspunkter are measurement selectors — every combination appears 4 times (2×2). Filter both: e.g. overnat1='11' AND tidspunkter='11'.
- indhold unit is "-" which means percentage (LA1/LA2) or procentpoint (LA3) — never a raw count. These values cannot be summed across fuddomr or bopomr.
- bopomr joins dim.nuts. Same join as veu20: niveau 1=regioner, 2=landsdele, 3=kommuner. bopomr='0' is the national total (not in dim.nuts). Use ColumnValues("nuts", "titel", for_table="ligeui2") to browse available areas.
- fuddomr here is simpler than veu20 — only top-level H-codes (H10, H15, H20, ..., H80) plus TOT. No deep sub-levels in this table.
- Sample query for gender gap in course participation by region (2023, all ages, kursister, kalenderår): SELECT d.titel, f.indhold FROM fact.ligeui2 f JOIN dim.nuts d ON f.bopomr=d.kode WHERE f.indikator1='LA3' AND f.alder='0000' AND f.overnat1='11' AND f.tidspunkter='11' AND f.fuddomr='TOT' AND f.tid='2023-01-01' AND d.niveau=1;
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.