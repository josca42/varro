table: fact.kuiv2
description: Kulturiværksætteri efter område, enhed og tid
measure: indhold (unit -)
columns:
- omr20: join dim.nuts on omr20=kode; levels [2]
- enhed: values [30=Job ultimo november, 50=Nye virksomheder]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- enhed is a measurement selector: 30=Job ultimo november, 50=Nye virksomheder. Always filter to one.
- omr20 joins dim.nuts at niveau=2 (11 landsdele, codes 1–11). Code 0 is national total, not in dim.
- Join: SELECT f.*, d.titel FROM fact.kuiv2 f JOIN dim.nuts d ON f.omr20::text = d.kode WHERE d.niveau = 2 AND f.omr20 != 0
- Map: /geo/landsdele.parquet — merge on omr20=dim_kode. Exclude omr20=0.