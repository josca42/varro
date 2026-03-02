table: fact.best11
description: Bestyrelsesmedlemmer og direktører efter type, køn, uddannelse, alder, bopælsområde og tid
measure: indhold (unit Antal)
columns:
- type: values [10=I alt, 20=Bestyrelse, 30=Direktører, 40=Uoplyst]
- kon: values [100=Køn i alt, 200=Mænd, 300=Kvinder, 400=Uoplyst køn]
- uddannelse: values [TOT=I alt uddannelser, H10=Grundskole, H20=Gymnasiale uddannelser mv., H30=Erhvervsfaglige uddannelser, H40=Korte videregående uddannelser, H5060=Mellemlange videregående- og bacheloruddannelser, H70=Lange videregående uddannelser mv., H90=Uoplyst]
- alder: values [IALT=Alder i alt, U20=Under 20 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 70OV=70 år og derover, UK=Ukendt alder]
- bopland: join dim.nuts on bopland=kode [approx]; levels [2]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- bopland uses numeric codes 0–12. Codes 1–11 join dim.nuts at niveau=2 (landsdele). Code 0 = Hele landet (total), code 12 = Landsdel ukendt. Exclude code 0 when summing across regions; ColumnValues("best11", "bopland") returns all labels without needing a dim join.
- type has a total row (10=I alt) plus 20=Bestyrelse, 30=Direktører, 40=Uoplyst. Filter type to avoid double-counting.
- This table has 5 dimension columns. For a simple total, filter all non-target dimensions to their aggregate: type='10', kon='100', uddannelse='TOT', alder='IALT', bopland='0'. Forgetting any one inflates the sum.
- Map: context/geo/landsdele.parquet (niveau 2) — merge on bopland=dim_kode. Exclude bopland IN (0, 12).