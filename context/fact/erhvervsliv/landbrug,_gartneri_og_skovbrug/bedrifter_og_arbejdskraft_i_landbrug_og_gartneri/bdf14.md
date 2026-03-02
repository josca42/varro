table: fact.bdf14
description: Bedrifter efter virksomhedsform, bedriftstype og tid
measure: indhold (unit Antal)
columns:
- virkf1: values [10=Alle virksomhedsformer, 20=Enkeltmandsvirksomhed, 30=Interessentskab, 40=Selskab, 50=Andre virksomhedsformer]
- bedrift: values [1004=Alle bedrifter, 1012=Agerbrug, 1080=Kvæg, 1085=Svin, 1094=Andre husdyrbrug, 1096=Blandet landbrug, 1098=Gartneri]
- tid: date range 2006-01-01 to 2024-01-01

notes:
- virkf1: 10=Alle virksomhedsformer is the total. The 4 specific forms (20, 30, 40, 50) sum to the total. Filter to 10 for national totals; don't sum across all 5 values.
- bedrift: 1004=Alle bedrifter is the total. The 6 specific types (1012-1098) sum to 1004. Filter to 1004 for totals.
- No regional breakdown — national only. Use bdf11 if you need regional farm counts by farm type.