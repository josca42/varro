table: fact.ligedi11
description: Ligestillingsindikator for bestyrelsesmedlemmer og direktører efter indikator, type, uddannelse, alder og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- type: values [20=Bestyrelse, 30=Direktører]
- uddannelse: values [TOT=I alt uddannelser, H10=Grundskole, H20=Gymnasiale uddannelser mv., H30=Erhvervsfaglige uddannelser, H40=Korte videregående uddannelser, H5060=Mellemlange videregående- og bacheloruddannelser, H70=Lange videregående uddannelser mv., H90=Uoplyst]
- alder: values [IALT=Alder i alt, U20=Under 20 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 70OV=70 år og derover, UK=Ukendt alder]
- tid: date range 2019-01-01 to 2023-01-01

notes:
- indhold is a percentage or procentpoint, NOT a count. LA1=share of men (pct), LA2=share of women (pct), LA3=difference men–women (procentpoint). Never sum indhold across indikator rows.
- Each indikator is an independent rate — select the one you need (e.g. WHERE indikator='LA2' for female share).
- type only has 20=Bestyrelse and 30=Direktører — there is no "I alt" type for these tables.
- For a simple gender-gap lookup: SELECT type, indhold FROM fact.ligedi11 WHERE indikator='LA3' AND uddannelse='TOT' AND alder='IALT' AND tid='2023-01-01'.