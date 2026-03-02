table: fact.kunst2
description: Kunstnere efter kunstområde, bopælsregion og tid
measure: indhold (unit Antal)
columns:
- kunstomr: values [TOTK=Kunstområde i alt, 1000=Musik, 1010=Forfattere og ord, 1020=Billedkunst og formgivere, 1030=Film og TV, 1040=Skuespil og scenekunst]
- bopreg: join dim.nuts on bopreg=kode; levels [1]
- tid: date range 2022-01-01 to 2022-01-01
dim docs: /dim/nuts.md

notes:
- Only covers a single year (2022).
- bopreg joins dim.nuts at niveau=1 (5 regioner: 81–85). Code 0 is national total, not in dim. Filter or exclude code 0 when joining.
- Join: SELECT f.*, d.titel FROM fact.kunst2 f LEFT JOIN dim.nuts d ON f.bopreg::text = d.kode WHERE d.niveau = 1
- Map: context/geo/regioner.parquet — merge on bopreg=dim_kode. Exclude bopreg=0.