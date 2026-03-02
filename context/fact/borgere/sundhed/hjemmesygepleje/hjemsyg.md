table: fact.hjemsyg
description: Modtagere af hjemmesygepleje (eget hjem) efter område, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- alder1: values [50=Alder i alt, 100=Under 65 år, 375=65-69 år, 400=70-74 år, 500=75-79 år, 600=80-84 år, 700=85-89 år, 800=90 år og derover]
- koen: values [100=Mænd og kvinder i alt, 200=Mænd, 300=Kvinder]
- tid: date range 2016-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 3 only (98 kommuner). Use ColumnValues("nuts", "titel", for_table="hjemsyg") to browse available municipalities. No regional aggregates — this table is kommuner-only.
- koen and alder1 both include totals (koen=100, alder1=50). To get a single count per municipality, filter both: WHERE koen=100 AND alder1=50. Omitting either doubles or multiplies the sum.
- alder1 groups are: under 65, then five-year bands from 65–69 up to 90+. No finer age breakdown. To get elderly recipients, sum the 65+ bands or use alder1=50 and filter koen only.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.