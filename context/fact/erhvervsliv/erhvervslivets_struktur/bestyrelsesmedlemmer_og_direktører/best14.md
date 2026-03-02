table: fact.best14
description: Bestyrelsesmedlemmer og direktører efter type, branche (DB07 19-grp), køn og tid
measure: indhold (unit Antal)
columns:
- type: values [10=I alt, 20=Bestyrelse, 30=Direktører, 40=Uoplyst]
- branchedb0721: join dim.db on branchedb0721=kode::text [approx]
- kon: values [100=Køn i alt, 200=Mænd, 300=Kvinder, 400=Uoplyst køn]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- branchedb0721 uses DB07 section letter codes (A–S, X, TOT), NOT the numeric codes in dim.db. The dim.db join does not work. Use ColumnValues("best14", "branchedb0721") to get labels — all 21 values with titles are available there.
- TOT = Erhverv i alt (total), X = Uoplyst aktivitet. Exclude TOT when aggregating across branches to avoid double-counting.
- type has total row type='10'. Filter type and kon to their totals (10 and 100) unless you need a breakdown.