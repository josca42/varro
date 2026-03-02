table: fact.ligepb4
description: Domme for personfarlig kriminalitet efter overtrædelsens art, alder, køn og tid
measure: indhold (unit Antal)
columns:
- overtraed: values [LS1=I ALT, LS11=SEKSUALFORBRYDELSER I ALT, LS1110=Blodskam mv., LS1120=Voldtægt mv., LS117=Blufærdighedskrænkelse ... LS1366=Afpresning og åger, LS1380=Røveri, LS14=ANDRE FORBRYDELSER I ALT, LS1485=Freds- og æreskrænkelser, LS14A=Overtrædelse af advarsel/Lov om tilhold, opholdsforbud og bortvisning]
- alder: values [TOT=Alder i alt, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70OV=70 år og derover]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 1991-01-01 to 2024-01-01

notes:
- overtraed uses LS-prefix codes (LS1, LS11, LS1110, etc.) — a completely different coding scheme from the straf tables (which use 1, 11, 1110 without prefix). Do NOT join with dim.overtraedtype; these are inline values.
- This table covers personfarlig kriminalitet only (violent crime: sexual offences, violence, robbery, extortion). It is NOT a subset of straf40 that you can filter — it uses a separate classification.
- alder uses grouped bands only (15-19, 20-24, 25-29, 30-39, 40-49, 50-59, 60-69, 70OV). No individual ages, no UA. TOT = I alt.
- Column is koen (not kon as in straf40/44). No VIRKSOMHEDER — persons only (TOT/M/K).
- LS1 = I ALT (all personfarlig); filter LS1 for grand total, or use LS11/LS12/LS13/LS14 for subcategories.
- Pair with ligepi4 for population-normalised rates on the same crime/age breakdown.