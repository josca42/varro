table: fact.forv2
description: Planer om større investeringer efter indikator og tid
measure: indhold (unit -)
columns:
- indikator: values [F14=Planer om køb af bil indenfor de næste 12 måneder?, F15=Planer om køb eller opførsel af bolig indenfor de næste 12 måneder?, F16=Planer om større forbedringer af eller renoveringer i hjemmet indenfor de næste 12 måneder?]
- tid: date range 1990-01-01 to 2025-10-01

notes:
- Quarterly frequency (January, April, July, October only). Each row is one indikator for one quarter. Filter to a specific indikator — never sum across them.
- indhold is a net balance score. All three indicators are consistently negative (F14: -80 to -45, F15: -87 to -56, F16: -86 to -28), meaning respondents generally say they do NOT plan these purchases. This is expected for large, infrequent investments.
- Only 3 indicators: F14=køb af bil, F15=køb/opførsel af bolig, F16=renovering i hjemmet.
- Example: SELECT tid, indhold FROM fact.forv2 WHERE indikator = 'F16' ORDER BY tid — gives quarterly renovation plans series from 1990.