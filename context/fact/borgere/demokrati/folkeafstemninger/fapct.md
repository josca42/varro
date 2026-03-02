table: fact.fapct
description: Folkeafstemninger efter valgresultat og tid
measure: indhold (unit Pct.)
columns:
- valres: values [STEMPCT=Stemmeprocent, UGYLPCT=Ugyldighedsprocent, BREVPCT=Brevstemmeprocent]
- tid: date range 1971-01-01 to 2022-01-01

notes:
- National level only — no geographic breakdown.
- The three valres values are independent rates, not parts of a whole. Never sum across valres. Each tid row has exactly 3 rows (one per valres).
- Best table for historical stemmeprocent across all referendums since 1971.