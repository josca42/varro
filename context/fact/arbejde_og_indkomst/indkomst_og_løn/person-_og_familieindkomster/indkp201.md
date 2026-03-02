table: fact.indkp201
description: Hovedtabel personindkomster efter indkomsttype, køn, alder, population, prisenhed, enhed og tid
measure: indhold (unit -)
columns:
- indkomsttype: values [100=1 Disponibel indkomst (2+30-31-32-35), 105=2 Indkomst i alt, før skatter mv. (3+7+22+26+29), 110=3 Erhvervsindkomst (4+5+6), 115=4 Løn, 120=5 Virksomhedsoverskud ... 270=35 Betalt underholdsbidrag, 275=Ækvivaleret disponibel indkomst, 280=Ejendomsskat (grundskyld), boligejere, 285=Ejendomsskat (grundskyld), lejere, 290=Skattepligtig indkomst]
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- alder: values [14TOT=I alt, 15 år og derover, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-00=80 år og derover]
- popu: values [5000=Alle uanset om de har indkomstypen, 5020=Kun personer med indkomsttypen]
- prisenhed: values [5=Faste priser (seneste dataårs prisniveau), 6=Nominelle priser]
- enhed: values [50=Gennemsnit (kr.), 55=Median (kr.), 60=Nederste kvartilgræsnse (kr.), 65=Øverste kvartilgrænse (kr.), 105=Personer (Antal)]
- tid: date range 1996-01-01 to 2024-01-01
notes:
- National-level headquarters table for personal income. No geography — use indkp101/indkp107/indkp109/indkp111 for regional breakdowns.
- Three mandatory measurement selectors that multiply row counts: enhed (5 types), popu (alle vs. kun med indkomsttypen), prisenhed (faste vs. nominelle). Always filter all three or counts inflate 10x+.
- indkomsttype is hierarchical (35+ types). The labels encode the formula: e.g. "100=1 Disponibel indkomst (2+30-31-32-35)". Never sum across multiple types — pick exactly one.
- Totals: koen='MOK', alder='14TOT'.
- enhed=105 gives person count (Antal); enhed=50/55/60/65 give kr-statistics — mixing them is meaningless.
- Example minimal query: WHERE indkomsttype='115' AND koen='MOK' AND alder='14TOT' AND popu='5000' AND prisenhed='6' AND enhed='50'
