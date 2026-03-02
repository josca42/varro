table: fact.ligeui5
description: Ligestillingsindikator for frafald inden for 5 år efter startuddannelse i gruppen, indikator, alder, herkomst og tid
measure: indhold (unit -)
columns:
- startud: values [TOT=I alt, H21=H21 Gymnasiale uddannelser, H31=H31 Erhvervsfaglige uddannelser, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser]
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- alerams: values [TOT=Alder i alt, -14=Under 15 år, 15=15 år, 16=16 år, 17=17 år ... 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-=50- år]
- herkomst: values [0=I alt, 10=Personer med dansk oprindelse, 21=Indvandrere i alt, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 31=Efterkommere i alt, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande, 0=Uoplyst herkomst]
- tid: date range 2008-01-01 to 2019-01-01

notes:
- indikator encodes gender as dropout rates: LA1=Mænd frafald (%), LA2=Kvinder frafald (%), LA3=Forskel (mænd minus kvinder, procentpoint). indhold is a percentage — never SUM across rows. The three indikator values are not additive. To get the gender gap, just read LA3 directly; LA3 ≠ LA1−LA2 for small samples due to statistical treatment of small cells.
- There is no kon column — gender is represented through indikator. To compare men vs women, pivot on indikator rather than filtering kon.
- alerams is the age column (same codes as startald in genmf10/ligeub5: TOT, -14, 15–29 individual years, 30-34, 35-39, 40-44, 45-49, 50-). Note: column is named alerams here, not startald.
- herkomst same coding as ligeub5: 0=I alt, 10=dansk, 21=Indvandrere i alt, 24/25=vestlige/ikke-vestlige, 31=Efterkommere, 34/35=vestlige/ikke-vestlige.
- startud same top-level codes as ligeub5 (TOT + H21–H80, no sub-levels).
- Only covers 2008–2019. For current data (up to 2024) you need genmf10/ligeub5 and compute gender rates yourself.
- DATA QUALITY: ~4k duplicate rows with different indhold values (39k rows, 35k distinct keys). Always use MAX(indhold) or AVG(indhold) when aggregating.