table: fact.dnbsuk
description: Dansk udstedte kort efter type, teknologi og tid
measure: indhold (unit 1.000 stk.)
columns:
- kortype: values [HVK=1. Hævekort, BTK=2. Betalingskort, DEBK=2.1. Debetkort, DANK=2.1.1. Dankort, CODANK=2.1.2. Co-brandede Dankort, INTDEBK=2.1.3. Internationale debetkort, KREK=2.2. Kreditkort, INTKREK=2.2.1 Internationale kreditkort]
- korttek: values [AK=I alt, NFCKORT=Kontaktløse kort, CHIPKORT=Chipkort]
- tid: date range 2016-01-01 to 2025-04-01

notes:
- kortype here includes HVK=Hævekort (withdrawal cards) as an additional top-level type not present in other tables. BTK is still the betalingskort total; the card hierarchy is otherwise the same as dnbsup/dnbstk/dnbstp.
- korttek: AK=I alt is the aggregate of NFCKORT+CHIPKORT. Always filter to a single level to avoid summing totals with their components.
- No `data` selector — indhold is always card count in 1.000 stk. Use this table to track contactless (NFC) adoption over time: WHERE korttek='NFCKORT'.
- To compare technologies for a single card type: fix kortype to one code and compare korttek='NFCKORT' vs 'CHIPKORT'.