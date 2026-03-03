table: fact.indkp222
description: Personlig indkomst før skat for personer over 14 år efter område, køn, alder, indkomstinterval, prisenhed og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2, 3]
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- alder: values [00=I alt, 15-19=15-19 år, 20-29=20-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70-79=70-79 år, 80-00=80 år og derover]
- indkints: values [0=Alle, 10=Under 25.000 kr., 20=25.000 - 49.999 kr., 30=50.000 - 74.999 kr., 40=75.000 - 99.999 kr. ... 599=550.000 - 599.999 kr., 649=600.000 - 649.999 kr., 699=650.000 - 699.999 kr., 749=700.000 - 749.999 kr., 750=750.000 kr. og derover]
- prisenhed: values [5=Faste priser (seneste dataårs prisniveau), 6=Nominelle priser]
- tid: date range 2000-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at levels 2 (landsdele) and 3 (kommuner). Filter WHERE d.niveau=... when joining.
- omrade='0' is national aggregate, not in dim.nuts.
- indkints='0' is "Alle" (total). Note: column name is indkints (not indkintb). Brackets slightly coarser than indkp221 (upper end caps at 750k+ vs 1M+ in indkp221).
- prisenhed is a selector (faste vs. nominelle). Always filter to one.
- alder uses broader 10-year groups (not 5-year like indkp221). alder='00' is total.
- koen='MOK' is total.
- indhold = Antal (count of persons in each bracket).
- Map: /geo/kommuner.parquet (niveau 3) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.
