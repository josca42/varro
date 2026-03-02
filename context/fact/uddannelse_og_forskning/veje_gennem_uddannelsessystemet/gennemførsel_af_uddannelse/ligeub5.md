table: fact.ligeub5
description: Gennemførsel af uddannelsesgrupper efter startuddannelse i gruppen, herkomst, køn, status ved 1 og 5 år, alder ved start på gruppe og tid
measure: indhold (unit Antal)
columns:
- startud: values [TOT=I alt, H21=H21 Gymnasiale uddannelser, H31=H31 Erhvervsfaglige uddannelser, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser]
- herkomst: values [0=I alt, 10=Personer med dansk oprindelse, 21=Indvandrere i alt, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 31=Efterkommere i alt, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande, 0=Uoplyst herkomst]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- stat: values [TOT=I alt, 0=I gang i gruppen efter 1 år, 1=Fuldført i gruppen inden for 1 år, 2=Bestået deleksamen inden for 1 år, 3=Tidligt afbrud i gruppen inden for 1 år, 4=Ingen 1-årsstatus, 5=I gang i gruppen efter 5 år, 6=Fuldført i gruppen inden for 5 år, 7=Frafald i gruppen inden for 5 år, 8=Ingen 5-årsstatus]
- startald: values [TOT=Alder i alt, -14=Under 15 år, 15=15 år, 16=16 år, 17=17 år ... 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-=50- år]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- stat semantics are identical to genmf10: 1-year statuses (0–4) and 5-year statuses (5–8) each independently sum to TOT. Never sum all stat values together. Use stat='TOT' for cohort size.
- startud only has top-level codes (TOT + H21–H80, 8 values total). No sub-level breakdown unlike genmf10. ColumnValues("ligeub5", "startud") shows all 8 codes.
- herkomst total is '0' (integer), not 'TOT'. More detailed than genmf10: 0=I alt, 10=dansk oprindelse, 21=Indvandrere i alt, 24=vestlige indvandrere, 25=ikke-vestlige indvandrere, 31=Efterkommere i alt, 34=vestlige efterkommere, 35=ikke-vestlige efterkommere. Use ligeub5 when western/non-western distinction matters.
- kon total is 'TOT' (not '10' as in genmf10). Values: TOT=I alt, M=Mænd, K=Kvinder.
- DATA QUALITY: ligeub5 has ~35k duplicate rows with conflicting indhold values (358k rows but only 323k distinct keys). Always aggregate: SELECT startud, MAX(indhold) or AVG(indhold) rather than raw SELECT. Simple GROUP BY on all dimension columns plus MAX(indhold) will deduplicate safely.