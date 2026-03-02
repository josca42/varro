table: fact.erhv5
description: Arbejdssteder efter område, sektor og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [3]
- sektor: values [1015=Stat, 1020=Regioner, 1025=Kommuner, 1030=Sociale kasser og fonde, 1035=Offentlige virksomheder, 1040=Private virksomheder, 1045=Private nonprofit-organisationer]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- No `tal` selector — indhold is always number of workplaces (ARBSTED). No branch breakdown — use this specifically for sector × region questions.
- omrade joins dim.nuts at niveau=3 (99 kommuner). omrade='0' = Denmark total, '950' = unknown area — these are not in dim.nuts and are excluded by the join.
- sektor is a 7-value inline column with no total/aggregate code. Values are mutually exclusive public/private ownership categories. Sum across all sektor values to get total workplaces (or filter to one).
- Sample: workplaces by sektor nationally → filter omrade='0' to get Danish total without joining dim.nuts.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.