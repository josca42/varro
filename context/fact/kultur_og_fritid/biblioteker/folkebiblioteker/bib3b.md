table: fact.bib3b
description: Folkebibliotekernes fysiske materialer efter område, samling, opgørelse, materialetype, alder og tid
measure: indhold (unit Pct.)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- samling: values [35=Børnesamling, 39=Voksen samling]
- opgoer1: values [14=Udlån, 15=Fornyelse af udlån (-2015)]
- mater: values [500=Alle materialetyper, 560=I ALT, MONOGRAFIER, 503=Bøger, 506=Noder (trykte), 509=Kartografiske materiale (trykt) ... 548=Andet lyd (digital), 551=Genstande, 554=Sammensat materiale, 557=Andre materialer, 563=Seriepublikationer]
- alerams: values [0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-84=80-84 år, 85-89=85-89 år, 90-94=90-94 år, 95-=95 år og derover]
- tid: date range 2010-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Like bib3 but shows percentage distribution of loans/renewals by age group (Pct.), not absolute counts.
- opgoer1 limited to 14=Udlån and 15=Fornyelse af udlån (-2015). No Bestand/Tilvækst/Afgang.
- alerams: 5-year age bands from 0-4 through 95+. No total row — values represent each band's share of the selected collection+materialtype+area combination.
- Still requires filtering samling (35 or 39) and mater (use 500 for all types, or a specific type) to avoid mixing.
- omrade joins dim.nuts at niveau 1 and niveau 3. omrade=0 = Hele landet.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
