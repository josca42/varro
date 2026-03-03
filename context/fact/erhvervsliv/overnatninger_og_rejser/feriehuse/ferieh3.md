table: fact.ferieh3
description: Udlejning af feriehuse efter område, gæstens nationalitet, enhed og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- nation1: values [TOT=I alt, DAN=Danmark, HOL=Nederlandene, SVE=Sverige, NOR=Norge, TYS=Tyskland, ANDRE=Uoplyst land]
- tal: values [1270=Overnatninger, 1280=Udlejede hus-uger, 1290=Kontrakter]
- tid: date range 1992-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts but code 0 = "Hele landet" (national total) is NOT in dim.nuts — a plain JOIN excludes it. Use LEFT JOIN or add WHERE omrade != 0 if you only want regional rows.
- Two nuts hierarchy levels are used: niveau=1 (5 regions, kode 81–85) and niveau=2 (9 landsdele, kode 3–11; landsdele 1 and 2 are not present). Filter d.niveau to pick your granularity and avoid double-counting across levels.
- Use ColumnValues("nuts", "titel", for_table="ferieh3") to see the 14 area codes in this table.
- tal is a measurement selector (3 values: 1270=Overnatninger, 1280=Udlejede hus-uger, 1290=Kontrakter — note: no 1300=Disponible husuger here unlike ferieh1/ferieh6). Always filter to one tal value.
- nation1=TOT is the national total; do not sum across all nation1 values.
- tid is always Jan 1 of the reporting year (1992–2024 annual data).
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.