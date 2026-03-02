table: fact.sitc5r4m
description: Im- og eksport (Rev. 4 SITC) efter im- og eksport, SITC-hovedgrupper, land, enhed og tid
measure: indhold (unit -)
columns:
- indud: values [1=Import, 2=Eksport]
- sitc: join dim.sitc on sitc=kode; levels [3]
- land: join dim.lande_uhv on land=kode; levels [4]
- enhed: values [98=Kilo, 99=Kroner]
- tid: date range 2007-01-01 to 2013-12-01
dim docs: /dim/lande_uhv.md, /dim/sitc.md

notes:
- sitc is at niveau 3 (5-digit SITC subgroups). All matched codes are niveau 3 — no hierarchy mixing.
- enhed is a MEASUREMENT SELECTOR: every combination appears twice (98=Kilo, 99=Kroner). Always filter.
- No uhbegreb column — simpler than sitc5r4.
- Monthly data 2007–2013 only. For 2014–2021 there is a gap; use sitc5r4y for annual. Use sitc5r4 for current (2022+).