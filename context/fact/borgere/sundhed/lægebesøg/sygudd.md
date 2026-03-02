table: fact.sygudd
description: Lægebesøg efter nøgletal, ydelsesart, uddannelsesniveau, køn, alder og tid
measure: indhold (unit -)
columns:
- bnogle: values [1000=Kontakter (gennemsnitligt antal pr. person), 1010=Personer med kontakt (pct.)]
- ydelsesart: values [120=I ALT, 130=ALMEN LÆGE I ALT, 140=Almen læge, konsultation, dagtid, 150=Almen læge, konsultation, aften mv., 151=Almen læge, besøg, dagtid ... 270=KIROPRAKTIK, 280=FYSIOTERAPI, 290=FODTERAPI, 300=PSYKOLOGHJÆLP, 320=ØVRIGE YDELSER]
- uddniv: values [UNTOT=Uddannelsesniveau i alt, 03000=Grundskole, 03005=Gymnasiale uddannelser, 03010=Erhvervsfaglige uddannelser, 03015=Korte videregående uddannelser, 03020=Mellemlange videregående uddannelser, 03030=Lange videregående uddannelser, 03040=Ph.d. mv., 03045=Ukendt uddannelsesniveau]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [IALT=Alder i alt, 0-9=0-9 år, 10-17=10-17 år, 18-29=18-29 år, 30-59=30-59 år, 60-=60 år og derover]
- tid: date range 2021-01-01 to 2024-01-01
notes:
- bnogle is a measurement selector — each row exists twice, once per bnogle value (1000=average contacts per person, 1010=% of persons with any contact). These are independent metrics; never aggregate across bnogle values.
- ydelsesart is hierarchical (120=I ALT grand total). Filter to ydelsesart=120 for all-visit totals; do not sum all ydelsesart values.
- No regional breakdown — national-level statistics only. Only available from 2021.
- alder uses broad age bands (0-9, 10-17, 18-29, 30-59, 60+) plus IALT.
