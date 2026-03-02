table: fact.ligepi4
description: Ligestillingsindikator for domme for personfarlig kriminalitet efter overtrædelsens art, alder, indikator og tid
measure: indhold (unit -)
columns:
- overtraed: values [LS1=I ALT, LS11=SEKSUALFORBRYDELSER I ALT, LS1110=Blodskam mv., LS1120=Voldtægt mv., LS117=Blufærdighedskrænkelse ... LS1366=Afpresning og åger, LS1380=Røveri, LS14=ANDRE FORBRYDELSER I ALT, LS1485=Freds- og æreskrænkelser, LS14A=Overtrædelse af advarsel/Lov om tilhold, opholdsforbud og bortvisning]
- alder: values [TOT=Alder i alt, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70OV=70 år og derover]
- indikator: values [M1=Mænd (pr. 100.000), K1=Kvinder (pr. 100.000), F1=Forskel mellem mænd og kvinder (point, pr. 100.000)]
- tid: date range 1991-01-01 to 2024-01-01

notes:
- indhold is a RATE (per 100,000 inhabitants) or a point difference — do NOT sum across rows.
- indikator encodes gender and metric: M1 = mænd per 100,000, K1 = kvinder per 100,000, F1 = forskel (mænd minus kvinder, in points per 100,000). These three values are independent — never sum them.
- No kon column (gender is folded into indikator). To compare men vs women, filter WHERE indikator IN ('M1','K1').
- Same overtraed (LS-prefix) and alder groupings as ligepb4. Pair with ligepb4 (raw counts) + ligepi4 (rates) for the same crime/age categories.