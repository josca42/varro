table: fact.sitc5r4y
description: Im- og eksport (Rev. 4 SITC) efter im- og eksport, SITC-hovedgrupper, land, enhed og tid
measure: indhold (unit -)
columns:
- indud: values [1=Import, 2=Eksport]
- sitc: join dim.sitc on sitc=kode; levels [3]
- land: join dim.lande_uhv on land=kode; levels [4]
- enhed: values [98=Kilo, 99=Kroner]
- tid: date range 2007-01-01 to 2021-01-01
dim docs: /dim/lande_uhv.md, /dim/sitc.md

notes:
- sitc is at niveau 3 (5-digit SITC subgroups). All matched codes are niveau 3.
- enhed is a MEASUREMENT SELECTOR: every combination appears twice (98=Kilo, 99=Kroner). Always filter — use enhed='99' for DKK.
- No uhbegreb column.
- Annual data 2007–2021. Best table for long annual series at 5-digit SITC granularity with both value and quantity.