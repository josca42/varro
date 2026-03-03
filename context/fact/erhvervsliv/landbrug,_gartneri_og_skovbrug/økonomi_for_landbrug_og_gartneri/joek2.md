table: fact.joek2
description: Økonomien i jordbrugssektoren efter region, produkt og tid
measure: indhold (unit Mio. kr.)
columns:
- region: join dim.landbrugslandsdele on region::text=kode [approx: Fact has integer (84), dimension has zero-padded string (084)]
- produkt: values [180000=1 JORDBRUGSSEKTORENS SAMLEDE PRODUKTION AF VARER OG YDELSER I ALT (2 + 7), 160000=2 JORDBRUGETS PRODUKTION I ALT (3 + 6), 140000=3 JORDBRUGETS SALGSPRODUKTER I ALT (4 + 5), 100000=4 VEGETABILSK PRODUKTION, 10000=4.1 Korn ... 350000=20 Renteudgifter, 360000=21 Renteindtægter, 370000=22 VIRKSOMHEDSINDKOMST (18 - 19 - 20 + 21), 380000=23 Lagerændringer, 390000=24 Kapitaloverførsler]
- tid: date range 2022-01-01 to 2023-01-01
dim docs: /dim/landbrugslandsdele.md
notes:
- region is stored as integers (81–85 + 0) but dim.landbrugslandsdele uses zero-padded strings (081–085). Join with: `JOIN dim.landbrugslandsdele d ON LPAD(f.region::text, 3, '0') = d.kode AND d.niveau = 1`. The 5 codes correspond to the 5 Danish regions. Code 0 = hele landet, not in dim.
- produkt hierarchy is the same nested accounting tree as joek1, but a narrower subset. Pick a specific aggregate or leaf; never sum all produkt rows.
- Only 2 years of data (2022–2023). For the national series including 2024 use joek1 (no regional split there).
- Map: /geo/regioner.parquet — merge on region=dim_kode (5 standard regions, codes 81–85). Exclude region=0.
