table: fact.eb3
description: Børn af efterkommere 1. januar efter Oprindelig herkomst, køn, alder, oprindelsesland, område og tid
measure: indhold (unit Antal)
columns:
- opher: values [D=Oprindelig person med dansk oprindelse, E=Oprindelig efterkommer]
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- ieland: values [1=Vestlige lande, 2=Ikke-vestlige lande]
- omrade: join dim.nuts on omrade=kode; levels [3]
- tid: date range 2007-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade is niveau=3 only (98 kommuner). No national total code in this table (audit shows 98/98 match, all niveau=3). SUM across all kommuner for national totals.
- ieland is simplified: 1=Vestlige lande, 2=Ikke-vestlige lande. No total. SUM both for all-origin counts.
- Like eb2 but adds municipal (niveau=3) geographic breakdown. Use when you need børn af efterkommere by region.
- alder in 5-year bands (like eb1). No total band.
- No total row for opher or kon. SUM across all categories for aggregates.
- Map: /geo/kommuner.parquet — merge on omrade=dim_kode. No omrade=0 in this table (all rows are kommuner).