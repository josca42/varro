table: fact.barsel25
description: Orlov før fødslen og i barnet to første leveår for samboende forældre med mere end 46 ugers barselsorlov efter enhed, berettigelse, mors uddannelse, fars uddannelse, område og tid
measure: indhold (unit Dage)
columns:
- tal: values [0=Antal forældrepar, 110=Barnet - Antal orlovsdage med mindst én af forældrene, 120=Barnet - Antal kalenderdage mellem første og sidste orlovsdag, 200=Mor - Dage med barselsdagpenge i alt (gennemsnit), 202=Mor - Dage med barselsdagpenge før fødsel (gennemsnit), 220=Mor - Dage med barselsdagpenge efter fødsel (gennemsnit), 330=Far - Dage med barselsdagpenge efter fødsel (gennemsnit), 400=Mor - Dage med barselsdagpenge med løn i alt (gennemsnit), 404=Mor - Dage med barselsdagpenge med løn før fødsel (gennemsnit), 440=Mor - Dage med barselsdagpenge med løn efter fødsel (gennemsnit), 550=Far - Dage med barselsdagpenge med løn efter fødsel (gennemsnit), 600=Mor - Dage med barselsdagpenge uden løn i alt (gennemsnit), 606=Mor - Dage med barselsdagpenge uden løn før fødsel (gennemsnit), 660=Mor - Dage med barselsdagpenge uden løn efter fødsel (gennemsnit), 770=Far - Dage med barselsdagpenge uden løn efter fødsel (gennemsnit)]
- beret: values [3=Alle forældre(par), uanset berettigelse og orlov, 201=Far er berettiget til barselsdagpenge, 203=Far holdt barselsorlov, 209=Far er ikke berettiget til barselsdagpenge, 310=Mor er berettiget til barselsdagpenge ... 659=Mor holdt ikke barselsorlov, far er ikke berettiget, 791=Mor er ikke berettiget, far er berettiget til barselsdagpenge, 793=Mor er ikke berettiget, far holdt barselsorlov, 795=Mor er ikke berettiget, far holdt ikke barselsorlov, 799=Mor er ikke berettiget, far er ikke berettiget]
- morud: values [2=Alle mødre uanset uddannelse, 120=Mor har ingen ungdomsuddannelse, 130=Mor har ungdomsuddannelse, 150=Mor har kort videregående uddannelse (KVU), 160=Mor har mellemlang videregående uddannelse (MVU), 170=Mor har lang videregående uddannelse (LVU)]
- farud: values [4=Alle fædre uanset uddannelse, 220=Far har ingen ungdomsuddannelse, 230=Far har ungdomsuddannelse, 250=Far har kort videregående uddannelse (KVU), 260=Far har mellemlang videregående uddannelse (MVU), 270=Far har lang videregående uddannelse (LVU)]
- omrade: join dim.nuts on omrade=kode [approx]; levels [2, 3]
- tid: date range 2016-01-01 to 2022-01-01
dim docs: /dim/nuts.md

notes:
- This is a subset of barsel04: only parent cohorts where the child's parents together took MORE than 46 weeks of leave. Do not use for representative national statistics — results are not comparable to barsel04.
- Same column structure and filter logic as barsel04. `tal` is a measurement selector (always filter to one value), `beret` total is `'3'`, `morud` total is `'2'`, `farud` total is `'4'`.
- `omrade` joins dim.nuts. Code `0` = national total (not in dim). niveau 2 = 11 landsdele, niveau 3 = 98 kommuner. Filter `d.niveau` to avoid cross-level double counting.
- Shorter time range than barsel04 (2016–2022 vs. 2015–2023).
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.