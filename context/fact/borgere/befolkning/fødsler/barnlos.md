table: fact.barnlos
description: Barnløse pr. 1.000 efter køn, alder og tid
measure: indhold (unit Pr. 1.000 indb.)
columns:
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år ... 66=66 år, 67=67 år, 68=68 år, 69=69 år, 70=70 år]
- tid: date range 1986-01-01 to 2025-01-01
notes:
- indhold is a rate (childless per 1,000 inhabitants) — NEVER sum or average across kon or alder. Each cell is an independent rate for a specific gender×age combination.
- kon has no TOT: only 1=Mænd and 2=Kvinder. alder runs 20–70 with no IALT. Always filter to a specific kon and alder, or plot individual values as a series.
- Complements foraeld: barnlos gives the share without children; foraeld gives count of those with children.
