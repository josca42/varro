table: fact.barsel14
description: Dage med barselsdagpenge (forældreårgange) efter enhed, berettigelse, branche og tid
measure: indhold (unit -)
columns:
- enhed: values [1=Antal fædre, 2=Antal mødre, 200=Mor - Dage med barselsdagpenge i alt (gennemsnit), 202=Mor - Dage med barselsdagpenge før fødsel (gennemsnit), 220=Mor - Dage med barselsdagpenge efter fødsel (gennemsnit), 330=Far - Dage med barselsdagpenge efter fødsel (gennemsnit), 400=Mor - Dage med barselsdagpenge med løn i alt (gennemsnit), 404=Mor - Dage med barselsdagpenge med løn før fødsel (gennemsnit), 440=Mor - Dage med barselsdagpenge med løn efter fødsel (gennemsnit), 550=Far - Dage med barselsdagpenge med løn efter fødsel (gennemsnit), 600=Mor - Dage med barselsdagpenge uden løn i alt (gennemsnit), 606=Mor - Dage med barselsdagpenge uden løn før fødsel (gennemsnit), 660=Mor - Dage med barselsdagpenge uden løn efter fødsel (gennemsnit), 770=Far - Dage med barselsdagpenge uden løn efter fødsel (gennemsnit)]
- beret: values [201=Far er berettiget til barselsdagpenge, 203=Far holdt barselsorlov, 310=Mor er berettiget til barselsdagpenge, 330=Mor holdt barselsorlov, 511=Både mor og far er berettigede til barselsdagpenge, 513=Mor er berettiget, far holdt barselslov, 519=Mor er berettiget, far er ikke berettiget til barselsdagpenge, 631=Mor holdt barselsorlov, far er berettiget, 633=Både mor og far holdt barseslsorlov, 639=Mor holdt barselsorlov, far er ikke berettiget til barselsdagpenge, 791=Mor er ikke berettiget, far er berettiget til barselsdagpenge, 793=Mor er ikke berettiget, far holdt barselsorlov]
- erhverv: join dim.db on erhverv=kode::text [approx]; levels [5]
- tid: date range 2015-01-01 to 2023-01-01
dim docs: /dim/db.md

notes:
- `enhed` is a measurement selector (counts vs. averages) — always filter to a single value. Same codes as barsel11.
- `beret` same as barsel11 — no explicit "all parents" total code.
- `erhverv` uses proprietary 5-digit DST industry codes (e.g. `01000`, `10001`) that do NOT cleanly map to dim.db. The fact doc's suggested dim.db join is incorrect (only 9% false-match). The correct reference is dim.nr_branche, but only partial coverage at niveau 4. Use `ColumnValues("barsel14", "erhverv")` to browse available codes and their labels. Code `'TOT'` = national total; `'99999'` = unknown/unclassified. Do not attempt a dim.db join for erhverv.
- This is the most granular industry breakdown in the subject (128 distinct industry codes). For a coarser view use barsel11 (12 branche codes).