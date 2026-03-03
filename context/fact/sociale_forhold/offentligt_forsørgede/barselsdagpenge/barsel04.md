table: fact.barsel04
description: Forældres orlov før fødslen samt i barnets første leveår efter enhed, berettigelse, mors uddannelse, fars uddannelse, område og tid
measure: indhold (unit Dage)
columns:
- tal: values [0=Antal forældrepar, 110=Barnet - Antal orlovsdage med mindst én af forældrene, 120=Barnet - Antal kalenderdage mellem første og sidste orlovsdag, 200=Mor - Dage med barselsdagpenge i alt (gennemsnit), 202=Mor - Dage med barselsdagpenge før fødsel (gennemsnit), 220=Mor - Dage med barselsdagpenge efter fødsel (gennemsnit), 330=Far - Dage med barselsdagpenge efter fødsel (gennemsnit), 400=Mor - Dage med barselsdagpenge med løn i alt (gennemsnit), 404=Mor - Dage med barselsdagpenge med løn før fødsel (gennemsnit), 440=Mor - Dage med barselsdagpenge med løn efter fødsel (gennemsnit), 550=Far - Dage med barselsdagpenge med løn efter fødsel (gennemsnit), 600=Mor - Dage med barselsdagpenge uden løn i alt (gennemsnit), 606=Mor - Dage med barselsdagpenge uden løn før fødsel (gennemsnit), 660=Mor - Dage med barselsdagpenge uden løn efter fødsel (gennemsnit), 770=Far - Dage med barselsdagpenge uden løn efter fødsel (gennemsnit)]
- beret: values [3=Alle forældre(par), uanset berettigelse og orlov, 201=Far er berettiget til barselsdagpenge, 203=Far holdt barselsorlov, 209=Far er ikke berettiget til barselsdagpenge, 310=Mor er berettiget til barselsdagpenge ... 659=Mor holdt ikke barselsorlov, far er ikke berettiget, 791=Mor er ikke berettiget, far er berettiget til barselsdagpenge, 793=Mor er ikke berettiget, far holdt barselsorlov, 795=Mor er ikke berettiget, far holdt ikke barselsorlov, 799=Mor er ikke berettiget, far er ikke berettiget]
- morud: values [2=Alle mødre uanset uddannelse, 120=Mor har ingen ungdomsuddannelse, 130=Mor har ungdomsuddannelse, 150=Mor har kort videregående uddannelse (KVU), 160=Mor har mellemlang videregående uddannelse (MVU), 170=Mor har lang videregående uddannelse (LVU)]
- farud: values [4=Alle fædre uanset uddannelse, 220=Far har ingen ungdomsuddannelse, 230=Far har ungdomsuddannelse, 250=Far har kort videregående uddannelse (KVU), 260=Far har mellemlang videregående uddannelse (MVU), 270=Far har lang videregående uddannelse (LVU)]
- omrade: join dim.nuts on omrade=kode [approx: Missing codes 0, 99 (likely total/unknown)]; levels [2, 3]
- tid: date range 2015-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- `tal` is a measurement selector with 15 different measures (antal forældrepar, child days, mother/father days total/before/after birth, with/without pay). Every combination of beret × morud × farud × omrade is repeated for each `tal` value. Always filter to one `tal` to avoid overcounting. Use `tal='0'` for number of parent pairs, `tal='200'` for avg total maternal days, `tal='330'` for avg paternal days.
- `beret` total is `'3'` (Alle forældre(par), uanset berettigelse og orlov). Filter `beret='3'` when not analysing entitlement breakdown.
- `morud` total is `'2'`, `farud` total is `'4'`. Filter both to their totals when not analysing education.
- `omrade` joins dim.nuts via `f.omrade = d.kode`. Code `0` = landstal/national total (not in dim). niveau 2 = 11 landsdele, niveau 3 = 98 kommuner. Filter `d.niveau = 2` or `d.niveau = 3` to pick one granularity — mixing levels double-counts.
- For a simple national time series: `WHERE tal='200' AND beret='3' AND morud='2' AND farud='4' AND omrade='0'`.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.