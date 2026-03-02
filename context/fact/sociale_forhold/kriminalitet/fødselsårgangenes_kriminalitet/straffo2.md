table: fact.straffo2
description: Fødselsårgange (opgjort pr. 31. december 2024) efter enhed, fødselsår, køn, alder ved første frihedsstraf, frihedsstraf og tid
measure: indhold (unit -)
columns:
- overnat1: values [100=Antal, 200=Antal (kumuleret), 300=Pct. af fødselsårgangen, 400=Pct. af fødselsårgangen (kumuleret)]
- fodaar: values [1965=1965, 1966=1966, 1967=1967, 1968=1968, 1969=1969 ... 2004=2004, 2005=2005, 2006=2006, 2007=2007, 2008=2008]
- konams: values [TOT=I alt, M=Mænd, K=Kvinder]
- avffs: values [TOT=Alder i alt, 15=15 år, 16=16 år, 17=17 år, 18=18 år ... 55=55 år, 56=56 år, 57=57 år, 58=58 år, IFRI=Ingen frihedsstraffe]
- fristraf: values [1=1 Dom til frihedsstraf, 11=11 Ubetinget frihedsstraf, 12=12 Betinget frihedsstraf]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- overnat1 is a measurement selector that quadruples the row count — always filter it. 100=Antal, 200=Antal (kumuleret), 300=Pct. af fødselsårgangen, 400=Pct. af fødselsårgangen (kumuleret). Same semantics as straffo1.
- fristraf values are NOT mutually exclusive or hierarchical. 1=Dom til frihedsstraf (any), 11=Ubetinget, 12=Betinget. A person can have both unconditional and conditional sentences across their lifetime, so at age-specific level 11+12 can exceed 1. At avffs=TOT all three can end up equal (every person who received any prison sentence received both types across their lifetime). Never sum across fristraf values.
- avffs = age at first prison sentence (for each fristraf type independently). TOT = regardless of age, IFRI = no prison sentence of that type. Individual ages 15–58 for those first sentenced at exactly that age.
- konams has TOT/M/K — filter to one value.
- No dim joins — all columns are inline coded. No ColumnValues needed for dim lookup.
- This is a cohort/person table focused on prison sentences only. For first conviction by crime type use straffo1; for per-1000 conviction rates by age use straffo3/straffo4.