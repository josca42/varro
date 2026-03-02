table: fact.ofats1
description: Danske datterselskaber i udlandet efter branche, enhed og tid
measure: indhold (unit Antal)
columns:
- branche: join dim.db_10 on branche=kode::text [approx]; levels [1]
- enhed: values [DSANTAL=Datterselskaber, DSANSAT=Ansatte]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/db_10.md

notes:
- enhed is a measurement selector: every branche/tid row exists twice — once for DSANTAL (antal datterselskaber) and once for DSANSAT (antal ansatte). Always filter enhed to one value, e.g. WHERE enhed='DSANTAL'.
- branche joins dim.db_10 at niveau 1 (codes 1–10, the 10 main DB07 industry groups). TOT is an aggregate total not in the dim — exclude it when summing across branches.
- To get all branches with labels: JOIN dim.db_10 d ON f.branche = d.kode::text AND d.niveau = 1, then add WHERE f.enhed = '...' AND f.branche != 'TOT'.