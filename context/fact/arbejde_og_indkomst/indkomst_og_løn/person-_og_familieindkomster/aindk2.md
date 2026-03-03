table: fact.aindk2
description: A-indkomst i alt efter område, enhed, køn, alder, indkomstinterval og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2, 3]
- enhed: values [103=Personer i gruppen (antal), 110=Indkomstbeløb (1.000 kr.), 118=Gennemsnit for personer i gruppen (kr.)]
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- alder1: values [00=I alt, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 74-00=Over 74 år]
- indkintb: values [0=Alle, 10=Under 25.000 kr., 20=25.000 - 49.999 kr., 30=50.000 - 74.999 kr., 40=75.000 - 99.999 kr., 105=100.000 - 124.999 kr., 115=125.000 - 149.999 kr., 125=150.000 - 174.999 kr., 130=175.000 - 199.999 kr., 135=200.000 - 224.999 kr., 255=225.000 - 249.999 kr., 300=250.000 - 299.999 kr., 350=300.000 - 349.999 kr., 400=350.000 - 399.999 kr., 450=400.000 - 449.999 kr., 500=450.000 - 499.999 kr., 905=500.000 kr. og derover]
- tid: date range 2012-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at levels 2 (landsdele) and 3 (kommuner). Filter WHERE d.niveau=... when joining.
- omrade='0' is national aggregate, not in dim.nuts.
- indkintb='0' is "Alle" (total). Fine 25k-step brackets up to 500k+.
- alder1='00' is the total.
- enhed selector (3 types). Always filter to one.
- koen='MOK' is total. Only from 2012. Shows A-indkomst i alt distribution by income bracket — use aindk1 for breakdown by income type.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.
