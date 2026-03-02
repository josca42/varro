table: fact.kvotien
description: Klassekvotienter i grundskolen efter område, klassetrin, skoletype og tid
measure: indhold (unit Kvotienter)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- klasse: values [0=I alt, 1100=Børnehaveklasse, 1101=1. klasse, 1102=2. klasse, 1103=3. klasse, 1104=4. klasse, 1105=5. klasse, 1106=6. klasse, 1107=7. klasse, 1108=8. klasse, 1109=9. klasse, 1110=10./11. klasse]
- sktpe: values [ANTALSUM=I alt, ANTAL1012=Folkeskoler, ANTAL1013=Frie grundskoler]
- tid: date range 2009-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- indhold is a class size ratio (kvotient), not a headcount. Do NOT sum across areas or school types — use AVG or report individually.
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (99 kommuner). No niveau 2. Code 0 = national aggregate, not in dim.
- sktpe: ANTALSUM=total, ANTAL1012=folkeskoler, ANTAL1013=frie grundskoler. Always filter to one to avoid mixing.
- klasse='0' is the total across all class levels (børnehaveklasse through 10./11. klasse).
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.