table: fact.fisk1
description: Danske fiskefartøjer efter område, enhed, fartøjstype, længde, tonnage og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- tal: values [1=Antal fiskefartøjer, 2=Tonnage i BT, 3=Maskineffekt i kilowatt]
- fiskfar: values [0=Fartøjer i alt, 1=Trawlere, 2=Not og kombifartøjer, 3=Snurrevodfartøjer, 4=Garn- / krogefartøjer, 5=Andre fartøjer]
- laeng: values [0=Fartøjslængde i alt, 1=Under 10 meter, 2=10-11,9 meter, 3=12-17,9 meter, 4=18-23,9 meter, 5=24-39,9 meter, 6=Over 40 meter]
- tonnage: values [0=Fartøjstonnage i alt, 1=Under 10 BT, 2=10-49,9 BT, 3=50-199,9 BT, 4=Over 200 BT]
- tid: date range 1996-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- tal is a measurement-type selector (1=Antal fartøjer, 2=Tonnage i BT, 3=Maskineffekt i kW). Every dimension combination repeats 3 times. Always filter to one tal value — summing across them is meaningless.
- omrade joins dim.nuts but only niveau=1 (5 regions). Code '0' = national total, not in dim — use WHERE omrade='0' to get the Danish total. Use ColumnValues("nuts", "titel", for_table="fisk1") to see all 5 regions.
- fiskfar, laeng, and tonnage each have a total at code '0'. To get a simple vessel count by region, filter: tal='1', fiskfar='0', laeng='0', tonnage='0'. Omitting any one of these inflates results.
- laeng and tonnage are two alternative size dimensions. Use one at a time — they both describe vessel size from different angles and are correlated.
- Map: /geo/regioner.parquet — merge on omrade=dim_kode. Exclude omrade=0.