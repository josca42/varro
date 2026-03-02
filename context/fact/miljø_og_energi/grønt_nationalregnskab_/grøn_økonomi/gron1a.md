table: fact.gron1a
description: Grønne varer og tjenester (ny gruppering 2024) efter miljøformål, branche, enhed og tid
measure: indhold (unit -)
columns:
- mformaal: values [G00=00 Grønne varer og tjenester i alt, G01=01 Luftkvalitet og klima, G011=01.1 Reduktion af drivhusgasser, G012=01.2 Reduktion af anden luftforurening, G02=02 Energiforsyning og forbrug ... G06=06 Støj, vibrationer og stråling, G07=07 Forskning og udvikling på miljøområdet, G071=07.1 Forskning og udvikling vedr. miljøbeskyttelse, G072=07.2 Forskning og udvikling vedr. ressourcebesparelse, G08=08 Andre og tværgående miljøområder]
- branche: values [TOT=TOT Erhverv i alt, A=A Landbrug, skovbrug og fiskeri, C=C Industri, 28000=28000 Maskinindustri, C33=C33 Industri ekskl. maskinindustri, D=D Energiforsyning, E=E Vandforsyning og renovation, F=F Bygge og anlæg, M=M Videnservice]
- enhed: values [XOM=Omsætning (mio. kr.), EKS=Eksport (mio. kr.), BESK=Antal beskæftigede (i årsværk), XVT=Værditilvækst (mio. kr.)]
- tid: date range 2015-01-01 to 2023-01-01

notes:
- enhed is a measurement selector — 4 distinct units (XOM=Omsætning, EKS=Eksport, BESK=Beskæftigede i årsværk, XVT=Værditilvækst). Every branche/mformaal combination repeats 4 times, once per unit. Always filter to one enhed or the sum is meaningless.
- mformaal is hierarchical: G00 = total, G01–G08 = 8 main categories, G011/G012/G021/... = sub-categories. Don't mix levels in a SUM. For main categories only: WHERE LENGTH(mformaal) = 3 AND mformaal != 'G00'. For grand total: WHERE mformaal = 'G00'.
- branche includes TOT (total all sectors) plus 8 sector codes. Note that 28000 (Maskinindustri) and C33 (Industri ekskl. maskinindustri) are sub-splits of C (Industri) — don't sum C + 28000 + C33. Safest totals: use TOT or filter to the aggregated sector letters only (A, C, D, E, F, M).
- This table uses the new 2024 classification scheme. For data from 2012 or comparison with older classification, use gron1 (same structure, different mformaal codes).