table: fact.avislas1
description: Avislæsere efter nøgletal, geografisk område og tid
measure: indhold (unit 1.000 personer)
columns:
- aktp: values [DB138=Dagblade (antal), DB14=Antal læsere (1.000 stk.)]
- geoomr: values [DB143=Landsdækkende, DB144=Regionalt/lokalt, DB1440=Alle dagblade]
- tid: date range 2018-01-01 to 2024-01-01

notes:
- aktp is a measurement selector: DB138=Dagblade (antal), DB14=Antal læsere (1.000 stk.). Always filter to exactly one.
- geoomr=DB1440 (Alle dagblade) is the geographic total. DB143=Landsdækkende and DB144=Regionalt/lokalt are the sub-categories. DB1440 = DB143 + DB144.
- Simpler than dagblad3 — no laesinterval breakdown. Use for total reader counts by geographic coverage.
- Sample 2024: DB14+DB1440 = ~2.234 million total avis-readers (1.000 stk. unit).