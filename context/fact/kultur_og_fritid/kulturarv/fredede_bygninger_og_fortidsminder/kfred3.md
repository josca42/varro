table: fact.kfred3
description: Nyfredninger og affredninger efter enhed, område og tid
measure: indhold (unit Antal)
columns:
- enhed: values [1=Fortidsminder - Nyfredning, 2=Fortidsminder - afffredning, 3=Bygninger - nyfredning, 4=Bygninger - affredning]
- omrade: join dim.nuts on omrade=kode; levels [1]
- tid: date range 2012-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau=1 only (5 regioner: 81–85). Code 0 = landstal (national total) — not in dim.
- enhed selects between 4 independent series: 1=Fortidsminder nyfredning, 2=Fortidsminder affredning, 3=Bygninger nyfredning, 4=Bygninger affredning. Always filter to the specific enhed(s) you want — never sum across all 4 as it mixes fortidsminder and bygninger counts.
- To get net change in protected buildings: query enhed=3 (nyfredning) minus enhed=4 (affredning) for the same omrade and tid.
- Sample: annual new protected buildings nationally: SELECT tid, indhold FROM fact.kfred3 WHERE enhed='3' AND omrade='0' ORDER BY tid
- Map: context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.