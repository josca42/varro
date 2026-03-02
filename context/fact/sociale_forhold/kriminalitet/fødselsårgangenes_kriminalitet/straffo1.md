table: fact.straffo1
description: Fødselsårgange (opgjort pr 31. december 2024) efter enhed, fødselsår, køn, alder ved første dom, lovovertrædelse og tid
measure: indhold (unit -)
columns:
- overnat1: values [100=Antal, 200=Antal (kumuleret), 300=Pct. af fødselsårgangen, 400=Pct. af fødselsårgangen (kumuleret)]
- fodaar: values [1965=1965, 1966=1966, 1967=1967, 1968=1968, 1969=1969 ... 2004=2004, 2005=2005, 2006=2006, 2007=2007, 2008=2008]
- konams: values [TOT=I alt, M=Mænd, K=Kvinder]
- fdomald: values [TOT=Alder i alt, 15=15 år, 16=16 år, 17=17 år, 18=18 år ... 55=55 år, 56=56 år, 57=57 år, 58=58 år, IDOMT=Ikke dømt]
- lovov: join dim.overtraedtype on lovov=kode; levels [1, 2]
- tid: date range 2024-01-01 to 2024-01-01
dim docs: /dim/overtraedtype.md

notes:
- overnat1 is a measurement selector that quadruples the row count — always filter it. 100=Antal (count convicted at that specific age), 200=Antal (kumuleret), 300=Pct. af fødselsårgangen, 400=Pct. af fødselsårgangen (kumuleret). For most questions use 300 (share of cohort ever convicted by that age) or 100 (convicted at exactly that age).
- lovov joins dim.overtraedtype at niveaus 1 and 2 only. Only Straffelov (kode=1) and its 4 sub-categories (11=Seksual, 12=Vold, 13=Ejendom, 14=Andre) are present — no Færdselslov or Særlov rows exist in this table. Use `JOIN dim.overtraedtype d ON f.lovov = d.kode WHERE d.niveau = 2` for the sub-categories.
- lovov values are NOT mutually exclusive: a single conviction case can involve multiple crime types. At fdomald=18 for 1980-cohort men, sub-categories 11–14 sum to 811 but lovov=1 shows only 663 (unique persons). Never sum across lovov values — use lovov=1 for the Straffelov total and individual niveau-2 codes for breakdowns by type.
- fdomald = age at first conviction. TOT = regardless of age (the cohort total), IDOMT = never convicted. Individual ages 15–58 count those whose first conviction was exactly at that age. Summing individual ages yields more than TOT due to the person-counting issue above.
- konams has TOT/M/K — always filter to one value or the risk of double-counting across gender.
- This is a cohort/person table: each person is counted once (at their first conviction age) per lovov/overnat1 combination. Compare to straffo3 which counts convictions (events) per 1000 persons per age.