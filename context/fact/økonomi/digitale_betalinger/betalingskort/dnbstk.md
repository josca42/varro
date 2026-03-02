table: fact.dnbstk
description: Transaktioner i Danmark med dansk udstedte kort efter type, teknologi, datatype og tid
measure: indhold (unit -)
columns:
- kortype: values [BTK=1 Betalingskort, DEBK=1.1 Debetkort, DANK=1.1.1 Dankort, CODANK=1.1.2 Co-brandede Dankort, INTDEBK=1.1.3 Internationale debetkort, KREK=1.2 Kreditkort, INTKREK=1.2.1 Internationale kreditkort]
- korttek: values [AK=I alt, NFCKORT=Kontaktløse kort, CHIPKORT=Chipkort]
- data: values [A=Antal (1.000 stk.), V=Værdi (mio. kr.)]
- tid: date range 2016-01-01 to 2025-04-01

notes:
- `data` is a 2-way measurement selector — always filter to one: A=Antal (1.000 stk. transactions), V=Værdi (mio. kr.). Forgetting this doubles all counts.
- kortype hierarchy same as dnbsup: BTK is total, DEBK/KREK are subtotals, DANK/CODANK/INTDEBK/INTKREK are leaf types. Pick one level.
- korttek: AK=I alt is aggregate of NFCKORT+CHIPKORT. Filter to one level.
- This table covers only transactions in Denmark with Danish-issued cards. For foreign-issued cards used in Denmark or Danish cards used abroad, see dnbsts or dnbsk1.
- Typical query: WHERE data='A' AND kortype='BTK' AND korttek='AK' for total transaction count by month.