table: fact.ifif
description: Industriens investeringsforventninger efter branche (DB07), formål og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- formal: values [ERST=Erstatning af nedslidt materiel eller udstyr, UDVI=Udvidelse af produktionskapaciteten, RATI=Rationalisering af driften, ANDR=Andre formål, fx miljø og sikkerhed]
- tid: date range 2010-01-01 to 2026-01-01

notes:
- branche07 does NOT join dim.db. Same letter-coded scheme as ifi01: B, C, CA–CM, S1–S4. Use ColumnValues("ifif", "branche07") for labels.
- formal (formål) values sum to 100 for each branche07/tid — they are an allocation of investment budget across purposes (ERST+UDVI+RATI+ANDR = 100). These are mutually exclusive shares. Don't filter to one formal and interpret as an overall percentage — each value only makes sense relative to the others.
- To see which purpose dominates investment plans, compare all four formal values for the same branche07/tid.