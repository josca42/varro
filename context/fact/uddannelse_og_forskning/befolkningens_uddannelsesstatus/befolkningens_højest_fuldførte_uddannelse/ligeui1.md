table: fact.ligeui1
description: Ligestillingsindikator for befolkningens højeste fuldførte uddannelse (15-69 år) efter højest fuldførte uddannelse, indikator, alder, bopælsområde, herkomst og tid
measure: indhold (unit -)
columns:
- uddannelsef: values [TOT=I alt, H10=H10 Grundskole, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H35=H35 Adgangsgivende uddannelsesforløb, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser, H90=H90 Uoplyst mv.]
- indikator1: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- alder1: values [TOT=Alder i alt, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år]
- bopomr: join dim.nuts on bopomr=kode; levels [1, 3]
- herkams: values [0=I alt, 10=Personer med dansk oprindelse, 21=Indvandrere i alt, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 31=Efterkommere i alt, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande]
- tid: date range 2005-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- indikator1 is a MEASUREMENT SELECTOR — always filter to exactly one value: LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mænd-kvinder (procentpoint). Every dimension combination appears 3 times, once per indicator. Never sum across indikator1 values.
- indhold unit varies by indikator1: pct. for LA1/LA2, procentpoint for LA3. The column header says unit="-" because it's mixed.
- bopomr joins dim.nuts (smallint). 0=national total (not in dim), niveau 1=5 regioner, niveau 3=99 kommuner. Use ColumnValues("nuts", "titel", for_table="ligeui1") to see available codes.
- herkams is hierarchical inline: 0=I alt, 10=Dansk oprindelse, 21=Indvandrere i alt (=24+25), 31=Efterkommere i alt (=34+35). Filter to one level.
- Use ligeui0 instead if you don't need regional or herkomst breakdowns — it has data back to 1986.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.