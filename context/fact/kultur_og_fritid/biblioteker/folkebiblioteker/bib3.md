table: fact.bib3
description: Folkebibliotekernes fysiske materialer efter område, samling, opgørelse, materialetype og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- samling: values [35=Børnesamling, 39=Voksen samling]
- opgoer1: values [11=Bestand, 12=Tilvækst, 13=Afgang, 14=Udlån, 15=Fornyelse af udlån (-2015)]
- mater: values [500=Alle materialetyper, 560=I ALT, MONOGRAFIER, 503=Bøger, 506=Noder (trykte), 509=Kartografiske materiale (trykt) ... 548=Andet lyd (digital), 551=Genstande, 554=Sammensat materiale, 557=Andre materialer, 563=Seriepublikationer]
- tid: date range 2009-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (97 kommuner). omrade=0 = Hele landet.
- 4 active filter dimensions (omrade, samling, opgoer1, mater) — filter all four to avoid overcounting.
- opgoer1 is a measurement type selector: 11=Bestand, 12=Tilvækst, 13=Afgang, 14=Udlån, 15=Fornyelse (-2015). Always filter to one.
- samling: 35=Børnesamling, 39=Voksen samling. Filter to one unless you want both.
- mater contains hierarchy: 500=Alle materialetyper (grand total), 560=I ALT MONOGRAFIER (subtotal) — don't mix with individual material type codes or you double-count.
- Typical query for adult book loans by region: SELECT d.titel, SUM(f.indhold) FROM fact.bib3 f JOIN dim.nuts d ON f.omrade=d.kode WHERE f.opgoer1='14' AND f.samling='39' AND f.mater='503' AND d.niveau=1 GROUP BY d.titel.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
