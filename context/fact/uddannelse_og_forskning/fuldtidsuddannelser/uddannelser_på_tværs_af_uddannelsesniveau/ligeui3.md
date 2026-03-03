table: fact.ligeui3
description: Ligestillingsindikator for uddannelsesaktivitet efter uddannelse, indikator, alder, bopælsområde og tid
measure: indhold (unit -)
columns:
- uddannelse: values [TOT=I alt, H10=H10 Grundskole, H15=H15 Forberedende uddannelser, H20=H20 Gymnasiale uddannelser, H29=H29 Erhvervsfaglige grundforløb, H30=H30 Erhvervsfaglige uddannelser, H35=H35 Adgangsgivende uddannelsesforløb, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser]
- indikator1: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- alder: values [TOT=Alder i alt, -5=-5 år, 6=6 år, 7=7 år, 8=8 år ... 36=36 år, 37=37 år, 38=38 år, 39=39 år, 40-=40 år-]
- bopomr: join dim.nuts on bopomr=kode [approx]; levels [1, 3]
- tid: date range 2005-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- indhold is a rate, not a count. Never sum across rows. indikator1: LA1=Mænd (%), LA2=Kvinder (%), LA3=difference (pp). LA1+LA2≈100% and LA3=LA1−LA2.
- Covers all education levels (H10–H80), unlike ligeui6 which is STEM higher-ed only.
- bopomr joins dim.nuts (niveau=1 for 5 regioner, niveau=3 for 99 kommuner). Unmatched: '0'=national total (use directly without join), '998' and '999'=special/unknown (~8,060 each, same gap pattern as uddakt10).
- alder='TOT' for all ages. No fstatus or kon column — rates already represent gender balance across all students.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.