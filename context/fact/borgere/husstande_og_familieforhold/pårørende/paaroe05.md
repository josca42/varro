table: fact.paaroe05
description: Befolkningen 1. januar efter relation, hovedpersonens alder og tid
measure: indhold (unit Antal)
columns:
- relation: values [01=Partner, 03=Søn/datter, 04=Svigerbarn, 05=Forælder, 06A=Søskende, 13=Bedsteforælder, 14=Barnebarn]
- hoald: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 81=81 år, 82=82 år, 83=83 år, 84=84 år, 85=85 år]
- tid: date range 2020-01-01 to 2025-01-01

notes:
- relation codes are individual relation types (partner, child, parent, sibling, grandparent, grandchild) — NOT mutually exclusive. A 40-year-old can appear in both "01 Partner" and "03 Søn/datter". Never sum across relation values; always filter to a single relation type.
- This contrasts with paaroe03/04 which use combination categories (K00–K15) that are mutually exclusive. paaroe05 answers "how many people of age X have at least one relation of type Y" — independently per type.
- hoald has individual years (appears to be 0–85+) with no aggregate total code. Summing all ages for a single relation type gives the national count for that relation.
- No dim joins — no regional breakdown. No age-group aggregates — sum year-ranges manually if needed.