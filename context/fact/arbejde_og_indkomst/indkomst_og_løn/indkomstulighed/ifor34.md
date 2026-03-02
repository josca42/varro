table: fact.ifor34
description: Indkomstdecilers sammensætning efter indkomstdecil, alder, enhed og tid
measure: indhold (unit -)
columns:
- inddecil: values [1DC=1. decil, 2DC=2. decil, 3DC=3. decil, 4DC=4. decil, 5DC=5. decil, 6DC=6. decil, 7DC=7. decil, 8DC=8. decil, 9DC=9. decil, 10DC=10. decil]
- alder: values [0-14=0-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-00=80 år og derover]
- enhed: values [PCT=Andel af decil (pct.), ANT=Personer (antal)]
- tid: date range 2000-01-01 to 2023-01-01
notes:
- enhed is a measurement selector: PCT=andel af decil (pct.) and ANT=antal personer. Both units exist for every row. Always filter to one: WHERE enhed = 'PCT' or WHERE enhed = 'ANT'. Forgetting this doubles all values.
- alder has 15 age bands (0-14 through 80-00) with no aggregate/total row. Each band is mutually exclusive. The bands are coded as "0-14", "15-19", ... "80-00".
- inddecil has 10 codes (1DC–10DC), no aggregate. PCT values show what share of a given decil belongs to each age group — they sum to 100 across age bands within a decil.
- Similar to ifor33 (socio composition of decils) but with alder instead of socio.
