table: fact.best15
description: Bestyrelsesmedlemmer og direktører efter type, branche (DB07 19-grp), uddannelse og tid
measure: indhold (unit Antal)
columns:
- type: values [10=I alt, 20=Bestyrelse, 30=Direktører, 40=Uoplyst]
- branchedb0721: join dim.db on branchedb0721=kode::text [approx]
- uddannelse: values [TOT=I alt uddannelser, H10=Grundskole, H20=Gymnasiale uddannelser mv., H30=Erhvervsfaglige uddannelser, H40=Korte videregående uddannelser, H5060=Mellemlange videregående- og bacheloruddannelser, H70=Lange videregående uddannelser mv., H90=Uoplyst]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- branchedb0721 uses DB07 section letter codes (A–S, X, TOT), NOT dim.db numeric codes. The dim.db join does not work. Use ColumnValues("best15", "branchedb0721") to get labels.
- TOT = Erhverv i alt (total). Exclude TOT when aggregating across branches. X = Uoplyst aktivitet.
- type has total row type='10'. Filter type='10' and uddannelse='TOT' for overall counts.