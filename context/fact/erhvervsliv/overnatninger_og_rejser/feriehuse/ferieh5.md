table: fact.ferieh5
description: Feriehuse til udlejning efter kapacitet og tid
measure: indhold (unit Antal)
columns:
- kapmedie: values [3020=Udlejningskapacitet]
- tid: date range 2012-01-01 to 2024-01-01

notes:
- Trivial table: kapmedie=3020 (Udlejningskapacitet) is the only value, 13 rows total (one per year 2012–2024). Query as: SELECT tid, indhold FROM fact.ferieh5 ORDER BY tid.