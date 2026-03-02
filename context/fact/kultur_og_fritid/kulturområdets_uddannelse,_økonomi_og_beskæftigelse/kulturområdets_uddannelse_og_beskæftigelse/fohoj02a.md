table: fact.fohoj02a
description: Antallet af højskolekursister på mellemlange og lange kurser efter køn, alder, højest fuldførte uddannelse i familien, enhed, tidsangivelse og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, -17=Under 18 år, 1821=18-21 år, 2225=22-25 år, 2629=26-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- hoej_udd_fam: values [TOT=I alt, 10=10 GRUNDSKOLE                                               , 26=20+25 GYMNASIALE UDDANNELSER, 35=35 ERHVERVSUDDANNELSER, 40=40 KORTE VIDEREGÅENDE UDDANNELSER                           , 61=50+60 MELLEMLANGE VIDEREGÅENDE UDDANNELSER INKL. BACHELOR, 65=65 LANGE VIDEREGÅENDE UDDANNELSER                           , 9=Uoplyst]
- enhed: values [11=Kursister, 13=Årselever]
- tidspunkter: values [22=Skoleår, 11=Kalenderår]
- tid: date range 2016-01-01 to 2024-01-01
notes:
- CRITICAL: enhed and tidspunkter are both measurement selectors. Always filter both to a single value.
- Covers only medium and long courses (mellemlange og lange kurser) — no short courses.
- hoej_udd_fam=TOT is the total. Note: values have trailing spaces in some codes (e.g., "10 GRUNDSKOLE   ") — trim when filtering.
- kon=TOT and alder=TOT are totals. Filter unused dimensions.
- For short-course demographic detail by education, use fohoj03a (individual education level, not family).
