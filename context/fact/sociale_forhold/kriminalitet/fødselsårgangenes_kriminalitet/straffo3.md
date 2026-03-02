table: fact.straffo3
description: Domme (opgjort pr. 31. december 2024) fordelt på fødselsårgang efter enhed, fødselsår, køn, alder på domstidspunktet, lovovertrædelse og tid
measure: indhold (unit -)
columns:
- overnat1: values [500=Antal pr. 1000 personer, 600=Antal pr. 1000 personer (kumuleret)]
- fodaar: values [1965=1965, 1966=1966, 1967=1967, 1968=1968, 1969=1969 ... 2004=2004, 2005=2005, 2006=2006, 2007=2007, 2008=2008]
- konams: values [TOT=I alt, M=Mænd, K=Kvinder]
- adom: values [15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år ... 54=54 år, 55=55 år, 56=56 år, 57=57 år, 58=58 år]
- lovov: join dim.overtraedtype on lovov=kode; levels [1, 2]
- tid: date range 2024-01-01 to 2024-01-01
dim docs: /dim/overtraedtype.md

notes:
- overnat1 is a measurement selector that doubles the row count — always filter it. 500=Antal pr. 1000 personer (rate at that exact age), 600=Antal pr. 1000 personer (kumuleret). Values are rates, not counts — never sum across overnat1.
- This table counts convictions (events), not persons. indhold is the rate of convictions per 1000 persons in the birth cohort at that age. A single person can contribute multiple convictions at the same age. This differs fundamentally from straffo1/straffo2 which track first conviction per person.
- lovov joins dim.overtraedtype at niveaus 1 and 2 only — same as straffo1: Straffelov (1) and sub-categories 11/12/13/14 only. Same non-additivity caveat: a single conviction can span multiple crime types, so sub-categories can sum above the niveau-1 total.
- adom = age at conviction. No TOT row — adom only has individual ages 15–58. Safe to aggregate across ages by summing rates (e.g. cumulative convictions by a given age). The row count decreases at higher ages because older cohorts have fewer birth years that have reached that age.
- konams has TOT/M/K — filter to one value.
- For "what share of a cohort ever received a conviction", use straffo1 with overnat1=300 (pct. of cohort). straffo3 is better for "at what ages was conviction most common" or "conviction intensity over life course".