table: fact.akv11
description: Akvakultur efter anlægstype, enhed, fiske- og skaldyrsarter og tid
measure: indhold (unit -)
columns:
- anlaeg: values [0=Alle anlæg, 6=Traditionelle dambrug, 11=Anlæg med lav recirkulation , 12=Anlæg med middelhøj recirkulation, 13=Anlæg med høj recirkulation , 25=Havbrug, 36=Muslinge- og østersanlæg, 38=Tang, 42=Anden akvakultur ]
- tal: values [10=Mængde i tons, 20=Værdi i 1000 kr.]
- fiskskal: values [100=Total, 110=Ørred og laks, 120=Ål, 140=Blåmusling, 130=Andre arter]
- tid: date range 2021-01-01 to 2023-01-01

notes:
- tal is a measurement selector: 10=tons, 20=1000 kr. Every anlaeg×fiskskal combination is duplicated for each unit. Always filter to one value (e.g. WHERE tal=10 for quantity, WHERE tal=20 for value). Forgetting this doubles the sum.
- fiskskal=100 is the Total row that already includes all species (110, 120, 130, 140). Filter to fiskskal=100 for a total, or filter to specific species — do not sum across all including 100, as this double-counts.
- anlaeg=0 is Alle anlæg which already includes all facility subtypes. Same rule: pick either the aggregate (anlaeg=0) or sum the parts (anlaeg IN (6,11,12,13,25,36,38,42)), not both.
- Use ColumnValues("akv11", "fiskskal") and ColumnValues("akv11", "anlaeg") to see the full code→label mappings before querying.
- Only 3 years of data (2021–2023). For longer series use akregn1 (from 2017) but note it covers financials, not production volumes.