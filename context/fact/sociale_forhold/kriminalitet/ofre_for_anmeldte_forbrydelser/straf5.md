table: fact.straf5
description: Ofre for anmeldte forbrydelser efter overtrædelsens art, alder, køn og tid
measure: indhold (unit Antal)
columns:
- overtraed: values [1S=OFRE I ALT, 11S=OFRE FOR SEKSUALFORBRYDELSER I ALT, 1110S=Blodskam mv. i alt, 111072121=Blodskam, børn under 15 år, 111072122=Blodskam i øvrigt ... 381084453=Bortvisning, overtrædelse af (Ny fra 2012), 381084454=Tilhold og opholdsforbud, overtrædelse af (Ny fra 2012), 381084455=Bortvisning og tilhold, overtrædelse af (Ny fra 2012), 381084456=Bortvisning og opholdsforbud, overtrædelse af (Ny fra 2012), 381084457=Bortvisning, tilhold og opholdsforbud, overtrædelse af (Ny fra 2012)]
- alder: values [TOT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70-79=70-79 år, 80-=80 år og derover, 999=Uoplyst alder]
- koen: values [TOT=I alt, 1=Mænd, 2=Kvinder, 9=Uoplyst køn]
- tid: date range 2001-01-01 to 2024-01-01

notes:
- overtraed has 196 codes across 4+ hierarchy levels. Codes ending in 'S' are aggregates (28 total, e.g. 1S=OFRE I ALT, 11S=seksualforbrydelser i alt, 12S=voldsforbrydelser i alt). Leaf codes are numeric without S suffix. Never mix levels — summing all distinct overtraed values massively overcounts. Use overtraed='1S' for the national total, or filter to leaf codes with WHERE overtraed NOT LIKE '%S' for a breakdown without double-counting.
- koen uses numeric codes: 1=Mænd, 2=Kvinder, 9=Uoplyst køn, TOT=I alt. Note this differs from ligepb1/ligepi1 which use M/K. Always filter koen to a single value; TOT = 1 + 2 + 9.
- alder has TOT plus 13 age bands (0-4 through 80-) plus 999=Uoplyst alder. TOT = sum of all bands including 999. Filter to one value to avoid overcounting.
- To get a simple national victim count: WHERE overtraed='1S' AND koen='TOT' AND alder='TOT'. All three filters required.
- Use ColumnValues("straf5", "overtraed") to browse 204 crime type entries with labels. Fuzzy match is useful: ColumnValues("straf5", "overtraed", fuzzy_match_str="voldtægt") to find the right code.