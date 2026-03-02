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
- CRITICAL: enhed and tidspunkter are both measurement selectors — every dimension combination is repeated 4 times (2 enhed × 2 tidspunkter). Always filter BOTH to a single value or the count is 4× inflated.
- enhed: 11=Kursister (headcount, a person attending two courses counts twice), 13=Årselever (full-time equivalent student-years). Pick based on question.
- tidspunkter: 22=Skoleår (school year), 11=Kalenderår (calendar year). For most analyses, pick one consistently.
- kursus=TOT, kon=TOT, alder=0000, herkomst=TOT are totals. Filter unused dimensions.
- Covers all course types (short/medium/long). For course-type-specific demographic detail, see fohoj02a/02b (medium+long) or fohoj03a/03b (short).
