table: fact.arealan1
description: Arealanvendelse efter branche (19a2-gruppering), område, enhed og tid
measure: indhold (unit -)
columns:
- br19a2: values [TOTAREAL=I alt, VREKREA=Rekreative faciliteter, EHUSHOLD=Husholdninger, VA=A Landbrug, skovbrug og fiskeri, V01000=01000 Landbrug og gartneri ... VQ=Q Sundhed og socialvæsen, VR=R Kultur og fritid, VSA=SA Andre serviceydelser, VSB=SB Private husholdninger med ansat medhjælp, VX=X Uden kendt eller specifik anvendelse]
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- enhed: values [120=Kvadratkilometer (km2), 130=Kvadratmeter (m2) pr. indbygger, 140=Procent]
- tid: date range 2016-01-01 to 2016-01-01
dim docs: /dim/nuts.md

notes:
- Single year snapshot (2016 only). Not useful for time-series analysis.
- enhed is a measurement selector (120=km2, 130=m2 pr. indbygger, 140=%). Always filter to one enhed. Forgetting triples all counts.
- br19a2 has a two-level hierarchy: TOTAREAL is the grand total; top-level codes (VA, VB, VC, ... VX, EHUSHOLD, VREKREA) sum to TOTAREAL; sub-codes (V01000, V02000, V03000 under VA, etc.) are sub-categories. Summing parent and child codes double-counts. The top-level letters map to NACE sections (VA=Landbrug/skovbrug/fiskeri, VB=Råstofindvinding, etc.).
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 2 (11 landsdele) — no municipality breakdown. Filter d.niveau to pick one level. omrade='0' is "Hele landet" (not in dim.nuts).
- Use ColumnValues("arealan1", "br19a2") to see all industry land-use codes with their labels.
- Map: /geo/landsdele.parquet (niveau 2) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.