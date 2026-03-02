table: fact.nkhfk
description: Nationalregnskabets finansielle konti, hele økonomien efter konto, balance, finansielt instrument og tid
measure: indhold (unit Mio. kr.)
columns:
- konto1: values [P=Primobalance, U=Ultimobalance, T=Transaktioner, netto, O=Omvurderinger, A=Andre mængdemæssige ændringer]
- balance: values [AS=Finansielle aktiver, LI=Passiver]
- finins: values [F=F Finansielle instrumenter i alt, F1=- F.1 Monetært guld og særlige trækningsrettigheder (SDR), F11=- - F.11 Monetært guld, F12=- - F.12 Særlige trækningsrettigheder (SDR), F2=- F.2 Sedler og mønt samt indskud ... F8=- F.8 Andre forfaldne ikke-betalte mellemværender, F81=- - F.81 Handelskreditter og forudbetalinger, F89=- - F.89 Andre forfaldne, ikke betalte mellemværender, BF90=BF.90 Finansielle aktiver, netto, B9=B.9 Finansielle fordringserhvervelse, netto]
- tid: date range 1999-01-01 to 2025-04-01
notes:
- THREE dimension selectors: konto1 (P/U/T/O/A), balance (AS/LI), finins hierarchy. Filter all three.
- Quarterly financial accounts from 1999. Annual equivalent: nahfk (from 1995).
- Same structure as nahfk: konto1='T' for flow transactions, 'P'/'U' for balance sheet. finins='F' for total financial instruments.
