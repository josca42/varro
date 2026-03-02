table: fact.ligepb1
description: Ofre for personfarlig kriminalitet efter overtrædelsens art, alder, køn og tid
measure: indhold (unit Antal)
columns:
- overtraed: values [LS1=I ALT, LS11=SEKSUALFORBRYDELSER I ALT, LS1110=Blodskam mv., LS1120=Voldtægt mv., LS117=Blufærdighedskrænkelse ... LS1366=Afpresning og åger, LS1380=Røveri, LS14=ANDRE FORBRYDELSER I ALT, LS1485=Freds- og æreskrænkelser, LS14A=Overtrædelse af advarsel/Lov om tilhold, opholdsforbud og bortvisning]
- alder: values [TOT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70OV=70 år og derover]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2001-01-01 to 2024-01-01

notes:
- overtraed has 22 LS-prefixed codes in a 3-level hierarchy: LS1 (total) → LS11/LS12/LS13/LS14 (4 main categories) → LS1110/LS1120/etc. (sub-categories). Mixing levels causes double-counting. Use LS1 for the total, or pick one hierarchy level consistently.
- This table covers only personfarlig kriminalitet (sexual, violent, property, and other personal crimes) — a narrower scope than straf5. The LS-prefix coding is different from straf5's numeric S-suffix codes.
- koen uses letter codes: M=Mænd, K=Kvinder, TOT=I alt. Unlike straf5, there is no 'uoplyst' gender code. Filter to one value.
- alder has TOT plus bands 0-4 through 70OV. No 'uoplyst' alder code (unlike straf5's 999). Filter to one value.
- Minimal query: WHERE overtraed='LS1' AND koen='TOT' AND alder='TOT'.