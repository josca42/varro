table: fact.camp3
description: Campingpladser efter område, kapacitet og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- kapacitet: values [1220=Antal campingpladser - max., 1230=Antal campingpladser - min., 1240=Antal campingenheder - max., 1250=Antal campingenheder - min., 1260=Kapacitetsudnyttelse (pct.)]
- tid: date range 1992-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 1 only (5 regioner: 81–85). omrade=0 is the national total (Hele landet), not in dim.nuts.
- kapacitet is a measurement selector with 5 independent values: 1220=Antal campingpladser max, 1230=Antal campingpladser min, 1240=Antal campingenheder max, 1250=Antal campingenheder min, 1260=Kapacitetsudnyttelse pct. Always filter to one value. Max/min refer to within-year seasonal variation; they should not be summed.
- tid is annual (YYYY-01-01). This is the annual view of capacity with seasonal max/min. For monthly capacity data use camp2 instead.
- kapacitetsudnyttelse (1260) is a percentage — do not SUM across regions; use AVG if aggregating.
- Map: context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.