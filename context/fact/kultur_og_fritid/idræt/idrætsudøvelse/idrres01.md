table: fact.idrres01
description: Idrætsresultater i OL-discipliner efter disciplin, land, præstation og tid
measure: indhold (unit Antal)
columns:
- diciplin: values [OLSOM=Discipliner ved Sommer-OL , OLVIN=Discipliner ved Vinter-OL]
- land: values [TOT=Hele verden, 5100=Danmark, 5706=Belarus, 5126=Belgien, 5128=Bulgarien ... 372=Nordamerika, 374=Asien, 375=Oceanien, 373=Syd-og Mellemamerika, 5999=Uoplyst]
- praestation: values [WIN005=Guldmedalje/1. plads, WIN010=Medaljer/Podie, WIN015=Top-8-placeringer]
- tid: date range 2016-01-01 to 2024-01-01

notes:
- praestation values are CUMULATIVE/nested: guldmedalje (WIN005) ≤ medaljer/podie (WIN010) ≤ top-8 (WIN015). Never sum across praestation — always filter to one value.
- land TOT = hele verden. land 5100 = Danmark. The land column contains both individual countries and continental aggregates (e.g., 372=Nordamerika, 374=Asien) — mixing them causes double-counting.
- diciplin has only 2 values: OLSOM (sommer-OL) and OLVIN (vinter-OL). Filter if you only want one type.
- indhold = count of medals/placings. Each OL year is one tid value (2016, 2020/2021→2021-01-01, 2024).