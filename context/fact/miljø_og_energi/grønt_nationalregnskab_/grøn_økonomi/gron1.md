table: fact.gron1
description: Grønne varer og tjenester efter miljøformål, branche, enhed og tid
measure: indhold (unit -)
columns:
- mformaal: values [G_05=Grønne varer og tjenester i alt, G_10=A Miljøbeskyttelse i alt, G_15=A1 Beskyttelse af luftkvalitet og klima, G_20=A2 Spilde- og regnvandshåndtering, G_25=A3 Affaldshåndtering og genindvinding ... G_105=C1 Specifikke varer og tjenester, miljøbeskyttelse, G_110=C2 Specifikke varer og tjenester, ressourcebesparelse, G_115=D Renere og ressourcebesparende produkter, i alt, G_120=D1 Renere og ressourcebesparende produkter, miljøbeskyttelse, G_125=D2 Renere og ressourcebesparende produkter, ressourcebesparelse]
- branche: values [TOT=TOT Erhverv i alt, A=A Landbrug, skovbrug og fiskeri, C=C Industri, 28000=28000 Maskinindustri, C33=C33 Industri ekskl. maskinindustri, D=D Energiforsyning, E=E Vandforsyning og renovation, F=F Bygge og anlæg, M=M Videnservice]
- enhed: values [XOM=Omsætning (mio. kr.), EKS=Eksport (mio. kr.), BESK=Antal beskæftigede (i årsværk), XVT=Værditilvækst (mio. kr.)]
- tid: date range 2012-01-01 to 2023-01-01
notes:
- enhed is a measurement selector — 4 distinct units (XOM=Omsætning, EKS=Eksport, BESK=Beskæftigede i årsværk, XVT=Værditilvækst). Every branche/mformaal combination repeats 4 times. Always filter to one enhed.
- mformaal has 25 hierarchical codes: G_05 = grand total, G_10 = Miljøbeskyttelse i alt, G_55 = Ressourcebesparelse i alt (the two main branches). G_15 through G_50 are sub-categories under G_10; G_60 through G_95 under G_55. Plus special categories G_100/G_105/G_110/G_115/G_120/G_125. Filter to one level to avoid double counting.
- branche is identical to gron1a: TOT = total, then 8 sector codes where C33 and 28000 are sub-components of C (Industri). Use TOT for national totals or sum only the non-overlapping sector letters (A, C, D, E, F, M).
- This table uses the pre-2024 classification. For data from 2015 onward with the new 2024 classification, use gron1a. For detailed DB07 industry breakdown, use gron2.
