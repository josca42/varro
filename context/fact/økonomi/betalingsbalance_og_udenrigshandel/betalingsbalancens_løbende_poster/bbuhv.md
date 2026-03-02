table: fact.bbuhv
description: Overgangstabel for varer mellem udenrigshandel og betalingsbalance efter poster, indtægt/udgift, land og tid
measure: indhold (unit Mio. kr.)
columns:
- post: values [1.A.A.1.I=GENERALHANDEL (UHV), 1.A.A.1.II=Bunkring og proviantering, 1.A.A.1.III=Varer købt eller solgt i udlandet i forb. med forarbejdning i udlandet, 1.A.A.1.IV=Øvrige korrektioner, 1.A.A.1.IV.1.A=Øvrige korrektioner, varer der krydser grænsen i forbindelse med forarbejdning i Danmark, 1.A.A.1.IV.1.B=Øvrige korrektioner, varer der krydser grænsen i forbindelse med forarbejdning i udlandet, 1.A.A.1.IV.2=Øvrige korrektioner, returvarer, 1.A.A.1.IV.3=Øvrige korrektioner, varer der krydser grænsen i forbindelse med bygge og anlægsprojekter, 1.A.A.1.IV.4=Øvrige korrektioner, fragt på import (CIFFOB), 1.A.A.1.IV.5=Øvrige korrektioner, andre varer, 1.A.A.2=Merchanting, 1.A.A.3=Ikke monetært guld, 1.A.A=LØBENDE POSTER, VARER (FOB)]
- indudbop: values [K=Løbende indtægter, D=Løbende udgifter]
- land: join dim.lande_uht_bb on land=kode [approx]; levels [2]
- tid: date range 2005-01-01 to 2025-08-01
dim docs: /dim/lande_uht_bb.md

notes:
- This is a transition/reconciliation table showing the adjustment from udenrigshandel (foreign trade, CIF basis) to betalingsbalancen (balance of payments, FOB basis). The 13 post codes represent specific correction line items (generalhandel, bunkring, forarbejdning, korrektioner, merchanting, guld) — they are not a hierarchy. Summing all post values is not meaningful.
- land: only 3 values: B6 (EU-27), D6 (Extra EU-27), W1 (alle lande — not in dim). No country-level breakdown.
- indudbop: only K (indtægter) and D (udgifter) — no N (netto) in this table.
- The final post '1.A.A=LØBENDE POSTER, VARER (FOB)' is the reconciled total. Use post='1.A.A' for the bottom-line goods figure on the balance of payments.
- post='1.A.A.1.I' (GENERALHANDEL) is the starting point (from foreign trade); subsequent codes are the adjustments that lead to the FOB total.