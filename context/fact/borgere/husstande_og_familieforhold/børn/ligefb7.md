table: fact.ligefb7
description: Børn efter alder, familietype, mor status, far status og tid
measure: indhold (unit Antal)
columns:
- alder: values [TOT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år, 5=5 år, 6=6 år, 7=7 år, 8=8 år, 9=9 år, 10=10 år, 11=11 år, 12=12 år, 13=13 år, 14=14 år, 15=15 år, 16=16 år, 17=17 år]
- famtyp: values [TOT=I alt, 0=Udeboende, 1=Begge forældre, 2=Enlig mor, 3=Mor og partner, 4=Enlig far, 5=Far og partner]
- morstat: values [TOT=I alt, HM=Har mor, MD=Mor død, UK=Uoplyst mor]
- farstat: values [TOT=I alt, HF=Har far, FD=Far død, UM=Uoplyst far]
- tid: date range 1980-01-01 to 2025-01-01
notes:
- Has TOT rows for all four dimensions (alder, famtyp, morstat, farstat). Always filter all non-target dimensions to TOT to avoid overcounting. E.g. to get total children by famtyp: WHERE morstat='TOT' AND farstat='TOT' AND alder='TOT'.
- No geography — national totals only. Goes back to 1980 (longest historical series in this subject for familietype/forældrestatus data).
- famtyp=0 is "Udeboende". famtyp=TOT includes all categories including Udeboende.
- morstat/farstat codes here (HM/MD/UK, HF/FD/UM) are simpler than brn10 (no timing distinction). Covers only 0–17.
