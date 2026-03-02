table: fact.skolm10
description: Musikskolers samarbejde med folkeskoler efter kommune, kunstart, klassetrin, undervisningskategori, nøgletal og tid
measure: indhold (unit Antal)
columns:
- komk: join dim.kommunegrupper on komk=kode; levels [2]
- kunstart: values [TOTK=Kunstart i alt, 1001=Musik, 1002=Visuel kunst, 1003=Håndværk og design, 1004=Scenekunst, 1005=Dans, 1006=Film og animation, 1007=Skrivekunst, 1008=Medier, 1009=Øvrige]
- klasse: values [KLTOT=Klassetrin i alt, 1100=Børnehaveklasse, 1101=1. klasse, 1102=2. klasse, 1103=3. klasse, 1104=4. klasse, 1105=5. klasse, 1106=6. klasse, 1107=7. klasse, 1108=8. klasse, 1109=9. klasse, 1110=10. klasse]
- undkat: values [3080=Undervisningsategorier i alt, 3085=Kulturklasser, 3090=Obligatorisk, 3095=Valgfag]
- bnogle: values [3050=Forløb, 3070=Deltagende elever, 3075=Undervisningstimer]
- tid: date range 2022 to 2025
dim docs: /dim/kommunegrupper.md

notes:
- komk joins dim.kommunegrupper at niveau 2 (98 kommuner). komk='0' is national total, not in the dim.
- bnogle is a measurement selector — 3050=Forløb, 3070=Deltagende elever, 3075=Undervisningstimer. Always filter to one bnogle value.
- klasse='KLTOT' and undkat='3080' are the totals for their dimensions. This table has 5 dimension columns (komk, kunstart, klasse, undkat, bnogle) — filter all non-target dimensions to totals to avoid overcounting.
- Most granular collaboration table: breaks down by school grade (klasse) and teaching category (obligatorisk, kulturklasse, valgfag).
- Map: context/geo/kommuner.parquet — merge on komk=dim_kode. Exclude komk=0.