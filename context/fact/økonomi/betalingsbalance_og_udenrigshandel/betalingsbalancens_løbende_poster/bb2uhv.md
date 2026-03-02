table: fact.bb2uhv
description: Korrektion af varer mellem udenrigshandel og betalingsbalance efter varebegreb, poster, im- og eksport, land og tid
measure: indhold (unit Mio. kr.)
columns:
- uhbegreb: values [GP=Udenrigshandel med varer (Grænsepassageprincip), ES=Udenrigshandel med varer (Ejerskifteprincip)]
- post: values [1.A.A=VARER, 1.A.A.1.Z=VARER DER KRYDSER DANSK GRÆNSE, 1.A.A.1.0-4X2-3=Næringsmidler, drikkevarer, tobak mv., 1.A.A.1.2=Råstoffer, ikke spiselige, undt. brændsel, 1.A.A.1.3=Mineral, brændsels- og smørestoffer o.l., 1.A.A.1.5=Kemikalier og kemiske produkter, 1.A.A.1.6=Forarbejdede varer, primært halvfabrikata, 1.A.A.1.7X78-79=Maskiner, undt. transportmidler, 1.A.A.1.78-79=Transportmidler undt. Skibe og fly, 1.A.A.1.SOGF=Skibe, fly mv., 1.A.A.1.8-9=Færdigvarer og andre varer, 1.A.A.1.ZX=Øvrige varer der krydser grænsen, 1.A.A.1.Q=VARER DER IKKE KRYDSER DANSK GRÆNSE, 1.A.A.1.II=Bunkring og proviantering, 1.A.A.1.III.E=Varer solgt i udlandet ifm. forarbejdning, 1.A.A.1.III.I=Varer købt i udlandet ifm. forarbejdning, 1.A.A.2=Merchanting, 1.A.A.1.QX=Øvrige varer der ikke krydser grænsen]
- indud: values [1=Import, 2=Eksport]
- land: values [W1=LANDE I ALT]
- tid: date range 2016-01-01 to 2025-08-01

notes:
- uhbegreb is a critical measurement-principle selector: GP=Grænsepassageprincip (goods physically crossing the border, used in traditional udenrigshandel statistics) vs ES=Ejerskifteprincip (change of ownership, used in betalingsbalancen). All rows appear twice — once per principle. Always filter to one: WHERE uhbegreb='GP' or WHERE uhbegreb='ES'. The table exists specifically to compare these two principles side by side.
- indud: 1=Import, 2=Eksport. These are independent series (both measured under each uhbegreb). Do not sum Import + Eksport.
- land: only W1 (world total). No geographic breakdown — this table is only useful for total-Denmark reconciliation.
- post covers detailed goods categories (SITC-ish product codes) plus subtotals. Some posts overlap (e.g. '1.A.A' is a subtotal of '1.A.A.1.Z' + '1.A.A.1.Q'). Filter to leaf-level posts to avoid double-counting.
- Typical use: compare GP vs ES values for the same post/indud/tid to understand the methodological gap between the two trade data series.