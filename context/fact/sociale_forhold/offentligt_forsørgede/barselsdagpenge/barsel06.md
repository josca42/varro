table: fact.barsel06
description: Ikke samboende forældres orlov før fødslen samt i barnets første leveår efter enhed, dagpengeret, eksistens, uddannelseskombination, område og tid
measure: indhold (unit Dage)
columns:
- tal: values [0=Antal forældrepar, 110=Barnet - Antal orlovsdage med mindst én af forældrene, 120=Barnet - Antal kalenderdage mellem første og sidste orlovsdag, 200=Mor - Dage med barselsdagpenge i alt (gennemsnit), 202=Mor - Dage med barselsdagpenge før fødsel (gennemsnit), 220=Mor - Dage med barselsdagpenge efter fødsel (gennemsnit), 330=Far - Dage med barselsdagpenge efter fødsel (gennemsnit), 400=Mor - Dage med barselsdagpenge med løn i alt (gennemsnit), 404=Mor - Dage med barselsdagpenge med løn før fødsel (gennemsnit), 440=Mor - Dage med barselsdagpenge med løn efter fødsel (gennemsnit), 550=Far - Dage med barselsdagpenge med løn efter fødsel (gennemsnit), 600=Mor - Dage med barselsdagpenge uden løn i alt (gennemsnit), 606=Mor - Dage med barselsdagpenge uden løn før fødsel (gennemsnit), 660=Mor - Dage med barselsdagpenge uden løn efter fødsel (gennemsnit), 770=Far - Dage med barselsdagpenge uden løn efter fødsel (gennemsnit)]
- dagpengeret: values [0=Alle forældrepar, uanset dagpengeret, 101=Far er berettiget til barselsdagpenge, 209=Far er ikke berettiget til barselsdagpenge, 310=Mor er berettiget til barselsdagpenge, 490=Mor er ikke berettiget til barselsdagpenge, 511=Både mor og far er berettigede til barselsdagpenge, 619=Mor er berettiget, men far er ikke berettiget til barselsdagpenge, 791=Mor er ikke berettiget, far er berettiget til barselsdagpenge, 899=Hverken mor eller far er berettigede til barselsdagpenge]
- eksistens: values [0=Alle forældrepar, 22=Mor og far er kendte, men ikke samboende, 29=Mor er ukendt, 92=Far er ukendt, 99=Både mor og far er ukendte]
- uddkomb: values [0=Alle forældrepar, uanset uddannelse, 120=Mor har ingen ungdomsuddannelse, 130=Mor har ungdomsuddannelse, 150=Mor har kort videregående uddannelse (KVU), 160=Mor har mellemlang videregående uddannelse (MVU) ... 772=Mor har lang videregående uddannelse (LVU) og far har ingen ungdomsuddannelse, 773=Mor har lang videregående uddannelse (LVU) og far har ungdomsuddannelse, 775=Mor har lang videregående uddannelse (LVU) og far har kort videregående uddannelse (KVU), 776=Mor har lang videregående uddannelse (LVU) og far har mellemlang videregående uddannelse (MVU), 777=Mor har lang videregående uddannelse (LVU) og far har lang videregående uddannelse (LVU)]
- omrade: join dim.nuts on omrade=kode; levels [2]
- tid: date range 2015-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- `tal` is a measurement selector (same 15 measures as barsel04). Always filter to a single value. `tal='0'` for antal forældrepar, `tal='200'` for avg maternal days.
- `dagpengeret` total is `'0'` (Alle forældrepar, uanset dagpengeret). Filter to `'0'` when not analysing entitlement.
- `eksistens` total is `'0'`. The substantively interesting code is `'22'` (Mor og far er kendte, men ikke samboende) — the table's primary population. Codes 29/92/99 are parents with unknown identity.
- `uddkomb` encodes mother's and father's education jointly (codes like 120=Mor uden ungdomsuddannelse regardless of far, 511=Mor KVU + Far MVU, etc.). Total is `'0'`. This is not cross-joinable to morud/farud separately.
- `omrade` joins dim.nuts via `f.omrade = d.kode`. Code `0` = national total. niveau 2 only (11 landsdele) — no kommune-level data in this table.
- Coverage: non-cohabiting parents only. For cohabiting parents use barsel04/barsel25/barlov1.
- Map: context/geo/landsdele.parquet — merge on omrade=dim_kode. Exclude omrade=0.