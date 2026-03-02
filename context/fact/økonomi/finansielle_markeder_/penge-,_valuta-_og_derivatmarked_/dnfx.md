table: fact.dnfx
description: Bankers køb og salg af DKK opdelt på valuta, modpartssektor eller løbetid efter transaktionstype, dimension og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt1: values [FXBUYI=Køb af DKK, FXSELL=Salg af DKK]
- dimension: values [ALL=Samlet, FCCALL=Valuta - Alle, FCCEUR=Valuta - EUR, FCCUSD=Valuta - USD, FCCOTH=Valuta - Øvrig, CPSALL=Modpartssektor - Alle, CPSDBA=Modpartssektor - Indenlandske banker, CPSOFC=Modpartssektor - Øvrige indenlandske finansielle selskaber, CPSODO=Modpartssektor - Øvrig indland, CPSFOR=Modpartssektor - Udland, MATALL=Løbetid - Alle, MAT1DA=Løbetid - Op til og med 1 bankdag, MAT2DA=Løbetid - Over 1 bankdag op til og med 2 bankdage, MAT220=Løbetid - Over 2 bankdage op til og med 20 bankdage, MATO20=Løbetid - Over 20 bankdage]
- tid: date range 2023-04-01 to 2025-09-01

notes:
- `dimension` is a stacked breakdown column — each row reports one dimension perspective. Prefix FCC*=valuta, CPS*=modpartssektor, MAT*=løbetid. Always filter to exactly one group per query.
- `ALL` = `FCCALL` = `CPSALL` = `MATALL` — all equal the same grand total. Don't mix groups.
- For the grand total: `WHERE dimension = 'ALL'`. For currency breakdown: `WHERE dimension IN ('FCCEUR','FCCUSD','FCCOTH')`. For counterparty: `WHERE dimension IN ('CPSDBA','CPSOFC','CPSODO','CPSFOR')`. For maturity: `WHERE dimension IN ('MAT1DA','MAT2DA','MAT220','MATO20')`.
- Summing subcodes within a group (e.g. FCCEUR+FCCUSD+FCCOTH) equals FCCALL/ALL — no overlap.
- `transakt1` is independent: FXBUYI=køb af DKK, FXSELL=salg af DKK. Filter both dimensions together as needed.