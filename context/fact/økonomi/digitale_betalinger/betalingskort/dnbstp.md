table: fact.dnbstp
description: Transaktioner med dansk udstedte kort efter type, kortholder, datatype og tid
measure: indhold (unit -)
columns:
- kortype: values [BTK=1 Betalingskort, DEBK=1.1 Debetkort, DANK=1.1.1 Dankort, CODANK=1.1.2 Co-brandede Dankort, INTDEBK=1.1.3 Internationale debetkort, KREK=1.2 Kreditkort, INTKREK=1.2.1 Internationale kreditkort]
- privaterhverv: values [AK=I alt, PRIKORT=Privatperson, ERHKORT=Erhvervskunde]
- data: values [A=Antal (1.000 stk.), V=Værdi (mio. kr.)]
- tid: date range 2016-01-01 to 2025-04-01

notes:
- `data` is a 2-way measurement selector — always filter to one: A=Antal (1.000 stk.), V=Værdi (mio. kr.).
- kortype hierarchy same as dnbsup/dnbstk: BTK total → DEBK/KREK subtotals → leaf types. Pick one level.
- privaterhverv: AK=I alt is aggregate of PRIKORT+ERHKORT. Filter to one level.
- This table is the transaction-side twin of dnbsup (which counts cards). dnbsup tells you how many cards exist by holder type; dnbstp tells you how many transactions/value by holder type.
- Typical query: WHERE data='V' AND kortype='BTK' AND privaterhverv='AK' for total transaction value by month.