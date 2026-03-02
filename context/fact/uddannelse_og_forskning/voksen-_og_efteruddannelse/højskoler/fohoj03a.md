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
- `enhed` and `tidspunkter` are measurement selectors — filter both to avoid doubling. Both are smallint.
- `alder` total code is `'TOT'`. Age groups are broader than other fohoj tables to capture older demographics: `-17`, `1829`, `3049`, `5069`, `7079`, `8099`.
- `hfudd2` is the individual's own highest completed education (H10–H90 scale). This differs from fohoj02a's `hoej_udd_fam` (family education). H90=Uoplyst mv.
- Only covers korte kurser. For mellemlange og lange kurser with education breakdown, use fohoj02a.