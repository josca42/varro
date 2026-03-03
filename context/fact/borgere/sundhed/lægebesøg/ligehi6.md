table: fact.ligehi6
description: Ligestillingsindikator for lægebesøg hos praktiserende læge efter indikator, område, alder, familietype og tid
measure: indhold (unit -)
columns:
- indikator: values [M11=Mænd (pr. person), K11=Kvinder (pr. person), F11=Forskel mellem mænd og kvinder (point, pr. person)]
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- alder: values [TOT=Alder i alt, 0009=0-9 år, 1019=10-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8089=80-89 år, 9000=90 år og derover]
- famtype: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, EMHB=Enlige med hjemmeboende børn, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, PMHB=Par med hjemmeboende børn]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Equality indicator table — indhold values are NOT counts but derived rates/differences. Do NOT sum across indikator values.
- indikator: M11=visits per man, K11=visits per woman, F11=gender gap (M11 minus K11 in points). Read each row independently.
- omrade has niveau 1 (5 regioner) and niveau 3 (98 kommuner). omrade=0 is "Hele landet" — exclude when joining dim.nuts.
- famtype same hierarchy as ligehb6: TOT, F1, F2, E1, P1 are top-level; EUHB/EMHB sub-divide E1, PUHB/PMHB sub-divide P1.
- alder uses 10-year groups (0009, 1019, ... 9000=90+) plus TOT.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
