table: fact.ligehb6
description: Lægebesøg hos praktiserende læge efter område, køn, alder, familietype og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 0009=0-9 år, 1019=10-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8089=80-89 år, 9000=90 år og derover]
- famtype: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, EMHB=Enlige med hjemmeboende børn, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, PMHB=Par med hjemmeboende børn]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- GP visits only (no specialist/paramedic categories) — unlike sygk1 which covers all service types.
- omrade has niveau 1 (5 regioner) and niveau 3 (98 kommuner). omrade=0 is "Hele landet" (total, not in dim) — exclude when joining. Join clean otherwise (no uoplyst code).
- famtype hierarchy: TOT=total, F1/F2=families with/without children, E1=all singles, P1=all couples. EUHB/EMHB and PUHB/PMHB are sub-categories. Do not sum F1+F2+E1+P1 — they sum to the total. EUHB+EMHB=E1 and PUHB+PMHB=P1.
- alder uses 10-year groups (0009, 1019, ... 9000=90+) plus TOT. Note: code format is XXYY (e.g., 0009, not 0-9).
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
