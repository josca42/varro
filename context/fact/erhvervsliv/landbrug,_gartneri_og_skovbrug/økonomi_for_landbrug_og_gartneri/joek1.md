table: fact.joek1
description: Økonomien i jordbrugssektoren efter produkt, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- produkt: values [180000=1 JORDBRUGSSEKTORENS SAMLEDE PRODUKTION AF VARER OG YDELSER I ALT (2 + 7), 160000=2 JORDBRUGETS PRODUKTION I ALT (3 + 6), 140000=3 JORDBRUGETS SALGSPRODUKTER I ALT (4 + 5), 100000=4 VEGETABILSK PRODUKTION, 10000=4.1 Korn ... 370000=22 VIRKSOMHEDSINDKOMST (18 - 19 - 20 + 21), 380000=23 Lagerændringer, 390000=24 Kapitaloverførsler, 391000=24.1 Investeringstilskud, 399000=24.2 Andre kapitaloverførsler]
- prisenhed: values [0=Løbende priser, 5=Faste priser (sidste år)]
- tid: date range 2022-01-01 to 2024-01-01
notes:
- prisenhed is a measurement selector: every (produkt, tid) combination appears twice — once at løbende priser (0) and once at faste priser (5). Always filter to ONE prisenhed or sums double.
- produkt is a deeply hierarchical accounting tree. Six-digit codes (180000, 160000, 140000…) are top-level aggregates; five- and lower-digit codes are sub-items. Never sum across all produkt rows — filter to the specific aggregate or leaf-level items you need.
- Only 3 years of data (2022–2024). For regional breakdown use joek2 (but note joek2 only covers 2022–2023).
