table: fact.bdf15
description: Bedrifter efter virksomhedsform, bedriftsstørrelser og tid
measure: indhold (unit Antal)
columns:
- virkf1: values [10=Alle virksomhedsformer, 20=Enkeltmandsvirksomhed, 30=Interessentskab, 40=Selskab, 50=Andre virksomhedsformer]
- bedriftstr: values [3995=Alle bedrifter, 4200=Bedrifer med 0,0-29,9 ha, 4205=Bedrifter med 30,0-49,9 ha, 4210=Bedrifter med 50,0-99,9 ha, 4215=Bedrifter med 100,0-199,9 ha ... 4325=Bedrifter med 1-99 søer, 4330=Bedrifter med 100-199 søer, 4335=Bedrifter med 200-499 søer, 4340=Bedrifter med 500-999 søer, 4345=Bedrifter med 1.000 søer og derover]
- tid: date range 2006-01-01 to 2024-01-01

notes:
- virkf1: 10=Alle virksomhedsformer is the total. Don't sum across all 5 codes.
- bedriftstr mixes two completely independent farm-size classification schemes in one column: 3995=Alle bedrifter (grand total); 4200-4280 = size brackets by cultivated area (ha); 4285-4345 = size brackets by pig/livestock count. These schemes overlap — a farm appears in both a ha-bracket and a pig-bracket row. Never sum across codes from different schemes. Pick one scheme per query. Use 3995 for the grand total only.
- No regional breakdown — national only. Use bdf11 for regional farm counts.