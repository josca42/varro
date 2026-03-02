table: fact.ferieh6
description: Udlejning af feriehuse på månedsbasis efter område, gæstens nationalitet, enhed, periode og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- nation1: values [TOT=I alt, DAN=Danmark, HOL=Nederlandene, SVE=Sverige, NOR=Norge, TYS=Tyskland, ANDRE=Uoplyst land]
- tal: values [1270=Overnatninger, 1280=Udlejede hus-uger, 1290=Kontrakter, 1300=Disponible husuger]
- periode: values [1=Hele året, 2=År til dato, 1=Januar, 2=Februar, 3=Marts, 4=April, 5=Maj, 6=Juni, 7=Juli, 8=August, 9=September, 10=Oktober, 11=November, 12=December]
- tid: date range 2017-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts across 3 levels: niveau=1 (5 regions, kode 81–85), niveau=2 (10 landsdele, kode 2–11), niveau=3 (98 kommuner, kode 101+). Filter d.niveau to pick granularity and avoid double-counting across hierarchy levels.
- Four omrade codes are NOT in dim.nuts: 0 = "Hele landet" (national total), 12 = "Diskretionerede kommuner, Region Sjælland", 13 = "Diskretionerede kommuner, Region Syddanmark", 14 = "Diskretionerede kommuner, Region Midtjylland". These are privacy-suppressed municipalities grouped at region level. Use LEFT JOIN if you want to include them.
- Use ColumnValues("nuts", "titel", for_table="ferieh6") to browse the 113 matched area codes. The 4 unmatched codes (0, 12, 13, 14) won't appear in ColumnValues output.
- tal is a measurement selector (4 values: 1270=Overnatninger, 1280=Udlejede hus-uger, 1290=Kontrakter, 1300=Disponible husuger). Always filter to one tal value.
- periode has the same overloaded-code issue as ferieh1: periode=1 = both "Hele året" AND "Januar"; periode=2 = both "År til dato" AND "Februar". For unambiguous monthly data use periode >= 3. For annual totals use periode=1 but expect two rows per (omrade, nation1, tal, tid) — the larger value is Hele året.
- nation1=TOT is the total across nationalities; do not sum across all nation1 values.
- tid is always Jan 1 of the reporting year (2017–2025).
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade IN (0, 12, 13, 14).