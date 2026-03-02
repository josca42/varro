table: fact.dnbsts
description: Transaktioner med kort efter type, anvendelsessted, land, datatype og tid
measure: indhold (unit -)
columns:
- kortype: values [BTK=1 Danske betalingskort, DEBK=1.1 Debetkort, DANK=1.1.1 Dankort, CODANK=1.1.2 Co-brandede Dankort, INTDEBK=1.1.3 Internationale debetkort, KREK=1.2 Kreditkort, INTKREK=1.2.1 Internationale kreditkort, UDLKORT=2 Udenlandske betalingskort, UDLINTDEBK=2.1 Udenlandske debetkort, UDLINTKREK=2.2 Udenlandske kreditkort]
- anvsted: values [ADK=I alt, DKFH=Fysiske forretninger (betjent ekspedition), DKIH=E-handel mv., DKSB=Selvbetjening og automatsalg (kun danske kort, Danmark), DKATM=Kontanthævning]
- nation: values [TOT=I alt, DK=Danmark, UDL=Udland (kun danske kort)]
- data: values [A=Antal (1.000 stk.), V=Værdi (mio. kr.)]
- tid: date range 2016-01-01 to 2025-07-01

notes:
- `data` is a 2-way measurement selector — always filter to one: A=Antal (1.000 stk.), V=Værdi (mio. kr.).
- kortype covers both Danish cards (BTK and subtypes) and foreign cards (UDLKORT=2, UDLINTDEBK=2.1, UDLINTKREK=2.2). This is the broadest card coverage of any table in the group. Filter kortype='BTK' for Danish-only totals, 'UDLKORT' for foreign-only.
- anvsted: ADK=I alt is the aggregate. DKFH=physical shops, DKIH=e-commerce, DKSB=self-service/vending (Danish cards in Denmark only), DKATM=ATM withdrawals.
- nation: TOT=I alt, DK=Denmark, UDL=Abroad. Critical caveat: anvsted='DKSB' has no UDL rows — only DK and TOT. Filtering nation='UDL' will silently drop all DKSB rows. Be careful with GROUP BY nation or WHERE nation='UDL' in cross-tab queries.
- Typical query for e-commerce share: WHERE data='A' AND kortype='BTK' AND nation='TOT' AND anvsted IN ('ADK', 'DKIH').