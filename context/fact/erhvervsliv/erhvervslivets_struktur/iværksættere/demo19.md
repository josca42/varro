table: fact.demo19
description: Erhvervsdemografi efter kommune, enhed og tid
measure: indhold (unit Antal)
columns:
- regi07a: join dim.nuts on regi07a=kode; levels [3]
- maengde4: values [AFU=Fuldtidsansatte (antal), NYE=Nye firmaer (antal)]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- regi07a joins dim.nuts at niveau 3 (kommuner, 98 kommuner). Code 0 = national total (not in dim.nuts) — exclude regi07a = 0 when aggregating by kommune.
- maengde4 is a measurement selector — filter to one: AFU=fuldtidsansatte, NYE=nye firmaer.
- Finest geographic granularity in this subject. Use ColumnValues("nuts", "titel", for_table="demo19") to browse the 98 kommuner available.
- To roll up to region level, join via dim.nuts hierarchy: kommune (niveau 3) → landsdel (niveau 2) → region (niveau 1).
- Map: /geo/kommuner.parquet — merge on regi07a=dim_kode. Exclude regi07a=0.