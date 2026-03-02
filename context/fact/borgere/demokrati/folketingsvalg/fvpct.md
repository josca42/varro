table: fact.fvpct
description: Folketingsvalg efter valgresultat og tid
measure: indhold (unit Pct.)
columns:
- valres: values [STEMPCT=Stemmeprocent, UGYLPCT=Ugyldighedsprocent, BREVPCT=Brevstemmeprocent]
- tid: date range 1971-01-01 to 2022-01-01

notes:
- Simple national-level percentages. Three valres values: STEMPCT (voter turnout), UGYLPCT (invalid ballot rate), BREVPCT (postal vote rate). These are independent rates — never sum across valres.
- No overcounting risk: just filter to the valres you want and select by tid.