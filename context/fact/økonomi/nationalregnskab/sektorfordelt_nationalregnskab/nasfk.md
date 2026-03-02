table: fact.nasfk
description: Nationalregnskabets finansielle konti efter sektor, konto, balance, finansielt instrument, modpartssektor og tid
measure: indhold (unit Mio. kr.)
columns:
- sektornat: join dim.esa on sektornat=kode [approx]
- konto1: values [P=Primobalance, U=Ultimobalance, T=Transaktioner, netto, O=Omvurderinger, A=Andre mængdemæssige ændringer]
- balance: values [AS=Finansielle aktiver, LI=Passiver]
- finins: values [F=F Finansielle instrumenter i alt, F1=- F.1 Monetært guld og særlige trækningsrettigheder (SDR), F11=- - F.11 Monetært guld, F12=- - F.12 Særlige trækningsrettigheder (SDR), F2=- F.2 Sedler og mønt samt indskud ... F8=- F.8 Andre forfaldne ikke-betalte mellemværender, F81=- - F.81 Handelskreditter og forudbetalinger, F89=- - F.89 Andre forfaldne, ikke betalte mellemværender, BF90=BF.90 Finansielle aktiver, netto, B9=B.9 Finansielle fordringserhvervelse, netto]
- modseknat: join dim.esa on modseknat=kode [approx]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- sektornat and modseknat both use dot-dropped ESA codes. Join dim.esa with REPLACE(d.kode, '.', ''). Full subsector detail including S121 (Danmarks Nationalbank), S122A123, S1311, S1313, S1314. S122A123 has no dim.esa match. Use ColumnValues("nasfk", "sektornat") for labels.
- modseknat (counterpart sector) has one extra code: SALLE="I alt (alle indenlandske sektorer og udlandet som modpart, mv.)". Use WHERE modseknat='SALLE' to get totals without counterpart breakdown — this is the default for most questions.
- konto1 defines the account type: P=primo balance (start of year), U=ultimo balance (end of year), T=net transactions, O=revaluations, A=other quantity changes. These are not additive — always filter to one. For stock questions use U; for flow questions use T.
- balance: AS=financial assets, LI=liabilities. finins: F=all instruments total, F2=deposits, F3=debt securities, F4=loans, F5=equity, F6=insurance/pension, F7=derivatives, etc.
- This is a 5-dimension table: specify sektornat + konto1 + balance + finins + modseknat to get a single value. A typical query: WHERE sektornat='S12' AND konto1='U' AND balance='AS' AND finins='F' AND modseknat='SALLE' to get total financial assets of the financial sector at year-end. Annual table, 1995-2024. Quarterly equivalent: nksfk.