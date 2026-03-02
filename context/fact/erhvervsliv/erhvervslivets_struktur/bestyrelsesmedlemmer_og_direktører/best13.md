table: fact.best13
description: Bestyrelsesmedlemmer og direktører efter type, virksomhedsstørrelse, uddannelse og tid
measure: indhold (unit Antal)
columns:
- type: values [10=I alt, 20=Bestyrelse, 30=Direktører, 40=Uoplyst]
- virkstr: values [3001=I alt, 3005=Ingen ansatte, 3010=Under 10 årsværk, 3020=10-49 årsværk, 3030=50-249 årsværk, 3040=250 årsværk og derover]
- uddannelse: values [TOT=I alt uddannelser, H10=Grundskole, H20=Gymnasiale uddannelser mv., H30=Erhvervsfaglige uddannelser, H40=Korte videregående uddannelser, H5060=Mellemlange videregående- og bacheloruddannelser, H70=Lange videregående uddannelser mv., H90=Uoplyst]
- tid: date range 2019-01-01 to 2023-01-01

notes:
- All columns have total rows: type='10', virkstr='3001', uddannelse='TOT'. Filter all non-target dimensions to their total to avoid overcounting.
- uddannelse='H90' (Uoplyst) is included in TOT. Exclude it if you want only known education levels.