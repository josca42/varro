table: fact.camp2
description: Campingpladser efter område, kapacitet og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- kapacitet: values [1200=Antal campingpladser, 1210=Campingenheder (antal), 1260=Kapacitetsudnyttelse (pct.)]
- tid: date range 1992-03-01 to 2025-08-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 1 only (5 regioner: 81–85). omrade=0 is the national total (Hele landet), not in dim.nuts. Filter to one omrade or use the national total; never sum across all omrade values including 0.
- kapacitet is a measurement selector — 1200=Antal campingpladser (number of sites), 1210=Campingenheder (number of camping units/pitches), 1260=Kapacitetsudnyttelse pct. These are completely different metrics; always filter to one value. Never sum across kapacitet values.
- tid is monthly (YYYY-MM-01). This is the monthly view of capacity, covering the camping season (March–December). camp3 is the annual equivalent with seasonal min/max figures.
- kapacitetsudnyttelse (1260) is a percentage — do not SUM it; take an average if aggregating across regions.
- Map: context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.