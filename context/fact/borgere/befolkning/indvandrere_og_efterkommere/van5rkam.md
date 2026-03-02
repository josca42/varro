table: fact.van5rkam
description: Asylansøgninger (registreringstallet) efter statsborgerskab, køn, alder og tid
measure: indhold (unit Antal)
columns:
- statsb: join dim.lande_psd on statsb=kode; levels [3]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70OV=70 år og derover]
- tid: date range 2014-01-01 to 2025-09-01
dim docs: /dim/lande_psd.md

notes:
- This table is exclusively registreringstallet (SPO) — no asyltype column. All data is the official registration count.
- statsb has no total code — SUM across all statsb values for national count. All statsb codes are niveau=3 individual countries (~143 nationalities present).
- kon='TOT' and alder='TOT' are the aggregate codes. Use both when querying totals.
- Use ColumnValues("lande_psd", "titel", for_table="van5rkam") to see which nationalities are in this table.
- tid is monthly. For nationality-only counts without gender/age breakdown, van5m is simpler.