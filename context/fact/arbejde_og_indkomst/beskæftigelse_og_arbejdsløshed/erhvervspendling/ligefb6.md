table: fact.ligefb6
description: Beskæftigede efter familietype, pendlingsafstand, køn, alder og tid
measure: indhold (unit Antal)
columns:
- famtyp: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, E2=Enlige med hjemmeboende børn, i alt, E4=Enlige med hjemmeboende børn, yngste barn mellem 0-5 år, E3=Enlige med hjemmeboende børn, yngste barn 6 år og derover, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, P2=Par med hjemmeboende børn, i alt, P4=Par med hjemmeboende børn, yngste barn mellem 0-5 år, P3=Par med hjemmeboende børn, yngste barn 6 år og derover, U9=Uoplyst familietype]
- pendafst: values [0=I alt, 10=Ingen pendling, 20=Indtil 5 km, 30=5-10 km, 40=10-20 km, 45=20-30 km, 50=30-40 km, 60=40-50 km, 70=Over 50 km, 80=Ikke beregnet]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, -16=Under 16 år, 16-19=16-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-66=65-66 år, 67-=67 år og derover]
- tid: date range 2008-01-01 to 2023-01-01

notes:
- famtyp has two overlapping cross-cuts of the same population — do NOT mix them in a single sum. Cross-cut A (Enlige/Par): E1+P1+U9=TOT. Cross-cut B (børn): F1+F2+U9=TOT. 'E1' and 'F1' overlap (enlige with children appear in both). Pick one categorization per query.
- Non-overlapping exhaustive sets: {TOT}, {E1, P1, U9}, {F1, F2, U9}, or {EUHB, E2, PUHB, P2, U9}.
- pendafst=0 is total (I alt); pendafst=80 is 'Ikke beregnet'. kon=TOT and alder=TOT are the aggregate rows. Filter all non-target dimensions to TOT to avoid overcounting.
- To get total employed by pendlingsafstand: WHERE famtyp='TOT' AND kon='TOT' AND alder='TOT'.