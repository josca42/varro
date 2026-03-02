table: fact.fohoj01
description: Antallet af højskolekursister efter kursustype, køn, alder, herkomst, enhed, tidsangivelse og tid
measure: indhold (unit Antal)
columns:
- kursus: values [TOT=I alt, 40=Kort kursus, 50=Mellemlangt kursus, 60=Langt kursus]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [0000=Alder i alt, U20=Under 20 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 50OV=50 år og derover]
- herkomst: values [TOT=I alt, 1=Personer med dansk oprindelse, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande, 85=Uoplyst mv.]
- enhed: values [11=Kursister, 13=Årselever]
- tidspunkter: values [22=Skoleår, 11=Kalenderår]
- tid: date range 2016-01-01 to 2024-01-01

notes:
- `enhed` (11=Kursister, 13=Årselever) and `tidspunkter` (11=Kalenderår, 22=Skoleår) are both measurement selectors — always filter both. Both are smallint.
- 2024 data only has tidspunkter=22 (Skoleår). For Kalenderår, the latest available year is 2023.
- `alder` total code is `'0000'`. Individual age codes are text: `U20`, `2029`, `3039`, `4049`, `50OV` — not numeric ranges.
- `kursus`, `kon`, `herkomst` are varchar; `enhed` and `tidspunkter` are smallint. Use integer literals for the latter two.
- Simple total: `SELECT tid, indhold FROM fact.fohoj01 WHERE kursus='TOT' AND kon='TOT' AND alder='0000' AND herkomst='TOT' AND enhed=11 AND tidspunkter=11`