table: fact.bogs02
description: Solgte bøger efter hovedgenre, udgivelsessprog og tid
measure: indhold (unit Antal)
columns:
- hovedgenre: values [1000=Genre i alt, 1010=Børne- og ungelitteratur i alt, 1070=Faglitteratur i alt, 1200=Skønlitteratur i alt, 1280=Uoplyst genre]
- udgivelsessprog: values [1290=Sprog i alt, 1300=Dansk, 1310=Engelsk, 1320=Fransk, 1330=Norsk, 1340=Svensk, 1350=Tysk, 1360=Øvrige og flere sprog]
- tid: date range 2022-07-01 to 2024-04-01

notes:
- Tracks book SALES by top-level genre and publication language. Quarterly data from 2022 Q3.
- hoofdgenre only has level-0 (1000=Genre i alt) and level-1 subtotals (1010=børne- og ungelitteratur, 1070=faglitteratur, 1200=skønlitteratur, 1280=uoplyst) — no leaf categories. Safe to use any single value without overcounting.
- udgivelsessprog=1290 ("Sprog i alt") is the aggregate of all language codes. Filter to 1290 for totals, or a specific language code for breakdown.
- Simpler than bogs01 (no format column) and bogs03 (no original language). Use when you just need sales by genre + publication language.