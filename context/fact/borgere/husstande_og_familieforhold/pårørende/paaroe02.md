table: fact.paaroe02
description: Befolkningen (0-24-årige) 1. januar efter hovedpersonens alder, antal relationer og tid
measure: indhold (unit Antal)
columns:
- hoald: values [9924=0-24 år i alt, 9817=0-17 år i alt, 0=0 år, 1=1 år, 2=2 år ... 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år]
- antalrela: values [51=1 forælder, 52=2 forældre, 131=1 bedsteforælder, 132=2 bedsteforældre, 133=3 bedsteforældre, 134=4 bedsteforældre]
- tid: date range 2020-01-01 to 2025-01-01

notes:
- antalrela codes 51–52 (parents) and 131–134 (grandparents) are NOT mutually exclusive across groups — a child can simultaneously appear in "52 forældre" and "134 bedsteforældre". Never sum across the full column; filter to parents-only (51+52) or grandparents-only (131+132+133+134) to get additive counts.
- Within each group the codes are mutually exclusive: a child has exactly one of {1 parent, 2 parents} and exactly one of {1,2,3,4 grandparents}. 51+52 = all children with at least one living parent; 131+132+133+134 = all children with at least one living grandparent.
- hoald has 9924 (0–24 i alt) and 9817 (0–17 i alt) as aggregates on top of individual year-ages 0–24. Filter to one or the other.
- No dim joins — straightforward grouping and summation once the antalrela scope is fixed.