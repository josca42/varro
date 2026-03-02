table: fact.dnsnb2
description: Specifikation til Nationalbankens balance - Transaktioner efter specifikation, instrument og tid
measure: indhold (unit Mia. kr.)
columns:
- specnat: values [I=Ikke angivet, V=Valutareserve, N=Kreditinstitutters nettostilling]
- instrument: values [ATA=Alle aktiver (Aktiv), KRA=Indenlandske udlån samt værdipapirbeholdning (Aktiv), N4A=Nationalbankens nettovalutakøb (Aktiv), N5A=Nationalbankens nettoobligationskøb (Aktiv), N7A=Interventionskøb af valuta, netto (Aktiv) ... R6N=Kursregulering af valutareserven (nettoaktiv), N1I=Statens indenlandske bruttofinansieringsbehov (Ikke-specificeret), N2I=Salg af indenlandske statspapirer (Ikke-specificeret), N3I=Likviditetspåvirkning fra statens betalinger (Ikke-specificeret), N6I=Andre faktorer med påvirkning af penge- og realkreditinstitutternes nettostilling (Ikke-specificeret)]
- tid: date range 1987-01-01 to 2025-09-01

notes:
- Nationalbankens balance, transactions (transaktioner) — flow data, not stock.
- specnat: V=valutareserve, N=kreditinstitutters nettostilling, I=ikke angivet. Always filter to one specnat.
- instrument codes ending in A=aktiv, P=passiv, N=nettoaktiv, I=ikke-specificeret. Don't mix balance sheet sides.
- ATA=alle aktiver; all other A-codes are sub-components. Don't sum sub-components with ATA.
- Unit is mia. kr. (billions).
- dnsnb2 = transactions; dnsnb1 = holdings. For stock levels use dnsnb1.