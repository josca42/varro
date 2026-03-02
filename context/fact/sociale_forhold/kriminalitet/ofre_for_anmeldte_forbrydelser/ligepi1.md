table: fact.ligepi1
description: Ligestillingsindikator for ofre for personfarlig kriminalitet efter overtrædelsens art, alder, indikator og tid
measure: indhold (unit Pr. 100.000 personer)
columns:
- overtraed: values [LS1=I ALT, LS11=SEKSUALFORBRYDELSER I ALT, LS1110=Blodskam mv., LS1120=Voldtægt mv., LS117=Blufærdighedskrænkelse ... LS1366=Afpresning og åger, LS1380=Røveri, LS14=ANDRE FORBRYDELSER I ALT, LS1485=Freds- og æreskrænkelser, LS14A=Overtrædelse af advarsel/Lov om tilhold, opholdsforbud og bortvisning]
- alder: values [TOT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70OV=70 år og derover]
- indikator: values [M1=Mænd (pr. 100.000), K1=Kvinder (pr. 100.000), F1=Forskel mellem mænd og kvinder (point, pr. 100.000)]
- tid: date range 2001-01-01 to 2024-01-01

notes:
- indhold is a RATE (per 100,000 persons), not a count. Do not sum indhold across rows. Select a single overtraed × alder × indikator combination and read the rate directly.
- indikator is a measurement selector with 3 values: M1=mænd rate, K1=kvinder rate, F1=forskel (difference M1−K1, can be negative). Always filter to one indikator value. F1=-168 for LS1/TOT in 2024 means women were victimized 168 per 100K more than men.
- overtraed and alder use the same LS-prefix coding as ligepb1 (22 codes, same 3-level hierarchy). Mixing hierarchy levels causes double-counting even here.
- For actual victim counts use ligepb1. Use ligepi1 only for gender rate comparisons normalised to population size.