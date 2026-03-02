table: fact.lag8
description: Engroshandlens handelsvarelagre efter branche (DB07), prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- branche07: join dim.db on branche07=kode [approx]; levels [2, 3]
- prisenhed: values [ÅRPRIS=Årets priser, 2015=2015 priser]
- tid: date range 2001-01-01 to 2025-04-01
dim docs: /dim/db.md

notes:
- DO NOT join branche07 to dim.db. Although the numeric codes (10–17) technically match rows in dim.db, they map to completely wrong labels (e.g. code 12 → "Fremstilling af tobaksprodukter" in dim.db, but "Engroshandel med føde, drikke- og tobaksvarer" in this table). Use ColumnValues("lag8", "branche07") instead to get the correct engroshandel labels.
- branche07=17 is "Engroshandel i alt" (total aggregate). It equals the sum of codes 10–16. Exclude it when summing across branches to avoid double-counting.
- indhold is the quarterly CHANGE in inventory (lagertilvækst), not the stock level. Negative values are inventory drawdowns — this is normal.
- prisenhed is a measurement selector: every branche07/tid combination appears twice (ÅRPRIS and 2015-priser). Always filter to one prisenhed value before summing across branches or time.
- Data is quarterly (tid steps by quarter). The 8 branche07 codes cover the full wholesale sector (engroshandel og bilhandel): 10=bilhandel, 11=korn og foderstoffer, 12=føde/drikke/tobak, 13=tekstiler og husholdningsudstyr, 14=IT-udstyr, 15=andre maskiner, 16=anden engroshandel, 17=total.