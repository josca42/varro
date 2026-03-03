table: fact.idrfac01
description: Idrætsfaciliteter efter område, facilitetstype og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2, 3]
- idrfac: values [FAC1=Atletikanlæg, FAC2=Badmintonhaller, FAC3=Curlinghaller, FAC4=Fitnesscentre, FAC5=Fodboldanlæg ... FAC24=Padelanlæg, FAC25=Squashcentre, FAC26=Klatreanlæg, FAC27=Motorsportsanlæg, FAC28=MTB-spor og cykelanlæg]
- tid: date range 2017-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveaus 2 (11 landsdele) and 3 (98 kommuner). Always filter d.niveau to avoid mixing levels and double-counting. Use `ColumnValues("nuts", "titel", for_table="idrfac01")` to see available codes.
- omrade=0 is the national total (Danmark I alt) — not in dim.nuts. Use it directly to get a country-level number without joining.
- idrfac has 28 distinct facility types (FAC1–FAC28), no total/aggregate code. Summing all 28 gives total facility count. Use ColumnValues("idrfac01", "idrfac") to see the full label mapping.
- Example: facilities by landsdel: JOIN dim.nuts ON omrade=kode AND niveau=2, filter to desired idrfac and tid.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.