table: fact.indkp221
description: Personlig indkomst før skat for personer over 14 år efter køn, alder, prisenhed, indkomstinterval og tid
measure: indhold (unit Antal)
columns:
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- alder: values [14TOT=I alt, 15 år og derover, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-00=80 år og derover]
- prisenhed: values [5=Faste priser (seneste dataårs prisniveau), 6=Nominelle priser]
- indkints: values [0=Alle, 10=Under 25.000 kr., 20=25.000 - 49.999 kr., 30=50.000 - 74.999 kr., 40=75.000 - 99.999 kr. ... 649=600.000 - 649.999 kr., 699=650.000 - 699.999 kr., 749=700.000 - 749.999 kr., 751=750.000 - 999.999 kr., 950=1.000.000 kr. og derover]
- tid: date range 1995-01-01 to 2024-01-01
notes:
- indhold = Antal (count of persons). This table shows the income distribution by count — not an income amount.
- prisenhed is a selector (faste vs. nominelle priser). Always filter to one — doubles row count if not filtered.
- indkints='0' is "Alle" (total). Very fine income brackets in ~50k steps up to 1M+. Note: column name is indkints (not indkintb used in other tables).
- koen='MOK' and alder='14TOT' are the totals.
- No geography. For regional breakdown of income distribution use indkp222.
