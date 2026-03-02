table: fact.straffo4
description: Domme til frihedsstraf (opgjort pr. 31. december 2024) efter enhed, fødselsår, køn, frihedsstraf, alder på domstidspunktet og tid
measure: indhold (unit -)
columns:
- overnat1: values [500=Antal pr. 1000 personer, 600=Antal pr. 1000 personer (kumuleret)]
- fodaar: values [1965=1965, 1966=1966, 1967=1967, 1968=1968, 1969=1969 ... 2004=2004, 2005=2005, 2006=2006, 2007=2007, 2008=2008]
- konams: values [TOT=I alt, M=Mænd, K=Kvinder]
- fristraf: values [1=1 Dom til frihedsstraf, 11=11 Ubetinget frihedsstraf, 12=12 Betinget frihedsstraf]
- adom: values [15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år ... 54=54 år, 55=55 år, 56=56 år, 57=57 år, 58=58 år]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- overnat1 is a measurement selector that doubles the row count — always filter it. 500=Antal pr. 1000 personer, 600=Antal pr. 1000 personer (kumuleret). Values are rates, not counts.
- fristraf values are independent, not hierarchical: 1=Dom til frihedsstraf (any), 11=Ubetinget, 12=Betinget. A person can contribute to multiple fristraf categories within the same age year. Do not sum across fristraf — pick the one relevant to the question.
- adom = age at conviction. No TOT row — individual ages 15–58 only. Safe to aggregate across ages.
- konams has TOT/M/K — filter to one value.
- No dim joins — all columns inline coded.
- This is the rate-per-1000 equivalent of straffo2: use straffo4 for "how common are prison sentences by age", use straffo2 for "what share of a cohort ever received a prison sentence" (person-level, first sentence tracking).