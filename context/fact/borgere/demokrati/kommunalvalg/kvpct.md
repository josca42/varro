table: fact.kvpct
description: Valg til kommunalbestyrelser efter valgresultat og tid
measure: indhold (unit Pct.)
columns:
- valres: values [STEMPCT=Stemmeprocent, UGYLPCT=Ugyldighedsprocent]
- tid: date range 1970-01-01 to 2021-01-01

notes:
- National-level only — no regional breakdown. Two rows per election year: STEMPCT (voter turnout %) and UGYLPCT (invalid vote %). Always filter valres to the rate you need; these are independent percentages, never sum them.
- For counts (number of voters, valid/invalid votes) use kvbpct instead. For regional breakdown use kvres.