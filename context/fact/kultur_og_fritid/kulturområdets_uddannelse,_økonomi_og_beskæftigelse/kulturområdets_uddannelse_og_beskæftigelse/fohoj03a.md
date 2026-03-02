table: fact.fohoj03a
description: Antallet af højskolekursister på korte kurser efter køn, alder, højest fuldførte uddannelse, enhed, tidsangivelse og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, -17=Under 18 år, 1829=18-29 år, 3049=30-49 år, 5069=50-69 år, 7079=70-79 år, 8099=80 år og derover]
- hfudd2: values [TOT=I alt, H10=H10 Grundskole, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H35=H35 Adgangsgivende uddannelsesforløb, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser, H90=H90 Uoplyst mv.]
- enhed: values [11=Kursister, 13=Årselever]
- tidspunkter: values [22=Skoleår, 11=Kalenderår]
- tid: date range 2016-01-01 to 2024-01-01
notes:
- CRITICAL: enhed and tidspunkter are both measurement selectors. Always filter both to a single value.
- Covers only short courses (korte kurser) — no medium or long courses.
- hfudd2=TOT is the total. Education level of the individual (not family, unlike fohoj02a).
- kon=TOT and alder=TOT are totals. Filter unused dimensions.
- Age groups here are broader than fohoj02a: 6 bands (Under 18, 18-29, 30-49, 50-69, 70-79, 80+).
