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
- Single-year snapshot: only 2016 data. Not useful for time series.
- omrade joins dim.nuts. Codes 81-85 = niveau 1 (5 regioner), codes 1-11 = niveau 2 (11 landsdele). Code 0 = national total (not in dim.nuts — left join returns NULL). Use ColumnValues("nuts", "titel", for_table="arealan1") to see the 16 joinable regions.
- enhed is a measurement selector (km2, m2/person, pct). Filter to one value — e.g. WHERE enhed='120' — to avoid tripling the count.
- br19a2 includes TOTAREAL (grand total) plus many branch codes. Do not sum TOTAREAL together with individual branches — double counting. Either use TOTAREAL alone or sum leaf codes.
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.