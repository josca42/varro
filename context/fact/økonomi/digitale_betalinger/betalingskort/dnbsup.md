table: fact.dnbsup
description: Dansk udstedte kort efter type, kortholder og tid
measure: indhold (unit 1.000 stk.)
columns:
- kortype: values [BTK=1 Betalingskort, DEBK=1.1 Debetkort, DANK=1.1.1 Dankort, CODANK=1.1.2 Co-brandede Dankort, INTDEBK=1.1.3 Internationale debetkort, KREK=1.2 Kreditkort, INTKREK=1.2.1 Internationale kreditkort]
- privaterhverv: values [AK=I alt, PRIKORT=Privatperson, ERHKORT=Erhvervskunde]
- tid: date range 2016-01-01 to 2025-04-01

notes:
- kortype is a 3-level hierarchy. BTK is the grand total; DEBK/KREK are subtotals (debet/kredit); DANK/CODANK/INTDEBK sit under DEBK and INTKREK under KREK. Never mix levels in the same sum — BTK ≈ DEBK + KREK (verified).
- privaterhverv: AK=I alt is the aggregate of PRIKORT+ERHKORT. Filter to AK for a total, or to PRIKORT/ERHKORT to compare holder types. Don't sum all three.
- To get total number of payment cards: WHERE kortype='BTK' AND privaterhverv='AK'.
- No `data` selector column here — indhold is always the card count in 1.000 stk. (unlike the transaction tables).