table: fact.gron2
description: Grønne varer og tjenester efter branche (DB07), miljøformål, enhed og tid
measure: indhold (unit -)
columns:
- branche07: values [TOT=TOT Erhverv i alt, 01000=01000 Landbrug og gartneri, 02000=02000 Skovbrug, 031032=Fiskeri og akvakultur, 13000=13000 Tekstilindustri ... 42000=42000 Anlægsentreprenører, 43000=43000 Bygge- og anlægsvirksomhed, specialisering, 71000=71000 Arkitekter og rådgivende ingeniører, 72000=72000 Forskning og udvikling, 74000=74000 Anden videnservice]
- mformaal: values [G_05=Grønne varer og tjenester i alt, G_10=A Miljøbeskyttelse i alt, G_55=B Ressourcebesparelse i alt, G_105=C1 Specifikke varer og tjenester, miljøbeskyttelse, G_110=C2 Specifikke varer og tjenester, ressourcebesparelse, G_120=D1 Renere og ressourcebesparende produkter, miljøbeskyttelse, G_125=D2 Renere og ressourcebesparende produkter, ressourcebesparelse]
- enhed: values [XOM=Omsætning (mio. kr.), EKS=Eksport (mio. kr.), BESK=Antal beskæftigede (i årsværk), XVT=Værditilvækst (mio. kr.)]
- tid: date range 2012-01-01 to 2023-01-01

notes:
- enhed is a measurement selector — 4 distinct units (XOM=Omsætning, EKS=Eksport, BESK=Beskæftigede i årsværk, XVT=Værditilvækst). Always filter to one enhed.
- branche07 uses detailed DB07 industry codes. TOT = Erhverv i alt. No dim table join available — use ColumnValues("gron2", "branche07") to browse codes and labels. Many more granular branches than gron1/gron1a.
- mformaal is a subset of gron1's values (only top-level groupings: G_05 total, G_10 miljøbeskyttelse, G_55 ressourcebesparelse, G_105/G_110 specifikke varer, G_120/G_125 renere produkter). No sub-category detail in this table.
- Use gron2 when you need detailed DB07 industry breakdown. Use gron1/gron1a for detailed environmental purpose breakdown (more mformaal codes).