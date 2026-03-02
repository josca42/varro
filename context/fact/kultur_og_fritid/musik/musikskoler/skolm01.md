table: fact.skolm01
description: Musikskoler efter kommune, nøgletal og tid
measure: indhold (unit -)
columns:
- komk: join dim.kommunegrupper on komk=kode; levels [2]
- aktp: values [10110=Sæsonlængde under 36 uger, 10113=Sæsonlængde 36 uger, 10116=Sæsonlængde over 36 uger, 10120=Musikskoler - selvejende, 10130=Musikskoler - kommunale, 10200=Aflønning af kontaktlærere i folkeskolen, 10210=Uformel kontakt til folkeskolen, 10290=Musikskoler med nedsat deltagerbetaling pga. trang, 10300=Musikskoler med søskenderabat, 10310=Musikskoler med flerfagsrabat, 10320=Musikskoler med instrumentleje, 10330=Pris for leje af violin (Kr.)                                                      , 10420=Musikskoler med obligatorisk sammenspil (inkluderet i instrumentfag), 10425=Musikskoler med obligatorisk sammenspil (særskilt betaling)]
- tid: date range 2021 to 2025
dim docs: /dim/kommunegrupper.md

notes:
- komk joins dim.kommunegrupper at niveau 2 (98 kommuner). komk='0' is the national total and is not in the dim — exclude with WHERE f.komk != '0' or use LEFT JOIN when you want it.
- aktp is a measurement selector, not a category to aggregate across. Each code is a distinct key figure with different semantics: some count schools with a specific feature (e.g. 10300=schools offering søskenderabat), one is a price (10330=violin rental price in Kr.). Always filter to a single aktp value before using indhold.
- No TOT row for aktp — each aktp code is an independent metric. Query one at a time.
- Map: context/geo/kommuner.parquet — merge on komk=dim_kode. Exclude komk=0.