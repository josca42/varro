table: fact.nksfk
description: Nationalregnskabets finansielle konti efter sektor, konto, balance, finansielt instrument, modpartssektor og tid
measure: indhold (unit Mio. kr.)
columns:
- sektornat: join dim.esa on sektornat=kode [approx]
- konto1: values [P=Primobalance, U=Ultimobalance, T=Transaktioner, netto, O=Omvurderinger, A=Andre mængdemæssige ændringer]
- balance: values [AS=Finansielle aktiver, LI=Passiver]
- finins: values [F=F Finansielle instrumenter i alt, F1=- F.1 Monetært guld og særlige trækningsrettigheder (SDR), F11=- - F.11 Monetært guld, F12=- - F.12 Særlige trækningsrettigheder (SDR), F2=- F.2 Sedler og mønt samt indskud ... F8=- F.8 Andre forfaldne ikke-betalte mellemværender, F81=- - F.81 Handelskreditter og forudbetalinger, F89=- - F.89 Andre forfaldne, ikke betalte mellemværender, BF90=BF.90 Finansielle aktiver, netto, B9=B.9 Finansielle fordringserhvervelse, netto]
- modseknat: join dim.esa on modseknat=kode [approx]
- tid: date range 1999-01-01 to 2025-04-01
dim docs: /dim/esa.md

notes:
- Identical structure to nasfk but quarterly (1999Q1–2025Q1). All the same notes apply: dot-dropped ESA codes for sektornat and modseknat, SALLE for modseknat totals, 5 dimensions must all be specified.
- sektornat and modseknat: join dim.esa with REPLACE(d.kode, '.', ''). S122A123 has no dim.esa match. Use ColumnValues("nksfk", "sektornat") for labels.
- konto1: P=primo, U=ultimo, T=net transactions, O=revaluations, A=other. Always filter to one. For quarterly stock data use U (ultimo = end of quarter). For flow data use T.
- Typical query: WHERE sektornat='S1' AND konto1='U' AND balance='AS' AND finins='F' AND modseknat='SALLE' for total financial assets of the domestic economy at end of each quarter.