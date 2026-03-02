table: fact.atf3
description: Virksomheder, der søgte finansiering hos lånefinansieringskilden efter lånefinansieringskilde, udfald, population og tid
measure: indhold (unit Pct.)
columns:
- laanefin: values [LF_KIL_BANKER=Banker/sparekasser, LF_KIL_REALKREDIT=Realkreditinstitutter, LF_KIL_EJER=Virksomhedens ejer(e)/direktør(er)]
- udfald: values [FO=Fuldt opnået, DO=Delvist opnået, IO=Ikke opnået]
- popu: values [S1_N=Virksomheder, der ikke er ejet af et andet firma]
- tid: date range 2007-01-01 to 2018-01-01
notes:
- Survey percentages for loan financing sources specifically. indhold = % of firms seeking loan financing from laanefin source with given udfald outcome.
- popu has only one value (S1_N) — no filtering needed.
- laanefin sources (Banker, Realkreditinstitutter, Ejer/direktør) are mutually exclusive as categories, but a firm could seek from multiple sources simultaneously. Don't sum across laanefin.
- udfald (FO, DO, IO) same interpretation as atf2: independent percentages, don't sum.
- Data ends 2018 — outdated. Companion to atf2 (which shows outcomes by financing form type).
