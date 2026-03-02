table: fact.bogs03
description: Solgte bøger efter genre, originalsprog, udgivelsessprog og tid
measure: indhold (unit Antal)
columns:
- genre: values [1000=Genre i alt, 1010=Børne- og ungelitteratur i alt, 1020=Bøger for de helt små, billedbøger, aktivitetsbøger mv., 1030=Fagbøger til børn og unge, 1040=Skønlitteratur for børn og unge ... 1240=Krimier, thrillere og spændingsromaner, 1250=Romantik og erotik, 1260=Science fiction, fantasy o.l., 1270=Skønlitteratur, øvrige, 1280=Uoplyst genre]
- sprog: values [1290=Sprog i alt, 1300=Dansk, 1310=Engelsk, 1320=Fransk, 1330=Norsk, 1340=Svensk, 1350=Tysk, 1360=Øvrige og flere sprog, 1370=Uoplyst sprog]
- udgivelsessprog: values [1290=Sprog i alt, 1300=Dansk, 1310=Engelsk, 1360=Øvrige og flere sprog]
- tid: date range 2022-07-01 to 2024-04-01

notes:
- Tracks book SALES by genre, original language (sprog), and publication language (udgivelsessprog). Quarterly data from 2022 Q3.
- genre has the same 3-level hierarchy as bogs01 — never sum across all codes. Pick level 0 (1000), level 1 subtotals (1010/1070/1200/1280), or leaf codes, not a mix.
- sprog=1290 ("Sprog i alt") is the aggregate of all original-language codes (1300=Dansk, 1310=Engelsk, 1320=Fransk, 1330=Norsk, 1340=Svensk, 1350=Tysk, 1360=Øvrige, 1370=Uoplyst). Filter to 1290 for totals.
- udgivelsessprog=1290 ("Sprog i alt") is the aggregate of 1300 (Dansk), 1310 (Engelsk), 1360 (Øvrige). Narrower set than sprog. Filter to 1290 for totals.
- Use this table when you need to distinguish original vs publication language (e.g. translated books sold in Denmark).