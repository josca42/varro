table: fact.atf2
description: Virksomheder, der søgte finansieringsformen efter finansieringsform, udfald, population og tid
measure: indhold (unit Pct.)
columns:
- finform: values [LF=Lånefinansiering, EF=Egenkapitalfinansiering, AF=Andre former for finansiering]
- udfald: values [FO=Fuldt opnået, DO=Delvist opnået, IO=Ikke opnået]
- popu: values [S1_N=Virksomheder, der ikke er ejet af et andet firma]
- tid: date range 2007-01-01 to 2018-01-01
notes:
- Survey percentages: indhold = % of firms that sought a given financing form (finform) and had a given outcome (udfald). All values are independent percentages — never sum across finform or udfald.
- popu has only one value (S1_N) — no filtering needed.
- udfald (FO=Fuldt opnået, DO=Delvist opnået, IO=Ikke opnået): these three outcomes are not guaranteed to sum to 100% since some firms may have withdrawn. Treat each row as an independent percentage.
- Data ends 2018 — outdated. Use atf3 for breakdown by loan source, atf1 for sector comparison.
