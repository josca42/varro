table: fact.brande01
description: Boliger med brænde- eller træpilleovn og forbrug af brænde eller træpiller efter nøgletal og tid
measure: indhold (unit -)
columns:
- aktp: values [1030=Boliger med brændeovn (1.000 stk.), 1000=Boliger med træpilleovn (1.000 stk.), 1010=Forbrug af brænde (terajoule, TJ), 1020=Forbrug af træpiller (terajoule, TJ)]
- tid: date range 2013-01-01 to 2023-01-01

notes:
- aktp encodes 4 completely different metrics with incompatible units. Never sum across aktp. Pick the one you need: 1030 = boliger med brændeovn (1.000 stk.), 1010 = forbrug af brænde (TJ), 1000 = boliger med træpilleovn (1.000 stk.), 1020 = forbrug af træpiller (TJ).
- Coverage by aktp differs: 1030 (brændeovn count) and 1010 (brænde consumption) cover odd years 2013-2023; 1000 (træpilleovn count) and 1020 (træpiller consumption) only have 2023.
- This is a simple national summary — no geographic or housing-type breakdown. For breakdowns use brande02/brande03 (brænde) or pille02/pille03 (træpiller), but those only cover 2023.