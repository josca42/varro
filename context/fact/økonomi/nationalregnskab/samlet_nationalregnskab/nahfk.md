table: fact.nahfk
description: Nationalregnskabets finansielle konti, hele økonomien efter konto, balance, finansielt instrument og tid
measure: indhold (unit Mio. kr.)
columns:
- konto1: values [P=Primobalance, U=Ultimobalance, T=Transaktioner, netto, O=Omvurderinger, A=Andre mængdemæssige ændringer]
- balance: values [AS=Finansielle aktiver, LI=Passiver]
- finins: values [F=F Finansielle instrumenter i alt, F1=- F.1 Monetært guld og særlige trækningsrettigheder (SDR), F11=- - F.11 Monetært guld, F12=- - F.12 Særlige trækningsrettigheder (SDR), F2=- F.2 Sedler og mønt samt indskud ... F8=- F.8 Andre forfaldne ikke-betalte mellemværender, F81=- - F.81 Handelskreditter og forudbetalinger, F89=- - F.89 Andre forfaldne, ikke betalte mellemværender, BF90=BF.90 Finansielle aktiver, netto, B9=B.9 Finansielle fordringserhvervelse, netto]
- tid: date range 1995-01-01 to 2024-01-01
notes:
- THREE dimension columns that all act as selectors — filter all three for a meaningful result.
- konto1: P=primobalance, U=ultimobalance, T=transaktioner netto, O=omvurderinger, A=andre mængdemæssige ændringer. For flow (changes during year) use T; for balance sheet stocks use P or U.
- balance: AS=finansielle aktiver, LI=passiver. Filter to one side or you see both assets and liabilities together.
- finins codes are hierarchical: F=total, F1/F2/.../F8=main instrument categories, then subcategories. BF90=finansielle aktiver netto (=AS minus LI), B9=finansiel fordringserhvervelse netto. Do not sum all finins values.
- Annual from 1995. Quarterly version: nkhfk (from 1999).
